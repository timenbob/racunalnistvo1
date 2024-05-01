class Drevo: 
        
    def __init__(self, *args, **kwargs):
        if args:
            assert len(args) == 1
            self.prazno = False
            self.podatek = args[0]
            self.levo = kwargs.pop('levo', None) or Drevo()  
            self.desno = kwargs.pop('desno', None) or Drevo()
        else:
            self.prazno = True
        assert not kwargs

    def __repr__(self, zamik=''):
        if self.prazno:
            return 'Drevo()'.format(zamik)
        elif self.levo.prazno and self.desno.prazno:
            return 'Drevo({1})'.format(zamik, self.podatek)
        else:
           return 'Drevo({1},\n{0}      levo = {2},\n{0}      desno = {3})'.\
               format(
                   zamik,
                   self.podatek,
                   self.levo.__repr__(zamik + '             '),
                   self.desno.__repr__(zamik + '              ')
               )

    def __eq__(self, other):
        if self.prazno and other.prazno:
            return True
        elif not self.prazno and not other.prazno:
            return (
                self.podatek == other.podatek and
                self.levo == other.levo and
                self.desno == other.desno
            )
        else:
            return False

    def __hash__(self):
        if self.prazno:
            return hash(())
        else:
            return hash((self.podatek, self.levo, self.desno))

def urejenaje_z_zlivanjem(seznam):
    if len(seznam) > 1:
        
        n = len(seznam) // 2
        leva = seznam[:n]
        desna = seznam[n:]

        urejenaje_z_zlivanjem(leva)
        urejenaje_z_zlivanjem(desna)

        i = j = k = 0
        while i < len(leva) and j < len(desna):
            if leva[i] <= desna[j]:
                seznam[k] = leva[i]
                i += 1
            else:
                seznam[k] = desna[j]
                j += 1
            k += 1

        while i < len(leva):
            seznam[k] = leva[i]
            i += 1
            k += 1
            
        while j < len(desna):
            seznam[k] = desna[j]
            j += 1
            k += 1
        return seznam

def premi_pregled(drevo):
    if drevo.prazno:
        return []

    return [drevo.podatek] + premi_pregled(drevo.levo) + premi_pregled(drevo.desno)

def k_najvecji(idd, k):
    if idd.prazno:
        return "prazen"
    premi = premi_pregled(idd)
    urejena = urejenaje_z_zlivanjem(premi)
    return [urejena[i] for i in range(len(premi))][::-1][k-1]

idd = Drevo(13, levo=Drevo(7, levo=Drevo(5, levo=Drevo(4)), desno=Drevo(11)), desno=Drevo(18, levo=Drevo(17)))
idd2 = Drevo(5, desno=Drevo(8))
idd3 = Drevo()
idd4 = Drevo(11, levo=Drevo(8, levo=Drevo(5, levo=Drevo(1))))
idd5 = Drevo(25, desno=Drevo(50, levo=Drevo(40)))
idd6 = Drevo(2, levo=Drevo(0), desno=Drevo(6))
print(k_najvecji(idd, 3)) #Resitev: 13
print(k_najvecji(idd2, 2)) #Resitev: 1
print(k_najvecji(idd3, 3)) #Resitev: "prazen"
print(k_najvecji(idd4, 2)) #Resitev: 8
print(k_najvecji(idd5, 1)) #Resitev: 50
print(k_najvecji(idd6, 2)) #Resitev: 2






