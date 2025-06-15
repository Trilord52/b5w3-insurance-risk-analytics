# B5W3: End-to-End Insurance Risk Analytics & Predictive Modeling

This repository contains the code, data, and documentation for the Week 3 Challenge of the 10 Academy Artificial Intelligence Mastery Program. The project focuses on analyzing historical car insurance claim data (`MachineLearningRating_v3.txt`) for AlphaCare Insurance Solutions (ACIS) to optimize marketing strategies, identify low-risk customer segments, and reduce churn through premium adjustments. The goal is to deliver actionable insights using exploratory data analysis (EDA), data version control (DVC), hypothesis testing, and predictive modeling.

## 🧭 Project Structure

b5w3-insurance-risk-analytics/

├── data/

│   └── MachineLearningRating_v3.txt  # Raw insurance claims data

├── scripts/

│   ├── eda.py                     # Script for exploratory data analysis

│   └── (future scripts for Tasks 3 & 4)

├── plots/                         # Generated EDA visualizations

├── reports/                       # Analysis reports

├── .dvc/                          # DVC configuration

├── .gitignore                     # Excludes local artifacts

├── requirements.txt              # Dependencies

└── README.md                      # You're here

## 📌 Project Objectives
Main goal: Analyze 18 months of car insurance data (Feb 2014–Aug 2015) to enhance customer retention and profitability by targeting low-risk segments.

- **Task 1**: Set up Git, CI/CD, and perform EDA to uncover risk and profitability patterns.
- **Task 2**: Implement DVC for reproducible data management.
- **Task 3**: Conduct A/B hypothesis testing on risk drivers.
- **Task 4**: Build predictive models for claim severity and premium optimization.

## Initial Setup and Project Structure

- ☑️ Set up GitHub repository with clear folder structure
- ☑️ Define modular code layout (scripts/, data/, plots/, reports/)
- ☑️ Add .gitignore to exclude local artifacts (e.g., venv/, data_storage/)
- ☑️ Create and document environment dependencies (requirements.txt)
- ☑️ Initialize DVC for data versioning

## Data Collection and Preprocessing (Task 1)

- ☑️ Load and preprocess `MachineLearningRating_v3.txt` (pipe-delimited text file)
- ☑️ Generate cleaned dataset for analysis

## Exploratory Data Analysis (Task 1)

- ☑️ Perform EDA on insurance claims data
- ☑️ Generate visualizations: distribution of claims, gender breakdown, premium vs. claims, correlation matrix, outliers, loss ratio by province, claims by vehicle type, and temporal trends
- ☑️ Save results in plots/

## Data Version Control (Task 2)

- ☑️ Initialize DVC and configure local remote storage
- ☑️ Track `MachineLearningRating_v3.txt` with DVC

## 🔧 Data Pipeline Implemented in scripts/:

### eda.py:
- Step: Load and preprocess `MachineLearningRating_v3.txt`
- Step: Perform univariate, bivariate, and creative visualizations
- Step: Calculate Loss Ratio by Province
- Callable via: `python scripts/eda.py`

## 📊 EDA Highlights

- ☑️ Distribution and outliers in TotalClaims
- ☑️ Gender and Province-based insights
- ☑️ Loss Ratio trends by Province
- ☑️ Temporal trends in claims

## 🌍 Usage

### Setup Environment
- git clone https://github.com/Trilord52/b5w3-insurance-risk-analytics.git
- cd b5w3-insurance-risk-analytics
- python -m venv venv
- venv\Scripts\activate  # Windows
- pip install -r requirements.txt

### Run EDA
- python scripts/eda.py

## 📈 Contribution Summary

### Feature:
- Implemented EDA pipeline: ☑️ eda.py
- Set up DVC tracking: ☑️ DVC initialization and data push
- Git commits & PR hygiene: ☑️ Followed task-1 and task-2 branching
