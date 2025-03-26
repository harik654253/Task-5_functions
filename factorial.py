#program to find a factorial 

num = int(input("enter a number to find the factorial:"))

def factorial(x):
    
    if x == 1: #base condition.
        return 1
    else:
        return(x*factorial(x-1))

print("the factorial of", num, "is", factorial(num))
