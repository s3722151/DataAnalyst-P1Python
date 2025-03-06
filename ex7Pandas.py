# https://www.w3schools.com/python/pandas/default.asp

#What is it?
# Pandas is a Python library used for working with data sets.
# Pandas gives you answers about the data. 
#Like:
# Is there a correlation between two or more columns?
# What is average value?
# Max value?
# Min value?

# BELOW won't work as need Jupytar Notebook
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)
