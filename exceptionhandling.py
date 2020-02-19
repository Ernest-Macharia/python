#example 1
try:
    x = 4/0
except Exception as e:
    print(e)

#example 2
try:
    sum = 0
    file = open("numbers.txt","r")
    for number in file:
        sum = sum + 1/int(number)
    print(sum)
except ZeroDivisionError:
    print("number in file is equal to zero")
except IOError:
    print("The file does not exist")

#throwing exceptions
a = 1
def RaiseError(a):
    if type(a) != type("a"):
        raise ValueError("This is not a string")
try:
    RaiseError(a)
except ValueError as e:
    print(e)

#using assert
def TestCase(a, b):
    assert a < b, "a is greater than b"
try:
    TestCase(3, 1)
except AssertionError as e:
    print(e) 