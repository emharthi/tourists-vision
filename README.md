<p align="center">
  <img src="Assets/Project Logo Without Background.png" width="400">
</p>

<h1 align="center">Tourist's Vision</h1>

<p align="center">
  An Intelligent Dashboard for Sentiment Analysis of Tourism Reviews in Saudi Arabia
</p>



<p align="center">
 • Google Maps • TikTok • YouTube • NLP • Machine Learning • Power BI
</p>

## 1. Overview

Tourist's Vision is a graduation project developed by Data Science students at Umm Al-Qura University.

The project aims to transform large-scale tourism reviews and social media comments into actionable insights that support tourism development and decision-making in Saudi Arabia.

Using Natural Language Processing (NLP), Machine Learning, Deep Learning, and Interactive Dashboards, the system analyzes visitor opinions collected from multiple online platforms and provides comprehensive sentiment insights across all regions of the Kingdom.

The project aligns with the objectives of Saudi Vision 2030 by supporting the growth of the tourism and entertainment sectors through data-driven decision making.

---

## 2. Project Objectives

* Analyze visitor opinions toward tourism and entertainment destinations.
* Measure visitor satisfaction across different regions of Saudi Arabia.
* Extract sentiment trends from large-scale user-generated content.
* Support stakeholders with interactive dashboards and tourism KPIs.
* Transform unstructured textual data into meaningful insights.

---

## 3. Processed Dataset

The project collected data from three major platforms:

| Source      |       Reviews |
| ----------- | ------------: |
| Google Maps |     1,016,595 |
| TikTok      |       128,412 |
| YouTube     |        73,555 |
| **Total**   | **1,218,562** |

### 3.2 Geographic Coverage

The dataset covers all major regions of Saudi Arabia:

  * Central Region
  * Western Region
  * Eastern Region
  * Southern Region
  * Northern Region

### 3.3 Access to the Data

The processed datasets used in this project are available through the following resources:

-  **Google Maps Reviews**
  - [Access Folder](https://drive.google.com/file/d/1vNVrToDvrjnE_hCgxnIxBxagcW8Jn2db/view?usp=sharing)

| Column Name | Description |
| :--- | :--- |
| `categoryName` | Represents the type of tourist destination (e.g., Park, Farm, Forest, Museum, Archaeological Site, etc.). |
| `city` | The name of the city, governorate, or district where the location is situated. |
| `location/lat & lng` | Two separate columns representing the latitude and longitude coordinates for each tourist site. |
| `neighborhood` | The area or vicinity adjacent to the intended tourist landmark. |
| `publishedAtDate` | The date the review was written and published on Google Maps. |
| `stars` | The column containing the star ratings for the tourist destination. |
| `street` | The name of the street where the tourist site is located. |
| `text` | Represents the written comments and reviews provided by users who visited the location. |
| `title` | The actual name and title of the tourist landmark. |

-  **TikTok Dataset**
  - [Access Folder](https://drive.google.com/drive/folders/1R0NA9x6H3s2kluDccCofoGI1gHFCCs9l?usp=sharing)

| Column Name | Description |
| :--- | :--- |
| `text` | Represents the column of comments written by users. |
| `diggCount` | Represents the number of likes each comment received. |
| `replyCommentTotal` | Represents the total number of replies to each comment. |
| `createTimeISO` | Represents the date and time each comment was posted (in ISO format). |
| `videoWebUrl` | A column containing the direct link to the video clip. |
| `cid` | Acts as a unique Comment ID to distinguish each comment from others. |

-  **YouTube Dataset**
  - [Access Folder](https://drive.google.com/drive/folders/1QF9JbmlgVOhA8iDwiYQsj12KrStodIqQ?usp=sharing)

| Column Name | Description |
| :--- | :--- |
| `comment` | Represents the text of the comment written by users on the videos. This is the primary column used for sentiment analysis and opinion mining. |
| `pageUrl` | Contains the URL of the YouTube video page, allowing reference to the original source of the comment. |
| `replyCount` | Reflects the number of replies each comment received, indicating the level of interaction and discussion. |
| `title` | Represents the title of the video from which the comments were extracted, often related to tourism or entertainment content. |
| `videoID` | A unique identifier for each video, used to distinguish videos and link comments to them. |
| `voteCount` | Represents the number of likes each comment received, indicating user agreement or acceptance. |

---

## 4. Data Collection

Data was collected using the Apify platform.

### 4.1 Sources

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

## 5. Data Preprocessing Pipeline

A comprehensive preprocessing pipeline was developed to handle Arabic text challenges and multi-source data integration.

### 5.1 Processing Steps

<p align="center">
  <img src="Assets/Pre-Processing Figure.png" alt="Data Preprocessing Pipeline" width="90%">
</p>

<p align="center">
  <em>Figure 1. Data Preprocessing Workflow used in Tourist's Vision.</em>
</p>

The preprocessing pipeline includes data validation, missing value handling, column standardization, Arabic text normalization, noise removal, emoji processing, translation handling, text cleaning, quality filtering, and sentiment labeling.

### 5.2 Additional Features

* Aspect Extraction
* Tourism Type Extraction
* Seasonal Classification
* Place Name Extraction
* Comment Quality Scoring

---

## 6. Build Models

The project evaluates three different sentiment analysis approaches:

### 6.1 CAMeLBERT-DA

Transformer-based Arabic language model.

**Strengths**

* Context-aware understanding
* Arabic dialect support
* State-of-the-art performance

### 6.2 Bi-LSTM

Deep learning sequence model.

**Strengths**

* Captures contextual dependencies
* Effective for structured review datasets

### 6.3 LinearSVC

Traditional machine learning model using TF-IDF features.

**Strengths**

* Fast training
* Lightweight deployment
* Strong baseline performance

---

## 7. System Architecture
<p align="center">
  <img src="Assets/Project Architecture.png" alt="Tourist's Vision Architecture" width="900">
</p>

<p align="center">
  <em>Figure 2. System Architecture of the Tourist's Vision Platform</em>
</p>

The architecture illustrates the complete workflow of the project, starting from multi-source data collection, followed by data preprocessing, sentiment analysis using machine learning and deep learning models, and finally visualization through interactive Power BI dashboards.

---

## 8. Technologies Used

### 8.1 Programming

<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="45" alt="Python"/>
</p>

### 8.2 Data Processing

<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="45" alt="Pandas"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" height="45" alt="NumPy"/>
</p>

### 8.3 NLP

<p>
  <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" height="45" alt="Transformers"/>
</p>

- CAMeLBERT
- Arabic NLP Processing

### 8.4 Machine Learning

<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg" height="45" alt="Scikit-learn"/>
</p>

- LinearSVC

### 8.5 Deep Learning

<p>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" height="45" alt="TensorFlow"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/keras/keras-original.svg" height="45" alt="Keras"/>
</p>

- Bi-LSTM

### 8.6 Visualization

<p>
  <img src="https://upload.wikimedia.org/wikipedia/commons/c/cf/New_Power_BI_Logo.svg" height="45" alt="Power BI"/>
</p>

### 8.7 Data Collection

<p>
  <img src="Assets/Apify Logo.svg" height="45" alt="Apify"/>
</p>

## 8.8 Key Features

* Multi-source tourism analytics
* Arabic sentiment analysis
* Large-scale data processing
* Tourism trend monitoring
* Geographic insights
* Interactive dashboards
* KPI monitoring
* Regional performance comparison

---

## 9. Results

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

## 10. Repository Structure

```text
tourists-vision/
│
├── Assets/
├── Dashboards/
|
├── Models/
|
├── Raw Data/
│   
│   
│   
│
|
│
├── src/
│   ├── Pre-Processing Stage/
│   ├── Exploratory Data Analysis (EDA)/
│   ├── Build Models/
│   ├── Aspect Extraction/
│   
│
|
│
├── README.md
├── requirements.txt

```

---

## 11. Setup Instructions

Follow these steps to set up and run the project locally.

### 11.1 Clone the Repository

```bash
git clone https://github.com/emharthi/tourists-vision.git
cd tourists-vision
```

### 11.2 Create a Virtual Environment

```bash
python -m venv venv
```

### 11.3 Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac / Linux**

```bash
source venv/bin/activate
```

### 11.4 Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 11.5 Run the Project

Navigate to the desired project module inside the `src/` directory and execute the corresponding Python scripts.

```bash
cd src
```

Available modules:

- Pre-Processing Stage
- Exploratory Data Analysis (EDA)
- Build Models
- Aspect Extraction

### 11.6 Open Dashboards

Power BI dashboard files are available in the `Dashboards/` directory.

Open the `.pbix` files using **Power BI Desktop** to explore the project's interactive dashboards.

---

## 12. License

This project was developed as part of the Bachelor of Science in Data Science graduation requirements at Umm Al-Qura University.

All Rights Reserved © Tourist's Vision Team.
