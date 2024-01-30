#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:12:50 2024

@author: sanelisiwe
"""

import pandas
file = pandas.read_csv("country_data.csv")
print(file)
print(file.info())

print(file.describe())

import pandas
file = pandas.read_csv("iris.csv")
print(file)
print(file.info())
print(file.describe())

import pandas
file = pandas.read_csv("diab_data.csv")
print(file)
print(file.info())
print(file.describe())

import pandas
print(file)
file = pandas.read_csv("insurance_data.csv",skiprows=5)
print(file)
print(file.info())
print(file.describe())

file = pandas.read_csv("housing_data.csv")
print(file)




print(file.info())
column_names = ("A","B","C")
print(column_names)
file = pandas.read_csv("housing_data.csv",names = comlumn_names)