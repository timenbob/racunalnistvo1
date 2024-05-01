import itertools

p= 101 
b= 256 

niz="abc for elt in range(5)"

# Define a list of numbers
#my_list = range(66,123)
#my_list = range(0,256)

# Generate all possible two-element combinations
# Convert the resulting iterator to a list
#ombinations = list(itertools.combinations(my_list, 3))

stevec = 0



for i in range(len(niz)-2):
        print(f'"{niz[i:i+3]}" - {(ord(niz[i])*b**2+ord(niz[i+1])*b+ord(niz[i+2]))%p}')


