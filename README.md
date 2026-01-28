
# Slooze – Data Science & Analytics Assignment

## Objective
Analyze inventory, purchases, and sales data to generate actionable insights including:
- ABC Inventory Classification
- EOQ Calculation
- Demand Forecasting
- Lead Time Analysis

## Project Structure
```
slooze_submission/
│── inventory_analysis.py
│── data/
│   ├── SalesFINAL12312016.csv
│   └── InvoicePurchases12312016.csv
```

## How to Run Locally

### 1. Prerequisites
- Python 3.8+
- pip

### 2. Install Dependencies
```
pip install pandas numpy matplotlib
```

### 3. Prepare Data
Place the following files inside the `data/` folder:
- SalesFINAL12312016.csv
- InvoicePurchases12312016.csv

### 4. Run Analysis
```
python inventory_analysis.py
```

## Outputs Generated
- abc_inventory.csv
- eoq_report.csv
- demand_forecast.csv
- demand_forecast.png
- lead_time_analysis.csv

## Notes
- Demand forecasting uses moving averages (3M & 6M)
- Lead time is calculated at vendor level due to data availability
