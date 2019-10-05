x = 35 #global namespace
def my_fun():
    x = 55 #defining x in the fuction scope
    return x
print(x) #it will print the global namespace
print(my_fun()) #it will print the x within the function scope
my_fun()
print(x) #it will print the global namespace since it has more priority than the local namespace

#local
lambda x: x**2

#enclosing function locals and global
name = "hello this is a global name"
def greet():
    name = "Marion"

    def hello():
        print("hello " + name)

    hello()
greet()

y = 50
def glob():
    global y
    y = 2000
print("before function call y is: ", y)
glob()
print("after function call y is: ", y)


