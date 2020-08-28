import sys

def main():
    narr = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    n = narr[0]
    k = narr[1]

    tongTime = 0
    tongSach = 0
    maxSach = 0

    i,j = 0,0
    tongTime += arr[j]
    tongSach += 1
    while i < n and j < n:
        if tongTime <= k:
            maxSach = max(maxSach, tongSach)
            j += 1
            if j >= n:
                break
            tongTime += arr[j]
            tongSach += 1
            continue

        if tongTime > k:
            while tongTime > k and i <= j and i < n and j < n:
                i += 1
                tongTime -= arr[i-1]
                tongSach -= 1
            continue

    print(maxSach)




if __name__ == "__main__":
    main()