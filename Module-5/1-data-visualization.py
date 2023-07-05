# Step 1: Install Matplotlib
# pip install matplotlib
# pip install plotly
# pip install seaborn

# Step 2: Import Matplotlib
import matplotlib.pyplot as plt

##################################################
#               E X A M P L E - 1                #
##################################################
# Sample data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Simple Line Plot')

# Display the plot
plt.show()

##################################################
#               E X A M P L E - 2                #
##################################################

plt.plot(x, y, color='red', marker='o', linestyle='--')
plt.title('Squared Values')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

