#program using nested functions

def ofunc(): #outer function definition
    
    print('this is outer function') #outer function body

    def ifunc():#inner function definition

        print('this is inner function') #inner function body

    ifunc() #inner function calling

ofunc() #outer function calling



