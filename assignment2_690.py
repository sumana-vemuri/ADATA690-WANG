#!/usr/bin/env python
# coding: utf-8

# ASSIGNMNET 2

# QUESTION: 
# Write a program that generates 100 random integers between 0 and 9.
# 
# Print them in a 10 by 10 matrix neatly arranged following the format below (numbers can be different but the asterisks * must be included):
# 
# **********************************
# *  5  1  5  6  2  7  8  6  4  2  *
# *  2  3  7  0  6  9  2  4  2  8  *
# *  0  0  8  6  4  1  7  2  7  6  *
# *  0  1  9  0  0  8  5  8  6  8  *
# *  4  1  0  5  5  7  4  6  4  4  *
# *  6  0  2  0  1  9  8  2  3  9  *
# *  4  0  4  8  1  7  6  6  2  1  *
# *  1  7  6  8  5  4  1  9  6  7  *
# *  6  4  7  9  9  3  8  2  6  1  *
# *  9  0  6  4  0  1  0  6  9  9  *
# **********************************
# 
# Note: You can submit either a Python script (.py) or a Jupyter Notebook (.ipynb) file
# 
# Hint: 
# 
# 1)  You can use Python standard library random to generate one random number at a time or you can use NumPy random library to generate 100 random number altogether in one shot. 
# 
# 2)  You are likely to use nested loop - a loop within in another loop since you are dealing with a 10 x 10 matrix.
#     

# In[5]:


import random

# Initializing matrix matrix 
matrix = [] 

# for printing the first part of the sequence with "*"
#34 indicates, the below line of "*" consists of 2 spaces between numbers, i.e.,
#11*2=22 and 10 numbers and 2 *'s, i.e for the left and right pattern of *
#therefore the total number of * are 22+10+2=34
for i in range(34):
    print("*", end="")
#after printing 34 *'s, new line should start
print()

#this loop is for the 10 row entries
for i in range(10):   
    a =[] 
    #this loop is for 10 column entries
    for j in range(10):
        # #for generating random numbers from 1 to 10 and printing as 10*10 matrix
        a.append(random.randrange(10)) 
    matrix.append(a) 

#for printing the matrix given in the question 
for i in range(10): 
    
    #this print statement is for the left side of the sequence containing '*'
    #adding a star before every random number is printed in the matrix
    print("*","", end=" ")
    
##this loop is for columns enteries
    for j in range(10): 
        print(matrix[i][j], end = "  ")
    #this print statement is for printing the random numbers in rows* columns matrix after printing *
    print("*")
   
# for printing the last part of the sequence with "*"
#34 indicates, the below line of "*" consists of 2 spaces between numbers, i.e.,
#11*2=22 and 10 numbers and 2 *'s, i.e for the left and right pattern of *
#therefore the total number of * are 22+10+2=34   
for i in range(34):
    print("*",end="")
print("\r")


# ASSIGNMENT 2

# QUESTION: 
# Write a program that generates 100 random integers between 0 and 9.
# 
# Print them in a 10 by 10 matrix neatly arranged following the format below (numbers can be different but the asterisks * must be included):
# 
# **********************************
# *  5  1  5  6  2  7  8  6  4  2  *
# *  2  3  7  0  6  9  2  4  2  8  *
# *  0  0  8  6  4  1  7  2  7  6  *
# *  0  1  9  0  0  8  5  8  6  8  *
# *  4  1  0  5  5  7  4  6  4  4  *
# *  6  0  2  0  1  9  8  2  3  9  *
# *  4  0  4  8  1  7  6  6  2  1  *
# *  1  7  6  8  5  4  1  9  6  7  *
# *  6  4  7  9  9  3  8  2  6  1  *
# *  9  0  6  4  0  1  0  6  9  9  *
# **********************************
# 
# Note: You can submit either a Python script (.py) or a Jupyter Notebook (.ipynb) file
# 
# Hint: 
# 
# 1)  You can use Python standard library random to generate one random number at a time or you can use NumPy random library to generate 100 random number altogether in one shot. 
# 
# 2)  You are likely to use nested loop - a loop within in another loop since you are dealing with a 10 x 10 matrix.
#     

# METHOD 2: Prompting the user to enter number of rows and columns manually
# in this question, the number of rows and columns asked is 10

# In[6]:


#random library for generating random numbers in the matrix
import random

#asking the user to enter the number of rows and columns
#in this question the number of rows and columns asked is 10
Rows = int(input("Enter the number of rows:")) 
Columns = int(input("Enter the number of columns:")) 
  
# Initializing a matrix where all the rows and columns are stored
matrix = []  

# for printing the first part of the sequence with "*"
#34 indicates, the below line of "*" consists of 2 spaces between numbers, i.e.,
#11*2=22 and 10 numbers and 2 *'s, i.e for the left and right pattern of *
#therefore the total number of * are 22+10+2=34

for i in range(34):
    print("*", end="")
#after printing 34 *'s, new line should start
print()

#this loop is for the row enteries
for i in range(Rows):   
    a =[] 
    #this loop is for columns enteries
    for j in range(Columns):
        #for generating random numbers from 1 to 10 and printing as 10*10 matrix
        a.append(random.randrange(10)) 
    matrix.append(a) 
  

#printing the matrix in the structure given in the question
for i in range(Rows): 
    #this print statement is for the left side of the sequence containing '*'
    #adding a star before every random number is printed in the matrix
    print("*","", end=" ")
    for j in range(Columns): 
        # this print statement is for printing the random numbers in rows* columns matrix after printing *
        print(matrix[i][j], end = "  ")
    #this print statement is for the right side of the sequence containing '*'
    #adding a star after every random number is printed in the matrix
    print("*")
     

# for printing the last part of the sequence with "*"
#34 indicates, the below line of "*" consists of 2 spaces between numbers, i.e.,
#11*2=22 and 10 numbers and 2 *'s, i.e for the left and right pattern of *
#therefore the total number of * are 22+10+2=34
for i in range(34):
    print("*",end="")
print("\r")


# In[ ]:




