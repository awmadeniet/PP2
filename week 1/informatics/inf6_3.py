s = input()
if len(s)//2 == len(s)/2:
    n = len(s) /2
    n = int(n)
    print(s[n:] + s[0: n])
else:
    n = len(s) / 2 + 1
    n = int(n)
    print(s[n:] + s[0: n])