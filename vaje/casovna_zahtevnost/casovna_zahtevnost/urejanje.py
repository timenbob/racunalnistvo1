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

sez=[1,4,7,77,43,7,25]
bubblesort(sez)
print(sez)