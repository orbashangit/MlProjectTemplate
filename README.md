# **ML Project Pipeline Template**

## **Overview**
This project provides a comprehensive and modular **MLOps pipeline** designed to automate the lifecycle of machine learning projects. From **data ingestion** and **preprocessing** to **model training**, **evaluation**, **deployment**, and **monitoring**, this pipeline is built to handle the complexities of machine learning workflows in a secure, closed environment.

## **Key Features**
- **Modular Design**: Each component is independent, enabling easy testing, maintenance, and scalability.
- **Pre-Production Testing**: Rigorous testing of models before transitioning to production.
- **Production-Ready Deployment**: Automated deployment of validated models.
- **Tracking and Monitoring**: Version control for datasets and models, coupled with performance monitoring for data drift.
- **Integration with Azure Pipelines**: CI/CD pipeline automation for reliable code integration and deployment.

---

## **Project Structure**

```plaintext
MLPROJECTTEMPLATE/
├── azure_pipelines/              # CI/CD configuration for Azure DevOps
├── config/                       # Configuration files (e.g., paths, parameters, logging)
├── data/                         # Datasets at various processing stages
│   ├── raw/                      # Unprocessed raw data
│   ├── interim/                  # Intermediate data during processing
│   ├── processed/                # Final cleaned and feature-engineered data
│   └── sourceModels/             # Pretrained reference models
├── mlflow/                       # MLflow configuration for experiment tracking
├── notebooks/                    # Jupyter notebooks for EDA and prototyping
├── preproduction/                # Pre-production models and evaluation results
├── production/                   # Production-ready models and results
├── scripts/                      # Main and shell scripts for pipeline automation
├── src/                          # Core source code for the pipeline
│   ├── data_ingestion/           # Data loading and validation modules
│   ├── data_preprocessing/       # Data cleaning and feature engineering
│   ├── models/                   # Model implementations (e.g., BERT, XGBoost)
│   ├── evaluation/               # Model evaluation metrics and reporting
│   ├── inference/                # Prediction and inference logic
│   ├── pipeline/                 # Pipeline orchestrators
│   └── utils/                    # Helper functions and utilities
├── tests/                        # Unit, integration, and QA tests
├── tracking/                     # Data and model versioning modules
├── training_logs/                # Logs generated during model training
├── Documentation.docx            # Detailed project documentation
├── ML Pipeline Template Presentation.pptx # Pipeline presentation
├── requirements.txt              # Python dependencies
└── README.md                     # Project overview and usage instructions
```

---

## **Getting Started**

### **1. Prerequisites**
- Python 3.8+
- Required Python libraries (listed in `requirements.txt`):
  - pandas
  - numpy
  - scikit-learn
  - torch
  - transformers
  - mlflow
- Azure DevOps for CI/CD (optional but recommended)

### **2. Installation**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd MLPROJECTTEMPLATE
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **3. Configuration**
- Update `config/config.yaml` with project-specific paths, parameters, and settings.
- Modify `logging.yaml` for custom logging levels or formats.

---

## **Usage**

### **1. Run the Full Pipeline**
To execute the entire pipeline, run the following:
```bash
python scripts/main_pipeline/main_pipeline.py
```

### **2. Run Individual Stages**
You can run specific pipeline stages independently:
- **Data Preprocessing**:
  ```bash
  python scripts/main_scripts/main_data_preprocessing.py
  ```
- **Model Training**:
  ```bash
  python scripts/main_scripts/main_training.py
  ```
- **Model Evaluation**:
  ```bash
  python scripts/main_scripts/main_evaluation.py
  ```

### **3. Automate with Shell Scripts**
Shell scripts in `scripts/shell_scripts/` provide automation for pipeline execution:
- Pre-production testing:
  ```bash
  bash scripts/shell_scripts/pre_production.sh
  ```
- Deploying models to production:
  ```bash
  bash scripts/shell_scripts/production.sh
  ```

---

## **Key Components**

### **Data Handling**
- **Data Loader**: Loads raw data from CSV or MSSQL (`src/data_ingestion/data_loader.py`).
- **Data Validator**: Validates schema and integrity (`src/data_ingestion/data_validator.py`).
- **Data Cleaner**: Cleans and preprocesses raw data (`src/data_preprocessing/data_cleaner.py`).

### **Modeling**
- **BERT Model**: Implements BERT for text classification (`src/models/bert_model.py`).
- **XGBoost Model**: Implements XGBoost for tabular data (`src/models/xgb_model.py`).

### **Evaluation and Inference**
- **Evaluator**: Computes performance metrics like accuracy and F1 score (`src/evaluation/evaluator.py`).
- **Predictor**: Runs inference on new data (`src/inference/predictor.py`).

### **Tracking and Monitoring**
- **Data Versioning**: Tracks changes in datasets (`tracking/data_versioning/`).
- **Model Versioning**: Logs model metadata and performance metrics (`tracking/model_versioning/`).
- **Monitoring**: Detects data drift and performance degradation (`tests/tpi/`).

---

## **Testing**

Comprehensive tests ensure pipeline reliability:
- **Unit Tests**: Isolate individual components (`tests/unit/`).
- **Integration Tests**: Validate full pipeline workflows (`tests/integration/`).
- **QA Tests**: Focus on data quality and compliance (`tests/qa/`).

Run all tests with:
```bash
pytest tests/
```

---

## **CI/CD Integration**
The pipeline integrates with Azure DevOps for automated testing, building, and deployment:
1. Update `azure_pipelines/azure_pipeline.yaml` with your project configuration.
2. Push changes to trigger the CI/CD pipeline.

---
