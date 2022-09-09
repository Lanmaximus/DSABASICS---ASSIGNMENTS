def a(x, y):
    a1 = len(x)
    a2 = len(y)
    temp = ''
 
    if a1 != a2:
        return 0
 

    temp = x + y

    if (temp.count(y)> 0):
        return 1
    else:
        return 0
 
str1 = "APPLE"
str2 = "PPLEA"
 
if a(str1, str2):
    print ("Are rotations of each other")
else:
    print ("Not rotations of each other")