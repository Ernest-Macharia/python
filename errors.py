try:
    f = open("simp.txt","w")
    f.write("test write to simp text")

except IOError:
    print("Error!could not find or read data")
else:
    print("Success!")
print("You can continue writing your code")
