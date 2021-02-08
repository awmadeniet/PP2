def otr(x1, y1, x2, y2):
    x = abs(x2 - x1)
    y = abs(y2 - y1)
    g = (x**2 + y**2)**0.5
    print(g) 
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
otr(x1, y1, x2, y2)