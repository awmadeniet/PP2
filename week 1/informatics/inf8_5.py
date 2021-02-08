def krug(x, y, xc, yc, r):
    if (x - xc)**2 + (y - yc)**2 <= r**2:
        return True
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
if krug(x, y, xc, yc, r) == True:
    print("YES")
else:
    print("NO")