import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

product_sales=pd.read_csv(r'C:/Users/Hlobisile/OneDrive\Desktop/achievements/practical_project/product_sales.csv')

# Validate and clean data
product_sales=product_sales.fillna(0)
product_sales['sales_method']=product_sales['sales_method'].replace(['em + call', 'email'], ['Email + Call', 'Email'])
print(product_sales)

# How many customers were there for each approach?
customers_for_each_method=product_sales['sales_method'].value_counts()
print(customers_for_each_method)
sns.countplot(x='sales_method', data=product_sales, order=['Email', 'Call', 'Email + Call'])
plt.show()

# boxplot for overall revenue
print(product_sales['revenue'].describe())
sns.boxplot(data=product_sales, y='revenue')
plt.show()

# Calculate the statistic for each sales method and What does the spread of the revenue look like each method?
print(product_sales.groupby('sales_method')['revenue'].describe())
sns.boxplot(x='sales_method', y='revenue', data=product_sales, order=['Call', 'Email', 'Email + Call'])
plt.show()

# boxplot for overall revenue
sns.histplot(data=product_sales, x='revenue')
plt.show()

# histogram of the week distribution for each sales method
sns.lineplot(data=product_sales, x='week', y='revenue', hue='sales_method')
plt.show()

# number of sites visit for each sales method
sns.lineplot(data=product_sales, x='week', y='revenue')
plt.show()

# sum of revenues for each sales category
print(product_sales.groupby('sales_method')['revenue'].sum()) 

