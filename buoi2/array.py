import sys

def main():
    nhap = list(map(int, input().split()))
    day = list(map(int, input().split()))

    n = nhap[0]
    k = nhap[1]

    adict = {}
    total = 0
    for x in range(len(day)):
        adict[day[x]] = 1
    if len(adict.keys()) < k:
        print("-1 -1")
    else:
        minlength = len(day)
        startp = 0
        endp = 0
        adict = {}
        i,j = 0,0
        ktemp = 1
        adict = check(adict, day[0])
        while i < n and j < n:
            # print(str(i) + " " + str(j) + " " + str(ktemp) + " " + str(adict) + " " + str(minlength) + " " + str(j-i))
            if ktemp == k:
                if minlength > (j - i):
                    # print(str(i) + " " + str(j) + " " + str(ktemp) + " " + str(adict) + " " + str(minlength) + " " + str(j-i))
                    minlength = j - i;
                    startp = i
                    endp = j
                i += 1
                adict = add(adict, day[i-1], -1) 
                if adict[day[i-1]] == 0:
                    ktemp -= 1
                continue
            if ktemp < k:
                j += 1
                if(j < n):
                    adict = check(adict, day[j])
                    if adict[day[j]] == 1:
                        ktemp += 1
                continue
            if ktemp > k:
                while ktemp > k and i < n:
                    i += 1
                    adict = add(adict, day[i-1], -1) 
                    if adict[day[i-1]] == 0:
                        ktemp -= 1
                continue
        print (str(startp + 1) + " " + str(endp + 1))            
        



                
            
def add(adict,key,number = 0):
    value = adict.get(key,0)
    if value != 0:
        adict[key] = value + number
    return adict

def check(adict, number):
    adict[number] = adict.get(number,0) + 1;
    return adict
if __name__ == '__main__':
    main()        

    
