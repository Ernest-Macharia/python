#strings
mystrings = "abahord"
print(mystrings[-1])

#slicing
mystrings1 = "abahord"
print(mystrings1[3:])

mystrings2 = "abahord" #starts from the first character going to but not including the (3) character 
print(mystrings2[:3])

mystrings3 = "abahord"
print(mystrings3[2:6])

mystrings4 = "abahord" #displaying starts from the first character skipping the next character upto the end
print(mystrings4[::2])

mystrings4 = "abahord" #reverses the string
print(mystrings4[::-1])

#Basic methods
u = mystrings.upper() #change the characters to uppercase. Its opposite is .lower
print(u)

v = mystrings.capitalize() #capitalize only the the first character
print(v)

mystr = "I love coding"
x = mystr.split('o') #removes the single items or characters in a string
print(x)

#print formatting
w = "language one: {} language two: {}".format("python","javascript")
print(w)




