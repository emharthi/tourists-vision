import numpy as np
import pandas as pd
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report, confusion_matrix

import torch
from torch.utils.data import Dataset

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding,
    set_seed,
    EarlyStoppingCallback
)

# =========================
# CONFIG
# =========================
DATA_ROOT = Path(r"C:\Users\ziyad\Downloads\OneDrive_1447-08-23\Cleaned Data\المنطقة الجنوبية")  # عدّله لمنطقة الشمال لاحقًا

MODEL_NAME = "aubmindlab/bert-base-arabertv2"
OUT_DIR = "arabert_south_region_model"

TEXT_COL = "Text_TR"
STARS_CANDIDATES = ["Stars", "stars"]

BINARY_MODE = True   # 1-2 NEG, 4-5 POS, drop 3
MAX_ROWS = None      # مثال: 200_000 للتجارب
MAX_LEN = 128
TEST_SIZE = 0.15
VAL_SIZE = 0.15
SEED = 42
set_seed(SEED)

# =========================
# HELPERS
# =========================
def pick_stars_col(df: pd.DataFrame):
    for c in STARS_CANDIDATES:
        if c in df.columns:
            return c
    return None

def load_all_xlsx(root: Path):
    return sorted(list(root.rglob("*.xlsx")))

def load_dataset(root: Path, max_rows=None):
    files = load_all_xlsx(root)
    print("Found files:", len(files))
    if len(files) == 0:
        raise ValueError("No .xlsx files found. Check DATA_ROOT.")

    parts = []
    used_files = 0
    skipped_missing_cols = 0
    skipped_empty_after = 0

    for fp in files:
        try:
            df = pd.read_excel(fp)
        except Exception:
            continue

        stars_col = pick_stars_col(df)
        if (TEXT_COL not in df.columns) or (stars_col is None):
            skipped_missing_cols += 1
            continue

        # keep rows with text
        df = df[df[TEXT_COL].fillna("").astype(str).str.strip() != ""].copy()
        if len(df) == 0:
            skipped_empty_after += 1
            continue

        # numeric stars
        df[stars_col] = pd.to_numeric(df[stars_col], errors="coerce")
        df = df[df[stars_col].notna()].copy()
        if len(df) == 0:
            skipped_empty_after += 1
            continue

        df[stars_col] = df[stars_col].astype(int)

        # labeling
        if BINARY_MODE:
            df = df[df[stars_col].isin([1, 2, 4, 5])].copy()
            if len(df) == 0:
                skipped_empty_after += 1
                continue
            df["label"] = df[stars_col].map({1: 0, 2: 0, 4: 1, 5: 1}).astype(int)
        else:
            df = df[df[stars_col].isin([1, 2, 3, 4, 5])].copy()
            if len(df) == 0:
                skipped_empty_after += 1
                continue
            df["label"] = df[stars_col].map({1: 0, 2: 0, 3: 1, 4: 2, 5: 2}).astype(int)

        df["source_file"] = str(fp)
        df.rename(columns={stars_col: "Stars"}, inplace=True)  # unify internally

        parts.append(df[[TEXT_COL, "label", "Stars", "source_file"]])
        used_files += 1

    if not parts:
        raise ValueError("No valid data found after filtering. Check columns and content.")

    data = pd.concat(parts, ignore_index=True)
    print("Used files:", used_files)
    print("Skipped (missing cols):", skipped_missing_cols)
    print("Skipped (empty after filter):", skipped_empty_after)
    print("Rows after filtering:", f"{len(data):,}")

    if max_rows is not None and len(data) > max_rows:
        data = data.sample(n=max_rows, random_state=SEED).reset_index(drop=True)
        print("Sampled to:", f"{len(data):,}")

    print("\nLabel distribution:")
    print(data["label"].value_counts().sort_index())

    return data

# =========================
# DATASET CLASS
# =========================
class TextDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_len=128):
        self.texts = list(texts)
        self.labels = list(labels)
        self.tokenizer = tokenizer
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        enc = self.tokenizer(
            str(self.texts[idx]),
            truncation=True,
            max_length=self.max_len,
            padding=False
        )
        enc["labels"] = int(self.labels[idx])
        return enc

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "f1_macro": f1_score(labels, preds, average="macro"),
        "f1_weighted": f1_score(labels, preds, average="weighted"),
    }

# =========================
# CLASS WEIGHTS (for imbalance)
# =========================
def compute_class_weights(labels: np.ndarray, num_labels: int):
    counts = np.bincount(labels, minlength=num_labels).astype(float)
    weights = counts.sum() / (num_labels * counts)
    return torch.tensor(weights, dtype=torch.float)

class WeightedTrainer(Trainer):
    def __init__(self, class_weights=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_weights = class_weights

    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        labels = inputs.pop("labels")
        outputs = model(**inputs)
        logits = outputs.logits
        loss_fct = torch.nn.CrossEntropyLoss(weight=self.class_weights.to(logits.device))
        loss = loss_fct(logits, labels)
        return (loss, outputs) if return_outputs else loss

# =========================
# TRAIN
# =========================
def main():
    df = load_dataset(DATA_ROOT, max_rows=MAX_ROWS)

    train_df, test_df = train_test_split(
        df, test_size=TEST_SIZE, random_state=SEED, stratify=df["label"]
    )

    train_df, val_df = train_test_split(
        train_df, test_size=VAL_SIZE, random_state=SEED, stratify=train_df["label"]
    )

    print(f"\nSplit sizes | Train: {len(train_df):,} | Val: {len(val_df):,} | Test: {len(test_df):,}")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    num_labels = 2 if BINARY_MODE else 3
    model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=num_labels)

    train_ds = TextDataset(train_df[TEXT_COL], train_df["label"], tokenizer, max_len=MAX_LEN)
    val_ds   = TextDataset(val_df[TEXT_COL],   val_df["label"],   tokenizer, max_len=MAX_LEN)
    test_ds  = TextDataset(test_df[TEXT_COL],  test_df["label"],  tokenizer, max_len=MAX_LEN)

    collator = DataCollatorWithPadding(tokenizer=tokenizer)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print("\nDevice:", device)

    cw = compute_class_weights(train_df["label"].values, num_labels=num_labels)
    print("Class weights:", cw.tolist())

    args = TrainingArguments(
        output_dir=OUT_DIR,

        # Transformers 5.x uses eval_strategy (NOT evaluation_strategy)
        eval_strategy="epoch",
        save_strategy="epoch",

        logging_strategy="steps",
        logging_steps=200,

        learning_rate=2e-5,
        per_device_train_batch_size=8 if device == "cuda" else 4,
        per_device_eval_batch_size=16 if device == "cuda" else 8,

        num_train_epochs=3 if device == "cuda" else 1,
        weight_decay=0.01,
        warmup_ratio=0.06,

        fp16=True if device == "cuda" else False,

        load_best_model_at_end=True,
        metric_for_best_model="f1_macro",
        greater_is_better=True,

        save_total_limit=2,
        report_to="none"
    )

    trainer = WeightedTrainer(
        class_weights=cw,
        model=model,
        args=args,
        train_dataset=train_ds,
        eval_dataset=val_ds,
        data_collator=collator,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=2)]
    )

    trainer.train()

    preds = trainer.predict(test_ds)
    y_true = preds.label_ids
    y_pred = np.argmax(preds.predictions, axis=1)

    print("\n=== Test Report ===")
    print(classification_report(y_true, y_pred, digits=4))
    print("Confusion Matrix:")
    print(confusion_matrix(y_true, y_pred))

    trainer.save_model(OUT_DIR)
    tokenizer.save_pretrained(OUT_DIR)
    print(f"\n✅ Model saved to: {OUT_DIR}")

if __name__ == "__main__":
    main()
