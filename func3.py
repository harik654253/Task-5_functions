#program using function with multi parameters

def f1(a,b): #function definition
    
    print(a+b) #function body

f1(10,20) #function calling

def f2(a1,b1): 
    
    c = a1+b1
    print("the sum of {},{} is".format(a1,b1),c)

f2(1,10)

def f3(a1 = 7,b1 = 8,c1 = 10): 
    
    sum = a1+b1+c1
    print("the sum of {},{},{} is".format(a1,b1,c1),sum)

f3()
f3(2,10)
f3(b1=50)