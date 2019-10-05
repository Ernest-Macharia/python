#lists
mylists = ['a','b','a','h','o','r','d']
print(mylists[-1])

#slicing
mylists1 = ['a','b','a','h','o','r','d']
print(mylists1[3:])

mylists2 = ['a','b','a','h','o','r','d'] #starts from the first character going to but not including the (3) character 
print(mylists2[:3])

mylists3 = ['a','b','a','h','o','r','d']
print(mylists3[2:6])

mylists4 = ['a','b','a','h','o','r','d'] #displaying starts from the first item skipping the next item upto the end
print(mylists4[::2])

#mutability
mylist = ['a','b','c','d']
print("before assigment: ",mylist)
mylist[0] = "new item"
print("after assigment: ",mylist)

#Basic methods
mylists.append("new item") #adds a new item in a list
print(mylists)

list2 = ['x','y','z']
mylists.extend(list2) #adds a new set of list in an exsisting list
print(mylists)

mylists.reverse() #reverses the items in a list
print(mylists)

thislist = [8,0,57,45,3,9,27,16]
thislist.sort() #arranges the items in a list according to a hierarchy
print(thislist)

item = mylists.pop() #removes an item from a list and returns it
print(mylists)
print(item)

#nested list
nestedlist = [2,6,4,['o','r','w']]
print(nestedlist[3][2]) #returns an item in a nested list

#list comrehension
matrix = [[1,2,3],[3,4,5],[6,7,8]]
firstcol = [row[1] for row in matrix] #retuns an item in every row of a given list
print(firstcol)

