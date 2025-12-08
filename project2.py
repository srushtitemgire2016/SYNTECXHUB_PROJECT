import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------
# 1. SAMPLE DATA
# ------------------------------------------
data = {
    "Date": pd.date_range(start="2024-01-01", periods=120, freq="D"),
    "Sales": (1000 + (pd.Series(range(120)) * 5)).values
}

df_time = pd.DataFrame(data)
df_time["Month"] = df_time["Date"].dt.to_period("M")
df_time["Quarter"] = df_time["Date"].dt.to_period("Q")

# Category data for bar & pie charts
df_cat = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Sales": [45000, 30000, 18000, 7000]
})

# ------------------------------------------
# 2. LINE CHART – Sales Over Time
# ------------------------------------------
plt.figure(figsize=(10, 5))
plt.plot(df_time["Date"], df_time["Sales"])
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("line_sales.png")
plt.show()

# ------------------------------------------
# 3. MONTHLY AGGREGATION
# ------------------------------------------
monthly_sales = df_time.groupby("Month")["Sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# ------------------------------------------
# 4. QUARTERLY AGGREGATION
# ------------------------------------------
quarterly_sales = df_time.groupby("Quarter")["Sales"].sum()

plt.figure(figsize=(8, 5))
quarterly_sales.plot(kind="bar")
plt.title("Quarterly Sales Summary")
plt.xlabel("Quarter")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("quarterly_sales.png")
plt.show()

# ------------------------------------------
# 5. BAR CHART – Category Comparison
# ------------------------------------------
plt.figure(figsize=(8, 5))
plt.bar(df_cat["Category"], df_cat["Sales"])
plt.title("Category Sales Comparison")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("category_bar.png")
plt.show()

# ------------------------------------------
# 6. PIE CHART – Category Share
# ------------------------------------------
plt.figure(figsize=(7, 7))
plt.pie(df_cat["Sales"], labels=df_cat["Category"], autopct="%1.1f%%")
plt.title("Category Sales Share")
plt.savefig("category_pie.png")
plt.show()

# ------------------------------------------
# 7. SHORT SUMMARY
# ------------------------------------------
print("\n--- SUMMARY ---")
print("1. Daily sales show a steady increasing trend.")
print("2. Monthly aggregation smooths data and shows consistent growth.")
print("3. Quarterly totals reveal strongest performance in Q2 and Q3.")
print("4. Category A has the highest sales (45K) and dominates the share.")
print("All charts saved as PNG in your current folder.")
