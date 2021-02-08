s = input()
cnt = s.find(" ")
cnt = int(cnt)
print(s[cnt+1:], s[0: cnt])