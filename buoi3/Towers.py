import sys

def main():
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    arr1 = []
    arr2 = []
    
    value,total = arr[0],1
    if n == 1:
        print("1 1")
        sys.exit()
    i = 1
    while i < n:
        if value == arr[i]:
            total += 1
        if value != arr[i]:
            arr1.append(value)
            arr2.append(total)
            value = arr[i]
            total = 1
        if i == n-1:
            arr1.append(value)
            arr2.append(total)
        i += 1

    maxl = 0
    for i in range(len(arr1)):
        maxl = max(maxl, arr2[i])
    print(str(maxl) + " " + str(len(arr1)))


if __name__ == "__main__":
    main()