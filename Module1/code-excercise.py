# In a fictional country named Lowtaxland, the income tax is 5%. In another fictional country, Ripoffland, the income tax is 43%. You are given a sample variable named income with the value of 250,000.

# 1. Create two additional variables: lowtaxland_rate with the value of 0.05 (which is the same as 5%) and ripoffland_rate with the value of 0.43 (which is the same as 43%).

# 2. Print to the output the following (all output on a single line):

# Your income is {income} and you would pay {tax amount in Lowtaxland} income tax in Lowtaxland or {tax amount in Ripoffland} income tax in Ripoffland. You would save {difference between the tax amounts} by paying taxes in Lowtaxland!

# Your solution must replace the curly brackets (e.g. {income}) with the actual values (e.g. 250000). The values must be calculated correctly. The tax amount should be calculated as {income * income = 250000.00


# Try to combine the knowledge from all the lectures presented so far to solve this exercise. If it turns out too difficult, take a look at the Hints tab.


#declaring variables
income = 250000.00
lowtaxland = 0.05
ripoffland = 0.43

print("Your income is", income, " and you will pay ", (income * lowtaxland), "income taz in Lowtaxland or", (income * ripoffland), "income tax in Ripoffland You would save", (lowtaxland - ripoffland), "by paying taxes in Lowtaxland")


#Correct Solution


income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43
 
print('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or', income * ripoffland_rate, 'income tax in Ripoffland. You would save', income * ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowtaxland!')