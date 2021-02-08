n = int(input())
i = 2
l = 0
ok = False
while i**l <= n:
    if i**l == n:
        ok = True
    l+=1
if ok == True:
    print("YES")
else:
    print("NO")