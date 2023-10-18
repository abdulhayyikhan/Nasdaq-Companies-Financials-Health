#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import pyodbc


# In[36]:


pyodbc.drivers()


# In[37]:


conn = pyodbc.connect(
    Trusted_Connection="Yes",
    Driver='{ODBC Driver 17 for SQL Server}',
    Server="ABDUL-HAI\SQLEXPRESS",
    Database="Nasdaq_database"
)

cursor = conn.cursor()


# In[38]:


csv_file = "E:\Abdul Hai\Personal\Dolphic Analytics\clean_financial_data.csv"
df = pd.read_csv(csv_file)
df.head()


# In[39]:


# Rename the columns
new_column_names = {
    'Period Ending:': 'Period_Ending',
    'Total Revenue': 'Total_Revenue',
    'Cost of Revenue': 'Cost_of_Revenue',
    'Gross Profit': 'Gross_Profit',
    'Research and Development': 'R_and_D',
    'Sales General and Admin': 'Sales_Gen_and_Admin',
    'Non-Recurring Items': 'Non_Recurring_Items',
    'Other Operating Items': 'Other_Operating_Items',
    'Operating Income': 'Operating_Income',
    'Add\'l income/expense items': 'Additional_Income_Expense',
    'Earnings Before Interest and Tax': 'EBIT',
    'Interest Expense': 'Interest_Expense',
    'Earnings Before Tax': 'EBT',
    'Income Tax': 'Income_Tax',
    'Minority Interest': 'Minority_Interest',
    'Equity Earnings/Loss Unconsolidated Subsidiary': 'Equity_Earnings_Loss',
    'Net Income': 'Net_Income',
    'Net Income Applicable to Common Shareholders': 'Net_Income_Common',
    'Symbol': 'Symbol'
}

df.rename(columns=new_column_names, inplace=True)


# In[40]:


df.columns


# In[41]:


cursor.execute("""
    CREATE TABLE Financial_data (
        Period_Ending DATE,
        Total_Revenue FLOAT,
        Cost_of_Revenue FLOAT,
        Gross_Profit FLOAT,
        R_and_D FLOAT,
        Sales_Gen_and_Admin FLOAT,
        Non_Recurring_Items FLOAT,
        Other_Operating_Items FLOAT,
        Operating_Income FLOAT,
        Additional_Income_Expense FLOAT,
        EBIT FLOAT,
        Interest_Expense FLOAT,
        EBT FLOAT,
        Income_Tax FLOAT,
        Minority_Interest FLOAT,
        Equity_Earnings_Loss FLOAT,
        Net_Income FLOAT,
        Net_Income_Common FLOAT,
        Symbol VARCHAR(255)
    )
""")


# In[42]:


for row in df.itertuples():
    cursor.execute('''
    INSERT INTO Nasdaq_database.dbo.Financial_data (
        Period_Ending, Total_Revenue, Cost_of_Revenue, Gross_Profit,
        R_and_D, Sales_Gen_and_Admin, Non_Recurring_Items,
        Other_Operating_Items, Operating_Income, Additional_Income_Expense,
        EBIT, Interest_Expense, EBT, Income_Tax, Minority_Interest,
        Equity_Earnings_Loss, Net_Income, Net_Income_Common, Symbol
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''',
    row.Period_Ending,
    row.Total_Revenue,
    row.Cost_of_Revenue,
    row.Gross_Profit,
    row.R_and_D,
    row.Sales_Gen_and_Admin,
    row.Non_Recurring_Items,
    row.Other_Operating_Items,
    row.Operating_Income,
    row.Additional_Income_Expense,
    row.EBIT,
    row.Interest_Expense,
    row.EBT,
    row.Income_Tax,
    row.Minority_Interest,
    row.Equity_Earnings_Loss,
    row.Net_Income,
    row.Net_Income_Common,
    row.Symbol)
    
conn.commit()

