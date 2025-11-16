#!/usr/bin/env python3
"""
Data Processing Script for Quantium Project
Processes Soul Foods transaction data and filters for Pink Morsels.

Author: Quantium Data Analysis Team
Date: 2025-11-16
"""

import pandas as pd
import glob
import os


def process_sales_data():
    """
    Process all CSV files in the data folder:
    1. Filter for 'pink morsel' products only
    2. Calculate sales (quantity * price)
    3. Keep only sales, date, and region columns
    4. Combine all files into one output file
    """
    
    # Get all CSV files from the data folder
    data_files = glob.glob('data/daily_sales_data_*.csv')
    
    if not data_files:
        print("Error: No CSV files found in the data folder.")
        return
    
    print(f"Found {len(data_files)} CSV files to process...")
    
    # List to store dataframes
    all_data = []
    
    # Process each CSV file
    for file in data_files:
        print(f"Processing {file}...")
        
        # Read CSV file
        df = pd.read_csv(file)
        
        # Display original data info
        print(f"  Original rows: {len(df)}")
        
        # Filter for pink morsel only
        df_filtered = df[df['product'] == 'pink morsel'].copy()
        print(f"  After filtering for 'pink morsel': {len(df_filtered)} rows")
        
        # Calculate sales (quantity * price)
        # Remove '$' from price and convert to float
        df_filtered['price'] = df_filtered['price'].str.replace('$', '').astype(float)
        df_filtered['sales'] = df_filtered['quantity'] * df_filtered['price']
        
        # Keep only the required columns: sales, date, region
        df_final = df_filtered[['sales', 'date', 'region']].copy()
        
        # Add to list
        all_data.append(df_final)
    
    # Combine all dataframes
    combined_df = pd.concat(all_data, ignore_index=True)
    
    print(f"\nTotal rows in combined dataset: {len(combined_df)}")
    print(f"\nSample of processed data:")
    print(combined_df.head(10))
    
    # Save to output file
    output_file = 'data/processed_sales_data.csv'
    combined_df.to_csv(output_file, index=False)
    print(f"\nProcessed data saved to: {output_file}")
    
    # Display summary statistics
    print("\n=== Summary Statistics ===")
    print(f"Date range: {combined_df['date'].min()} to {combined_df['date'].max()}")
    print(f"Regions: {combined_df['region'].unique()}")
    print(f"Total sales: ${combined_df['sales'].sum():,.2f}")
    print(f"Average sales per transaction: ${combined_df['sales'].mean():,.2f}")
    print("\nSales by region:")
    print(combined_df.groupby('region')['sales'].sum().sort_values(ascending=False))
    
    return combined_df


if __name__ == '__main__':
    print("Starting data processing...\n")
    processed_data = process_sales_data()
    print("\nData processing complete!")
