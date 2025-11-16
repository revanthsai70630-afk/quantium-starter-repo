# Data Processing for Quantium Project

## Task 2: Pink Morsels Sales Data Processing

This document explains the data processing workflow for Soul Foods Pink Morsels sales analysis.

## Input Data

The project contains three CSV files in the `data/` folder:
- `daily_sales_data_0.csv`
- `daily_sales_data_1.csv`
- `daily_sales_data_2.csv`

### Input Data Format

Each CSV file contains the following fields:
- **product**: Type of morsel (pink morsel, gold morsel, magenta morsel, chartreuse morsel)
- **price**: Price per unit (formatted as $X.XX)
- **quantity**: Number of units sold
- **date**: Date of transaction (YYYY-MM-DD format)
- **region**: Geographic region (north, south, east, west)

## Data Processing Steps

The `process_data.py` script performs the following operations:

### 1. Filter for Pink Morsels
- Reads all three CSV files
- Filters data to include only rows where `product == 'pink morsel'`
- Removes all other product types from the dataset

### 2. Calculate Sales
- Removes the '$' symbol from the price field
- Converts price to float
- Calculates sales: `sales = quantity * price`

### 3. Extract Required Fields
- Keeps only three fields in the output:
  - **sales**: Calculated sales amount
  - **date**: Transaction date
  - **region**: Geographic region

### 4. Combine Data
- Merges data from all three CSV files
- Creates a single consolidated dataset

## Running the Script

### Prerequisites
Make sure you have set up your virtual environment and installed dependencies (see SETUP.md).

### Execution

```bash
# Activate your virtual environment first
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Run the processing script
python process_data.py
```

### Output

The script generates:
- **Output File**: `data/processed_sales_data.csv`
- **Console Output**: Summary statistics including:
  - Total number of processed rows
  - Date range
  - Regions included
  - Total sales amount
  - Average sales per transaction
  - Sales breakdown by region

## Output File Format

The processed CSV file (`processed_sales_data.csv`) contains three columns:

```
sales,date,region
1638.00,2018-02-06,north
1647.00,2018-02-06,south
1731.00,2018-02-06,east
...
```

### Field Descriptions

| Field | Type | Description |
|-------|------|-------------|
| sales | float | Total sales amount (quantity × price) |
| date | string | Transaction date in YYYY-MM-DD format |
| region | string | Geographic region (north, south, east, west) |

## Example Output

Sample of processed data:

| sales | date | region |
|-------|------|--------|
| 1638.00 | 2018-02-06 | north |
| 1647.00 | 2018-02-06 | south |
| 1731.00 | 2018-02-06 | east |
| 1557.00 | 2018-02-06 | west |

## Data Quality Notes

- All Pink Morsel transactions are included
- Other product types (gold, magenta, chartreuse) are excluded
- Sales values are calculated precisely from quantity and price
- No aggregation is performed - each row represents one transaction
- Date format is preserved from source data

## Next Steps

After processing:
1. The processed data is ready for visualization in a Dash application
2. Data can be filtered by region for regional analysis
3. Time-series analysis can be performed using the date field
4. Sales trends can be identified and visualized

## Verification

To verify the processing:
1. Check the output file exists: `data/processed_sales_data.csv`
2. Verify the file has three columns: sales, date, region
3. Confirm all product values were 'pink morsel' (not in output but was filtered)
4. Review summary statistics printed by the script

## Troubleshooting

### Common Issues

**FileNotFoundError**: Make sure you're running the script from the project root directory where the `data/` folder is located.

**ImportError**: Ensure pandas is installed in your virtual environment:
```bash
pip install pandas
```

**Empty Output**: Check that the input CSV files contain 'pink morsel' products.

## Task Completion

This completes Task 2: Data Processing requirements:
- ✅ Three CSV files processed
- ✅ Filtered for Pink Morsels only
- ✅ Sales calculated (quantity × price)
- ✅ Output contains sales, date, and region fields
- ✅ Single formatted output file created

The processed data is now ready for visualization in Task 3!
