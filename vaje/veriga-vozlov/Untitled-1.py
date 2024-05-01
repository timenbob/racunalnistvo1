class Vozel:
    """
    Osnovni sestavni del verižnega seznama.
    """
    def __init__(self, podatek=None, naslednji=None):
        self.podatek = podatek
        self.naslednji = naslednji

    def __str__(self):
        if self.naslednji is not None:
            return '{} -> {}'.format(self.podatek, self.naslednji)
        else:
            return '{} -> X'.format(self.podatek)
        
def vrni_seznam(prvi):
    sez=[]
    pot=prvi
    while pot != None:
        sez.append(pot.podatek)
        pot=pot.naslednji
    return sez

def iz_seznama(seznam):
    if seznam==[]:
        veriga=None
    else:
        veriga=Vozel(seznam[0])
        pot=veriga
        for el in seznam[1:]:
            pot.naslednji=Vozel(el)
            pot=pot.naslednji
        
    return veriga

nov1=iz_seznama([4,3,2,1])
nov2=iz_seznama([7,2,1,5,6])
baza=10
kaz=Vozel()
ostanek=0
odg=kaz
while True:
    print(nov1)
    print(nov2)
    print(odg)
    if nov1==None:
        while nov2 != None:
            odg.podatek=nov2.podatek
            odg=odg.naslednji
            nov2=nov2.naslednji
            break
    if nov2==None:
        while nov1 != None:
            odg.podatek=nov1.podatek
            odg=odg.naslednji
            nov1=nov1.naslednji     
        break
    else:
        x=nov2.podatek
        y=nov1.podatek
        print(x,y)
        nov1=nov1.naslednji
        nov2=nov2.naslednji
        ost=(x+y+ostanek)%baza
        ostanek=(x+y+ostanek)//baza
        pisi=Vozel(ost)
        odg.naslednji=pisi
        odg=odg.naslednji
        print(odg)

print(kaz.naslednji)
