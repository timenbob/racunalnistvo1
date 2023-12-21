def kovanec_dol_n(sez):
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