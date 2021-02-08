def kva(x, y):
    if x <= 1 and x >= -1 and y <= 1 and y >= -1:
        return True
x = float(input())
y = float(input())    
if kva(x, y) == True:
    print("YES") 
else:
    print("NO")