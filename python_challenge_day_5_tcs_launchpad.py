# -*- coding: utf-8 -*-
"""Python challenge Day 5_tcs_launchpad.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GyyZim0_vLLOnApYDPWsJpTYV4R_rT-N
"""

weather=input()
if(weather=="sunny"):
  print("Take sunglass")
if(weather=="rainy"):
  print("Take umbrella")

if(True):
  print("Hello")

if(False):
  print("World")

if(10=="10"):
  print("Equal")

score=58
if(score<80):
  print("Study Well")
print("Good Luck")

score=int(input("Enter your score : "))
if(score<80):
  print("Study well")
else:
  print("Well done")

if 10*10==100:
  print("Correct")

age=int(input("Input your age : "))
if(age<18):
  print("You are a kid")
else:
  print("You are an adult")

score=int(input())
if((score>=90)):
  print("A")
elif score>=80:
  print("B")
elif score>70:
  print("C")
elif(score>60):
  print("D")
else:
  print("F")

scoreeng=int(input("Score for English : "))
scoresci=int(input("Score for Science : "))
if scoreeng<=50 and score<=50:
  print("F")
else:
  print("Passed")