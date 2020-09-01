import sys
from queue import Queue
def main():
    while True:
        n = int(input())
        if n == 0:
            break
        process(n)
        
def process(n):

    if n == 1:
        print("Discarded cards:")
        print(f"Remaining card: 1")
        return

    arrq = []

    queue = Queue()
    throwQueue = Queue()
    for i in range(1,n+1):
        arrq.append(i)
    leng = len(arrq)-1
    
    s = "Discarded cards:"
    s += f" {arrq[0]}"
    i = 1
    while True:
        # queue.put(queue[-1]))
        # print(queue.qsize())
        arrq.append(arrq[i])
        i += 1
        if (len(arrq)) - i > 1:
            s += f", {arrq[i]}"
            i += 1
        else:
            break

    print(s)
    print(f"Remaining card: {arrq[i]}")

    

if __name__ == "__main__":
    main()