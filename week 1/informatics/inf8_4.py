def kva(x, y):
    z = (1**2 + 1**2)**0.5
    if (x <= 1 and y == 0) or (x <= z and y <= z and x >= -z and y >= -z) or (y <= 1 and x == 0):
        return True
x = float(input())
y = float(input())    
if kva(x, y) == True:
    print("YES") 
else:
    print("NO")