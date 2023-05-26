import re

f = open("file1.txt", "r")
for x in f:
    y = re.findall("[a-zA-Z0-9.]+@[a-zA-Z]+\.[a-z]{2,4}",x)

    for i in y:
        if i.find(".gmai") == -1 and i.find("daemon@googlemail.com") == -1:
            print(i)




