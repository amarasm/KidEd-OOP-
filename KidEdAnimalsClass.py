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
        self.category = animalsCateg

    def getAnimals(self, count):
        animalList = []
        for keys in self.category.keys():
            animalList.append(keys)
        yourchoices = random.choices(animalList, k=count)
        for key in yourchoices:
            print("Its name is", key, ", its sound is", self.category[key]["sound"],
                  "and it's a type of", self.category[key]["kind"], ".")

    def getAnimalCateg(self):
        print(self.category.keys())

def main():
    print("\nDear user welcome to this application. Here you can learn more about animals.")


    while True:
        choice = input("\nDo you want to learn about animals right now or not? yes/no")

        if choice == "yes":
            animals = Animals()

            print("Here are the keys:")
            animals.getAnimalCateg()

            number = 0
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

