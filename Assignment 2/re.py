import re
txt= "aa*bbbb* + aaa*bbb* + aaaa*bb*"

x= re.search("^b.*b",txt)

if x:
    print("There is a match.")
else:
    print("There is no match.")

