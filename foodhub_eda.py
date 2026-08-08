#!/usr/bin/env python3
"""
FoodHub Restaurant Order Data Analysis
Author: AI Collaborator (Texas McCombs PGP-AIML Portfolio)
Description: Comprehensive Exploratory Data Analysis (EDA) covering 
             Questions 1 to 6 for the FoodHub project.
"""

# =====================================================================
# 1. ENVIRONMENT SETUP & LIBRARY IMPORTS
# =====================================================================
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configure notebook and plot visualization settings
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

# =====================================================================
# 2. DATA LOADING & STRUCTURAL HEALTH CHECKS
# =====================================================================
# Define path (adjust if using Google Drive or local workspace folder structure)
file_path = 'data/foodhub_order.csv'

if not os.path.exists(file_path):
    # Fallback to current directory if data folder isn't configured
    file_path = 'foodhub_order.csv'

try:
    df = pd.read_csv(file_path)
    print("✓ Dataset successfully loaded!")
except FileNotFoundError:
    print("❌ Error: 'foodhub_order.csv' not found. Creating placeholder dummy data for structural verification...")
    # Generating mock structural data matching the actual schema for execution safeguard
    np.random.seed(42)
    df = pd.DataFrame({
        'order_id': np.random.randint(1477000, 1479000, 1898),
        'customer_id': np.random.randint(50000, 400000, 1898),
        'restaurant_name': np.random.choice(['Hangawi', 'Blue Ribbon Sushi', 'Cafe Habana'], 1898),
        'cuisine_type': np.random.choice(['Korean', 'Japanese', 'Mexican', 'American'], 1898),
        'cost_of_the_order': np.random.uniform(4.47, 35.41, 1898),
        'day_of_the_week': np.random.choice(['Weekday', 'Weekend'], 1898, p=[0.3, 0.7]),
        'rating': np.random.choice(['3', '4', '5', 'Not given'], 1898, p=[0.1, 0.2, 0.3, 0.4]),
        'food_preparation_time': np.random.randint(20, 36, 1898),
        'delivery_time': np.random.randint(15, 31, 1898)
    })

# =====================================================================
# QUESTION 1: Shape Check
# =====================================================================
print("\n=== QUESTION 1: DATA SHAPE ===")
print(f"Total number of rows: {df.shape[0]}")
print(f"Total number of columns: {df.shape[1]}")
print(f"DataFrame dimensions: {df.shape}")

# =====================================================================
# QUESTION 2: Datatypes Validation
# =====================================================================
print("\n=== QUESTION 2: DATA TYPES & MEMORY STRUCTURE ===")
df.info()

# =====================================================================
# QUESTION 3: Missing Value Treatment
# =====================================================================
print("\n=== QUESTION 3: MISSING VALUE ANALYSIS ===")
print(f"Total explicit NaN/Null values in DataFrame: {df.isnull().sum().sum()}")
print("\nMissing values breakdown per field:")
print(df.isnull().sum())

# =====================================================================
# QUESTION 4: Statistical Summaries
# =====================================================================
print("\n=== QUESTION 4: STATISTICAL SUMMARY ===")
prep_stats = df['food_preparation_time'].describe()
print(f"Food Preparation Metrics Summary Table:")
print(prep_stats)
print(f"\nMinimum Food Preparation Time: {prep_stats['min']} minutes")
print(f"Average Food Preparation Time: {prep_stats['mean']:.2f} minutes")
print(f"Maximum Food Preparation Time: {prep_stats['max']} minutes")

# =====================================================================
# QUESTION 5: Unrated Data Trapping
# =====================================================================
print("\n=== QUESTION 5: UNRATED DATA ANALYSIS ===")
unrated_count = (df['rating'] == 'Not given').sum()
unrated_percentage = (unrated_count / len(df)) * 100
print(f"Total orders masked as 'Not given': {unrated_count}")
print(f"Percentage of unrated orders on platform: {unrated_percentage:.2f}%")

# =====================================================================
# QUESTION 6: Univariate Exploration Plots
# =====================================================================
print("\n=== QUESTION 6: EXECUTING UNIVARIATE VISUALIZATIONS ===")

# Plot 1: Distribution of Order Costs ($)
mean_cost = df['cost_of_the_order'].mean()
median_cost = df['cost_of_the_order'].median()
skew_cost = df['cost_of_the_order'].skew()

plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='cost_of_the_order', kde=True, color='teal')
plt.axvline(mean_cost, color='red', linestyle='--', linewidth=2, label=f'Mean: ${mean_cost:.2f}')
plt.axvline(median_cost, color='green', linestyle='-', linewidth=2, label=f'Median: ${median_cost:.2f}')
plt.title('Distribution of Order Costs ($)')
plt.xlabel('Cost of the Order ($)')
plt.ylabel('Frequency (Order Count)')
plt.legend()
plt.tight_layout()
plt.show()

print(f"• Order cost ranges from ${df['cost_of_the_order'].min():.2f} to ${df['cost_of_the_order'].max():.2f}")
print(f"• Skewness score for order cost distribution: {skew_cost:.2f}")

# Plot 2: Distribution of Food Preparation Time
mean_prep = df['food_preparation_time'].mean()
median_prep = df['food_preparation_time'].median()

plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='food_preparation_time', kde=True, bins=16, color='darkorange')
plt.axvline(mean_prep, color='red', linestyle='--', linewidth=2, label=f"Mean: {mean_prep:.2f} min")
plt.axvline(median_prep, color='green', linestyle='-', linewidth=2, label=f"Median: {median_prep:.0f} min")
plt.title('Distribution of Food Preparation Time')
plt.xlabel('Preparation Time (minutes)')
plt.ylabel('Frequency (Order Count)')
plt.legend()
plt.tight_layout()
plt.show()

print("✓ Pipeline execution complete. Visual charts displayed successfully.")
