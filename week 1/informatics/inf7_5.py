n = int(input())
i = 2
l = 0
while i**l <= n+100:
    if i**l >= n:
        print(l)
        exit()
    l+=1