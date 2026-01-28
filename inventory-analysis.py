
# Slooze Data Science & Analytics Assignment
# Inventory, Sales, Demand Forecasting & Lead Time Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

DATA_DIR = "data"

# ---------------- Load Data ----------------
sales = pd.read_csv(os.path.join(DATA_DIR, "SalesFINAL12312016.csv"), parse_dates=["SalesDate"])
purchases = pd.read_csv(os.path.join(DATA_DIR, "InvoicePurchases12312016.csv"), parse_dates=["InvoiceDate"])

# ---------------- Revenue & ABC Analysis ----------------
sales["Revenue"] = sales["SalesQuantity"] * sales["SalesPrice"]
product_revenue = sales.groupby("InventoryId")["Revenue"].sum().sort_values(ascending=False)

abc = pd.DataFrame(product_revenue)
abc["CumPct"] = abc["Revenue"].cumsum() / abc["Revenue"].sum() * 100
abc["Class"] = np.where(abc["CumPct"] <= 80, "A",
                        np.where(abc["CumPct"] <= 95, "B", "C"))
abc.to_csv("abc_inventory.csv")

# ---------------- EOQ ----------------
annual_demand = sales.groupby("InventoryId")["SalesQuantity"].sum()
S, H = 50, 5
eoq = pd.DataFrame({
    "AnnualDemand": annual_demand,
    "EOQ": np.sqrt((2 * annual_demand * S) / H)
})
eoq.to_csv("eoq_report.csv")

# ---------------- Demand Forecasting ----------------
monthly_demand = sales.set_index("SalesDate").resample("ME")["SalesQuantity"].sum()
forecast = pd.DataFrame({
    "ActualDemand": monthly_demand,
    "MA_3": monthly_demand.rolling(3).mean(),
    "MA_6": monthly_demand.rolling(6).mean()
})
forecast.to_csv("demand_forecast.csv")

forecast.plot(title="Monthly Demand Forecast")
plt.savefig("demand_forecast.png")
plt.close()

# ---------------- Lead Time Analysis ----------------
purchases = purchases.sort_values(["VendorNumber", "InvoiceDate"])
purchases["PrevInvoiceDate"] = purchases.groupby("VendorNumber")["InvoiceDate"].shift(1)
purchases["LeadTimeDays"] = (purchases["InvoiceDate"] - purchases["PrevInvoiceDate"]).dt.days

lead_time = (
    purchases.groupby("VendorNumber")["LeadTimeDays"]
    .agg(["mean", "std", "min", "max"])
    .dropna()
)
lead_time.to_csv("lead_time_analysis.csv")

print("Analysis completed. Output files generated.")
