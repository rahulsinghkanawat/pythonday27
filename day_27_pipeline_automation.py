# ##python
# import pandas as pd

# # ==========================================
# # 1. LOAD RAW SALES DATA
# # ==========================================

# input_file = r"C:\python 30 days course\day_27\raw_sales.csv"

# df = pd.read_csv(input_file)

# print("Raw data:")
# print(df.head())


# # ==========================================
# # 2. CLEAN CUSTOMER NAME, CITY AND STATE
# # ==========================================

# # Remove extra spaces
# df["Customer_Name"] = (
#     df["Customer_Name"].astype("string").str.strip() .str.replace(r"\s+", " ", regex=True).str.title()
# )

# df["City"] = (
#     df["City"].astype("string").str.strip().str.replace(r"\s+", " ", regex=True).str.title()
# )

# df["State"] = (
#     df["State"].astype("string").str.strip().str.replace(r"\s+", " ", regex=True).str.title()
# )


# # ==========================================
# # 3. REMOVE DUPLICATE ORDERS
# # ==========================================

# # Remove duplicate Order_ID values
# df = df.drop_duplicates(subset=["Order_ID"], keep="first")


# # ==========================================
# # 4. CONVERT NUMERIC COLUMNS PROPERLY
# # ==========================================

# numeric_columns = ["Quantity","Unit_Price","Discount"]

# for column in numeric_columns:
#     df[column] = pd.to_numeric(df[column], errors="coerce")



# # Convert Order_Date to datetime
# df["Order_Date"] = pd.to_datetime(
#     df["Order_Date"],
#     errors="coerce"
# )


# # ==========================================
# # 5. HANDLE MISSING NUMERIC VALUES
# # ==========================================

# df["Quantity"] = df["Quantity"].fillna(0)
# df["Unit_Price"] = df["Unit_Price"].fillna(0)
# df["Discount"] = df["Discount"].fillna(0)


# # ==========================================
# # 6. CALCULATE TOTAL SALES
# # ==========================================

# df["Total_Sales"] = ((df["Quantity"] * df["Unit_Price"])- df["Discount"])

# # Prevent negative sales values
# df["Total_Sales"] = df["Total_Sales"].clip(lower=0)


# # ==========================================
# # 7. CATEGORIZE ORDERS BY VALUE
# # ==========================================

# def categorize_order(value):
#     if value >= 10000:
#         return "High"
#     elif value >= 5000:
#         return "Medium"
#     else:
#         return "Low"


# df["Order_Value_Category"] = df["Total_Sales"].apply(categorize_order)


# # ==========================================
# # 8. CREATE SUMMARY: TOTAL SALES BY CITY
# # ==========================================

# city_summary = (
#     df.groupby("City", as_index=False)["Total_Sales"]
#     .sum()
#     .sort_values("Total_Sales", ascending=False)
# )

# city_summary["Total_Sales"] = city_summary["Total_Sales"].round(2)


# # ==========================================
# # 9. CREATE SUMMARY: TOTAL SALES BY PRODUCT CATEGORY
# # ==========================================

# category_summary = (
#     df.groupby("Product_Category", as_index=False)["Total_Sales"]
#     .sum()
#     .sort_values("Total_Sales", ascending=False)
# )

# category_summary["Total_Sales"] = category_summary["Total_Sales"].round(2)


# # ==========================================
# # 10. EXPORT CLEANED DATA
# # ==========================================

# df.to_csv("cleaned_sales_data.csv",index=False)


# # ==========================================
# # 11. EXPORT SUMMARY REPORTS
# # ==========================================

# city_summary.to_csv(
#     "sales_by_city.csv",
#     index=False
# )

# category_summary.to_csv(
#     "sales_by_product_category.csv",
#     index=False
# )


# # ==========================================
# # 12. DISPLAY RESULTS
# # ==========================================

# print("\nCleaning and automation completed successfully!")

# print("\nSales by City:")
# print(city_summary)

# print("\nSales by Product Category:")
# print(category_summary)

# print("\nFiles created:")
# print("1. cleaned_sales_data.csv")
# print("2. sales_by_city.csv")
# print("3. sales_by_product_category.csv")

import os
folder_name="day_27_project"
os.makedirs(folder_name, exist_ok=True)
print("folder created successfully")
