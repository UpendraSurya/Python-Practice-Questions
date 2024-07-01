#%%
import numpy as np
#%% md
# 1. Basic Operations:
#%%
arr=np.arange(0,10)
print(arr)
#%%
arr2=np.random.rand(3,3)#here we are creating a 2d array with 3 and 3 
print(arr2)
#%%
identity_matrix=np.eye(3)# eye function is used to create a 2d array with ones on the diagonal and zeros elsewhere
print(identity_matrix)
#%%
identity_matrix2=np.eye(3,k=1)#here we have to create a identity matrix of size 3 x 3 with main diagonal shifted by 1
print(identity_matrix2)
#%% md
# 2. Array Manipulations:
#%%
arr_1d=np.arange(6)
print(arr_1d)
#reshaping hr array from 1d to 2d
arr_2d=np.reshape(arr_1d,(3,2))
print(arr_2d)
#%%
#now we will have to flatten the arr_2d to arr1d.
arr1d_flatten=arr_2d.flatten()
print(arr1d_flatten)
#%%
aarray=np.array([1,2,3,3,4,5,6,7])
Aarray=np.array([20,3,0,44,2,22])
#here we are going to concatenate.
concatenated_array=np.concatenate((aarray,Aarray))
print(concatenated_array)
#%%
# Create a 2D array
array_2d = np.array([[0, 1, 2, 3],
                     [4, 5, 6, 7],
                     [8, 9, 10, 11]])

# Extract the elements of the second row
second_row = array_2d[1]
print(second_row)
#%%
# Extract the elements of the third column
third_column = array_2d[:, 2]
print(third_column)
#%%
# Create a 4x4 matrix
matrix_4x4 = np.array([[ 1,  2,  3,  4],
                       [ 5,  6,  7,  8],
                       [ 9, 10, 11, 12],
                       [13, 14, 15, 16]])

# Extract a 2x2 sub-matrix from the center
sub_matrix = matrix_4x4[1:3, 1:3]
print(sub_matrix)
#%% md
# 3. Mathematical Operations:
#%%
operation_array1=np.array([[1,2,3],[4,5,6]])
operation_array2=np.array([[7,8,9],[10,11,12]])

# element addition
addition_matrix=operation_array1+operation_array2
print(addition_matrix)

# element subtraction
subtraction_matrix=operation_array1-operation_array2
print(subtraction_matrix)

# element multiplication
multiplication_matrix=operation_array1*operation_array2
print(multiplication_matrix)

# element division
division_matrix=operation_array1/operation_array2
print(division_matrix)
#%%
# Create an array of numbers
array = np.array([1, 2, 3, 4, 5])

# Calculate sum
sum_array = np.sum(array)
print("Sum of elements:", sum_array)

# Calculate mean
mean_array = np.mean(array)
print("Mean of elements:", mean_array)

# Calculate standard deviation
std_dev_array = np.std(array)
print("Standard deviation of elements:", std_dev_array)

#%%
# Create a random 2D array of shape (5, 5)
array_2d = np.random.randint(1, 10, size=(5, 5))
print(array_2d)

# Compute sum along each row
sum_along_rows = np.sum(array_2d, axis=1)
print(sum_along_rows)

# Compute sum along each column
sum_along_columns = np.sum(array_2d, axis=0)
print(sum_along_columns)

#%% md
# 
#%%
# Generate a random array of shape (5, 5)
random_array = np.random.randint(1, 50, size=(5, 5))
print("\nRandom Array:")
print(random_array)

# Sort along rows
sorted_rows = np.sort(random_array, axis=1)
print("\nSorted along rows:")
print(sorted_rows)

# Sort along columns
sorted_columns = np.sort(random_array, axis=0)
print("\nSorted along columns:")
print(sorted_columns)

#%%
# Create a 2D array
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Create a 1D array to add to each row
add_array = np.array([10, 20, 30])

# Use broadcasting to add add_array to each row of array_2d
result_array = array_2d + add_array[:, np.newaxis]
print(result_array)

#%%
