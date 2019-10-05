import re
patterns = ["term1","term2"]

text = "This is a string with term1 but not the other"

for pattern in patterns:
    print("I am searching for: " + pattern)
    if re.search(pattern,text):
        print("match")
    else:
        print("no match")



