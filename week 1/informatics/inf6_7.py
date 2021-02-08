s = input()
f = s.find("h")
l = s.rfind("h")
print(s[0: f] + s[l+1:])