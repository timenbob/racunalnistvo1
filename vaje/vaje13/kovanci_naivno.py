def kovanec(sez):
    
    if len(sez)==0:
        return 0
    elif len(sez)==1:
        return sez[0]
    else:
        vs1=sez[0]+kovanec(sez[2:])
        vs2=kovanec(sez[1:])
        
        return max(vs1,vs2)

print(kovanec([3, 7, 6, 1, 6, 10, 5, 4, 2, 7, 8, 11, 13, 15, 14]))