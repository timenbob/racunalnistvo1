# Verižni seznam

**Ime:** Timen Bobnar

**Datum:** 18.11.2023

---

Delali smo z veriznimi seznami. Za verizni seznam smo ustvarili razred ter nekaj osnovnih metod. Z temi metodami smo nato reševali ostale naloge. Ustvarili smo še dve funkciji in sicer:
-vstavi veriga vozlov
-vstavi verizni seznam
in ju stestirali


## Komentarji in opombe

Vaje so se meni zdele super.


## Organizacija dela


Delal sem sam, z kakšnimi namigi od sošolcev.


# Veriga vozlov in verižni seznam

**Navodilo:** Napišite funkcijo vstavi_veriga_vozlov(veriga, stevilo), ki prejme naraščajoče urejeno verigo vozlov ter število vstavi na pravilno mesto v zaporedju vrednosti. Če vrednost že obstaja, naj vozel vstavi za zadnjega z enako vrednostjo . Funkcija naj strukturo spremeni na mestu (angl. in place), torej naj ustvari največ en nov vozel (lahko pa seveda ustvarite dodatne "kazalce" na vozle).

Predpostavite, da so vsi elementi števila in urejeni po vrsti. Prav tako lahko predpostavite, da ima struktura vsaj en element.

**Rešitev:**
```python
from verizni_seznam import Vozel

def vstavi_veriga_vozloc(veriga,st):
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
```

**Komentar:**
Imamo dva kazalca prejsnjega in enega pred njim (predhodnika). Premikamo se toliko časa dokler ne najdemo pravega mesta, kamor bomo število vstavili. Ko smo dosegli to mesto potrebujemo kazalce samo pravilno povezati. Prejsnjega na novega (nov je vozel, ki vsebuje to stevilo) ter novega na predhodnika od prejsnega. 

**Testi**

```python
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
```
```python
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
```
```python
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
```
```python
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
```
```python
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
```


**Testi od kolegice(Kumelj Urša):**
```python
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
```
```python
    1->2->3->4->5
```
```python
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
```
```python
    1->2->4->5->5
```
```python
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
```
```python
    1->1->2->4->5
```

**Komentar na teste:** Testi delujejo pravilno

## Verižni seznam
**Navodilo:** Napišite funkcijo vstavi_verizni_seznam(veriga, stevilo), ki prejme naraščajoče urejeni verizni seznam ter število vstavi na pravilno mesto v zaporedju vrednosti. Če vrednost že obstaja, naj vozel vstavi za zadnjega z enako vrednostjo . Funkcija naj strukturo spremeni na mestu (angl. in place), torej naj ustvari največ en nov vozel (lahko pa seveda ustvarite dodatne "kazalce" na vozle).

Predpostavite, da so vsi elementi števila in urejeni po vrsti. Prav tako lahko predpostavite, da ima struktura vsaj en element.

**Rešitev:**
```python
from verizni_seznam import VerizniSeznam,Vozel

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

```

**Komentar:**
Imamo dva kazalca prejsnjega in enega pred njim (predhodnika). Premikamo se toliko časa dokler ne najdemo pravega mesta, kamor bomo število vstavili. Ko smo dosegli to mesto potrebujemo kazalce samo pravilno povezati. Prejsnjega na novega (nov je vozel, ki vsebuje to stevilo) ter novega na predhodnika od prejsnega. Edino kar moramo tukaj paziti je, če moramo število vstaviti na konec verižnega seznama, saj se nam bo potem spremnil kazalec za konec, drugače pa končni kazalec ostaja vseskozi nespremenjen.

**Testi**
```python
# vstavi 7 v 1->3->5->9
s5 = VerizniSeznam()
vstavi_verizni_seznam(s5, 1)
vstavi_verizni_seznam(s5, 3)
vstavi_verizni_seznam(s5, 5)
vstavi_verizni_seznam(s5, 9)
print(vstavi_verizni_seznam(s5, 7)) # 1->3->5->7->9
```
```python
# vstavi 0 v 2->4->6->8
s6 = VerizniSeznam()
vstavi_verizni_seznam(s6, 2)
vstavi_verizni_seznam(s6, 4)
vstavi_verizni_seznam(s6, 6)
vstavi_verizni_seznam(s6, 8)
print(vstavi_verizni_seznam(s6, 0)) # 0->2->4->6->8
```
```python
# vstavi 5 v prazen
s7 = VerizniSeznam()
print(vstavi_verizni_seznam(s7, 5)) # 5->
```
```python
# vstavi 6 v 1->2->3->4
s8 = VerizniSeznam()
vstavi_verizni_seznam(s8, 1)
vstavi_verizni_seznam(s8, 2)
vstavi_verizni_seznam(s8, 3)
vstavi_verizni_seznam(s8, 4)
print(vstavi_verizni_seznam(s8, 6)) # 1->2->3->4->6
```
**Testi od kolegice(Kumelj Urša):**
```python
# vstavi 10 v 1->2->4->5
s1 = VerizniSeznam()
vstavi_verizni_seznam(s1, 1)
vstavi_verizni_seznam(s1, 2)
vstavi_verizni_seznam(s1, 4)
vstavi_verizni_seznam(s1, 5)
print(vstavi_verizni_seznam(s1,10))# 1->2->4->5->10
```
```python
    1->2->4->5->10
```
```python
# vstavi 2 v prazen
s2 = VerizniSeznam()
print(vstavi_verizni_seznam(s2,2)) # 2->
```
```python
    2->
```
```python
# vstavi 1 v 1->2->4->5
s3 = VerizniSeznam()
vstavi_verizni_seznam(s3, 1)
vstavi_verizni_seznam(s3, 2)
vstavi_verizni_seznam(s3, 4)
vstavi_verizni_seznam(s3, 5)
print(vstavi_verizni_seznam(s3,1)) # 1->1->2->4->5
```
```python
    1->1->2->4->5
```
```python
# vstavi 3 v 1->2->4->5
s4 = VerizniSeznam()
vstavi_verizni_seznam(s4, 1)
vstavi_verizni_seznam(s4, 2)
vstavi_verizni_seznam(s4, 4)
vstavi_verizni_seznam(s4, 5)
print(vstavi_verizni_seznam(s4,3)) # 1->2->3->4->5
```
```python
    1->2->3->4->5
```
**Komentar na teste:** Testi delujejo pravilno

**Razmislek:** Vrednosti vračamo dokler vozel ni none. Po mojem mnenju ni zares razlike med verogo vozlov in veriznim seznamom strukturi sta si zelo podobni.

# Viri

1. Cone, M., Markdown Cheat Sheet, pridobljeno s [https://www.markdownguide.org/cheat-sheet/] https://www.markdownguide.org/cheat-sheet/), 18. 11. 2023.
