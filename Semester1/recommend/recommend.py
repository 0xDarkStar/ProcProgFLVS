from MenuCreator import *
from time import sleep
from random import choice

# Get desired destination (concert, beach, hot, cold, etc.)
# Get user preferences (favorite color, style, maybe more)
# After receiving all those inputs, recommend them clothing for the occasion
# NOTE: They do not need to choose the clothes, just say that the clothes are recommended.

# Requirements according to assignment:
#  1. Obtain user input (at least three values, show proper use of int(), float() and/or str())
#  2. Have at least one nested if/else and/or elif statement
#  3. Do proper math                     How tf do I include this???
#  4. Provide output based on user input

# Current Problem:
#  What is supposed to be using math?
#  Could changing a number or index count as "math" since I'd do "x = 5" "x += 1" or "x = x + 1"?

# Product class
class product:
    def __init__(self, name, style, category, color, generalTemp = 0):
        self.name = name
        self.style = style
        self.category = category
        self.generalTemp = generalTemp
        self.color = color

# Dictionaries:
# Type Limits Dictionary:
typeLimits = { # This will limit what styles and clothes can be used depending on destination type
    "Concert": ["Casual"],
    "Hiking": ["Sporty"],
    # "Water Activity": [],
    "Prom": ["Romantic", "Business Casual", "Casual"],
    "Business Meeting": ["Business Casual"]
}
# Category Dictionary:
categories = { # This will hold all the products depending on what they are. Don't want to be giving them a shoes but nothing to cover their private bits.
    "Shirts": [],
    "Pants": [],
    "Shorts": [],
    "Jackets": []
    # "Dresses": []
}

def recommend(destination, color):
    # Yes, I will be recommending a pair of shorts and pants at the same time, but I don't have time to worry about that
    allowed = {"Shirts": [], "Pants": [], "Shorts": [], "Jackets": []} # To store the clothes that could be chosen for recommendation
    recommended = [] # To store the recommended clothes
    stylesL = typeLimits[destination] # Grabs the limit on styles from the dictionary
    if len(stylesL) == 1: # There is only one item in the list
        style = stylesL[0] # Since there is only one, this makes it simpler
        for i in categories.keys(): # look at all the categories
            for j in categories[i]: # Look at all the items
                if j.style == style: # It is the allowed style
                    allowed[i].append(j) # Add it to the dicitonary
                    if j.color == color: # It is their favorite color
                        allowed[i].append(j) # Make it more likely to be chosen
    else: # There is more than one style allowed
        for i in categories.keys(): # look at all the categories
            for j in categories[i]: # Look at all the items
                if j.style in stylesL: # It is one of the allowed styles
                    allowed[i].append(j) # Add it to the dicitonary
                    if j.color == color: # It is their favorite color
                        allowed[i].append(j) # Make it more likely to be chosen
    for i in allowed.keys(): # Look through the dictionary of allowed clothes
        if len(allowed[i]) == 0: # There are no allowed clothes for this category...
            recommended.append(choice(categories[i])) # Randomly choose one from the original category dicitonary
        else:
            recommended.append(choice(allowed[i])) # Randomly choose one from the list
    return recommended

def products(): # Make all the products
    casBlueShirt = product("Casual Blue Shirt", "Casual", "Shirts", "Blue")
    casRedShirt = product("Casual Red Shirt", "Casual", "Shirts", "Red")
    casBluePants = product("Casual Blue Pants", "Casual", "Pants", "Blue")
    casRedPants = product("Casual Red Pants", "Casual", "Pants", "Red")
    casBlueShorts = product("Casual Blue Shorts", "Casual", "Shorts", "Blue")
    casRedShorts = product("Casual Red Shorts", "Casual", "Shorts", "Red")
    casBlueJacket = product("Casual Blue Jacket", "Casual", "Jackets", "Blue")
    casRedJacket = product("Casual Red Jacket", "Casual", "Jackets", "Red")
    sportyBlueShirt = product("Sporty Blue Shirt", "Sporty", "Shirts", "Blue")
    sportyRedShirt = product("Sporty Red Shirt", "Sporty", "Shirts", "Red")
    sportyBluePants = product("Sporty Blue Pants", "Sporty", "Pants", "Blue")
    sportyRedPants = product("Sporty Red Pants", "Sporty", "Pants", "Red")
    sportyBlueShorts = product("Sporty Blue Shorts", "Sporty", "Shorts", "Blue")
    sportyRedShorts = product("Sporty Red Shorts", "Sporty", "Shorts", "Red")
    sportyBlueJacket = product("Sporty Blue Jacket", "Sporty", "Jackets", "Blue")
    sportyRedJacket = product("Sporty Red Jacket", "Sporty", "Jackets", "Red")
    romBlueShirt = product("Romantic Blue Shirt", "Romantic", "Shirts", "Blue")
    romRedShirt = product("Romantic Red Shirt", "Romantic", "Shirts", "Red")
    romBluePants = product("Romantic Blue Pants", "Romantic", "Pants", "Blue")
    romRedPants = product("Romantic Red Pants", "Romantic", "Pants", "Red")
    romBlueShorts = product("Romantic Blue Shorts", "Romantic", "Shorts", "Blue")
    romRedShorts = product("Romantic Red Shorts", "Romantic", "Shorts", "Red")
    romBlueJacket = product("Romantic Blue Jacket", "Romantic", "Jackets", "Blue")
    romRedJacket = product("Romantic Red Jacket", "Romantic", "Jackets", "Red")
    buscasBlueShirt = product("Business Casual Blue Shirt", "Business Casual", "Shirts", "Blue")
    buscasRedShirt = product("Business Casual Red Shirt", "Business Casual", "Shirts", "Red")
    buscasBluePants = product("Business Casual Blue Pants", "Business Casual", "Pants", "Blue")
    buscasRedPants = product("Business Casual Red Pants", "Business Casual", "Pants", "Red")
    buscasBlueShorts = product("Business Casual Blue Shorts", "Business Casual", "Shorts", "Blue")
    buscasRedShorts = product("Business Casual Red Shorts", "Business Casual", "Shorts", "Red")
    buscasBlueJacket = product("Business Casual Blue Jacket", "Business Casual", "Jackets", "Blue")
    buscasRedJacket = product("Business Casual Red Jacket", "Business Casual", "Jackets", "Red")
    productsL = [casBlueShirt, casRedShirt, casBluePants, casRedPants, casBlueShorts, casRedShorts, casBlueJacket, casRedJacket, sportyBlueShirt, sportyRedShirt, sportyBluePants, sportyRedPants, sportyBlueShorts, sportyRedShorts, sportyBlueJacket, sportyRedJacket, romBlueShirt, romRedShirt, romBluePants, romRedPants, romBlueShorts, romRedShorts, romBlueJacket, romRedJacket, buscasBlueShirt, buscasRedShirt, buscasBluePants, buscasRedPants, buscasBlueShorts, buscasRedShorts, buscasBlueJacket, buscasRedJacket]
    for i in productsL:
        categories[i.category].append(i) # Put them into the dicitonary


def main():
    sleep(1)
    products()
    while True:
        # Introduce them to the recommendation store/site/whatever
        mainMenu = Menu(["Get Recommendation", "Recommended Outfit", "Exit"], "Closet Companion", "I'm here to help you pick out the \"\x1B[3mperfect\x1B[23m\"")
        # They have three options: Get Recommendation, Recommended Outfits, or Exit
        choiceM = mainMenu.startMenu()
        # If they choose "Get Recommendation", start the input gathering process
        match choiceM:
            case "Get Recommendation":
                # First menu (in the recommendation path): The type of destination
                typeMenu = Menu(["Concert", "Hiking", "Prom", "Business Meeting", "???"], "What type of destination is it?")
                destination = typeMenu.startMenu()
                if destination == "???": # No reason for this, just dumb.
                    a = 0
                    while a < 10:
                        print("???")
                        a = a + 1
                        sleep(.5)
                    exit()
                # Second menu: The time they'd most likely be at the destination (EXCLUDED FOR NOW)
                # Third menu: The weather that they'd most likely be experiencing (EXCLUDED FOR NOW)
                # Fourth menu: The temperature it would be at their destination (EXCLUDED FOR NOW)
                # Fifth menu: Get their favorite color
                colorMenu = Menu(["Red", "Blue", "Green", "Yellow", "Pink", "Purple", "Orange"], "Choose your favorite color.") # Not really important
                color = colorMenu.startMenu()
                # They finished all the menus, use all the inputs to search dictionaries for matching tags
                recommended = recommend(destination, color)
                # Choose at most one item for each part (hat, scarf, shirt, jacket, pants, shoes, socks, gloves, etc.) (too much with too little time)
                # Notice how I said "at most", if no items are found for a certain part, it will skip that part. (Not happening, something WILL be chosen)
            case "Recommended Outfit":
                try:
                    # After choosing all the items, tell them what they should wear
                    recommendMen = Menu(["Exit"], "Recommended Outfit", f"Shirt: {recommended[0].name}\nPants: {recommended[1].name}\nShorts: {recommended[2].name}\nJacket: {recommended[3].name}")
                    choiceM = recommendMen.startMenu()
                except UnboundLocalError:
                    print("You don't have a recommended outfit yet. Select \"Get Recommendation\" to get a recommended outfit.")
                    sleep(3)
            case "Exit":
                exit()
                # End the program
main()