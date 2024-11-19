
import pandas as pd

# read excel 
file = 'DataScience/sample3.xlsx'
df = pd.read_excel(file)

# read csv

file = 'DataScience/username.csv'
df = pd.read_csv(file)

# data frame with with dictionaries

students = {
    "John": ["Math", "Science", "English"],
    "Emily": ["History", "Biology", "French"],
    "Michael": ["Computer Science", "Physics", "Spanish"],
    "Sarah": ["English", "Math", "Art"],
    "David": ["Biology", "Chemistry", "Music"],
    "Jessica": ["History", "Geography", "Drama"],
    "Kevin": ["Computer Science", "Electronics", "Photography"],
    "Laura": ["English", "French", "Theater"],
    "Chris": ["Math", "Physics", "Robotics"],
    "Olivia": ["Biology", "Environmental Science", "Graphic Design"]
}
df = pd.DataFrame(students)

# data frame with with tuples 

data = [
    ("John", 25, "Software Engineer", "USA", "California", "San Jose", "Male", "2022-01-01"),
    ("Jane", 30, "Data Scientist", "Canada", "Toronto", "Ontario", "Female", "2020-06-15"),
    ("Bob", 28, "DevOps Engineer", "UK", "London", "England", "Male", "2019-03-22"),
    ("Alice", 22, "Junior Developer", "Germany", "Berlin", "Berlin", "Female", "2021-09-10"),
    ("Mike", 35, "Full Stack Developer", "Australia", "Sydney", "New South Wales", "Male", "2018-11-25"),
    ("Emily", 29, "UX Designer", "France", "Paris", "Île-de-France", "Female", "2020-02-14"),
    ("David", 32, "Backend Developer", "Japan", "Tokyo", "Tokyo", "Male", "2017-05-01"),
    ("Sarah", 26, "Frontend Developer", "India", "Mumbai", "Maharashtra", "Female", "2021-04-01"),
    ("Tom", 38, "Dev Manager", "China", "Shanghai", "Shanghai", "Male", "2015-08-15"),
]
df = pd.DataFrame(data, columns=["Name", "Age", "Job Title", "Country", "City", "State", "Gender", "Start Date"])

# read csv

file = 'DataScience/sample2.xlsx'
df = pd.read_excel(file)
print(df)


# operations on data frame 

# 1. number of rows and columns


# print("Number of rows:", df.shape[0])
# print("Number of columns:", df.shape[1])

r,c = df.shape
print("Number of rows:", r)
print("Number of columns:", c)

# 2. retrieving data using head and tail


print(df.head())  # first 5 rows
print("########################")
print(df.tail())  # last 5 rows
print("########################")
print(df.head(3))
print(df.tail(3))
print("########################")

# 3. slicing

print(df[2:4])

print(df[0::3]) # display alternat rows

print(df[5:0:-1]) # reverse ordering

# 4. retrieving columns

print(df.columns) # display columns

print(df[['Order ID', 'Order Date']])

# 5. finding maximum and minimum values

print(f"Maximum Profit = {df['Profit'].max()}")
print(f"Minimum Profit = {df['Profit'].min()}")

# 6. display statistical information

print(df.describe())
print("################################")
# 7. performing queries

print(df[df['Profit'] > 10000])

print("################################")
print(df[df['Order Quantity'] ==  1])

print(df[['Order ID', 'Order Quantity']][df['Order Quantity'] ==  1])

print(df.index)
df = df.set_index('Order ID')
print(df)

print(df.loc[388]) # locate data using order id 

# df = df.set_index(inplace=True) # reset index to auto-generated

# 8. sorting data

df = df.sort_values('Customer Name') # in ascending order
df = df.sort_values('Customer Name', ascending=False) # in descending order

# sort multiple

df = df.sort_values(by=['Order ID', 'Customer Name'], ascending=[False, True])

print(df)

# 9. Handling missing data

df = df.fillna(0) # replace NaN values with 0
df = df.fillna({'Order ID': 0, 'Customer Name':'Missing Customer Name', 'Sales':0, 'Unit Price':0, 'Ship Mode':'Unknown'}) 

df = df.dropna() # drop missing data
print(df)