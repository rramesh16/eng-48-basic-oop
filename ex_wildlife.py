from animal_class import *
from reptile_class import *

# Creating an instance of Animal class
Simba = Animal('Simba',3,1, 8)

# Creating an instance of Reptile class
ringo = Reptile('Ring', 3, 1, 8)

# Checking the data type
print(type(Simba))
print(type(ringo))

# Calling the attributes
print(Simba.eat('Chicken'))
print(Simba.mating())
print(Simba.mate_calling())
print(Simba.go_potty())
print(Simba.sleep())

print(ringo.seek_heat())
print(ringo.mate_calling())
