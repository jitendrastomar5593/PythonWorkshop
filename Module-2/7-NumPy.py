# Installation
# pip install NumPy

# Importing NumPy
import numpy as np

##################################################
#               E X A M P L E : 1                #
##################################################
import numpy as np

# working on single array
arr1 = np.array([1, 2, 3, 4])
print (arr1)

# add 2 to every element
print ("Adding 2 to every element:", arr1+2)

# subtract 1 from each element
print ("Subtracting 1 from each element:", arr1-1)

# multiply each element by 10
print ("Multiplying each element by 10:", arr1*10)
 
# square each element
print ("Squaring each element:", arr1**2)
 
# modify existing array
arr1 *= 2
print ("Doubled each element of original array:", arr1)

##################################################
#               E X A M P L E : 2                #
##################################################
import numpy as np
# Creating array object
arr2 = np.array( [[1,2,3],
                  [4,5,6],
                  [7,8,9]])
# print (arr1)
print (arr2[2])             # access row of given INDEX
print (arr2[:3])            # access row(s)

# Printing type of arr object
print("Array type: ", type(arr2))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr2.ndim)

# Printing shape of array
print("Array Shape: ", arr2.shape)

# Printing size of array
print("Size of array: ", arr2.size)


##################################################
#               E X A M P L E : 3                #
##################################################
import numpy as np

# Creating array from "list"
a = np.array([[1, 2, 3], [4, 5, 6]])
print ("Array created using list:\n", a)

# Creating array from "tuple"
b = np.array((1,2,3))
print ("Array created using tuple:\n", b)

# Creating a "3X3 array with all zeros"
c = np.zeros((3,3))
print ("An array initialized with all zeros:\n", c)

# "Reshaping" 3X4 array to 2X2X3 array
arr3 = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
 
newarr = arr3.reshape(2, 2, 3)
 
print ("Original array:\n", arr3)
print ("Reshaped array:\n", newarr)

