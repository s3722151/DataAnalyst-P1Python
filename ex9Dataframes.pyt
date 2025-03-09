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

#Return the shape of a file: https://youtu.be/TKj0mjmSVgQ?t=631
# (Rows, Columns)
dfNetflix.shape

# This returns the first 5 rows - specify rows in brackets
dfNetflix.head()
 # Note there is indexes (0, 1..)

# Return the last 5 rows 
dfNetflix.tail()

# Get a specific column
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