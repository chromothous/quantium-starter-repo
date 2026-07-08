import pandas as pd

# Load the three files
df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine them
df = pd.concat([df0, df1, df2], ignore_index=True)

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Converting price string to float
df["price"] = (
    df["price"]
    .replace(r"[\$,]", "", regex=True)
    .astype(float)
)

# Create Sales column
df["Sales"] = df["price"] * df["quantity"]

# Keep only required columns
output = df[["Sales", "date", "region"]]

# Rename columns if desired
output = output.rename(columns={
    "date": "Date",
    "region": "Region"
})

# Save result
output.to_csv("formatted_sales_data.csv", index=False)

print("Output saved to formatted_sales_data.csv")