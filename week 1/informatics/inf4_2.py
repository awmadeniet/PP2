a = int(input())
b = int(input())
gg = a
if b >= a:
    for i in range(a, b+1):
        print(i, end=" ")
elif b == 0: 
    for i in range(0, a+1):
        print(gg, end=" ")
        gg-=1
elif b < 0:
    for i in range(a+abs(b)+1):
        print(gg, end=" ")
        gg-=1
else:
    for i in range(a-b+1):
        print(gg, end=" ")
        gg-=1