from .IncreaseSales.MenuCreator import *

while True:
    sleep(.25)
    choice = ""
    mainOptions = ["Stock", "Cart", "Buy", "Exit"]
    mainMen = Menu(mainOptions, "Buy Animals Here!!!")
    choice = mainMen.startMenu()

    match choice:
        case "Stock":
            while True:
                sleep(.25)
                stockOptions = ["Duck", "Dog", "Cat", "Boar", "Lion", "Back"]
                stockMenu = Menu(stockOptions, "Stock")
                choice = stockMenu.startMenu()
                match choice:
                    case "Back":
                        break
        case "Exit":
            exit()