#if statements
if 2 < 5:
    print("first block")
    if 24 < 7:
        print("second block")

#if else statements
if 2 > 5:
    print("first block")
else:
    print("second block")

#elif statements
if 2 > 5:
    print("first block")
elif 3 == 3:
    print("middle block")
else:
    print("second block")

#for loops
#in a list
seq = [1,2,3] #for loop in a list
for item in seq:
    print(item)
    print("each item")
#in a dictionary
structures = {'lists':1,'dictionaries':2,'sets':3,'tuples':4} #for loop in a dictionary
for item in structures:
    print(item) #prints the keys
    print(structures[item]) #prints both the keys and values

#in a tuple
mytuple = [(1,2),(3,4),(5,6)] #for loop in a tuple
for item in mytuple:
    print(item)

mytuple1 = [(1,2),(3,4),(5,6)] #for loop in a tuple
for (tup1,tup2) in mytuple1: #tuple unpacking
    print(tup1)
    print(tup2)

#while loops
i = 1
while i < 4:
    print("the value of i is: {}".format(i))
    i = i + 1

#using range
for item in range(4):
    print(item)
    
#list comprehension
x = [1,2,3,4]

y = []
for num in x:
    y.append(num ** 2)
print(y)

# another way to write list comprehension
x = [1,2,3,4]
y = [num**2 for num in x]
print(y)