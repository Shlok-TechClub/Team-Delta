# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 18:15:04 2020

@author: Admin
"""

y=0
n=0

while True:
    a=int(input("Enter the number: "))
    
    print("The Square of " + str(a) + " is " + str(a*a))
    
    b=(input("Do you want to continue calculations (y/n): "))
    
    if b == "y":
        print ("ok")        

    else:
        print("Thank you")
        break