# Task 1 — EDA on Retail Sales Data

## Objective
Perform a thorough Exploratory Data Analysis on a retail sales dataset to uncover patterns, customer behaviour trends, and actionable business insights.

## Dataset
- **File:** `retail_sales_dataset.csv`
- **Rows:** 1000 transactions
- **Period covered:** January 2023 – January 2024
- **Columns:** Transaction ID, Date, Customer ID, Gender, Age, Product Category, Quantity, Price per Unit, Total Amount

## Tools & Libraries
- Python 3
- pandas
- matplotlib
- seaborn
- Jupyter Notebook

## What the Notebook Covers
1. Data loading and initial inspection (shape, dtypes, nulls)
2. Data type correction (Date → datetime)
3. Descriptive statistics (mean, median, mode, std dev)
4. Monthly and quarterly sales trend analysis
5. Customer demographics: age distribution, gender breakdown
6. Product analysis: revenue and units sold by category
7. Correlation heatmap across numeric variables
8. Additional insight: average spend by category and gender
9. Bonus: sales by day of week
10. Business recommendations based on findings

## How to Run
1. Make sure `retail_sales_dataset.csv` is in the same folder as the notebook
2. Install dependencies: `pip install pandas matplotlib seaborn`
3. Open `YourName_Task1.ipynb` in Jupyter Notebook / JupyterLab
4. Run all cells top to bottom

## Key Findings
- Electronics and Clothing generate the highest revenue, closely followed by Beauty
- Sales show noticeable month-to-month variation, with certain months standing out as peaks
- Customer base is nearly evenly split between genders (51% Female, 49% Male)
- Average customer age is ~41, with a fairly wide spread (18–64)

## Author
Submitted as part of the Data Analytics track.