import json
import random

class LinkedList:
    def __init__(self):
        self.head = None

    def setHead(self, animalName, animalSound, animalKind):
        self.head = Animal(animalName, animalSound, animalKind)

    def appending(self, animalName, animalSound, animalKind):
        temp = self.head
        if temp is None:
            self.setHead(animalName, animalSound, animalKind)
        else:
            while temp.next is not None:
                temp = temp.next
            newAnimal = Animal(animalName, animalSound, animalKind)
            temp.next = newAnimal


    def displayData(self, key):
        printAnimal = self.head
        while printAnimal is not None:
            if printAnimal.name == key:
                print("Its name is", printAnimal.name, ", its sound is", printAnimal.sound,"and it's a type of", printAnimal.kind)
                break
            else:
                printAnimal = printAnimal.next


    def createCategory(self):
        names = []
        keys = self.head
        while keys is not None:
            names.append(keys.name)
            keys = keys.next
        return names

class Animals:

    def __init__(self):
        self.category = LinkedList()
        self.loadFromJson()

    def loadFromJson(self):
        with open('Animals.json') as data_file:
            file = json.load(data_file)
        animalsCateg = file["animals"]
        return animalsCateg


    def appendingNewAnimals(self):
        animalsCateg = self.loadFromJson()
        for key in animalsCateg:
            self.category.appending(animalsCateg[key]["name"], animalsCateg[key]["sound"], animalsCateg[key]["kind"])


    def getCategoryNames(self):
        temp = self.category
        print((", ").join(temp.createCategory()))

    def getAnimals(self, count):
        categ = self.category.createCategory()
        yourchoices = random.choices(categ, k=count)
        for key in yourchoices:
            self.category.displayData(key)



class Animal:
    def __init__(self, name, sound, kind):
        self.name = name
        self.sound = sound
        self.kind = kind
        self.next = None




def main():
    print("\nDear user welcome to this application. Here you can learn more about animals.")

    while True:
        choice = input("\nDo you want to learn about animals right now or not? yes/no")

        if choice == "yes":
            animals = Animals()

            animals.appendingNewAnimals()

            print("Here are the keys:")
            animals.getCategoryNames()


            while True:
                number = input("\nNumber of animals you want to learn today:\n")
                if number.isnumeric():
                    number = int(number)
                    if number < 26:
                        break
                    else:
                        print("\n\noops!You have to type a number from 1 to 25!Now try again!")
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
