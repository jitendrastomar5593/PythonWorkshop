import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


##################################################
#    E X A M P L E - 1 - Scatter plot            #
##################################################

# reading the database
data = pd.read_csv("Module-5\\file2.csv")
# print (data)
# Scatter plot with day against tip
plt.scatter(data['day'], data['tip'], c=data['size'],
            s=data['total_bill'])
 
# Adding Title to the Plot
plt.title("Scatter Plot")
 
# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')

plt.colorbar()

plt.show()


##################################################
#     E X A M P L E - 2 - Line Chart             #
##################################################
data = pd.read_csv("Module-5\\file2.csv")
 
# Scatter plot with day against tip
plt.plot(data['tip'])
plt.plot(data['size'])
 
# Adding Title to the Plot
plt.title("Scatter Plot")
 
# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')
 
plt.show()


##################################################
#     E X A M P L E - 3 - Bar Chart              #
##################################################
# reading the database
data = pd.read_csv("Module-5\\file2.csv")
 
# Bar chart with day against tip
plt.bar(data['day'], data['tip'])
 
plt.title("Bar Chart")
 
# Setting the X and Y labels
plt.xlabel('Day')
plt.ylabel('Tip')
 
# Adding the legends
plt.show()

##################################################
#     E X A M P L E - 4 - Gender Chart           #
##################################################
# reading the database
data = pd.read_csv("Module-5\\file2.csv")

# using Scatter plot
# sns.scatterplot(x='day', y='tip', data=data, hue='Gender')

# using histplot approach
sns.histplot(x='total_bill', data=data, kde=True, hue='Gender')

plt.show()