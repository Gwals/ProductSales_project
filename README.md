# Product Sales Analysis
## Project Overview
The project aims to identify the most effective sales approach among three methods (Email, Call, and Email+Call) for Pens and Printers Company, which specializes in office stationery. The company tested these methods on a new line of office stationery and provided six weeks of data 
following the product launch.

## Data Source
The primary data source used for this project is 'product_sales.csv' containing information about customers approached by different methods.

## Tools
- Pandas- data cleaning
- Python searbon- data visualization
- Python Jupyter

## Data cleaning
- Handling missing values
- Handling inconsistant naming

## Exploratory Data Analysis
We need to know:
 - How many customers were there for each approach?
 - What does the spread of the revenue look like overall? And for each method?
 - Was there any difference in revenue over time for each of the methods?
 - Based on the data, which method would you recommend we continue to use? Some
of these methods take more time from the team so they may not be the best for us
to use if the results are similar

# Data Analysis
language used: Python

## Validate and clean data
```python
product_sales=product_sales.fillna(0)
product_sales['sales_method']=product_sales['sales_method'].replace(['em + call', 'email'], ['Email + Call', 'Email'])
print(product_sales)
```


## How many customers were there for each approach?
```python
customers_for_each_method=product_sales['sales_method'].value_counts()
print(customers_for_each_method)
```

## sum of revenues for each sales category
```python
print(product_sales.groupby('sales_method')['revenue'].sum())
```

## Findings/Results

- For Call method most customers spent less on products, with fewer customers spending more.
- For Email method most customers spent less on products, with fewer customers spending more. There are few customers who spent significantly more than than the majority.
- For Email + Call method most customers spent more on products, with fewer customers spending less on product

![each_method_boxplot](https://github.com/user-attachments/assets/318e7fc7-e9c0-4324-877c-57843f4974d9)

![lineplot](https://github.com/user-attachments/assets/3f1d57f4-4616-48ef-9e46-b6d62773ad76)

## Recomendations
- Based on the analysis the following is recommended:
 - the Email + Call method is recommended for its consistent average revenue growth, making it the most effective sales strategy over time.
