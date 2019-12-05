# Define Animal Class

class Animal () :
    # Class is a cookie cutter for objects:
        # Wraps its' characteristics and its' behaviours

    # Define some characteristics -
    def __init__(self, name, eyes, legs, age):
        self.bones = True
        self.alive = True
        self.number_eyes = eyes
        self.number_legs = legs
        self.age = age
        self.name = name

    # Define some behaviours - Methods:
        # Things an instance of an object can do
        # Functions that are dependent on an object type

    def eat(self, food):
        return 'NOM NOM NOM! ' + food

    def mating(self):
        return ' <3 '

    def mate_calling(self):
        return ' Swipe right ;) '

    def go_potty(self):
        return 'HHUMMM!!! ... O_O ... -_- --- zen'

    def sleep(self):
        return ' Zzzzzzzz '





