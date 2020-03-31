#!/usr/bin/env python
# coding: utf-8

# ASSIGNMENT 2.5

# QUESTION 1

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# In[3]:



#importing the library date time
#citation https://codereview.stackexchange.com/questions/201703/find-the-year-when-the-user-will-turn-100
import datetime
#for knowing today's date
now = datetime.datetime.now()
#print(now.year, now.month, now.day)
 
name = input("Hi. Please enter your name: ") 
 
print("Hello", name)

#running a while loop if the number entered is anything other than numerics,
#so that the exception can be caught and an error message will be displayed

while True:
    age = input("Please enter your age: ")
    try:
        age2=int(age)
        break
    except:
        print("enter only numbers, entered val is not integer")
        #continue
print("You are going to be age 100 on the year", (now.year-age2+100))

#age=100-int(age)+2020


# QUESTION 2

# In[ ]:


Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


# In[4]:


number=input("enter a number")
number2=int(number)
#to chceck if number is even, the remainder diveded my 2 should be zero
if(number2%2==0):
    print("the entered number is even ")
else:
    print("the entered number is odd")
if(number2%4==0):
    print("number is multiple of 4")


# In[5]:


num=input("enter a number")
divide=input("enter a number to divide")
if(int(num)%int(divide)==0):
    print("number is divided equally")
else:
    print("number is not divided equally")


# In[ ]:


QUESTION 3


# In[ ]:


Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:

Instead of printing the elements one by one, make a new list that has all 
the elements less than 5 from this list in it and print out this new list.
Write this in one line of Python.
Ask the user for a number and return a list that contains only elements from 
the original list a that are smaller than that number given by the user.


# In[6]:


list1=[1,2,5,6,7,9,1,2,445,4]
#in the question it says 5, so that all the numbers below 5 in the list will be displayed
number= input("enter a number that are smaller than that number given ")
number_int=int(number)
#taking a new empty list to enter the values below the number entered
list2=[]
for i in list1:
    #iterating the list1
    #print(i)
    if i< number_int:
        #if the number is below the number entered, it should append with new list
        list2.append(i)
print("the numbers below the entered number in a list are" )
print(list2)
print("the numbers below the entered number are" )
for j in list2:
    
    print(j)
    


# QUESTION 4

# Create a program that asks the user for a number and
# then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.          For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# In[7]:


number= input("enter a number")
num=int(number)
list2=[]
for i in range(1,11):
    #print(i)
    if(num%i==0):
        list2.append(i)
        #print("The divisors of the number are:",i)
#print(list2)
print("the divisors of the entered number are")
for i in list2:
    print(i)


# QUESTION 5

# Take two lists, say for example these two:
# 
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# In[8]:


#taking 2 lists list1 and list2
list1=[2,4,6,8,10,12,3,6,7,55,77]
list2=[2,5,6,7,8,9,10,11,12,13,14,55,66,99]
#taking a new list to append all the common elements in list1 and list2
list3=[]
for i in list1:
    for j in list2:
        #comparing common elements in list
        if(i==j):
            #appending common elements into new list3
            list3.append(i)
print(list3)
            


# QUESTION 6

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

# In[9]:


#asking the user to enter a string to find if the entered string is palindrome or not
palindromeString=input("enter a string")
#taking a new list to append all the characters to the list
list2=[]
for i in palindromeString:
    #print(i)
    #appending all the characters in the string to list
    list2.append(i)
#print(list2)
#new list to enter the reverse of the string
#performing slicing operation to reverse string and comparing them 
list3=list2[::-1]
if list2==list3:
    print("The entered string is palindrome")
else:
    print("The entered string is not a palindrome")
#print(list2[0:len(list2)])


# list1=[1,2,1]
# list2=list1[::-1]
# print(list1[0:5])
# print(list1[::-1])
# if list1==list2:
#     print("palindrome")
# else:
#     print("not a palindrome")

# In[ ]:




