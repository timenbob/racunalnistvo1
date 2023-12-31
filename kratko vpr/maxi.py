from vrsta import Vrsta
def maxi_k(sez,k):
    '''funkcija vrne seznam stevil ki so maximalne v podseznamih dolzin k'''
    #osnovni predpogoji
    if sez==[]:
        raise ValueError("NO VALUE")
    if len(sez)<k:
        raise ValueError("K needs to be smaller ther sez")
    if len(sez)==1:
        return sez
    
    maximumi=[]
    najvecji_trenutni=sez[0] #kateri je trenutni najvecji v drsečem kvadratu in kolikokrat se ta element pojavi
    stevec_ponovitev_najvecjega=0
    
    #predelamo prvi kvadrat dolžine k
    stevec_ponovitev_najvecjega=0
    pomozni=Vrsta()
    for i in range(k):
        if sez[i]>najvecji_trenutni:
            najvecji_trenutni=sez[i]
            stevec_ponovitev_najvecjega=1
        elif najvecji_trenutni==sez[i]:
            stevec_ponovitev_najvecjega+=1
        pomozni.vstavi(sez[i])

    maximumi.append(najvecji_trenutni)

    #obdelava preostalik členov v osnovnem seznamu
    izpadajoči=pomozni.beri()
    for i in range(k,len(sez)):
        izpadajoči=pomozni.beri()

        #uredimo ponovitve v odvisnoti od izpadajočega in vstopajočega
        if izpadajoči==najvecji_trenutni:
            stevec_ponovitev_najvecjega-=1
        if najvecji_trenutni==sez[i]:
            stevec_ponovitev_najvecjega+=1

        pomozni.odstrani()
        pomozni.vstavi(sez[i])

        #če je največji trenutni večji od vstopajočega in največji trenutni šezneraj notri imamo nasledji max element
        if najvecji_trenutni>sez[i] and (najvecji_trenutni!=izpadajoči or stevec_ponovitev_najvecjega>0):
            maximumi.append(najvecji_trenutni)

        #če sta ista
        elif najvecji_trenutni==sez[i]:
            maximumi.append(sez[i])
        #če je vstopajoči večji od največji trenutni
        elif najvecji_trenutni<sez[i]:
            maximumi.append(sez[i])
            stevec_ponovitev_najvecjega=1
            najvecji_trenutni=sez[i]

        else:
            #piščemo max v pomozni vrsti in stevec in te stvari resetiramo
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


print(maxi_k([1], 1))


print(maxi_k([-4, 20, 11, -9, -14, -3, -16, -2, 16, -11, 13, 12, -13, 16], 1))
        