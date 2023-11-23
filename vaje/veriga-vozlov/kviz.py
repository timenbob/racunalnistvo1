from veriga_vozlov import Vozel, dodaj_na_konec, dodaj_na_zacetek, vrni_seznam, iz_seznama

sez=[1,2,3,4,5,6]

def fun(prvi):
    if prvi is None:
        return
    print(prvi.podatek, end=" ")

    if prvi.naslednji is not None:
        fun(prvi.naslednji.naslednji)
    print(prvi.podatek, end=" ")
    
#fun(iz_seznama(sez))

veriga = iz_seznama([1,2,3,4,5,6,7,8,9])
k1 = veriga
k2 = veriga
while k2 is not None and k2.naslednji is not None:
    k1 = k1.naslednji
    k2 = k2.naslednji.naslednji

print(k1.podatek)