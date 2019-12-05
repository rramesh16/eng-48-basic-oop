from animal_class import *
from reptile_class import *

# Create 2 reptiles

reptile1 = Reptile('Ringo', 2, 4, 3, 17)
reptile2 = Reptile('Susan', 2, 4, 3, 16)


# Make the reptile sleep
reptile1.sleep()
reptile2.sleep()

print(reptile1.sleep())
print(reptile1.eat('foood'))
print(reptile2.n_chamber_heart)