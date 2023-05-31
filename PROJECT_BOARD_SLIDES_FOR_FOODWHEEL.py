#1 What cuisines does FoodWheel offer?
#The board wants to make sure that FoodWheel offers a wide, diverse, variety of restaurants. Having many different options makes customers more likely to come back. You’ve been provided with a CSV, restaurants.csv , which contains all of the restaurants that partner with FoodWheel.
#Let’s create pie chart showing the different types of cuisines available on FoodWheel.

import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

restaurants = pd.read_csv('restaurants.csv')

print(restaurants.head())

cuisine_options_count = restaurants.cuisine.nunique()

cuisine_counts = restaurants.groupby('cuisine').name.count().reset_index()

print(cuisine_counts)

#2 What cuisines does FoodWheel offer?
#You’ve generated the following table that counts the number of different restaurants for each cuisine that partner with FoodWheel.

restaurants = pd.read_csv('restaurants.csv')

cuisine_counts = restaurants.groupby('cuisine')\
                            .name.count()\
                            .reset_index()

print(cuisine_counts)
cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values

plt.pie(counts, labels=cuisines, autopct='%1.1f%%')
plt.title('What cuisines does FoodWheel offer?')
plt.axis()
plt.show()

#3 Orders Over Time
#FoodWheel is a relatively new startup. They launched in April, and have grown more popular since then. Management suspects that the average order size has increased over time. They’d like you to investigate if this claim is true and answer these questions:
#How has the average order amount changed over time?
#What does this say about the trajectory of the company?

orders = pd.read_csv('orders.csv')
print(orders.head())

date = orders['date']
date_split = date.apply(lambda x: x.split('-')[0])
orders['month'] = date_split

avg_order = orders.groupby('month').price.mean().reset_index()
std_order = orders.groupby('month').price.std().reset_index()

#3.2 Orders Over Time
#You’ve now created two new DataFrames from the orders DataFrame, avg_order, which gives the average amount spent on an order for each month and std_order, which gives the standard deviation for each month. Now it’s time to create a bar chart that uses both of these DataFrames.

ax = plt.subplot()
bar_heights = avg_order['price']
bar_errors = std_order['price']
plt.bar(range(len(bar_heights)),
            bar_heights,
            yerr = bar_errors, capsize = 5)
ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Order')
plt.title('Order over Time')
plt.show()

#4 Customer Types
#There is a range of amounts that customers spend on FoodWheel. Let’s investigate and aim to answer our final question:
#How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?
#A great way to answer this question is to create a histogram of the amount spent by each customer over the past six months.

customer_amount = orders.groupby('customer_id').price.sum().reset_index()
print(customer_amount.head())

plt.hist(customer_amount.price.values, range=(0, 200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Amount')
plt.show()
