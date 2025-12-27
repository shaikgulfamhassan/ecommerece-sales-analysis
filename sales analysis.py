import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

# --- 1. DATA GENERATION (Mock Data) ---
# This section creates a realistic dataset of 1,000 e-commerce transactions
def generate_data(num_rows=1000):
    np.random.seed(42)
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
    
    data = {
        'Order_ID': np.arange(1001, 1001 + num_rows),
        'Date': [datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(num_rows)],
        'Category': np.random.choice(categories, num_rows),
        'Quantity': np.random.randint(1, 10, num_rows),
        'Unit_Price': np.round(np.random.uniform(10, 500, num_rows), 2),
        'Customer_Rating': np.random.randint(1, 6, num_rows)
    }
    
    df = pd.DataFrame(data)
    df['Total_Sales'] = df['Quantity'] * df['Unit_Price']
    return df

# --- 2. DATA ANALYSIS ---
def analyze_data(df):
    print("--- Data Analytics Report ---\n")
    
    # Insight 1: Total Revenue
    total_revenue = df['Total_Sales'].sum()
    print(f"Total Revenue: ${total_revenue:,.2f}")
    
    # Insight 2: Top Performing Category
    category_sales = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
    print(f"\nTop Performing Category: {category_sales.index[0]} (${category_sales.iloc[0]:,.2f})")
    
    # Insight 3: Average Transaction Value
    avg_transaction = df['Total_Sales'].mean()
    print(f"Average Transaction Value: ${avg_transaction:,.2f}")
    
    return category_sales

# --- 3. VISUALIZATION ---
def plot_data(category_sales):
    plt.figure(figsize=(10, 6))
    sns.barplot(x=category_sales.index, y=category_sales.values, palette="viridis")
    
    plt.title('Total Sales by Product Category (2024)', fontsize=16)
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Total Sales ($)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Save the plot as an image file for the GitHub repo
    plt.savefig('sales_chart.png')
    print("\n[SUCCESS] Chart saved as 'sales_chart.png'")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    df = generate_data()
    category_sales = analyze_data(df)
    plot_data(category_sales)
    # Save processed data to CSV to simulate a "real" output
    df.to_csv('processed_sales_data.csv', index=False)