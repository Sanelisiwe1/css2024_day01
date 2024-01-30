#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:38 2024

@author: sanelisiwe
"""

"""
Storing data in Python
1. Lists
2. Dictionaries
3. Data Frames- specific to pandas
"""
import pandas
file = pandas.read_csv("country_data.csv")
print(file)
age1 = 30
age2 = 30
age3 = 29

age = [30,25,29,46,22]
print(age)
[30, 25, 29, 46, 22]

print(age[0])
30
print(min(age))
22
print(max(age))
46
print(sum(age))
152
print(len(age))
5
avg = sum(age)/len(age)
print(avg)
30.4
C2 = "M"
C3 = "M"
C4 = "F"
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

country = ["South Africa","Botswana","South Africa","South Africa","Kenya","Mozambique","Lesotho","Kenya","Kenya","Egypt","Sudan"]
print(country)
print(country[0])
print(country[5])

"""
DO LISTS
"""
my_list = [42, -2021, 6.283,"tau", "node"]
print(my_list)
print(my_list[:])
my_list.append("pi")
print(my_list)
my_list.insert(1,"pi2")



cat: "a cute animal"

mammals = {"cat":"a cute animal","lion":"king of the jungle","elephant":"a gigantic herbivore"}
print(mammals["cat"])

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
Size_nm = ["9.8, 10.1, 13.2, 8.7, 20.5"]
fruit_sizes = {'fruits': fruits, 'sizes': Size_nm}
import pandas as pd
data = {'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
    'gender': ["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
    'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]}

df = pd.DataFrame(data)

print(df)
print(df['age'])
print(df['gender'])
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())
print(df[df['age'] > 30])
print(df[1:4])
df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(df)
df.drop(columns=['new_column'], inplace=True)
print(df)














