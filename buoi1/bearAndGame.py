import sys

def main():
    n = int(input())
    arr = list(map(int,input().split()))

    sumT = 15
    for i in range(0,n):
        if sumT >= arr[i]:
            sumT = arr[i] + 15 if  arr[i] + 15 <= 90 else 90
    print(str(sumT))
if __name__ == '__main__':
    main()
    