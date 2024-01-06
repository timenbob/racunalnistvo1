from Sklad import Sklad
from vrsta import Vrsta
print(2<None)
V=Vrsta([2,0,5,1,3,4,4])
U=Vrsta()
S=Sklad()
while not V.prazna():
    while (not S.prazen()) and V.zacetek() < S.vrh():
        U.vstavi(S.odstrani())
    S.vstavi(V.odstrani())
    while not U.prazna():
        V.vstavi(U.odstrani())
while not S.prazen():
    V.vstavi(S.odstrani())

print(V)
