import sys

def main():
    n = int(input())
    arr = []
    for i in range(n):
        s = input()
        r = xuli(s)
        print(r)
    
    
def xuli(s):
    r = ""
    stackOper = []
    for i in range(len(s)):
        if s[i] == "(":
            continue
        elif s[i] in "+,-,*, /,^,%":
            stackOper.append(s[i])
        elif s[i] == ")":
            r += str(stackOper.pop())
        else:
            r += s[i]
    return r
if __name__ == "__main__":
    main()