import sys

def main():
    s1 = input()
    s2 = input()
    l = list(s1)

    flag = True
    for i in range(len(s1)):
        if (flag and s1[i] == s2[i]) or abs(ord(s1[i]) - ord(s2[i])) == 1:
            if abs(ord(s1[i]) - ord(s2[i])) == 1:
                flag = False
        else: 
            l[i] = chr(ord(s1[i])+1)
            print (''.join(l))
            sys.exit()
    
    print("No such string")

if __name__ == '__main__':
    main()
    