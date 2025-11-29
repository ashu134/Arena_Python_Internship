#1 Load and Explore Different Datasets

'''
import pandas as pd
df = pd.read_csv("students.csv")   # load CSV file
print(df.head())                  # first 5 rows
print(df.tail())                  # last 5 rows
print(df.info())                  # columns + data types
print(df.describe())              # statistics summary

'''


# 2 Clean Data by Handling Missing Values

'''
# check missing data
print(df.isnull().sum())

# fill missing values
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# drop rows with missing data
df = df.dropna()

# remove duplicates
df = df.drop_duplicates()

'''

#3 Filter and Sort Data Based on Conditions

'''
# Filter students with marks > 80
high_marks = df[df['Marks'] > 80]
print(high_marks)

# Sort values by marks
sorted_df = df.sort_values(by='Marks', ascending=False)
print(sorted_df)

'''

#4 Calculate Basic Statistics on Datasets

'''
print("Mean Marks:", df['Marks'].mean())
print("Highest Marks:", df['Marks'].max())
print("Lowest Marks:", df['Marks'].min())
print("Standard Deviation:", df['Marks'].std())

'''

#5 Group Data and Perform Aggregations

'''
grouped = df.groupby("Class")["Marks"].mean()
print(grouped)

count_students = df.groupby("Class")["Name"].count()
print(count_students)

'''

#6 Create Simple Plots from Data

'''
import matplotlib.pyplot as plt

df['Marks'].plot(kind='bar')
plt.title("Students Marks")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.show()

'''