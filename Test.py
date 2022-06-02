# Write a Pandas program to covert dictionary into Series data structure.
import pandas as pd
d1 = eval(input())
# print(d1)
new_series = pd.Series(d1)
print(new_series)

# Input: {'a' : 0., 'b' : 1., 'c' : 2.}
# Output:
# a    0.0
# b    1.0
# c    2.0
# dtype: float64

# Input: {'col1' : 'Red', 'col2' : 'Blue', 'col3' : 'Green'}
# Output:
# col1      Red
# col2     Blue
# col3    Green
# dtype: object

# Write a Python program to sum all the items in a dictionary.
def Sum(Dict):

	list = []
	for i in Dict:
		list.append(Dict[i])
	final = sum(list)

	return final

dict = eval(input())
print(Sum(dict))

# Input: {'data1':100,'data2':-54,'data3':247}
# Output: 293
# Input: {'Item1':10,'Item2':33,'Item3':24,'Item4':-2,'Item5':20}
# Output: 85

# Write a program in python to display number of lines in a file(“file2.txt”).
file = open("file2.txt","r")
Count = 0

Data = file.read()
List = Data.split("\n")

for i in List:
	if i:
		Count += 1
		
print(Count)

# Input: Welcome
# Hello World
# Python Programming
# Ease of programs
# Predefined methods
# Less lines of code
# Has Many built in packages
# Popular now a days
# Output: 8

# To read n lines from a file named as file1.txt
n = int(input())
file = open("file1.txt","r")
for i in range(n):
	print(file.readline(), end = "")

# Input: 3
# ("Hello", "World")
# [Good Morning]
# (Welcome to Python Class)
# Complete the assignment
# “Due date for submission is tomorrow”
# Output: ("Hello", "World")
# [Good Morning]
# (Welcome to Python Class)

# Write a program to display all the lines in a file “Words.txt” along with line/record number.
file = open("Words.txt", "r")
count = 1
while True:
    data = file.readline()
    if data == "":
        break
    print(count, data)
    count = count + 1
file.close()

# Input: Machine Learning
# Neural Networks
# Python Programming
# Output: 1 Machine Learning

# 2 Neural Networks

# 3 Python Programming

# Write a Python script to print a dictionary where the keys are numbers between 1 and N (both included) and the values are square of keys.
d=dict()
N = int(input())
for x in range(1,N):
    d[x]=x**2
print(d)

# Input: 16
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# Input: 5
# Output: {1: 1, 2: 4, 3: 9, 4: 16}

# Write a Pandas program to drop a 2nd and 4th rows from a specified DataFrame.
# Original DataFrame

# col1 col2 col3

# 0 1 4 7

# 1 4 5 8

# 2 3 6 9

# 3 4 7 0

# 4 5 8 1

import pandas as pd
import numpy as np
d = eval(input())
df = pd.DataFrame(d)
print("New DataFrame after removing 2nd & 4th rows:")
df = df.drop(df.index[[2,4]])
print(df)

# Input: {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
# Output: New DataFrame after removing 2nd & 4th rows:
#    col1  col2  col3
# 0     1     4     7
# 1     4     5     8
# 3     4     7     0