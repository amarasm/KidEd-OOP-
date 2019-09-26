import json

class Categories:

    def __init__(self, type):
        self.type = type
        


    @staticmethod
    def categ():
        with open('Categories.json') as File:
            file = json.load(File)
        categ = file["categories"]
        for list in categ.keys():
            return list



class Animals(Categories):

    type = "animals"

    def __init__(self):
        super().__init__(Animals.type)

    def AnimalJson(self):
        self.aname = self.categ["name"]
        self.akind = self.categ["kind"]
        self.asound = self.categ["sound"]


    def defineTheAnimal(self):
        print("\nanimal:")
        print("name:", self.aname,"\nkind:", self.akind,"\nsound:", self.asound)
        print("\n*****************")


class Colors(Categories):

    type = "colors"

    def __init__(self):
        super().__init__(Colors.type)

    def AnimalJson(self):
        self.cname = self.categ["name"]
        self.cprimary = self.categ["isPrimaryColor"]

    def defineColor(self):
        print("\ncolor:")
        print("name:", self.cname, "\nIs it a primary color?", self.cprimary)
        print("\n*****************")

class Alphabet(Categories):

    type = "alphabet"

    def __init__(self):
        super().__init__(Alphabet.type)

    def AnimalJson(self):
        self.Upper = self.categ["upperCase"]
        self.Lower = self.categ["lowerCase"]
        self.example = self.categ["example"]



    def defineAlphabet(self):
        print("\nletter:")
        print("Upper case:", self.Upper,"\nLower case:", self.Lower, "\nExample:", self.example, ".")
        print("\n*****************")

class Numbers(Categories):

    type = "numbers"

    def __init__(self):
        super().__init__(Alphabet.type)


    def AnimalJson(self):
        self.written = self.categ["name"]


    def defineNumber(self):
        print("\nnumber:")
        print("Written form:", self.written, ".")
        print("\n*****************")



def main():

    print("Dear user, welcome to this app. Here you can learn about", Categories.categ())
    type = input("Please choose which one you want to learn")
    while True:

        if type == "animals":
            print(Animals.defineTheAnimal())
            break
        elif type == "colors":
            print(Colors.defineColor())
            break
        elif type == "numbers":
            print(Numbers.defineNumber())
            break
        elif type == "alphabet":
            print(Alphabet.defineAlphabet())
            break
        else:
            print("Please try again")


main()