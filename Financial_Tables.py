#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
from IPython.display import display


# In[4]:


def initialize_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

def accept_cookies(driver):
    try:
        cookie = driver.find_element("id", "onetrust-accept-btn-handler")
        cookie.click()
    except Exception as e:
        print(f"Error accepting cookies: {str(e)}")

def navigate_to_url(driver, url):
    driver.get(url)
    time.sleep(2)

def extract_table_data(driver):
    # Find the table element using XPath
    table = driver.find_element("xpath", "//table[@class='financials__table']")
    soup = BeautifulSoup(table.get_attribute('outerHTML'), "html.parser")

    # Initialize empty lists to store row headers and table data
    row_headers = []
    table_data = []

    # Find all rows in the table
    table_rows = soup.find_all('tr')

    for row in table_rows:
        # Extract the data cells in the row
        row_data = [cell.text.strip() for cell in row.find_all(['th', 'td'])]
        table_data.append(row_data)

    # Assume the first row contains headers
    headers = table_data[0]
    table_data = table_data[1:]

    return headers, table_data

def create_dataframe(headers, table_data):
    # Create a DataFrame from the table data
    df = pd.DataFrame(table_data, columns=headers)
    return df

def transpose_dataframe(df):
    # Transpose the DataFrame
    df_transposed = df.transpose()
    df_transposed.columns = df_transposed.iloc[0].astype(str)
    df_transposed = df_transposed.drop(df_transposed.index[0])
    return df_transposed

def scrape_and_process_financial_data(symbol, url):
    driver = initialize_driver()
    navigate_to_url(driver, url)
    accept_cookies(driver)

    # Extract and create DataFrame
    headers, table_data = extract_table_data(driver)
    df = create_dataframe(headers, table_data)
    
    df_transposed = transpose_dataframe(df)
    df_transposed["Symbol"] = symbol
    
    driver.delete_all_cookies()
    driver.quit()
    
    return df_transposed


# In[5]:


if __name__ == "__main__":
    # List of companies and their URLs
    companies = [
        {"symbol": "AAPL", "url": "https://www.nasdaq.com/market-activity/stocks/aapl/financials"},
        {"symbol": "MSFT", "url": "https://www.nasdaq.com/market-activity/stocks/msft/financials"},
        {"symbol": "GOOG", "url": "https://www.nasdaq.com/market-activity/stocks/goog/financials"},
        {"symbol": "CSCO", "url": "https://www.nasdaq.com/market-activity/stocks/csco/financials"},
        {"symbol": "CMCSA", "url": "https://www.nasdaq.com/market-activity/stocks/cmcsa/financials"},
        {"symbol": "TBC", "url": "https://www.nasdaq.com/market-activity/stocks/tbc/financials"},
        {"symbol": "LLY", "url": "https://www.nasdaq.com/market-activity/stocks/lly/financials"},
        {"symbol": "UNH", "url": "https://www.nasdaq.com/market-activity/stocks/unh/financials"},
        {"symbol": "NVO", "url": "https://www.nasdaq.com/market-activity/stocks/nvo/financials"},
        {"symbol": "HSBC", "url": "https://www.nasdaq.com/market-activity/stocks/hsbc/financials"},
        {"symbol": "JPM", "url": "https://www.nasdaq.com/market-activity/stocks/jpm/financials"},
        {"symbol": "MS", "url": "https://www.nasdaq.com/market-activity/stocks/ms/financials"},
        {"symbol": "PLD", "url": "https://www.nasdaq.com/market-activity/stocks/pld/financials"},
        {"symbol": "AMT", "url": "https://www.nasdaq.com/market-activity/stocks/amt/financials"},
        {"symbol": "EQIX", "url": "https://www.nasdaq.com/market-activity/stocks/eqix/financials"},
        {"symbol": "AMZN", "url": "https://www.nasdaq.com/market-activity/stocks/amzn/financials"},
        {"symbol": "V", "url": "https://www.nasdaq.com/market-activity/stocks/v/financials"},
        {"symbol": "WMT", "url": "https://www.nasdaq.com/market-activity/stocks/wmt/financials"},
        {"symbol": "KO", "url": "https://www.nasdaq.com/market-activity/stocks/ko/financials"},
        {"symbol": "SONY", "url": "https://www.nasdaq.com/market-activity/stocks/sony/financials"},
        {"symbol": "MDLZ", "url": "https://www.nasdaq.com/market-activity/stocks/mdlz/financials"},
        {"symbol": "TMO", "url": "https://www.nasdaq.com/market-activity/stocks/tmo/financials"},
        {"symbol": "LIN", "url": "https://www.nasdaq.com/market-activity/stocks/lin/financials"},
        {"symbol": "DHR", "url": "https://www.nasdaq.com/market-activity/stocks/dhr/financials"},
        {"symbol": "NEM", "url": "https://www.nasdaq.com/market-activity/stocks/nem/financials"},
        {"symbol": "GOLD", "url": "https://www.nasdaq.com/market-activity/stocks/gold/financials"},
        {"symbol": "SHEL", "url": "https://www.nasdaq.com/market-activity/stocks/shel/financials"},
        {"symbol": "CVX", "url": "https://www.nasdaq.com/market-activity/stocks/cvx/financials"},
        {"symbol": "COP", "url": "https://www.nasdaq.com/market-activity/stocks/cop/financials"},
        {"symbol": "NGG", "url": "https://www.nasdaq.com/market-activity/stocks/ngg/financials"},
        {"symbol": "NEE", "url": "https://www.nasdaq.com/market-activity/stocks/nee/financials"},
        {"symbol": "EPD", "url": "https://www.nasdaq.com/market-activity/stocks/epd/financials"},
        # Add more companies with their symbols and URLs
    ]
    
    # Initialize an empty dictionary to store scraped data for each company
    scraped_data = {}

    # Loop through the list of companies and scrape their financial data
    for company in companies:
        symbol = company["symbol"]
        url = company["url"]
        
        financial_data = scrape_and_process_financial_data(symbol, url)
        
        # Store the scraped data in the dictionary
        scraped_data[symbol] = financial_data
        
        print(f"Financial Data for {symbol}:")
        display(financial_data)


# In[65]:


# if __name__ == "__main__":
#     driver = initialize_driver()
#     url = "https://www.nasdaq.com/market-activity/stocks/msft/financials"
#     navigate_to_url(driver, url)
#     accept_cookies(driver)

#     # Extract and create DataFrame
#     headers, table_data = extract_table_data(driver)
#     df_msft = create_dataframe(headers, table_data)
    
#     df_msft_transposed = transpose_dataframe(df_msft)
#     df_msft_transposed["Symbol"] = "MSFT"
    
# df_msft_transposed


# In[37]:


# Initialize an empty list to store DataFrames for each company
all_dataframes = []

# Loop through the scraped data and append DataFrames for each company to the list
for symbol, data in scraped_data.items():
    all_dataframes.append(data)

# Concatenate all DataFrames into a single DataFrame vertically (row-wise)
combined_df = pd.concat(all_dataframes)

# Display the combined DataFrame
display(combined_df)


# In[38]:


combined_df.info()


# In[39]:


# Replace custom placeholders with NaN
combined_df.replace(['--', 'N/A', 'NA', ''], pd.NA, inplace=True)

# Now, check for missing values
missing_data = combined_df.isna()

missing_data


# In[40]:


combined_df.drop(columns=['Operating Expenses','Net Income-Cont. Operations'], inplace=True)

combined_df


# In[41]:


# List of columns to convert to numeric data type
columns_to_convert = [
    'Total Revenue', 'Cost of Revenue', 'Gross Profit', 'Research and Development',
    'Sales, General and Admin.', 'Non-Recurring Items',
    'Other Operating Items', 'Operating Income', "Add'l income/expense items",
    'Earnings Before Interest and Tax', 'Interest Expense', 'Earnings Before Tax',
    'Income Tax', 'Minority Interest', 'Equity Earnings/Loss Unconsolidated Subsidiary',
    'Net Income', 'Net Income Applicable to Common Shareholders'
]

# Loop through the specified columns and convert them to 'float'
for col in columns_to_convert:
    combined_df[col] = pd.to_numeric(combined_df[col].str.replace('$', '').str.replace(',', ''), errors='coerce')

# Now, the specified columns have been converted to 'float' data type.


# In[42]:


combined_df.info()


# In[43]:


combined_df.index = pd.to_datetime(combined_df.index)
combined_df


# In[44]:


# Function to clean a column (remove non-numeric characters)
def clean_numeric_column(column):
    return column.astype(str).str.replace('[^\d.]', '', regex=True)

# Loop through the specified numeric columns and clean them
for col in columns_to_convert:
    combined_df[col] = clean_numeric_column(combined_df[col])

# Convert the cleaned columns to numeric data type
combined_df[columns_to_convert] = combined_df[columns_to_convert].apply(pd.to_numeric)

# Now, non-numeric characters like "-" have been removed from the specified numeric columns.
combined_df


# In[45]:


# Check for missing data in each column
missing_data = combined_df.isna().any()

# Print columns with missing data
print("Columns with missing data:")
print(missing_data[missing_data].index.tolist())

# Determine the percentage of missing data in each column
missing_percentage = (combined_df.isna().sum() / len(combined_df)) * 100

# Print columns with their corresponding missing percentages
print("\nMissing data percentages:")
print(missing_percentage[missing_data].sort_values(ascending=False))


# In[46]:


# Replace NaN values with 0 in the specified columns
combined_df[columns_to_convert] = combined_df[columns_to_convert].fillna(0)
combined_df


# In[47]:


# Remove commas and full-stops from column headers
combined_df.columns = combined_df.columns.str.replace('[,.]', '', regex=True)

# Now, combined_df has column headers with commas and full-stops removed
combined_df


# In[49]:


file_path = 'E:\Abdul Hai\Personal\Dolphic Analytics\clean_financial_data.csv'
combined_df.index.name = 'Period Ending:'

# Use the to_csv() method to save the DataFrame to a CSV file
combined_df.to_csv(file_path, index=True, header=True)


# In[ ]:




