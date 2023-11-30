from random import randint
from maxi_k import maxi_k as maxi1
from maxi import maxi_k as maxi2
from collections import deque
import time 
testov=10000

testni=[]
resitve=[]
resitev_prve=[]
resitev_druge=[]
T1=time.perf_counter()
for _ in range(testov):
    test=[]
    k=0
    for _ in range(14):
        test.append(randint(-20,20))
    k=randint(1,14)

    resitve.append(maxi2(test,k))

    test=[]
T2=time.perf_counter()
print(T2-T1)