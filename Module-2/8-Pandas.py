# Installing Pandas
    # pip install pandas

# Importing module
import pandas as pd
import numpy as np

##################################################
#                 S E R I E S                    #
##################################################

# Creating empty series
ser1 = pd.Series()
print(ser1)

# Creating array by using numpy
myarr = np.array(['j','e','e','t','u'])
ser2 = pd.Series(myarr)
print(ser2)
print(ser2[2])

##################################################
#               D A T A  F R A M E               #
##################################################
import pandas as pd

# Calling DataFrame constructor
df = pd.DataFrame()
print(df)

# list of strings
lst = ['WELCOME', 'FROM', 'PBS']
   
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)


# Dataframe Ex: 2
data = {
    'Col1': [1,2,3,4], 
    'Col2': [5,6,7,8]
}
purchases = pd.DataFrame(data)
print(purchases)

# Dataframe Ex: 3 - with indexing
data2 = {
    'Col3': [1,2,3,4], 
    'Col4': [5,6,7,8]
}
purchases = pd.DataFrame(data2, index=['one','two','three','four'])
print(purchases)

# Reading data from CSV file.
csv = pd.read_csv('Module-2\pandas.csv')
print(csv)