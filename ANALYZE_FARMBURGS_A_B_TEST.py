#Brian gives you a CSV of results called clicks.csv. It has the following columns:
#user_id: a unique id for each visitor to the FarmBurg site
#ab_test_group: either A, B, or C depending on which group the visitor was assigned to
#click_day: only filled in if the user clicked on a link to purchase

import codecademylib
import pandas as pd

df = pd.read_csv('clicks.csv')
print(df.head())

#2 Calculating Purchase Rates
#We need to help Brian determine whether or not there is a significant difference in the percent of users who purchased the upgrade package among groups A, B, and C.

df['is_purchase'] = df.click_day.apply(
  lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase')

purchase_counts = df.groupby(['group', 'is_purchase']).user_id.count().reset_index()
print(purchase_counts.head())

#3 Performing a Significance Test
#The data from this A/B test is categorical data.
#Why?
#Because a user’s response can be either "Purchase" or "No Purchase".
#There are more than 2 conditions: users could be in either Group A, Group B, or Group C.
#Recall our table for determining which significance test to use:

from scipy.stats import chi2_contingency
contingency = [[316, 1350],
               [183, 1483],
               [83, 1583]]
#Utilizo Chi cuadrado.

chi2_stat, pvalue, dof, t = chi2_contingency(contingency)
print (pvalue)
#El valor es: 2.41262135467e-35
is_significant = True

#4 Calculating Necessary Purchase Rates
#Let’s assume that num_visits is how many visitors we generally get each week. Given that, calculate the percent of visitors who would need to purchase the upgrade package at each price point ($0.99, $1.99, $4.99) in order to generate Brian’s target of $1,000 per week.

num_visits = len(df)
print(num_visits)

p_clicks_099 = (1000 / 0.99) / num_visits
p_clicks_199 = (1000 / 1.99) / num_visits
p_clicks_499 = (1000 / 4.99) / num_visits
#A más precio, menos paquetes deben venderse para alcanzar el objetivo.
print(p_clicks_099)
print(p_clicks_199)
print(p_clicks_499)

#5 Performing a Significance Test II
#We want to see if the percent of Group A that purchased an upgrade package is significantly greater than p_clicks_099 (the percent of visitors who need to buy an upgrade package at $0.99 in order to make our target of $1,000).
#We are comparing a single set of samples to a target. Our data is still categorical.
#Which type of test should we use?

pvalueA = binom_test(316, 1666, p_clicks_099)
pvalueB = binom_test(183, 1666, p_clicks_199)
pvalueC = binom_test(83, 1666, p_clicks_499)
print(pvalueA)
print(pvalueB)
print(pvalueC)
#pvalueC obtiene un valor significante.

#5.1 What price should Brian charge for the upgrade package?
final_answer = 4.99
