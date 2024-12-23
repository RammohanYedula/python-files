#1.Local Scope: Variables defined within a function have local scope and are only accessible inside that function.

def my_function():
    x = 10 # local variable
    print(x)
my_function()

#print (x) # This will raise an error since 'x' is not defined outside the function.


#2.Global Scope: Variables defined outside of any function have global scope and can be accessed throughout the entire code.

y = 20 # Globa variabe

def another_function():
    print(y)  # This will access the global variable 'y'

another_function()
print(y)  # This will print 20