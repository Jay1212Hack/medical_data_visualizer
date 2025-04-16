# 📊 Medical Data Visualizer

This project is part of the freeCodeCamp Data Analysis with Python certification. The goal is to analyze and visualize medical examination data to uncover insights about cardiovascular disease and lifestyle factors.

## 🏥 Dataset

The dataset is provided in the file `medical_examination.csv`. Each row represents a patient with the following features:

| Feature         | Description                           |
|----------------|---------------------------------------|
| age            | Age in days                           |
| height         | Height in cm                          |
| weight         | Weight in kg                          |
| gender         | Categorical (1 = women, 2 = men)      |
| ap_hi          | Systolic blood pressure               |
| ap_lo          | Diastolic blood pressure              |
| cholesterol    | 1: normal, 2: above normal, 3: high    |
| gluc           | 1: normal, 2: above normal, 3: high    |
| smoke          | 0 = no, 1 = yes                        |
| alco           | 0 = no, 1 = yes                        |
| active         | 0 = no, 1 = yes                        |
| cardio         | Target variable (1 = disease, 0 = none)|

---

## 🧪 Features

### ✅ Data Cleaning & Transformation
- Added `overweight` column based on BMI (BMI > 25).
- Normalized `cholesterol` and `gluc` values to binary (0 = good, 1 = bad).

### 📊 Visualizations

#### 1. Categorical Plot
Displays comparisons of features like `cholesterol`, `gluc`, `smoke`, `alco`, `active`, and `overweight` against the presence (`cardio = 1`) or absence (`cardio = 0`) of cardiovascular disease.

#### 2. Heat Map
Displays a correlation matrix of all numerical features after filtering out invalid or extreme values:
- Systolic ≥ Diastolic
- Height and weight between 2.5th and 97.5th percentiles

---

## 🛠 Development

To run the project:

```bash
# Install dependencies
pip install pandas matplotlib seaborn

# Run the visualizations
python main.py
