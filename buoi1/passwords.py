import sys

nhap = list(map(int, input().split()))

n = nhap[0]
k = nhap[1]

arr = [0] * 101
for x in range(n):
    s = input()
    arr[len(s)] += 1
righpass = input()

worstcase = 0
bestcase = 0
buff = 0
kcount = 0
for x in range(len(righpass)):
    if arr[x] != 0:
        temp = kcount + arr[x]
        buff += temp//k * 5
        buff += arr[x]
        kcount = 0 if (temp % k == 0) else (temp % k)
worstcase = buff
bestcase = buff

worstcase +=  (arr[len(righpass)])
lastround = (kcount + arr[len(righpass)]) // k
sodu = (kcount + arr[len(righpass)]) % k
worstcase += 5 * (lastround if sodu != 0 else lastround -1 )
if kcount + 1 == k:
    bestcase += 1
else:
    bestcase += 1
print(str(bestcase) + " " + str(worstcase))