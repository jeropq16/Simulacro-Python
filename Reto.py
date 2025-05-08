inventory = {}

lgenres= ["fiction", "nonfiction", "science", "biography", "children"]



def addbooks():
    name = input("Enter the name of the book: ")
    author = input("Enter the author: ")
    copies = int(input("Enter the number of copies: "))

    genre = input(''' 
                  fiction
                  nonfiction
                  science
                  biography
                  children 
                  
                  Enter the genre of the book: ''')
    
    if genre == "fiction" or genre == "nonfiction" or genre == "science" or genre == "biography" or genre == "children":

        inventory [name] = {"name": name, "author": author, "copies": copies, "genre": genre}
        print (f"{name} added correctly")
    else:
        print("Please enter a valid option: ")

    print (inventory)

def searchbooks():
    name = input("Enter the name of the book: ")
    if name in inventory:
        product = inventory[name]
        print(f"book name : {name}, author: {product ["author"]}, copies: {product["copies"]}, genre: {product["genre"]}")
    else:
        print(f"The book {name} is not in the inventory")


def loanbooks():
    name = input("Enter the name of the book you want to loan: ")
    if name in inventory:
        if inventory[name]["copies"] >0:
           inventory[name]["copies"] -=1
           print(f"The book has been loan, return the book in two days")
        else:
            print("No copies of this book are available")
    else:
        print("This book is not in inventory")


def returnbooks():
    name = input("Enter the name of the book what you want to return: ")
    if name in inventory:
        inventory [name]["copies"] +=1
        print("Tnaks for return the book")


def deletebooks():
    name = input("Enter the name of the book what you want delete: ")
    if name in inventory:
        deletecopies = int(input("How many copies do you want delete?: "))
        if deletecopies <= inventory[name]["copies"]:
            inventory [name]["copies"] -= deletecopies
            print(f"{deletecopies} copies of {name} has been deleted")
        else:
            print("You can't delete more copies than those in your inventory")
    else:
        print("The book is not in the inventory")


def listbooks():
    for i, x in enumerate (lgenres,1):
        print (f"{i}: {x}")

    case= int(input("Enter a number?: "))


    for name, a in inventory.items():
    
        if case == 1:
            if "fiction" == a["genre"]:
                print (name)
        elif case == 2:
            if "nonfiction" == a["genre"]:
                print (name)
        elif case == 3:
            if "science" == a["genre"]:
                print (name)
        elif case == 4:
            if "biography" == a["genre"]:
                print (name)
        elif case == 5:
            if "children" == a["genre"]:
                print (name)
        else:
            print("please enter a valid option")
            

def totalinventory():
    for name, a in inventory.items():
        print(f"{name}: {a["copies"]} copies")


while True:
    print('''main menu
          1. add books
          2. search books
          3. loans books
          4. return books
          5. delete books
          6. search for genre
          7. total inventory
          8. quit the program  ''')
    
    option = input("Enter an option: ")
    if option == "1":
        addbooks()
    elif option == "2":
        searchbooks()
    elif option == "3":
        loanbooks()
    elif option == "4":
        returnbooks()
    elif option == "5":
        deletebooks()
    elif option == "6":
        listbooks()
    elif option == "7":
        totalinventory()
    elif option == "8":
        print ("Thanks for using the program")
        break    
    else:
        print("Please enter a valid option")
