def my_func(param1 = "default"): #passing a default parameter to function my_func
    """
    this is a docstring
    """
    print("my first function in python and it has become by {}".format(param1))

my_func() #calling the function

#printing and returning a function

#only printing
def hello():
    print("hy")
hello()
#both returning and printing
def milly():
    return("hello") #by returning you are storing the string for later use
result = milly()
print(result)

#adding 2 numbers
def addNum(num1,num2):
    return num1 + num2
result = addNum(3,7)
print(result)

#adding 2 numbers by using type
def numAdd(num1,num2):
    if type(num1) == type(num2) == type(6):
        return num1 + num2
    else:
        return("sorry you need to convert to integer")
result = numAdd("3","7")
print(result)

#filter function
mylist = [1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2 == 0
evens = filter(even_bool,mylist)
print(list(evens))

#lambda expression
mylist1 = [1,2,3,4]
evens = filter(lambda num: num%2 == 0,mylist1)
print(list(evens))

tweet = "turn to massive #coding"
res = tweet.split("#")[1]
print(res)

#boolean using in
print("x" in [1,2,4,"x"])

