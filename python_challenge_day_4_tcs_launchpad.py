# -*- coding: utf-8 -*-
"""Python challenge Day 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uFkFalpod3sOmBaB0gJMOWbQfkjOOG8U
"""

print("Welcome to the python session")
print('Hello World')

print('Hello')
print("World")

print('Hello ',end=" ")
print('world')

print('Hello','World',sep="\n")

a=10
b=20
c=a+b
print(c)
print(type(c))

name=input("Enter your name \n")
print(name)

a=10
b=20.32
print(a+b)

#input will always return a string
a=input()
b=input()
print(a+b)

a=int(input())
b=int(input())
print(a+b)

a=int(input())
b=int(input())
print("{x}+{y}={z}".format(x=a,y=b,z=a+b))#string formatting
print("{x}-{y}={z}".format(x=a,y=b,z=a-b))#string formatting
print("{x}*{y}={z}".format(x=a,y=b,z=a*b))#string formatting
print("{x}/{y}={z}".format(x=a,y=b,z=a/b))#string formatting
print("{x}**{y}={z}".format(x=a,y=b,z=a**b))#string formatting
print("{x}//{y}={z}".format(x=a,y=b,z=a//b))#result is truncated
print("{x}%{y}={z}".format(x=a,y=b,z=a%b))#string formatting

a=int(input())
b=int(input())
print(a*b+a/b)
print(a**b*a)
print(a/b*a)
print(a%b+a)