a = input().split()
s1 = ""
s2 = ""
for i in range(len(a)):
    if a[i] == "0":
        s2 = s2 + " " + str(a[i])
    else:
        s1 = s1 + " " + str(a[i])
print(s1 + s2)