#program using keyarguments function

def f1(**name): #function definition
    
    print(name) #function body

f1(name='hari',place='rjy') #function calling



def f2(first_name,last_name):
    
    print("first name",first_name)
    print("last name",last_name)

f2(first_name = 'hari',last_name = 'krishna')