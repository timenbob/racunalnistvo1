# Verižni seznam

**Ime:** Timen Bobnar

**Datum:** 10.12.2023


# Testni primeri

**Navodilo:** navedite testne primere za nalogo ogrevanje. Poskrbite, da testi pokrijejo vse veje pogojnih stavkov v programu. Vključite kakšen manjši primer, kakšen večji primer, robne primere (na primer prazno drevo), ... Za testne primere obvezno zapišite pričakovan izhod (preden na njih poženete funkcijo in vidite, kaj vrne).


## Vrni koren
**Navodila:** Napišite funkcijo `vrni_koren(drevo)`, ki vrne podatek v korenu drevesa, če pa je drevo prazno pa vrne `None`.

**Test1:**
Vrniti mora None
```Python
drevo1 = Drevo()
print(vrni_koren(drevo1 ))
```
**Test2:**
Vrniti mora 1
```Python
drevo2 = Drevo(1)
print(vrni_koren(drevo2))
```
**Test3:**
Vrniti mora 1
```Python
drevo3 = Drevo(1,levo=Drevo(2),desno=Drevo(3,levo=Drevo(5)))
print(vrni_koren(drevo3))
```
**Test4:**
Vrniti mora 5
```Python
drevo4 = Drevo(5,levo=Drevo(5),desno=Drevo(7,levo=Drevo(42,desno=Drevo(5))))
print(vrni_koren(drevo4))
```
## Je list
**Navodila:** Napišite funkcijo `je_list(drevo)`, ki preveri ali je podano drevo list.

**Test1:**
Vrniti mora false
```Python
drevo1 = Drevo()
print(je_list(drevo1))
```
**Test2:**
Vrniti mora True
```Python
drevo2 = Drevo(1)
print(je_list(drevo2))
```
**Test3:**
Vrniti mora False
```Python
drevo3 = Drevo(1,levo=Drevo(2),desno=Drevo(3,levo=Drevo(5)))
print(je_list(drevo3))
```
**Test4:**
Vrniti mora False
```Python
drevo4 = Drevo(5,levo=Drevo(5),desno=Drevo(7,levo=Drevo(42,desno=Drevo(5))))
print(je_list(drevo4))
```
## Nikoli Levo
**Navodila:** Napišite funkcijo `nikoli_levo(drevo)`, ki preveri, da ima vsako vozlišče drevesa kvečjemu desno poddrevo.

**Test1:**
Vrniti mora True
```Python
drevo1 = Drevo()
print(nikoli_levo(drevo1))
```
**Test2:**
Vrniti mora True
```Python
drevo2 = Drevo(1)
print(nikoli_levo(drevo2))
```
**Test3:**
Vrniti mora False
```Python
drevo3 = Drevo(1,levo=Drevo(2),desno=Drevo(3,levo=Drevo(5)))
print(nikoli_levo(drevo3))
```
**Test4:**
Vrniti mora False
```Python
drevo4 = Drevo(5,levo=Drevo(7,levo=Drevo(42,levo=Drevo(5))))
print(nikoli_levo(drevo4))
```
**Test5:**
Vrniti mora False
```Python
drevo5 = Drevo(5,desno=Drevo(7,desno=Drevo(42,desno=Drevo(5))))
print(nikoli_levo(drevo5))
```

## Visina
**Navodila:** Napišite funkcijo `visina(drevo)`, ki izračuna višino dvojiškega drevesa.

**Test1:**
Vrniti mora 0
```Python
drevo1 = Drevo()
print(visina(drevo1))
```
**Test2:**
Vrniti mora 1
```Python
drevo2 = Drevo(1)
print(visina(drevo2))
```
**Test3:**
Vrniti mora 3
```Python
drevo3 = Drevo(1,levo=Drevo(2),desno=Drevo(3,levo=Drevo(5)))
print(visina(drevo3))
```
**Test4:**
Vrniti mora 4
```Python
drevo4 = Drevo(5,levo=Drevo(7,levo=Drevo(42,levo=Drevo(5))))
print(visina(drevo4))
```
