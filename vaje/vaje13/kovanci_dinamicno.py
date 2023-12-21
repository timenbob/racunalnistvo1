def kovanec_gor(sez):
    pomoc=[0]*(len(sez)+2)
    
    for i in range(2,len(sez)+2):
        pomoc[i]=max(sez[i-2]+pomoc[i-2],pomoc[i-1])
    return pomoc[-1]

print(kovanec_gor([3, 7, 6, 1, 6, 10, 5, 4, 2, 7, 8, 11, 13, 15, 14]))

def kovanec_dol(sez):
    slovar={}
    def pomoc(sez):
        n=len(sez)
        if n==0:
            return 0
        elif n==1:
            return sez[0]
        elif n==2:
            slovar[2]=max(sez[0],sez[1])
            return slovar[2]
        else:
            if n not in slovar:
                slovar[n]=max(sez[0]+pomoc(sez[2:]),pomoc(sez[1:]))
            return slovar[n]
        
    return pomoc(sez)

print(kovanec_dol([3, 7, 6, 1, 6, 10, 5, 4, 2, 7, 8, 11, 13, 15, 14]))        