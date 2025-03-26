#program using arbitrary function

def f1(*a): #function definition
    
    print(a) #function body

f1(10,20,30,40) #function calling

def sum(*numbers):
    a = 0
    for num in numbers:
        a = a + num
    print("sum =",a )

sum(1,2,3,4,5)
sum(6,7,8)

