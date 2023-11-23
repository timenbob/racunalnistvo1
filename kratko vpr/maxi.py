from vrsta import Vrsta
def maxi_k(sez,k):
    '''funkcija vrne seznam stevil ki so maximalne v podseznamih dolzin k'''
    if sez==[]:
        raise ValueError("NO VALUE")
    if len(sez)<k:
        raise ValueError("K needs to be smaller ther sez")
    
    maximumi=[]
    najvecji_trenutni=sez[0]
    stevec_ponovitev_najvecjega=0
    
    pomozni=Vrsta()
    for i in range(k):
        if sez[i]>najvecji_trenutni:
            najvecji_trenutni=sez[i]
        pomozni.vstavi(sez[i])

    maximumi.append(najvecji_trenutni)

    stevec_ponovitev_najvecjega=1#TODO tut kle se lahko ponovi maxi

    izpadajoči=pomozni.beri()
    for i in range(k,len(sez)):
        izpadajoči=pomozni.beri()

        if izpadajoči==najvecji_trenutni:
            stevec_ponovitev_najvecjega-=1
        if najvecji_trenutni==sez[i]:
            stevec_ponovitev_najvecjega+=1

        #odstranimo in vstavimo v vrsto
        pomozni.odstrani()
        pomozni.vstavi(sez[i])

        if najvecji_trenutni>sez[i] and (najvecji_trenutni!=izpadajoči or stevec_ponovitev_najvecjega>0):
            maximumi.append(najvecji_trenutni)

        elif najvecji_trenutni==sez[i]:
            maximumi.append(sez[i])

        elif najvecji_trenutni<sez[i]:
            maximumi.append(sez[i])
            stevec_ponovitev_najvecjega=1
            najvecji_trenutni=sez[i]

        else:
            #piščemo max v pomozni vrsti in stevec in te stvari resetiramo
            #stevec_ponovitev_najvecjega=1
            najvecji_trenutni=pomozni.beri()
            prvi_krog=True#zato ker najvecji trenutni je ze dan kot beri in v elif ga povečamo kar ni ok za prvi kroga potem je ok
            pomozni.vstavi("strazar")
            while pomozni.beri()!="strazar":
                if najvecji_trenutni<pomozni.beri():
                    najvecji_trenutni=pomozni.beri()
                    stevec_ponovitev_najvecjega=1
                elif najvecji_trenutni==pomozni.beri():
                    if not prvi_krog:
                        stevec_ponovitev_najvecjega+=1
                    else:
                        prvi_krog=False
                x=pomozni.beri()
                pomozni.odstrani()
                pomozni.vstavi(x)
            prvi_krog=True
            pomozni.odstrani()
            maximumi.append(najvecji_trenutni)

    return maximumi


#print(maxi_k([1,1,1,1,1,1,1,1,1], 3))


#print(maxi_k([-4, 20, 11, -9, -14, -3, -16, -2, 16, -11, 13, 12, -13, 16], 1))
        