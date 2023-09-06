from MenuCreator import *

prices = {
    "Polish Flag Shirt": 13.99,
    "Indonesian Flag Shirt": 13.99
}
descriptions = {
    "Polish Flag Shirt": "Cost: $13.99\nThe perfect shirt to gift somebody that is traveling abroad!"
}

itemsInCart = []

while True:
    startOptions = ["Clothing Categories", "Cart", "Exit"]
    mainMenu = Menu(startOptions, "Fashion Boutique")
    choice = mainMenu.startMenu()
    match choice:
        case "Clothing Categories":
            while True:
                clothingOptions = ["Shirts", "Legwear", "Dressers", "Shoes", "Dresses", "Underwear", "Back"]
                clothingMenu = Menu(clothingOptions, "Categories")
                choice = clothingMenu.startMenu()
                match choice:
                    case "Shirts":
                        while True:
                            shirtsOptions = ["Polish Flag Shirt", "Indonesian Flag Shirt", "Back"]
                            shirtsMenu = Menu(shirtsOptions, "Shirts")
                            choice = shirtsMenu.startMenu()
                            if choice == "Back":
                                break
                            else:
                                while True:
                                    options = ["Add to Cart", "Back"]
                                    desc = descriptions[choice]
                                    product = choice
                                    productMenu = Menu(options, product, desc)
                                    choice = productMenu.startMenu()
                                    match choice:
                                        case "Add to Cart":
                                            itemsInCart.append(product)
                                            break
                                        case "Back":
                                            break
                    
                    case "Legwear":
                        while True:
                            shortsOptions = ["Back"]
                            shortsMenu = Menu(shortsOptions, "Legwear")
                            choice = shortsMenu.startMenu()
                            match choice:
                                case "Back":
                                    break
                    
                    case "Dressers":
                        while True:
                            dresserOptions = ["Back"]
                            dresserMenu = Menu(dresserOptions, "Dressers")
                            choice = dresserMenu.startMenu()
                            match choice:
                                case "Back":
                                    break
                    
                    case "Shoes":
                        while True:
                            shoesOptions = ["Back"]
                            shoesMenu = Menu(shoesOptions, "Shoes")
                            choice = shoesMenu.startMenu()
                            match choice:
                                case "Back":
                                    break
                    
                    case "Dresses":
                        while True:
                            dressOptions = ["Back"]
                            dressMenu = Menu(dressOptions, "Dresses")
                            choice = dressMenu.startMenu()
                            match choice:
                                case "Back":
                                    break
                    
                    case "Underwear":
                        while True:
                            underwearOptions = ["Caveman Leaf By Gucci", "Back"]
                            underwearMenu = Menu(underwearOptions, "Underwear")
                            choice = underwearMenu.startMenu()
                            match choice:
                                case "Back":
                                    break

                    case "Back":
                        break
        case "Cart":
            itemsInCartCode = []
            for i in itemsInCart:
                itemsInCartCode.append(i)
            count = 0
            for i in itemsInCart:
                for a in range(count):
                    itemsInCartCode[count] += " "
                count += 1
            itemsInCartCode.append("Back")
            while True:
                totalCost = 0
                for i in itemsInCart:
                    totalCost = totalCost + prices[i]
                tax = totalCost*.07
                totalCost += tax
                totalCost = int(totalCost*100)/100
                description = "Subtotal:\n"
                for i in itemsInCart:
                    addString = f"  {i}: {prices[i]}\n"
                    description += addString
                description += f"Total Cost: ${totalCost}"
                cartMenu = Menu(itemsInCartCode, "Your Cart", description)
                choice = cartMenu.startMenu()
                if choice == "Back":
                    break
                else:
                    count = 0
                    oldChoice = ""
                    oldChoice += choice
                    while True:
                        if choice[-1] != " ":
                            break
                        elif choice[count] != " " and choice[count + 1] == " ":
                            print(choice[count])
                            print(choice[count + 1])
                            print(choice[-1])
                            choice = choice[:count+1]
                            break
                        elif choice[count] != " " and choice[count + 2] == " ":
                            choice = choice[:count+1]
                            break
                        else:
                            count -= 1
                    while True:
                        desc = descriptions[choice]
                        productMenu = Menu(["Remove From Cart", "Back"], choice, desc)
                        product = choice
                        choice = productMenu.startMenu()
                        match choice:
                            case "Remove From Cart":
                                itemsInCart.remove(product)
                                print(itemsInCartCode)
                                itemsInCartCode.remove(oldChoice)
                                break
                            case "Back":
                                break
        case "Exit":
            os.system("clear")
            exit()
