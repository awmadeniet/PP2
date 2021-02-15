a = list(input().split())
b = list(input().split())
n = len(a) + len(b)
s = set()
for i in range(len(a)):
    s.add(a[i])
for i in range(len(b)):
    s.add(b[i])
print(n - len(s))