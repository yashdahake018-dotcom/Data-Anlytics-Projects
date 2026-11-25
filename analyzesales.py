import pandas as pd

# CSV file load karein (same folder se)
df = pd.read_csv("sales_data.csv")

# Net revenue calculate karein
df["gross_amount"] = df["quantity"] * df["unit_price"]
df["net_revenue"] = (df["gross_amount"] * (1 - df["discount_pct"] / 100)).round(2)

print("=== Dataset Preview ===")
print(df.head())

print("\n=== Total Net Revenue ===")
print(round(df["net_revenue"].sum(), 2))

print("\n=== Revenue by Region ===")
region_summary = (
    df.groupby("region", as_index=False)["net_revenue"]
    .sum()
    .sort_values(by="net_revenue", ascending=False)
)
print(region_summary)

print("\n=== Revenue by Category ===")
category_summary = (
    df.groupby("category", as_index=False)[["quantity", "net_revenue"]]
    .sum()
    .sort_values(by="net_revenue", ascending=False)
)
print(category_summary)
