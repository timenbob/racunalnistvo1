# Verižni seznam

**Ime:** Timen Bobnar

**Datum:** 25.11.2023

---
Dopolnili smo datoteko merilnik.py, da lažje ocenjujemo časovne zahtevnosti problemov urejaja podatkov. Implementirali smo še 2 algoritma za urejanje in sicer:
* Urejanje z mehurčki ([_bubble sort_](https://en.wikipedia.org/wiki/Bubble_sort))
* Urejanje z zlivanjem ([_merge sort_](https://en.wikipedia.org/wiki/Merge_sort))


## Komentarji in opombe

Vaje so se meni zdele super.


## Organizacija dela

Z Milico Vukićević sva si pomagala.

# Časovna zahtevnost

**Navodilo:** Vaje imajo dva sklopa. V prvem sklopu si bomo ogledali preprosto knjižnico za pomoč pri ocenjevanju in analizi časovne zahtevnosti algoritmov. V drugem delu bomo eksperimentirali z različnimi algoritmi za urejanje


## Knjižnica za merjenje časa izvajanja
**Navodilo:** Najprej dopolnite funkcije `izmeri_cas`, `oceni_potreben_cas`, `narisi_in_pokazi_graf` in `izpisi_case`. Vse štiri funkcije kot argument sprejmejo funkcijo `fun`, katere čas izvajanja nas zanima. Vse funkcije, razen  funkcije `izmeri_cas` pa sprejmejo tudi generator primerov `gen_primerov`. Generator primerov je funkcija, ki ji podamo število `n`, in nam vrne primeren in relevanten vhod za `fun` velikosti `n`.

Funkcije imajo dokumentacijski komentar, v kodi pa so podani še dodatni namigi in komentarji za lažje dopolnjevanje funkcij.

Preverite pravilnost delovanja funkcij s pomočjo priloženih testnih funkcij `test_fun_lin`, `test_fun_kvad` z linearno in kvadratično časovno zahtevnostjo. Pri tem lahko uporabite generator naključnih seznamov dolžine `n`: `test_gen_sez`. Testno kodo "zapakirajte" v `if __name__ == "__main__"` ([več o tem](https://realpython.com/if-name-main-python/)).

Knjižnici dodajte še eno nadgradnjo:
* funkcije za primerjavo algoritmov (tabela z več stolpci ali graf, ki prikazuje več funkcij)
* izvoz podatkov (shranjevanje grafov, tabel v formatu po izbiri)
* dodatne testne funkcije z določeno časovno zahtevnostjo
* kakšna nadgradnja po lastni presoji, ki se vam zdi uporabna

**Rešitev:**
```python
import time                         

import matplotlib.pyplot as plt     
import random                      


def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""
    
    t1=time.perf_counter()
    fun(primer)
    t2=time.perf_counter()
    return(t2-t1)



def oceni_potreben_cas(fun, gen_primerov, n, k):
    """Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih velikosti `n` 
    kot povprečje `k` ponovitev."""

    casi=[]
    for _ in range(k):
        primer=gen_primerov(n)
        casi.append(izmeri_cas(fun,primer))
    return(sum(casi)/len(casi))



def narisi_in_pokazi_graf(fun, gen_primerov, sez_n, k=10):
    """Funkcija nariše graf porabljenega časa za izračun `fun` glede na velikosti 
    primerov v `sez_n`. Za oceno časa uporabi `k` ponovitev. """
    sez_n.sort()
    sez_x=sez_n
    sez_y=[]
    for n in sez_n:
        sez_y.append(oceni_potreben_cas(fun, gen_primerov, n, k))
    plt.plot(sez_x, sez_y, 'r')
    plt.savefig('mrilnik.pdf',format="pdf",bbox_inches="tight")
    plt.show()



def izpisi_case(fun, gen_primerov, sez_n, k=10):
    """Funkcija izpiše tabelo časa za izračun `fun` glede na velikosti primerov v `sez_n`. 
    Za oceno uporabi `k` ponovitev."""
    
    sez_n.sort()
    casi = list(map(lambda x : oceni_potreben_cas(fun, gen_primerov, x, k),sez_n))

    pad = len(str(max(sez_n)))  
    
    print("{:{pad}} | Čas izvedbe [s]".format("n", pad=pad))

    sep_len = pad + 4 + max(len(str(x))for x in casi) 
    print("-"*sep_len)

    for i in range(len(sez_n)):
        print(f'{sez_n[i]:{pad}} | {casi[i]}')

```


**Testi**
```
# Nekaj preprostih testnih funkcij

def test_fun_lin(sez):
    "Testna funkcija z linearno časovno zahtevnostjo."
    x = 0
    for n in sez:
        x += n
    return x


def test_fun_kvad(sez):
    "Testna funkcija s kvadratično časovno zahtevnostjo."
    x = 0
    for n in sez:
        for n in sez:
            x += n
    return x


def test_gen_sez(n):
    "Generira testni seznam dolžine n."
    return [random.randint(-n, n) for _ in range(n)]

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    izpisi_case(test_fun_kvad, test_gen_sez, [10,70,20,50,60,70,80,10], 10)
```

```python
#n  | Čas izvedbe [s]
#----------------------------
#10 | 6.85999999983089e-06
#10 | 6.139999999943413e-06
#20 | 2.4630000000014362e-05
#50 | 0.0001512599999999864
#60 | 0.00021470999999997353
#70 | 0.0003008600000000694
#70 | 0.0003060900000001254
#80 | 0.00040122000000000215
lahko narišemo tudi grafe
```


## Algoritmi za urejanje
**Navodilo:** Ogledali si bomo štiri klasične algoritme za urejanje seznamov.
* Urejanje z mehurčki ([_bubble sort_](https://en.wikipedia.org/wiki/Bubble_sort))
* Urejanje z vstavljanjem ([_insertion sort_](https://en.wikipedia.org/wiki/Insertion_sort))
* Urejanje z zlivanjem ([_merge sort_](https://en.wikipedia.org/wiki/Merge_sort))
* Hitro urejanje ([_quick sort_](https://en.wikipedia.org/wiki/Quicksort))

Ustvarite novo datoteko `urejanje.py`. V njej implementirajte vsaj enega izmed prvih dveh in vsaj enega izmed zadnjih dveh algoritmov. Pravilnost delovanja funkcij ustrezno testirajte.  

Ko ste se prepričali o pravilnosti implementacije, uporabite knjižnico `merilnik`. Eksperimentirajte z različnimi velikostmi seznamov. Razmislite:
* Bi znali s pomočjo grafa ali tabele oceniti časovno zahtevnost? Se ta ujema s pričakovanji?
* Kako veliko tabelo naključnih števil še lahko uredimo v eni minuti?
* Ali algoritem v kakšnem primeru deluje veliko hitreje oziroma počasneje od povprečja? (urejeni seznami, izbira pivota pri hitrem urejanju, ...)
* Kakšne so prednosti in kakšne slabosti algoritma?
* Bi znali oceniti prostorsko zahtevnost? (Koliko prostora porabi algoritem _poleg_ prostora za vhodne in izhodne podatke)
* Bi se dalo kaj izboljšati?
* Primerjajte različne algoritme na različno velikih problemih. Kaj ugotovite?

Tistim, ki ste prisotni na vajah, priporočam delo v parih. Vsak iz para lahko na primer implementira dva izmed algoritmov, nato pa si implementacije izmenjata (obvezno označite, katere funkcije so vaše lastno delo), lahko pa skupaj implementirata vse izmed algoritmov. Skupaj lahko načrtujeta različne eksperimente in diskutirata o ugotovitvah. Na koncu vaj bi nekaj minut namenili deljenju ugotovitev.

**Rešitev1:**
```python
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

```

**Komentar:**
* Če uporabimo narisi_in_pokazi_graf(bubblesort, test_gen_sez, [10,20,30,40,50,60,100,200,300,400,600,800,1000], k=10) lahko hitro opazimo, da je videti kot neki približek kvadratne funkcije. To se ujema z mojimi pričakovanji, saj imamo 2 zanki.
* Tabelo s približno 10000 števili.
* Če, je tabela urejena smo malo hitrejši, v vsakem primeru je počasen algoritem.
* Prednost je, da ga je zelo preprosto implementirati in za malo število podatkov je dovolj hiter. Slabost je, da je počasen.
* Prostorske zahtevnosti ne znam zares oceniti, vendar v vsaki zanki potrebujemo prostor še za x in y tako, da nekaj je vendar ne veliko.
* Razen da uporabimo drug algoritem, se mi zdi, da ne.


**Rešitev2:**
'''python
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

arr = [12, 11, 13, 5, 6, 7]

mergesort(arr)
print(arr)

''''

**Komentar:**
* Če uporabimo narisi_in_pokazi_graf(mergesort, test_gen_sez, [10,20,30,40,50,60,100,200,300,400,600,800,1000], k=10) lahko hitro opazimo, da je videti kot neki približek linearne funkcije. To se približno ujema s pričakovanji, saj sem prebral, da ima časovno zahtevnost O(n*log(n))
* Tabelo s približno 30000000 števili.
* Če, je tabela urejena smo malo hitrejši.
* Prednost je, da je izredno hiter. Slabost da je implementacija teška.
* Prostorske zahtevnosti ne znam zares oceniti.
* Razen da uporabimo drug algoritem, se mi zdi, da ne.

# Viri
* https://en.wikipedia.org/wiki/Merge_sort
* https://www.programiz.com/dsa/merge-sort
* https://www.geeksforgeeks.org/python-program-for-merge-sort/
* ChatGPT



