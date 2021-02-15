a = list((input()).split())
minim = 1000001
for i in range(len(a)):
    if int(a[i]) > 0 and int(a[i]) < minim:
        minim = min(minim, int(a[i]))
print(minim)