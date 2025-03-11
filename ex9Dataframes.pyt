#https://www.w3schools.com/python/pandas/pandas_dataframes.asp

# Create a simple dataframe
import pandas as pd
data = {
  "TV Shows": ["Dark", "3 Body Problem", "Squid game"],
  "Rating": [5, 4, 4]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df) 


#Run ALL code below in Juptar Notebook

#Get data from a csv then convert into a dataframe
#https://www.w3schools.com/python/pandas/pandas_csv.asp
# https://www.w3schools.com/python/pandas/trypandas.asp?filename=demo_pandas_csv
# Where to get data: https://www.kaggle.com/datasets/shivamb/netflix-shows/data

import pandas as pd 
dfNetflix = pd.read_csv("netflix_titles.csv") 
print(dfNetflix.head()) 

#How to format data
import numpy as np
import matplotlib as mpl

df = pd.DataFrame({
    "strings": ["Adam", "Mike"],
    "ints": [1, 3],
    "floats": [1.123, 1000.23]
})
df.style \
  .format(precision=3, thousands=".", decimal=",") \
  .format_index(str.upper, axis=1) \
  .relabel_index(["row 1", "row 2"], axis=0)




#Video 1: Create Dataframe & Read from Web
# https://www.youtube.com/watch?v=TKj0mjmSVgQ&t=1sv

#Return the shape of a file: https://youtu.be/TKj0mjmSVgQ?t=631
# (Rows, Columns)
dfNetflix.shape

# This returns the first 5 rows - specify rows in brackets
dfNetflix.head()
 # Note there is indexes (0, 1..)

# Return the last 5 rows 
dfNetflix.tail()




#Video 2: https://www.youtube.com/watch?v=VIa1ETYnFuc
# iloc loc isin Pandas Function

# Get a specific column to be a index
dfNetflix.set_index("director")

# To set an index manually 
dfNetflix = dfNetflix.set_index("director")

#Another way of getting a column 
dfNetflix.director
# This way is better for spaces and multiple columns
dfNetflix["director"]

# Get all columns for a specific row
dfNetflix.loc[1]

# Get 1 column for a specific row
dfNetflix.loc[1,"country"]

# Get 1 row and 1 column
dfNetflix.iloc[0,1]

# Specify a range of rows
dfNetflix.iloc[0:5]
dfNetflix.iloc[:5]

# Specify a range of rows tail
dfNetflix.iloc[-5:]

# To get a range of columns with a specic range of columns
dfNetflix.iloc[-5:, :3]

# Boolean to identify if something is true or false
dfNetflix['type'] == "Movie"

# Boolean to identify if something is true or false - Also return all columns
dfNetflix [ dfNetflix['type'] == "Movie" ]

# Make a range for a dataframe
dfNetflix [ dfNetflix['release_year'] > 2020 ]

# AND conditions
dfNetflix [ (dfNetflix['release_year']>2020) & (dfNetflix['type'] == "TV Show") ]

# OR conditions
dfNetflix [ (dfNetflix['release_year']>2020) | (dfNetflix['type'] == "TV Show") ]

#OR conditions in the same column category 
# This provides easier syntax
dfNetflix [ dfNetflix['director'].isin(['Julien Leclercq', 'Mike Flanagan']) ]





#Video 3: Describe, Info, isnull, Len Functions
# https://www.youtube.com/watch?v=yq9Art2Yu54

#Info shows infor about the distribution about data
# So the different data types and frequency
dfNetflix.info()

dfNetflix.describe()
#To get statistics for all columns
# For each column it will give the count, mean and standard deviation 
# More useful for numerical columns

#To get statistics from 1 column 
# This would be more helpful getting data with numerical columns
dfNetflix['release_year'].describe()

dfNetflix['release_year'].value_counts()
#This counts all categories and frequency they appear in 

#To get average
dfNetflix['release_year'].mean()

#To get average for a specific column 
# Here we look we find the average release year for TV shows
dfNetflix['release_year'].loc[dfNetflix['type'] == 'TV Show'].mean()

#List all unique caretgories belonging to 1 column
dfNetflix['director'].unique().tolist()

#This will store a search value
unique_Directors = dfNetflix['director'].unique().tolist()

#To show all columns
dfNetflix.columns

#Check if anything is null and sum them 
dfNetflix.isnull().sum()

#How long is a dataset
len(dfNetflix)

#This finds the percentage of values that are null for a column
dfNetflix['director'].isnull().sum()/len(dfNetflix)