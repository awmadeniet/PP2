p = float(input())
x = float(input())
y = float(input())
gg = (x * p) / 100 
gg = gg + x
if gg == int(gg):
    print(gg, "0")
else:
    k = gg * 100
    l = k % 100
    print(int(gg), int(l))