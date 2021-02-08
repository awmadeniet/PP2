n = int(input())
a = n
b = int(n**0.5)
for i in range(2, b + 1):
        if n % i == 0:
                if a > i:
                        a = i
print(a)