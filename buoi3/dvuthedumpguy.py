import sys

nhap1 = list(map(int, input().split()))
nhap2 = list(map(int, input().split()))

nhap2.sort()

total = 0
temphour = nhap1[1]
for x in range (nhap1[0]):
    total += nhap2[x]*temphour
    temphour = temphour - 1 if temphour > 2 else 1

print(str(total))
