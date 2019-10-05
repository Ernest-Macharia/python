import re
def multi_re_find(patterns,phrase):
    for pat in patterns:
        print("searching for pattern in {}".format(pat))
        print(re.findall(pat, phrase))
        print("\n")

test_phrase = "sdsd..ssdd..sdddsdd..ssddssdd..dsds..sdddd..dssss"
test_patterns = ["sd*"]

multi_re_find(test_patterns,test_phrase)

