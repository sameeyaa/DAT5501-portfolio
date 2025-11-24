#I am creating a digital pet, similar to a Tamagochi, which can be nurtured 
#The pet will be able to be fed, played with and also put to bed
#Pet will engage with owner throughout the game

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

    #sleeping interaction
    def sleep(self):
        if not self.sleeping:
            self.sleeping = True
            self.energy += 3  #energy will increase by 3 when pet has slept
            if self.energy > 10:
                self.energy = 10  #ensures energy does not exceed the max of 10
            print(f"{self.name} is sleeping.")
        else:
            print(f"{self.name} is already asleep.")
    
    #waking interaction
    def wake_up(self):
        #when pet wakes up energy will reset to 10
        if self.sleeping:
            self.sleeping = False
            self.energy += 10
            print(f"You woke {self.name} up.")
            self.speak("I'm awake!")
        else:
            print(f"{self.name} is awake.")
    
    #exercise interaction
    #when pet exercises, happiness will increase by 1 and energy decreases by 3, hunger decreases by 2
    def exercise(self):
        if self.energy > 1:
            self.happiness +=1 
            self.energy  -= 3
            self.hunger -= 2
            self.interactions.append("exercised")
            print(f"You made {self.name} exercise.")
            self.speak("Ooof, what a workout!")
        else:
            print(f"{self.name} is too tired and does not want to exercise.")
            self.speak("I'm tired! I need a nap...")
    
    #playing interaction
    #happiness will increase by 3 and energy will reduce by 2 and hunger will reduce by 1
    def play(self):
        if self.energy >0:
            self.happiness += 3
            self.energy -=2
            self.hunger -= 1
            self.interactions.append("played")
            print(f"You played with {self.name}!")
            self.speak("I love playing with you! Your my bestfriend.")
        else:
            print(f"{self.name} is feeling tired and doesn't want to play.")
            self.speak("i'm feeling sleepy...")
            #owner promped to put pet to sleep
    
    #enable the pet to interact with owner to create a connection
    def speak(self,speech):
        print(f"{self.name} says: \"{speech}\"")

    #display pet vitals to pick what to do with pet
    def vitals(self):
        state = "sleeping" if self.sleeping else "awake"
        print(f"""{self.name}'s vitals:
              State: {state},
              Energy: {self.energy},
              Happiness: {self.happiness},
              Hunger: {self.hunger},
              Age: {self.age} years old.
              """)
        print(" past interactions: ", self.interactions)

    #stimulate time and change pet vitals
    def tick(self):
        if not self.sleeping:
            self.hunger -= 1
            self.energy -=2
            self.age += 0.5

            #setting the range of vitals scale
            if self.hunger >10:
                self.hunger = 10
            if self.hunger < 0 :
                self.hunger = 0
                self.speak("I am very very hungry!")
            if self.hunger < 4:
                self.happiness -=1
                self.speak("I am getting hungry...")
            if self.energy <0:
                self.energy = 0
                self.speak("I am drained! I want to sleep.")
                self.happiness -= 2
            if self.energy > 10:
                self.energy = 10
            if self.energy > 7:
                self.speak("I am very active!")   #when energy is above 7 pet will imply its ready to play or exercise
            if self.energy > 7:
                self.happiness += 2       #happiness increases by 2
            if self.happiness < 0:
                self.happiness = 0        #min happiness= 0 pet will initiate a response from owner
                self.speak("I am very unhappy!")
            if self.happiness > 10:
                self.happiness = 10       #hapiness max=10
            if self.happiness < 3:
                self.speak("I am feeling sad...")    #pet will let owner know if happiness is rapidly reducing
            elif self.happiness > 8:
                self.speak("I am sooo happy hehe!")   #pet shows its emotions regularly
        

 #create the actual digital pet
 #give owner the option to personalise their pet
def main():
    pet_name = input("What would you like to call your pet?")
    pet_type = input("What animal is your pet?")
    pet = DigitalPet(pet_name)

#ask owner to initiate what to do with the pet
    while True:
        task = input("\nPlease enter what you would like to do? (feed,play/exercise/sleep/wake/quit)")

        if task == 'feed':
            pet.feed()
        elif task == 'play':
            pet.play()
        elif task == 'exercise':
            pet.exercise()
        elif task == 'sleep':
            pet.sleep()
        elif task == 'wake':
            pet.wake_up()
        elif task == 'quit':
            print("goodbye...")
            break
        else:
            print("Error. Invalid Input.")
        
        pet.tick()
        pet.vitals()

main()
            


                  


