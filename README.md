<p align="center">
  <img src="Assets/Logo.png" width="400">
</p>

<h1 align="center">Tourist's Vision</h1>

<p align="center">
  AI-Powered Tourism Analytics Platform for Saudi Arabia
</p>



<p align="center">
  Google Maps • TikTok • YouTube • NLP • Machine Learning • Power BI
</p>

## Overview

Tourist's Vision is a graduation project developed by Data Science students at Umm Al-Qura University.

The project aims to transform large-scale tourism reviews and social media comments into actionable insights that support tourism development and decision-making in Saudi Arabia.

Using Natural Language Processing (NLP), Machine Learning, Deep Learning, and Interactive Dashboards, the system analyzes visitor opinions collected from multiple online platforms and provides comprehensive sentiment insights across all regions of the Kingdom.

The project aligns with the objectives of Saudi Vision 2030 by supporting the growth of the tourism and entertainment sectors through data-driven decision making.

---

## Project Objectives

* Analyze visitor opinions toward tourism and entertainment destinations.
* Measure visitor satisfaction across different regions of Saudi Arabia.
* Extract sentiment trends from large-scale user-generated content.
* Support stakeholders with interactive dashboards and tourism KPIs.
* Transform unstructured textual data into meaningful insights.

---

## Dataset

The project collected data from three major platforms:

| Source      |       Reviews |
| ----------- | ------------: |
| Google Maps |     1,016,595 |
| TikTok      |       128,412 |
| YouTube     |        73,555 |
| **Total**   | **1,218,562** |

### Geographic Coverage

The dataset covers all major regions of Saudi Arabia:

* Central Region
* Western Region
* Eastern Region
* Southern Region
* Northern Region

---

## Data Collection

Data was collected using the Apify platform.

### Sources

* Google Maps Reviews
* TikTok Comments
* YouTube Comments

The collected data includes:

* Review text
* Ratings
* Location information
* Publication dates
* Engagement metrics
* Geographic coordinates

---

## Data Preprocessing Pipeline

A comprehensive preprocessing pipeline was developed to handle Arabic text challenges and multi-source data integration.

### Processing Steps

* Data validation
* Missing value handling
* Column standardization
* Arabic text normalization
* Noise removal
* Emoji processing
* Translation handling
* Stopword processing
* Text cleaning
* Quality filtering
* Sentiment labeling

### Additional Features

* Aspect Extraction
* Tourism Type Extraction
* Seasonal Classification
* Place Name Extraction
* Comment Quality Scoring

---

## Machine Learning Models

The project evaluates three different sentiment analysis approaches:

### CAMeLBERT-DA

Transformer-based Arabic language model.

**Strengths**

* Context-aware understanding
* Arabic dialect support
* State-of-the-art performance

### Bi-LSTM

Deep learning sequence model.

**Strengths**

* Captures contextual dependencies
* Effective for structured review datasets

### LinearSVC

Traditional machine learning model using TF-IDF features.

**Strengths**

* Fast training
* Lightweight deployment
* Strong baseline performance

---

## Project Architecture
<p align="center">
  <img src="Assets/Project Architecture.png" alt="Tourist's Vision Architecture" width="900">
</p>

<p align="center">
  <em>Figure 1. System Architecture of the Tourist's Vision Platform</em>
</p>

The architecture illustrates the complete workflow of the project, starting from multi-source data collection, followed by data preprocessing, sentiment analysis using machine learning and deep learning models, and finally visualization through interactive Power BI dashboards.

## Technologies Used

### Programming

* Python

### Data Processing

* Pandas
* NumPy

### NLP

* Transformers
* CAMeLBERT
* Arabic NLP Processing

### Machine Learning

* Scikit-learn
* LinearSVC

### Deep Learning

* TensorFlow
* Keras
* Bi-LSTM

### Visualization

* Power BI

### Data Collection

* Apify

---

## Key Features

* Multi-source tourism analytics
* Arabic sentiment analysis
* Large-scale data processing
* Tourism trend monitoring
* Geographic insights
* Interactive dashboards
* KPI monitoring
* Regional performance comparison

---

## Results

The project demonstrated strong performance across multiple datasets using:

* CAMeLBERT-DA
* Bi-LSTM
* LinearSVC

Comparisons were conducted using:

* Accuracy
* Precision
* Recall
* F1-Score

The final outputs were integrated into Power BI dashboards for interactive analysis and decision support.

---

## Repository Structure

```text
tourists-vision/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── labeled/
│
├── notebooks/
│
├── src/
│   ├── preprocessing/
│   ├── labeling/
│   ├── feature_engineering/
│   ├── modeling/
│   └── evaluation/
│
├── models/
│
├── dashboards/
│
├── reports/
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Team Members

* Eyad Mohammed Alharthi
* Yazan Ibrahim Alghamdi
* Mohammed Nedal Alshareef
* Ziyad Omar Altalhi
* Ayman Abdulghani Alzahrani

---

## Supervisor

Dr. Zainy M. Aljawy

---

## University

Data Science Department

College of Computing

Umm Al-Qura University

2025–2026

---

## License

This project was developed as part of the Bachelor of Science in Data Science graduation requirements at Umm Al-Qura University.

All Rights Reserved © Tourist's Vision Team.
