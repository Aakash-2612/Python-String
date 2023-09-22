str1 = "123456789"
str2 = ""
for i in range(len(str1)):
    if(int(str1[i])%2 == 0):
        str2 += str1[i]
        str2 += "$"

print(str2)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
str3 = ""   
for i in list1:
    if(i%2 == 0):
        str3 += str(i)
        str3 += "$"

print(str3)