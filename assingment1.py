# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hmnRTRfizPEbsX3zE7T1Y49H3343fmxr
"""

#Write a program that will find all such numbers that are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.
a=[]
for x in range(2000,3202):
  if (x%7==0) and (x%5!=0):
    a.append(str(x))
print(','.join(a))

#Write a program that can compute the factorial of given numbers. The results should be printed in a comma-separated sequence on a single line.
t=int(input("t: "))
b=[]
c=1
for j in range(0,t):
  x=int(input("num:"))
  for i in range(1,x+1):
    c=c*i
  b.append(str(c))
  c=1
print(','.join(b))

#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included).
#and then the program should print the dictionary.
n=int(input("enter number: "))
dict={}
for i in range(1, n+1):
        dict[i] = i*i
print(dict)

#Write a program that accepts a sequence of comma-separated numbers from the console and generates a list and a tuple that contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')
str1=input("Enter a sequence of comma-separated numbers: ")
list1=str1.split(',')
tuple1=tuple(list1)
print("List:",list1)
print("Tuple:",tuple1)