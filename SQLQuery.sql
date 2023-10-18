SELECT * FROM Financial_data

--Calculate Total Revenue and Cost of Revenue by Symbol:
Select Symbol,
	SUM (Total_Revenue) AS TotalRevenue,
    SUM (Cost_of_Revenue) AS CostOfRevenue
From Financial_data
GROUP BY Symbol;

--Calculate Average Gross Profit by Symbol:
SELECT Symbol,
       AVG (Gross_Profit) AS AverageGrossProfit
FROM Financial_data
GROUP BY Symbol;

--Count the Number of Year Records by Symbol:
SELECT Symbol,
       COUNT(*) AS YearRecordCount
FROM Financial_data
GROUP BY Symbol;

--Filter Groups Based on Aggregate Conditions (HAVING Clause):
SELECT Symbol,
       SUM(Total_Revenue) AS RevOverFiveHundredMillion
FROM Financial_data
GROUP BY Symbol
HAVING SUM(Total_Revenue) > 500000000;

--To sort the result set in ascending order by a "Period Ending":
SELECT *
FROM Financial_data
ORDER BY Period_Ending ASC;

--To sort the result set in descending order by a specific column "Total Revenue":
SELECT *
FROM Financial_data
ORDER BY Total_Revenue DESC;

--Top 5 Companies with the Highest Total Revenue
SELECT TOP 5
    Symbol,
    SUM(Total_Revenue) AS TotalRevenueSum
FROM Financial_data
GROUP BY Symbol
ORDER BY TotalRevenueSum DESC;

--Company that Paid the Most Income Tax
SELECT TOP 1
    Symbol,
    SUM(Income_Tax) AS TotalIncomeTax
FROM Financial_data
GROUP BY Symbol
ORDER BY TotalIncomeTax DESC;

--The Average Revenue for Each Year
SELECT YEAR(Period_Ending) AS Year,
       AVG(Total_Revenue) AS AverageRevenue
FROM Financial_data
GROUP BY YEAR(Period_Ending)
ORDER BY Year;

--Companies with Highest Gross Profit Margin:
SELECT Symbol,
       ROUND((SUM(Gross_Profit) / SUM(Total_Revenue)) * 100, 2) AS GrossProfitMargin
FROM Financial_data
GROUP BY Symbol
ORDER BY GrossProfitMargin DESC;