import sys

nut = int(input())
sonut = list(map(int, input().split()))

if nut == 1:
    if sonut[0] == 1:
        print("YES")
    if sonut[0] == 0:
        print("NO")
else:
    count = 0
    for x in range(int(nut)):
        if sonut[x] == 0:
            if count == 1:
                print("NO") 
                sys.exit() 
            count += 1
    if count == 1:
        print("YES")
    else:
        print("NO")
        