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

# Print(reptile1.__age) --> does not work because it is encapsulated
print(reptile1.get_age())

reptile1.set_age(19)
print(reptile1.get_age())

print(reptile1._display_members())  # ---> Low level encapsulation