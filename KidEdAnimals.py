import json
import random

class Animals:

    def __init__(self):
        self.category = {}
        self.loadFromJson()
        
    def loadFromJson(self):
        with open('Animals.json') as data_file:
            file = json.load(data_file)
        animalsCateg = file["animals"]
        for key in animalsCateg:
            animal = Animal(key, animalsCateg[key]["sound"], animalsCateg[key]["kind"])
            self.category[key] = animal

    def getCategoryNames(self):
        names = []
        for key in self.category.keys():
            names.append(key)
        return names

    def getAnimals(self, count):
        yourchoices = random.choices(self.getCategoryNames(), k=count)
        for key in yourchoices:
            self.category[key].displayData()

    def getAnimalCateg(self):
        print(self.getCategoryNames())

class Animal:
    def __init__(self, name, sound, kind):
        self.name = name
        self.sound = sound
        self.kind = kind

    def displayData(self):
        print("Its name is", self.name, ", its sound is", self.sound,
              "and it's a type of", self.kind, ".")

def main():
    print("\nDear user welcome to this application. Here you can learn more about animals.")


    while True:
        choice = input("\nDo you want to learn about animals right now or not? yes/no")

        if choice == "yes":
            animals = Animals()

            print("Here are the keys:")
            animals.getAnimalCateg()

            while True:
                number = input("Number of animals you want to learn today:")
                if number.isnumeric():
                    number = int(number)
                    if number < 26:
                        break
                    else:
                        print("oops!You have to type a number from 1 to 25!Now try again!")
                else:
                    print("Please insert numbers only:)")
            
            animals.getAnimals(number)
            
            break
        elif choice == "no":
            print("\nOkay but be sure to come back.")
            break
        else:
            print("\ntry again.")

main()

