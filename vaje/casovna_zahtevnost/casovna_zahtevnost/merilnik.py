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