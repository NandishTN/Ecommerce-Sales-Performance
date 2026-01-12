import pandas as pd

# Load dataset
df = pd.read_csv("ecommerce_sales.csv")

# Remove missing values
df.dropna(inplace=True)

# Convert date
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Month"] = df["OrderDate"].dt.month

# Monthly revenue
monthly_revenue = df.groupby("Month")["Revenue"].sum()
print(monthly_revenue)

# Top products
top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(10)
print(top_products)
