#I am creating a digital pet, similar to a Tamagochi, which can be nurtured 
#The pet will be able to be fed, played with and also put to bed

class DigitalPet:
    def __init__(self, name):
        self.name = name
        #set pets vitals in the middle so it can increase and decrease
        #happiness = 10 means the pet is really happy, 0 means very sad
        self.happiness = 5
        #10 = pet is full, 0= pet is starving
        self.hunger = 5
        #10 = pet has full energy, 0 = pet has no energy at all to do anything
        self.energy = 5
        #pets age will increase throughout interactions
        self.age = 0   #pet is a newborn when first playing
        self.sleeping = False
        self.interactions = []

        
