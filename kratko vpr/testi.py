"""program ki nalkjučno generira primere in primera vse 3 programe ki resijo problem"""

from random import randint
from maxi_k import maxi_k as maxi1
from testna1 import maxSlidingWindow as maxS1
from testna2 import maxSlidingWindow as maxS2
from maxi import maxi_k as maxi2
from collections import deque

def primerjava(x,y):
    bol=True
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j]!=y[i][j]:
                bol = False
    return bol


testov=1000

testni=[]
resitve=[]
resitev_prve=[]
resitev_druge=[]

for _ in range(testov):
    test=[]
    k=0
    for _ in range(14):
        test.append(randint(-20,20))
    k=randint(1,14)

    testni.append((test,k))
    resitve.append(maxi2(test,k))
    resitev_prve.append(maxS1(test,k))
    resitev_druge.append(maxS2(test,k))
    test=[]

pravilni=0
for i in range(len(testni)):
    #print(testni[i])
    #print(resitve[i])
    #print(resitve_prave[i])
    # if resitve==resitve_prave:
    #     print("true")
    #     #print()
    # else:
    #     print("false")
    if not resitev_druge==resitve:#not(primerjava(resitev_druge,resitve)):# and resitev_prve == resitve):# or resitev_druge != resitev_prve:
        print("NAPAKA")
        print(testni[i])
        print(resitve[i])
       # print(resitev_prve[i])
        print(resitev_druge[i])
    else:
        pravilni+=1

print("st. pravilno: {}, st. vsi: {}, st. nepravilni: {}".format(pravilni,testov,testov-pravilni))



