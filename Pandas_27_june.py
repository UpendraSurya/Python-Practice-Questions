#%%
import pandas as pd
import numpy as np
# Create a Series from a list
data = [10, 20, 30, 40]
s = pd.Series(data, index=["a", "b", "c", "d"])
print("Series from list:")
print(s)

#%%
# Create a Series from a NumPy array
array_data = np.array([1.1, 2.2, 3.3, 4.4])
s_from_array = pd.Series(array_data, index=["x", "y", "z", "w"])
print("Series from array:")
print(s_from_array)

#%%
# Create a Series from a dictionary
dict_data = {"Apple": 100, "Banana": 200, "Cherry": 300}
s_from_dict = pd.Series(dict_data)
print("Series from dictionary:")
print(s_from_dict)

#%%
print("Index:", s.index)
print("Values:", s.values)
print("Data type:", s.dtype)
print("Size:", s.size)
print("First two elements:", s.head(2))
print("Last two elements:", s.tail(2))
print("Sorted values:", s.sort_values())
print("Mean of the Series:", s.mean())

#%%
data = [5, 10, 15, 20, 25]
s = pd.Series(data, index=["a", "b", "c", "d", "e"])
print("Original Series:")
print(s)

print("Series after addition:")
print(s + 5)

print("Series after multiplication:")
print(s * 2)

print("Elements greater than 10:")
print(s[s > 10])
def square(x):
    return x * x

print("Series after applying function:")
print(s.apply(square))


#%%
data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha"],
    "Age": [24, 27, 22, 32],
    "City": ["Delhi", "Mumbai", "Bangalore", "Chennai"]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Select a column
print("Select Age column:")
print(df["Age"])

# Select multiple columns
print("Select Name and City columns:")
print(df[["Name", "City"]])

# Select rows by index
print("Select first two rows:")
print(df.iloc[:2])

# Select rows by condition
print("Select rows where Age > 25:")
print(df[df["Age"] > 25])
# Add a new column
df["Salary"] = [50000, 60000, 55000, 70000]
print("DataFrame after adding Salary column:")
print(df)

# Drop a column
df = df.drop("City", axis=1)
print("DataFrame after dropping City column:")
print(df)
# Create a DataFrame with missing values
data = {
    "A": [1, 2, None, 4],
    "B": [None, 2, 3, 4],
    "C": [1, None, None, 4]
}
df = pd.DataFrame(data)
print("DataFrame with missing values:")
print(df)

# Fill missing values
df_filled = df.fillna(0)
print("DataFrame after filling missing values:")
print(df_filled)

# Drop rows with missing values
df_dropped = df.dropna()
print("DataFrame after dropping rows with missing values:")
print(df_dropped)

#%%
data = {
    "Name": ["Amit", "Rahul", "Priya", "Sneha", "Vikram"],
    "Department": ["HR", "IT", "HR", "Finance", "IT"],
    "Salary": [50000, 60000, 55000, 70000, 80000]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Group by Department and calculate mean salary
print("Mean salary by department:")
print(df.groupby("Department")["Salary"].mean())

# Group by Department and get summary statistics
print("Summary statistics by department:")
print(df.groupby("Department")["Salary"].describe())
data = {
    "Date": ["2023-01-01", "2023-01-01", "2023-01-02", "2023-01-02"],
    "City": ["Delhi", "Mumbai", "Delhi", "Mumbai"],
    "Sales": [100, 150, 200, 250]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Create a pivot table
pivot = df.pivot_table(values="Sales", index="Date", columns="City", aggfunc="sum")
print("Pivot Table:")
print(pivot)
df1 = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Amit", "Rahul", "Priya"]
})

df2 = pd.DataFrame({
    "ID": [1, 2, 4],
    "Age": [24, 27, 22]
})

# Merge DataFrames
merged_df = pd.merge(df1, df2, on="ID", how="inner")
print("Merged DataFrame (inner join):")
print(merged_df)

# Outer join
merged_df_outer = pd.merge(df1, df2, on="ID", how="outer")
print("Merged DataFrame (outer join):")
print(merged_df_outer)

#%%
date_rng = pd.date_range(start="2023-01-01", end="2023-01-10", freq="D")
df = pd.DataFrame(date_rng, columns=["date"])
df["data"] = np.random.randint(0, 100, size=(len(date_rng)))
df.set_index("date", inplace=True)
print("Time Series DataFrame:")
print(df)

# Resample and aggregate data
print("Resampled Data (Weekly Mean):")
print(df.resample("W").mean())

#%%
arrays = [
    ["A", "A", "B", "B"],
    ["one", "two", "one", "two"]
]
index = pd.MultiIndex.from_arrays(arrays, names=("letter", "number"))
df = pd.DataFrame({"data": [10, 20, 30, 40]}, index=index)
print("Multi-Indexed DataFrame:")
print(df)

# Accessing data
print("Data for index ('A', 'one'):")
print(df.loc[("A", "one")])
