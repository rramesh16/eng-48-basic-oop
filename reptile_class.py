from animal_class import *

class Reptile(Animal):

    def __init__(self, name, eyes, legs, n_chamber_heart,age):
        super().__init__(name,eyes,legs,age)
        self.scales = True
        self.cold_blood = True
        self.n_chamber_heart = n_chamber_heart

    def mate_calling(self):     # Example of polymorphism
        return 'Look at my scales! They look good!'

    def seek_heat(self):
        return 'humm bit chilly, lets get some sun'

    def seek_shade(self):
        return 'Who turned on the heating? ---> I am going to find some shade '

    def prey(self):
        return 'Waiitttt for it...Waaaaittt...AND...POUNCE!!!'

    def lay_eggs(self):
        return 'What are you looking at? Never seen a lizard lay eggs?'