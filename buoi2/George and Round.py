import sys

def main():
    n = list(map(int, input().split()))
    arra = list(map(int, input().split()))
    arrb = list(map(int, input().split()))

    an = n[0]
    bn = n[1]
    tong = an

    adict = {}
    bdict = {}

    for i in range(an):
        adict = checkAndAdd(adict,arra[i],1)
    
    for j in range(bn):
        bdict = checkAndAdd(bdict,arrb[j],1)
    
    numberOfProCanBeSimplified = 0
    i,j = bn-1,an-1

    while i >= 0 and j >= 0:
        if arrb[i] >= arra[j]:
            numberOfProCanBeSimplified += 1
            i -= 1
            j -= 1
        if arrb[i] < arra[j]:
            j -= 1
    
    print(str(tong - numberOfProCanBeSimplified))


    # for so, tanso in adict.items():
    #     tansothuc = bdict.get(so,0)
    #     tong -= min(tanso,tansothuc)
    # print(adict)
    # print(bdict)
    # print(tong)





def checkAndAdd(adict, key, number):
    value = adict.get(key,-1)
    if value > 0:
        adict[key] = value + 1
    if value == -1:
        adict[key] = number
    return adict
    

if __name__ == "__main__":
    main()