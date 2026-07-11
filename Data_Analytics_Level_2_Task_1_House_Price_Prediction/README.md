# Task 3 — Predicting House Prices with Linear Regression (Ames Housing)

## Objective
Build and evaluate a linear regression model that predicts house sale prices based on features such as living area, quality, garage capacity, and age, covering the full pipeline from EDA through model interpretation.

## Dataset
- **File:** `AmesHousing.csv`
- **Rows:** 2,930 residential property sales in Ames, Iowa
- **Columns:** 82 (size, quality, location, condition features)
- **Target:** `SalePrice`

## Tools & Libraries
- Python 3
- pandas, numpy
- scikit-learn (LinearRegression, Ridge, Lasso)
- matplotlib, seaborn

## What the Notebook Covers
1. EDA: null check, descriptive statistics, target variable distribution (right-skewed)
2. Feature selection: 14 features chosen from 82 based on correlation with `SalePrice` and domain reasoning (size, quality, age, location)
3. Missing value handling: `Total Bsmt SF`, `Garage Cars`, `Garage Area` nulls filled with 0 (representing "no basement/garage", not unknown values) — caught and fixed after the first model-fit attempt failed on unhandled NaNs
4. One-Hot Encoding: `Neighborhood`, `Central Air`
5. Correlation heatmap of selected numeric features
6. 80/20 train/test split
7. Linear Regression model training
8. Evaluation: MSE, RMSE, R²
9. Actual vs. predicted scatter plot
10. Residual plot
11. Coefficient analysis (which features drive price up/down)
12. Bonus: Ridge and Lasso regularised comparison

## How to Run
1. Make sure `AmesHousing.csv` is in the same folder as the notebook
2. Install dependencies: `pip install pandas numpy scikit-learn matplotlib seaborn`
3. Open `YourName_Task3.ipynb` in Jupyter Notebook / JupyterLab
4. Run all cells top to bottom

## Key Findings
- **Model performance:** RMSE ≈ $35,504, R² ≈ 0.843 on the test set (price range in the data: $12,789–$755,000)
- `Overall Qual` (material/finish quality) and `Gr Liv Area` (living area) are the strongest individual numeric predictors of price
- Certain neighborhoods (e.g. Green Hills, Stone Brook, Northridge) carry a substantial positive price premium independent of house size or quality
- Ridge and Lasso regularisation performed almost identically to plain Linear Regression (RMSE within ~$80 of each other), indicating the selected feature set wasn't significantly overfitting

## Author
Submitted as part of the Data Analytics track — OIBSIP internship program.
