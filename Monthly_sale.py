
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ],
    "Total Sales": [
        19640.427, 11833.618, 7159.670, 12455.482,
        15280.411, 11927.849, 10222.428, 26797.763,
        17158.932, 10112.641, 18792.184, 17525.2847
    ]
}

df = pd.DataFrame(data)

print("MONTHLY SALES ANALYSIS")
print(df.to_string(index=False))

print("\nHighest Sales:")
print(df.loc[df["Total Sales"].idxmax()])

print("\nLowest Sales:")
print(df.loc[df["Total Sales"].idxmin()])

plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Total Sales"], marker="o")
plt.title("Monthly Sales Trend - 2014")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_chart.png")
plt.show()
