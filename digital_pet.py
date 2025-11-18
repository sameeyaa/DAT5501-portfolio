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

    #feeding interaction
    def feed(self):
        #when the pet is fed, hunger vital will increase by 3, happiness will also increase by 2
        if self.hunger < 10:
            self.hunger += 3
            self.happiness += 2
            self.interactions.append("fed")
            print(f"You fed {self.name}.")
            self.speak("Yummy! That was tasty, thank you!")
            #when hunger level is 10, pet will mention it is full and cannot be fed
            if self.hunger == 10:
                print(f"{self.name} is full and does not want to eat anymore.")
            else:
                print(f"{self.name} is already full and cannot eat anymore!")


