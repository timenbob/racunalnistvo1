from vrsta import Vrsta
def maxi_k(sez,k):
    '''funkcija vrne seznam stevil ki so maximalne v podseznamih dolzin k'''
    #iz seznama naredimo vrsto
    nums=Vrsta()
    for i in sez:
        nums.vstavi(i)

    bol=False
    resitev=Vrsta()
    while not nums.prazna():

        #obdelava prvega in ga odstranimo
        spomin=Vrsta()
        maxi=nums.beri()
        nums.odstrani()

        #poisce maxi in jih k-1 prepiše
        for i in range(k-1):
            if nums.prazna():
                bol=True
                break
            else:
                y=nums.beri()
                if y>maxi:
                    maxi=y
                spomin.vstavi(y)
                nums.odstrani() 

        #če jih ni bilo več k zaključimo
        if bol:
            break
        
        #prepišemo v spomin še ostale
        while not nums.prazna():
            spomin.vstavi(nums.beri())
            nums.odstrani()
        
        #spomin prepišemo v nums
        while not spomin.prazna():
            nums.vstavi(spomin.beri())
            spomin.odstrani()
        
        resitev.vstavi(maxi)

    Resitev=[]
    #iz vrste naredimo seznam
    while not resitev.prazna():
        Resitev.append(resitev.beri())
        resitev.odstrani()

    return Resitev

#print(maxi_k([1,3,-1,-3,5,3,6,7],9))
        

