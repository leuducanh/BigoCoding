s = input()

sum1 = 0
if len(s) == 0 | len(s) == 1:
    curi = ord("a")
    nexti = ord(s[0])
    
    sub = abs(nexti - curi)
    
    sum1 += min(sub, 26-sub)
    
else:
    if s[0] != "a":
        s = "a" + s
    for i in range(len(s)-1):
        curi = ord(s[i])
        nexti = ord(s[i+1])
        sub = abs(nexti - curi)
        sum1 += min(sub, 26-sub)
    
print(sum1)

