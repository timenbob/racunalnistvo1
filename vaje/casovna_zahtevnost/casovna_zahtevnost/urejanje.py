from merilnik import *

def bubblesort(sez):
    n=len(sez)
    
    for i in range(1,n):#po vsakem el
        for j in range(1,n-i):#do unih ka jih še nismo uredil
            x=sez[j]
            y=sez[j+1]
            if x>y: #če je prejšni>od naslednjega ju zamenjamo
                sez[j+1]=x
                sez[j] = y   
    return

#narisi_in_pokazi_graf(bubblesort, test_gen_sez, [10,20,30,400,600,800,1000,5000], k=10)
#izpisi_case(test_fun_kvad, test_gen_sez, [10000], 10)

def zdruzi(sez, prvi, srednji, zadnji):
    id_prvi = srednji - prvi + 1
    id_drugi = zadnji - srednji

    l = []
    d = []
    for i in range(id_prvi):
        l.append(sez[prvi + i])

    for i in range(id_drugi):
        d.append(sez[srednji+1+i]) 

    i, j, k = 0, 0, prvi

    while i < id_prvi and j < id_drugi:
        if l[i] <= d[j]:
            sez[k] = l[i]
            i += 1
        else:
            sez[k] = d[j]
            j += 1
        k += 1
    while i < id_prvi:
        sez[k] = l[i]
        i += 1
        k += 1
    while j < id_drugi:
        sez[k] = d[j]
        j += 1
        k += 1

def mergesort(sez, prvi=0, zadnji=None):
    n = len(sez)
    if zadnji is None:
        zadnji = n - 1

    if prvi < zadnji:
        sredina = (prvi + zadnji) // 2

        mergesort(sez, prvi, sredina)
        mergesort(sez, sredina + 1, zadnji)
        zdruzi(sez, prvi, sredina, zadnji)



narisi_in_pokazi_graf(mergesort, test_gen_sez, [10,20,30,400,600,800,1000,5000], k=10)
#izpisi_case(test_fun_kvad, test_gen_sez, [10000], 10)