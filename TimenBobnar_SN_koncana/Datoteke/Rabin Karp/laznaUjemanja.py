import random
m=997  #101 439
p=256
os=(97*(p**2)+98*p+99)%m
niz=[]
ostanek=0
import itertools

# Define a list of numbers
my_list = range(0,126)

# Generate all possible two-element combinations
# Convert the resulting iterator to a list
combinations = list(itertools.combinations(my_list, 3))
stevec=0
while ostanek!=os:
    for el in combinations:
        niz=el
        ostanek=(el[0]*p**2+el[1]*p+el[2])%m
        if ostanek==os:
            print(el,os,ostanek,chr(el[0]),chr(el[1]),chr(el[2]))
            stevec+=1
    break
print("******")
print(stevec)
            


