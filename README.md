# Scenario For Task:
We are performing the task for an investment firm that is interested in analyzing the financial health of a list of the top three companies from each sector.
The task is to automate the process of scraping financial data for these companies from a financial data website and store the results for analysis.

## Step: Web Scraping with Selenium:
Python script using libraries such as Selenium and scrape financial data (balance sheets) for each company from a financial data website.
The code scrapes data for each company one by one, using its symbol to navigate to the relevant web pages.

## Step: Data Cleaning and Transformation with Pandas:
After scraping the data, we use Pandas to perform various data cleaning and transformation operations.

### Handling Missing Values:
Identified and handled any missing values in the dataset.
- Determine the presence of missing data in the columns.
- Decide on an appropriate strategy for handling missing data, such as imputation (using mean, median, or forward/backward fill) or removal of rows/columns with missing values.

### Converting Data Types:
We assess the data types of each column in the DataFrame.
- Convert monetary values from string format to numeric by removing symbols like "$" and commas.
- Check if dates are stored as strings and convert them to the datetime format for time-based analysis.

### Data Reshaping:
- Reshape the data so that the metrics (e.g., Total Revenue, Cost of Revenue) become column headers, and the period years (e.g., 9/24/2022) become rows.

### Dealing with Non-Standard Characters:
If there are non-standard characters or symbols in the data that could cause issues during analysis, we instruct to:
- Identify and remove non-numeric like “-” characters or symbols from numeric columns.
- Normalize data entries to ensure consistency.

## Step: Database Operations with Python and SQL:
We perform the following database operations using Python and SQL in a Separate File(Nasdaq_Database_Connection):
- Connect to a database.
- Create a new database(Nasdaq_database).
- Create tables with appropriate columns and data types.
- Alter a table by adding or modifying columns.

## Step: Data Insertion:
After scraping & cleaning the data, we have inserted the final dataset into the database we created earlier using Python and SQL.

## Step: SQL Queries:

### Aggregate Data:
- Use GROUP BY to group data by one or more columns.
- Apply aggregate functions like SUM, AVG, COUNT, etc., to calculate summary statistics.
- Employ the HAVING clause to filter grouped data based on aggregate conditions.

### Select Data:
- Use SELECT statements to retrieve specific columns and rows.
- Apply WHERE clauses to filter data based on specified conditions.
- Use ORDER BY to sort data.
- Utilize TOP to limit the number of rows returned.
