import sys
from queue import Queue

def process(n,arr):
    stack = []
    queue = Queue()
    current = 1

    for i in range(n):

        if arr[i] == current:
            current += 1
            queue.put(arr[i])
            continue

        while len(stack) != 0:
            if current == stack[-1]:
                current += 1
                queue.put(stack.pop())
            else:
                break
        stack.append(arr[i])

    while len(stack) != 0:
        if current == stack[-1]:
            current += 1
            queue.put(stack.pop())
        else:
            break

    if queue.qsize() == n:
        print("yes")
    else:
        print("no")

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        arr = list(map(int,input().split()))
        process(n,arr)
    



if __name__ == "__main__":
    main()