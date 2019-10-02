import json

class Animals:

    def __init__(self):
        self.category = []

    def getAnimalInformation(self):
        with open('Animals.json') as data_file:
            file = json.load(data_file)
        animalsCateg = file["animals"]
        self.name = animalsCateg.keys()


    def getAnimalCateg(self):
        with open('Animals.json') as data_file:
            file = json.load(data_file)
        animalsCateg = file["animals"]
        self.category.append(animalsCateg)
        print(animalsCateg.keys())


    # @staticmethod
    # def getAnimalList(category):
    #     for keys in category.keys():
    #         return keys

def main():
    print("\nDear user welcome to this application. Here you can learn more about animals.")


    while True:
        choice = input("\nDo you want to learn about animals right now or not? yes/no")

        if choice == "yes":
            print("Here are the keys:")
            # animalName = input("\nWhich animal do you want to learn about today?")
            # Animals.getAnimalInformation()
            Animals()

            break
        elif choice == "no":
            print("\nOkay but be sure to come back.")
            break
        else:
            print("\ntry again.")


main()

