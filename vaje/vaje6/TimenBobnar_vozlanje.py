class Vozel:
    '''
    Razred, ki predstavlja posamezen vozel s podatkom v verižnem seznamu.
    '''
    def __init__(self, podatek, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

class VerizniSeznam:
    '''
    Razred, ki predstavlja verižni seznam z začetkom in koncem.
    '''
    def __init__(self):
        self._zacetek = None
        self._konec = None

    def __str__(self):
        niz = ''
        vozel = self._zacetek
        while vozel is not None:
            niz += '{} -> '.format(repr(vozel.podatek))
            vozel = vozel.naslednji
        return niz + '•'


###########################################################

def vstavi_veriga_vozlov(veriga,st):
    trenutni=veriga
    pr=None
    while veriga is not None and st>trenutni.podatek:
        pr=trenutni
        trenutni=trenutni.naslednji
    vozu=Vozel(st)
    if pr is not None:
        pr.naslednji=vozu
    else:
        veriga=vozu
    vozu.naslednji=trenutni
    return veriga

# vstavi 0 v -10->-2->1->5
v1=Vozel(-10,Vozel(-2,Vozel(1,Vozel(5))))
v2=vstavi_veriga_vozlov(v1,0)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali -10->-2->0->1->5
print("\n")


# vstavi 0 v 1->2->3->4
v1 = Vozel(1, Vozel(2, Vozel(3, Vozel(4))))
v2 = vstavi_veriga_vozlov(v1, 0)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# Rezultat: 0->1->2->3->4

# vstavi 6 v 1->2->3->4
v1 = Vozel(1, Vozel(2, Vozel(3, Vozel(4))))
v2 = vstavi_veriga_vozlov(v1, 6)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# Rezultat: 1->2->3->4->6

# vstavi 3 v 1->3->5->7
v1 = Vozel(1, Vozel(3, Vozel(5, Vozel(7))))
v2 = vstavi_veriga_vozlov(v1, 3)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# Rezultat: 1->3->3->5->7

# vstavi 8 v 2->4->6->8
v1 = Vozel(2, Vozel(4, Vozel(6, Vozel(8))))
v2 = vstavi_veriga_vozlov(v1, 8)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# Rezultat: 2->4->6->8->8




# vstavi 3 v 1->2->4->5
v1 = Vozel(1, Vozel(2, Vozel(4, Vozel(5))))
v2 = vstavi_veriga_vozlov(v1, 3)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali 1->2->3->4->5
print("\n")
# vstavi 5 v 1->2->4->5
v1 = Vozel(1, Vozel(2, Vozel(4, Vozel(5))))
v2 = vstavi_veriga_vozlov(v1, 5)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali 1->2->4->5->5
print("\n")
# vstavi 1 v 1->2->4->5
v1 = Vozel(1, Vozel(2, Vozel(4, Vozel(5))))
v2 = vstavi_veriga_vozlov(v1, 1)
trenutni = v2
while trenutni is not None:
    print(trenutni.podatek, end="")
    if trenutni.naslednji is not None:
        print(" -> ", end="")
    trenutni = trenutni.naslednji
# dobiti bi morali 1->1->2->4->5
print("\n")


################################################################

def vstavi_verizni_seznam(sez,st):
    trenutni=sez._zacetek
    pr=None
    while trenutni is not None and st>trenutni.podatek:
        pr=trenutni
        trenutni=trenutni.naslednji
    vozu=Vozel(st)
    if pr is not None:
        pr.naslednji=vozu
    else:
        sez._zacetek=vozu
    vozu.naslednji=trenutni

    if trenutni is None:
        sez._konec=vozu
    return sez


# vstavi 7 v 1->3->5->9
s5 = VerizniSeznam()
vstavi_verizni_seznam(s5, 1)
vstavi_verizni_seznam(s5, 3)
vstavi_verizni_seznam(s5, 5)
vstavi_verizni_seznam(s5, 9)
print(vstavi_verizni_seznam(s5, 7)) # 1->3->5->7->9

# vstavi 0 v 2->4->6->8
s6 = VerizniSeznam()
vstavi_verizni_seznam(s6, 2)
vstavi_verizni_seznam(s6, 4)
vstavi_verizni_seznam(s6, 6)
vstavi_verizni_seznam(s6, 8)
print(vstavi_verizni_seznam(s6, 0)) # 0->2->4->6->8

# vstavi 5 v prazen
s7 = VerizniSeznam()
print(vstavi_verizni_seznam(s7, 5)) # 5->

# vstavi 6 v 1->2->3->4
s8 = VerizniSeznam()
vstavi_verizni_seznam(s8, 1)
vstavi_verizni_seznam(s8, 2)
vstavi_verizni_seznam(s8, 3)
vstavi_verizni_seznam(s8, 4)
print(vstavi_verizni_seznam(s8, 6)) # 1->2->3->4->6


# vstavi 10 v 1->2->4->5
s1 = VerizniSeznam()
vstavi_verizni_seznam(s1, 1)
vstavi_verizni_seznam(s1, 2)
vstavi_verizni_seznam(s1, 4)
vstavi_verizni_seznam(s1, 5)
print(vstavi_verizni_seznam(s1,10))# 1->2->4->5->10

# vstavi 2 v prazen
s2 = VerizniSeznam()
print(vstavi_verizni_seznam(s2,2)) # 2->

# vstavi 1 v 1->2->4->5
s3 = VerizniSeznam()
vstavi_verizni_seznam(s3, 1)
vstavi_verizni_seznam(s3, 2)
vstavi_verizni_seznam(s3, 4)
vstavi_verizni_seznam(s3, 5)
print(vstavi_verizni_seznam(s3,1)) # 1->1->2->4->5

# vstavi 3 v 1->2->4->5
s4 = VerizniSeznam()
vstavi_verizni_seznam(s4, 1)
vstavi_verizni_seznam(s4, 2)
vstavi_verizni_seznam(s4, 4)
vstavi_verizni_seznam(s4, 5)
print(vstavi_verizni_seznam(s4,3)) # 1->2->3->4->5