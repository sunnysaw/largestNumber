"""
In this block of code we will see how to find largest among two number.
_________________________________________________________________________
Question : In given two number find the largest number among both of them.
_______________________________________________________________________________
Approach : first we take two number as a input and them compare both of them with each other and then print the largest
           number.
"""
A = int(input("Enter the first number : "))
B = int(input("Entre the second number : "))
if(A > B):
    print("Greater number is : " , A)
else:
    if(B > A):
        print("Greater number is : " , B)