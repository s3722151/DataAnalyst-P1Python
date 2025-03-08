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

#Get data from a csv then convert into a dataframe
#https://www.w3schools.com/python/pandas/pandas_csv.asp
# https://www.w3schools.com/python/pandas/trypandas.asp?filename=demo_pandas_csv
# Where to get data: https://www.kaggle.com/datasets/shivamb/netflix-shows/data

# https://www.w3schools.com/python/pandas/pandas_csv.asp
# import pandas module 
import pandas as pd 
  # creating a data frame 
df = pd.read_csv("netflix_titles.csv") 
print(df.head()) 