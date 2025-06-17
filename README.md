# B5W3: End-to-End Insurance Risk Analytics & Predictive Modeling

This repository contains the code, data, and documentation for the Week 3 Challenge of the 10 Academy Artificial Intelligence Mastery Program. The project focuses on analyzing 18 months of historical car insurance claim data (`data/raw/MachineLearningRating_v3.txt`) for AlphaCare Insurance Solutions (ACIS) to optimize marketing strategies, identify low-risk customer segments, and reduce a 15% churn rate through premium adjustments. The goal is to deliver actionable insights using exploratory data analysis (EDA), data version control (DVC), A/B hypothesis testing, and predictive modeling.

## 📋 Project Objectives
The primary objective is to enhance customer retention and profitability by analyzing data from February 2014 to August 2015. Key tasks include:
- **Task 1**: Set up Git, CI/CD, and perform EDA to uncover risk and profitability patterns.
- **Task 2**: Implement DVC for reproducible data management.
- **Task 3**: Conduct A/B hypothesis testing to identify risk drivers.
- **Task 4**: Build predictive models for claim severity and premium optimization.

## 🗂️ Project Structure
b5w3-insurance-risk-analytics/
├── data/
│   ├── raw/                    # Raw data files (e.g., MachineLearningRating_v3.txt)
│   └── processed/             # Processed datasets
├── analysis_scripts/           # Analysis scripts (e.g., eda.py, ab_testing.py, predictive_modeling.py)
├── visualizations/            # Generated EDA and model visualizations
├── reports/                   # Analysis reports and documentation
├── analysis_outputs/          # Outputs from statistical tests and models
├── .dvc/                      # DVC configuration
├── .github/                   # CI/CD workflows
├── .gitignore                 # Excludes local artifacts (e.g., venv/, data_storage/)
├── requirements.txt           # Project dependencies
└── README.md                  # Project overview


## 🚀 Initial Setup and Project Structure
- ✅ Set up GitHub repository with a descriptive folder structure.
- ✅ Defined modular code layout (e.g., `analysis_scripts/`, `visualizations/`, `reports/`).
- ✅ Added `.gitignore` to exclude local artifacts (e.g., `venv/`, `data_storage/`).
- ✅ Documented environment dependencies in `requirements.txt`.
- ✅ Initialized DVC for data versioning.

## 📊 Data Collection and Preprocessing (Task 1)
- ✅ Loaded and preprocessed `MachineLearningRating_v3.txt` (pipe-delimited text file).
- ✅ Generated a cleaned dataset for analysis.

## 🔍 Exploratory Data Analysis (Task 1)
- ✅ Performed EDA on insurance claims data.
- ✅ Generated visualizations: distribution of claims, gender breakdown, premium vs. claims, correlation matrix, outliers, loss ratio by province, claims by vehicle type, and temporal trends.
- ✅ Saved results in `visualizations/`.

## 📦 Data Version Control (Task 2)
- ✅ Initialized DVC and configured a local remote storage.
- ✅ Tracked `data/raw/MachineLearningRating_v3.txt` with DVC and verified `dvc push`.

## 🔧 Data Pipelines Implemented in `analysis_scripts/`:
### `eda.py`:
- **Steps**: Load and preprocess `MachineLearningRating_v3.txt`, perform univariate, bivariate, and creative visualizations, calculate Loss Ratio by Province.
- **Execution**: `python analysis_scripts/eda.py`

### `ab_testing.py`:
- **Steps**: Conduct A/B hypothesis testing on claim frequency and LossRatio by Province and VehicleType, save results to `analysis_outputs/statistical_tests/`.
- **Execution**: `python analysis_scripts/ab_testing.py`

### `predictive_modeling.py`:
- **Steps**: Build Linear Regression and Random Forest models to predict claim severity, perform cross-validation, and generate SHAP-based feature importance plots saved to `analysis_outputs/model_outputs/`.
- **Execution**: `python analysis_scripts/predictive_modeling.py`

## 📈 Key Findings
- ✅ Distribution and outliers in `TotalClaims`.
- ✅ Gender and Province-based insights.
- ✅ Loss Ratio trends by Province (e.g., higher in Gauteng).
- ✅ Temporal trends in claims.

## 🌍 Usage

### Setup Environment
```bash
git clone https://github.com/Trilord52/b5w3-insurance-risk-analytics.git
cd b5w3-insurance-risk-analytics
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
dvc pull data/raw/MachineLearningRating_v3.txt
```

## Run Analyses

EDA: python analysis_scripts/eda.py
A/B Testing: python analysis_scripts/ab_testing.py
Predictive Modeling: python analysis_scripts/predictive_modeling.py

## 🤝 Contribution Guidelines
Use branching strategy: task-<number> for each task (e.g., task-3, task-4).
Submit Pull Requests with descriptive titles and comments.
Ensure code adheres to PEP 8 standards and includes documentation.

## 📋 CI/CD Workflow
Configured in .github/workflows/ci.yml to run linting and tests automatically on push/pull requests.

📜 License

