import sys

s = input()
t = input()

arrs = [0] * 26
arrt = [0] * 26
a = ord("a")
for x in range(len(s)):    
    cs = s[x]
    arrs[ord(cs) - a] += 1

for x in range(len(t)):
    ct = t[x]
    arrt[ord(ct) - a] += 1

for x in range(26):
    if arrt[x] != 0 and arrs[x] < arrt[x]:
        print ("need tree")
        sys.exit()
automaton = True

if len(t) == len(s):
    print("array")
    sys.exit()

pos = 0
for x in range(len(t)):
    pos = s.find(t[x],pos,len(s))
    if pos == -1:
        print("both")
        sys.exit()

print("automaton")