n = int(input())
mapp = dict()
for i in range(n):
    a = input().split()
    mapp[a[0]] = a[1]
    mapp[a[1]] = a[0]
c = input()
if c in mapp:
    print(mapp[c])
   