from MenuCreator import *
from PIL import Image
from time import time
from random import choice

# I wanted to make a program that would act as a fashion store with dumb, random products.
# However, I couldn't find out what to make for each category, so almost all of them are empty.
# I thought picking things that were already made would be better, but then I had trouble because of my plan for the project.
# This is now just a fashion store that is going out of buisness. That's it! I cna make it seem like a store desperate to make a few more bucks before finally closing!

productTags = { # Tags to recommend products
    # Shirts
    "Polish-Flag-Shirt": ["Shirt", "Travel"],
    "Indonesian-Flag-Shirt": ["Shirt", "Travel"],
    # Legwear
    "Mirror-Pants": ["Legwear", "Pants"],
    "Denim-Pants": ["Legwear", "Pants"],
    "Hip-Hop-Cargo-Shorts": ["Legwear", "Shorts"],
    "I-Fear-God-Shirts": ["Legwear", "Shorts"],
    "Denim-Skirt": ["Legwear", "Skirt", "Denim"],
    "Tight-Denim-Skirt": ["Legwear", "Skirt", "Denim"],
    # Dressers
    "Malm": ["Dresser"],
    "Bellmore": ["Dresser"],
    "Weslar": ["Dresser"],
    "Abdulbari": ["Dresser"],
    "Lakeleigh": ["Dresser"],
    # Dresses
    "Mini-Shirt-Dress": ["Dresses", "Shiny", "Mini"],
    "Shiny-Mini-Dress": ["Dresses", "Shiny", "Mini"],
    "Satin-Mermaid-Dress": ["Dresses", "Long"],
    "Long-Flower-Print-Dress": ["Dresses", "Long"],
    # Underwear
    "3-Pack-Warface-Camo-Glow": ["Underwear"],
    "Christmas-Briefs": ["Underwear"],
    "Caveman-Leaf-By-Gooccii": ["Underwear", "Travel"],
    # NFTs
    "Totsugeki": ["NFT", "Dumb"],
    "Neco-Arc": ["NFT", "Dumb"],
    "Cat": ["NFT", "Dumb"],
    "Spy": ["NFT", "Dumb"],
    "Kasumi": ["NFT", "Dumb"],
    "Fat-Fuck": ["NFT", "Dumb"]
}

searchTags = {
    "Shirt": ["Polish-Flag-Shirt", "Indonesian-Flag-Shirt"],
    "Travel": ["Polish-Flag-Shirt", "Indonesian-Flag-Shirt", "Caveman-Leaf-By-Gooccii"],
    "Legwear": ["Mirror-Pants", "Denim-Pants", "Hip-Hop-Cargo-Shorts", "I-Fear-God-Shirts", "Denim-Skirt", "Tight-Denim-Skirt"],
    "Pants": ["Mirror-Pants", "Denim-Pants"],
    "Shorts": ["Hip-Hop-Cargo-Shorts", "I-Fear-God-Shirts"],
    "Skirt": ["Denim-Skirt", "Tight-Denim-Skirt"],
    "Denim": ["Denim-Skirt", "Tight-Denim-Skirt"],
    "Dresser": ["Malm", "Bellmore", "Weslar", "Abdulbari", "Lakeleigh"],
    "Dresses": ["Mini-Shirt-Dress", "Shiny-Mini-Dress", "Satin-Mermaid-Dress", "Long-Flower-Print-Dress"],
    "Shiny": ["Mini-Shirt-Dress", "Shiny-Mini-Dress"],
    "Mini": ["Mini-Shirt-Dress", "Shiny-Mini-Dress"],
    "Long": ["Satin-Mermaid-Dress", "Long-Flower-Print-Dress"],
    "Underwear": ["Caveman-Leaf-By-Gooccii", "Christmas-Briefs", "3-Pack-Warface-Camo-Glow"],
    "NFT": ["Totsugeki", "Neco-Arc", "Cat", "Spy", "Kasumi", "Fat-Fuck"],
    "Dumb": ["Totsugeki", "Neco-Arc", "Cat", "Spy", "Kasumi", "Fat-Fuck"]
}

prices = { # All the prices
    # Shirts
    "Polish-Flag-Shirt": 13.99,
    "Indonesian-Flag-Shirt": 13.99,
    # Legwear
    "Mirror-Pants": 102.14,
    "Denim-Pants": 36.99,
    "Hip-Hop-Cargo-Shorts": 26.79,
    "I-Fear-God-Shirts": 20.00,
    "Denim-Skirt": 49.90,
    "Tight-Denim-Skirt": 59.33,
    # Dressers
    "Malm": 299.99, # Thank you, Ikea
    "Bellmore": 1099.00, # Thank you, Home Depot
    "Weslar": 239.99, # Thank you, Target
    "Abdulbari": 85.99, # Thank you, Wayfair
    "Lakeleigh": 999.99, # Thank you, Ashley Furniture (It looks ugly)
    # Dresses
    "Mini-Shirt-Dress": 650.00,
    "Shiny-Mini-Dress": 80.00,
    "Satin-Mermaid-Dress": 64.90,
    "Long-Flower-Print-Dress": 253.99,
    # Underwear
    "3-Pack-Warface-Camo-Glow": 65.00,
    "Christmas-Briefs": 9.00,
    "Caveman-Leaf-By-Gooccii": 4400.00,
    # NFTs
    "Totsugeki": 19.99,
    "Neco-Arc": 19.99,
    "Cat": 29.99,
    "Spy": 29.99,
    "Kasumi": 24.99,
    "Fat-Fuck": 39.99
}
descriptions = { # A lot of descriptions...
    # Shirts
    "Polish-Flag-Shirt": "The perfect shirt to gift somebody that is traveling abroad!",
    "Indonesian-Flag-Shirt": "The perfect shirt to gift somebody that is traveling abroad!",
    # Legwear
    "Mirror-Pants": "Step into the world of style and shine with our Mirror Pants. Crafted from a luxurious, sleek, and ultra-smooth material, these pants are designed to make a bold statement. With a dazzling rainbow shine, they catch the light and turn heads wherever you go. These pants are perfect for those who want to stand out in any crowd and make a fashion statement that's uniquely their own. Elevate your wardrobe with Mirror Pants and embrace a look that reflects your distinctive style.",
    "Denim-Pants": "Introducing our classic Denim Pants with a modern twist. These pants combine the timeless charm of denim with a contemporary flair. The standout feature of these pants is their flared ends, offering a touch of vintage-inspired elegance. Whether you're headed to a casual outing or a stylish event, these pants are versatile enough to complement any occasion. Elevate your fashion game with Denim Pants that blend comfort, style, and a dash of retro chic.",
    "Hip-Hop-Cargo-Shorts": "Get ready to unleash your inner hip-hop artist with our Hip Hop Cargo Shorts. These shorts take the concept of 'pockets' to a whole new level. With an abundance of pockets and pouches, you'll have space for everything, and we mean everything! Whether it's your keys, phone, snacks, or your collection of lucky pennies, these shorts have got you covered. And who can forget the stylish straps that add an element of intrigue to your look? Just remember, the more you carry, the more you can 'dance' your way through life. Upgrade your streetwear game with the ultimate in pocket-packed fashion.",
    "I-Fear-God-Shorts": "Elevate your casual style with our 'I Fear God' Shorts. These shorts make a powerful statement with their bold message. Featuring the words 'I Fear God' prominently emblazoned on the fabric, they serve as a testament to your faith and values. The design also incorporates three crosses on the left leg, symbolizing your commitment to spirituality. Made with comfort in mind, these shorts are perfect for everyday wear, whether you're hitting the court, running errands, or simply relaxing. Wear your faith proudly and stylishly with 'I Fear God' Shorts.",
    "Denim-Skirt": "Upgrade your wardrobe with our stylish Denim Skirt, a fusion of classic denim jeans and contemporary flair. This unique skirt showcases the creative transformation of jeans into a fashionable skirt that's as comfortable as it is chic. Crafted from quality denim material, this knee-length skirt exudes a relaxed yet trendy vibe. The visible jeans elements give it an edgy touch, making it a standout piece for any casual outing. Embrace the charm of denim with a twist, and make a fashion statement that's uniquely you.",
    "Tight-Denim-Skirt": "Unleash your inner fashionista with our Tight Denim Skirt, a daring fusion of sophistication and bold style. This skirt takes the concept of 'slim fit' to a whole new level by adopting the classic pencil skirt design and crafting it from denim, a material known for its unyielding nature. The result? A form-fitting masterpiece that accentuates your curves and leaves a lasting impression wherever you go. While comfort might take a backseat, your confidence will be front and center. Embrace the sleek, body-hugging allure of our Tight Denim Skirt and step into a world of fashion-forward elegance.",
    # Dressers
    "Malm": "A clean expression that fits right in, in the bedroom or wherever you place it. Smooth-running drawers and in a choice of finishes - pick your favorite. Psst! Please attach to the wall.\nOf course your home should be a safe place for the entire family. That's why hardware is included so that you can attach the chest of drawers to the wall.\n\nA wide chest of drawers gives you plenty of storage space as well as room for lamps or other items you want to display on top.\n\nSmooth running drawers with pull-out stop.",
    "Bellmore": "Enhance your bedroom decor with this Home Decorators Collection Bellmore nine-drawer dresser. The flat wooden top surface lets you display lamps, vases and more. For ample storage space, it comes with nine drawers. A white finish adds decorative charm.",
    "Weslar": "This classic and traditional 5 Drawer Dresser is the perfect solution for organized living. With plenty of space to keep your clothing neatly where it belongs, you can easily ensure a hassle-free morning routine for yourself and your family. The dresser is conveniently equipped with our SwitchLock™ Assembly System which cuts assembly time nearly in half. The interlocking pieces come preassembled in the boards, and your drawer slides are conveniently attached to the drawer sides to take away any guessing while assembling. This dresser is beautifully laminated in several neutral woodgrain finishes to give the Dresser a classic look that fits your unique bedroom décor. The 5 drawers feature durable metal slides to store your jeans, sweaters, or extra linens. Each drawer is finished in a smooth linen patterned paper to keep your clothes from snagging on raw edges. A wall anchor kit is included to prevent tipping injuries and keep your family safe. The Dresser ships flat to your door and requires assembly upon delivery. Two adults are recommended to assemble. Once assembled, the Dresser measures to be 49.33” H x 27.72” W x 15.67” D.",
    "Abdulbari": "A good dresser can do wonders for your home, like provide extra storage for clothes, maximize the lower half of a tiny closet, and double as a TV stand...This modern media chest features clean, simple lines and beautifully clashing finishes that will impress your guests. There's plenty of room on the middle shelf for your magazine and alarm clock.",
    "Lakeleigh": "Opposites attract. The Lakeleigh chest opens our eyes to how casually rustic styling and an industrial hip vibe make for one happy marriage. Elements that beautify Lakeleigh's chunky, linear profile include through-tenon styling, replicated planking and a high-grain finish rich with tonal variation. Unique \"barn door\" slider and shelved storage are a welcome surprise. What's even more unexpected: how such a high-quality designer piece can be so attractively priced.",
    # Dresses
    "Mini-Shirt-Dress": "Elevate your evening ensemble with our Mini Shirt Dress, a dazzling fusion of sophistication and glamour. This unique dress takes inspiration from the classic suit shirt and adds a playful twist with an attached skirt that exudes timeless elegance. The all-black design serves as the perfect canvas for an array of shimmering jewels, strategically placed to catch the light and turn heads wherever you go. Whether you're attending a special event or a night out on the town, this dress effortlessly combines class and dazzle. Make a statement in our Mini Shirt Dress and leave a trail of elegance in your wake.",
    "Shiny-Mini-Dress": "Prepare to steal the spotlight in our Shiny Mini Dress, a radiant showstopper that's perfect for those who love to shine. This dress boasts a sleek and form-fitting design, with long sleeves extending to the wrists and a convenient zipper closure at the back. The entire dress is drenched in a mesmerizing white hue, acting as the ultimate canvas for a dazzling array of reflective and shiny embellishments. With every move you make, the world around you transforms into a dance floor, casting captivating reflections and turning heads in awe. Our Shiny Mini Dress is your ticket to becoming a human disco ball, radiating pure elegance and charm.",
    "Satin-Mermaid-Dress": "Dive into the lap of luxury with our Satin Mermaid Dress, a breathtaking masterpiece that combines the rich allure of satin with the alluring silhouette of a mermaid-style gown. This dress is a testament to timeless elegance, with its seamless blend of satin's silky texture and the iconic mermaid flare. Crafted in a luxurious color reminiscent of satin's lustrous sheen, this dress promises to make you the embodiment of sophistication and grace.\n\nWhile its enchanting design is sure to captivate, it's important to note that the Satin Mermaid Dress prioritizes style over ease of movement. With its figure-hugging contours and a lack of slits, this dress is a statement piece for those who appreciate the artistry of fashion and are willing to embrace the challenge of navigating a world while wearing a work of art.",
    "Long-Flower-Print-Dress": "Embrace the ethereal beauty of our Long Flower Print Dress, a gown that sweeps you into a world of enchantment and elegance. This dress is a symphony of length and charm, designed to grace every step with its flowing presence. With a skirt that descends gracefully down a flight of stairs and beyond, it's truly a testament to the grandeur of fashion.\n\nAdorned with delicate floral patterns and whimsical butterflies, this dress brings a touch of nature's beauty to your every movement. Whether you're attending a gala, prom, or simply want to feel like a fairy-tale princess, the Long Flower Print Dress promises to make every moment a magical one. However, please note that its extraordinary length may require some strategic maneuvering, especially on staircases.",
    # Underwear
    "3-Pack-Warface-Camo-Glow": "Introducing our 3 Pack Warface Camo Glow underwear - the perfect blend of style and excitement. These briefs not only feature a bold warface design that'll make a statement but also come to life with a mesmerizing glow in the dark. Step into the night with confidence and a dash of adventure with every pair.",
    "Christmas-Briefs": "Elevate your holiday spirit with our Christmas Briefs, designed to bring the festive cheer right where it matters most. These comfortable and fun briefs showcase an adorable pattern of Christmas trees, adding a touch of yuletide magic to your everyday wear. Celebrate the season in style and comfort with this joyful addition to your wardrobe.",
    "Caveman-Leaf-By-Gooccii": "Introducing the 'Caveman Leaf By Goocci' - A truly prehistoric fashion statement that combines the sophistication of Gooccii with the timeless elegance of caveman couture. Crafted from the finest virtual leaves, this exclusive piece of underwear will transport you to an era when fashion was all about embracing your wild side.",
    # NFTs
    "Totsugeki": "Annoying ass dolphin that will scream \"\x1B[1;3mTOTSUGEKI!!!\x1B[0m\" every chance it gets.",
    "Neco-Arc": "Some stupid cat that ate a lemon and is now forever puckered.",
    "Cat": "Behold the \"Cat\" , featuring an infuriatingly grumpy white kitten. It's got arms drawn in at an angle that says, \"Why are you even looking at me?\" Perfect for those moments when you need a digital side-eye.",
    "Spy": "It's the freakin' Spy! And it's about as pixelated as your first dial-up internet connection. Grab it if you're into nostalgic pixel mayhem and don't mind squinting at your screen.",
    "Kasumi": "Meet \"Kasumi,\" caught in a meme moment that's funnier than your uncle's dad jokes. It cries just about as much as you do.",
    "Fat-Fuck": "Feast your eyes on \"Fat Fuck,\" it's stretched out wider than your grandma's couch and smells just as bad."
}

itemsInCart = []
ignoreList = []

def productPage(choice: str, itemsInCartCode: list = False): # This is to show the products information from anywhere
    productName = choice # Make a copy of the name before editing to show the copy to the user
    while " " in choice: # While there are spaces in the string
        choice = choice.replace(" ", "-") # Replace them with dashes
    product = choice # To have the code work (I don't want to take the risk of the code breaking because it's looking for "up.jpg" or "prices[up]")
    if itemsInCartCode != False: # They are from the cart
        options = ["Remove from Cart", "Back"] # Their options
    else: # They aren't from the cart
        options = ["Add to Cart", "Back"] # Their options
    desc = descriptions[product] # Grab the description for the product
    productMenu = Menu(options, productName, f"Cost: ${prices[product]}\n{desc}") # Make the menu (also grab the price of the product)
    try: # Try to get the image of the product
        productImage = Image.open(f"Product_Images/{product}.jpg", "r") # Grab the image
        productImage.show() # Open the image
    except FileNotFoundError: # Image not found!!!
        print("I couldn't find the image. :/") # Nobody would see this unless I get rid of the "os.systen("clear")"
    choice = productMenu.startMenu() # Start the menu
    try: # Try to close the image
        productImage.close() # Close the image in memory
    except UnboundLocalError: # "productImage" hasn't been defined yet!!!
        print("Woops! :p") # Doesn't matter! :)
    if choice == "Add to Cart": # They want to add it to their cart
        itemsInCart.append(productName) # Add it to their cart
    elif choice == "Remove from Cart":
        itemsInCart.remove(productName)
    # If they didn't choose to add it to their cart, the function would end anyway. It ending means they go back to the menu they were previously in.

def recommend(itemsInCart, ignoreList): # This is used to recommend a product to them based on the tags attached to each product.
    if itemsInCart == []: # There are no items in their cart
        return None # Don't recommend anything
    # There are items in their cart
    itemsInCartDashes = [] # Make this list for the code to use
    for i in itemsInCart: # Look at all the product
        i = i.replace(" ", "-") # Replace all the spaces with dashes to work with the code
        itemsInCartDashes.append(i) # Add it to the previous mentioned list
    tags = [] # List to store all the tags
    for i in itemsInCartDashes: # Look at all their items
        for j in productTags[i]: # Look at the tags of all their items
            tags.append(j) # Add those tags
    tagCount = {} # Dictionary to store how many times the tags appear
    for i in tags: # Look at all the tags
        if i not in tagCount.keys(): # That tag isn't in the dictionary
            tagCount[i] = 1 # Add it to the dictionary and set it's value to 1
        else: # It is in the dictionary
            tagCount[i] += 1 # Add 1 to the value
    highestValue = 0 # To find out the tag that appears the most
    mostFrequentTag = "" # To store the name of the tag that appears the most
    for i in tagCount.keys(): # Look at all the tags
        if tagCount[i] > highestValue: # The amount of times that tag appears is more than the other tags that it has checked
            highestValue = tagCount[i] # Update the highest value
            mostFrequentTag = i # Update the most frequent tag
        elif tagCount[i] == highestValue: # The tag occurs the same amount of times as another/the others
            mostFrequentTag += f" {i}" # Add it to the tags that occur the same amount
    if f" " in mostFrequentTag: # There is a space in the string (there are at least two tags)
        keyTags = mostFrequentTag.split(f" ") # Make it into a list to find the tags
        productListTrans = [] # List of the lists of products with the same tags
        for i in keyTags: # Look at all the tags
            productListTrans.append(searchTags[i]) # Add the list of products under that tag to the previously mentioned list
        productList = [] # List that would store all the products that can be recommended
        for i in productListTrans: # Look at all the lists in the list
            for j in i: # Look at every item inside the sub-list
                if j not in productList: # The item isn't already in the the list of products to recommend
                    productList.append(j) # Add it to the list
    else: # There is only one tag
        productList = searchTags[mostFrequentTag] # Add the list of products to recommend
    for i in itemsInCartDashes: # Look at the cart
        if i in productList: # An item in the cart is in the recommendation list
            productList.remove(i) # Remove the item from the recommendation list
    a = 0 # To keep track of how many times it loops
    while True: # Loop to find a recommendation
        recommendation = choice(productList) # Randomly choose a recommendation from the list
        recommendation = recommendation.replace("-", " ") # Replace the dashes with spaces for the user to read
        if recommendation not in ignoreList: # The recommendation is not in the ignore list
            break # Break out of the loop
        elif a == 50: # The loop has repeated for the 50th time
            recommendation = None # Say that there is no recommendation to give
            break # Break out of the loop
        else: # The recommendation was in the ingore list
            a += 1 # Cycle to the next instance
    return recommendation # Send the recommendation

def main(): # The entire store part
    stylistCard = False # To keep track if they have the card or not
    while True: # Loop for the main menu (the loops are to allow the user to go back and forth between parent and sub-menus as much as they like. Without loops, they'd only be able to choose something in that menu once.)
        startOptions = ["Product Categories", "Cart", "Exit"] # Their options in the menu
        mainMenu = Menu(startOptions, "Fashion Boutique", "\x1B[2mDisclaimer: This is all a joke. Don't take anything seriously.\x1B[0m") # Make the menu
        choice = mainMenu.startMenu() # We start the menu and recieve their choice
        match choice: # Check what their choice was
            case "Product Categories": # They choce to see the different products
                while True: # Loop for this menu
                    clothingOptions = ["Shirts", "Legwear", "Dressers", "Dresses", "Underwear", "NFTs", "Back"] # Their options
                    clothingMenu = Menu(clothingOptions, "Categories") # Make the menu
                    choice = clothingMenu.startMenu() # Start it
                    match choice: # Check what they chose
                        case "Shirts": # They want to look at shirts
                            while True: # Loop for the menu
                                shirtsOptions = ["Polish Flag Shirt", "Indonesian Flag Shirt", "Back"] # Their options
                                shirtsMenu = Menu(shirtsOptions, "Shirts") # Make the menu
                                choice = shirtsMenu.startMenu() # Start it
                                if choice == "Back": # They are done looking at the shirts
                                    break # Bring them back to the categories menu
                                else: # They chose a product
                                    productPage(choice) # Load the product
                        
                        case "Legwear": # They want to look at legwear (pants, shorts, skirts, whatever)
                            while True: # Loop for the menu
                                shortsOptions = ["Mirror Pants", "Denim Pants", "Hip Hop Cargo Shorts", "I Fear God Shirts", "Denim Skirt", "Tight Denim Skirt", "Back"] # Their options
                                shortsMenu = Menu(shortsOptions, "Legwear") # make the menu
                                choice = shortsMenu.startMenu() # Start the menu
                                if choice == "Back": # They are done looking at legwear
                                    break # Bring them back to the categories menu
                                else: # They chose a product
                                    productPage(choice) # Load the product
                        
                        case "Dressers": # They want to look at dressers
                            while True: # Loop for the menu
                                dresserOptions = ["Malm", "Bellmore", "Weslar", "Abdulbari", "Lakeleigh", "Back"] # Their options (all from the top results of searching "dressers")
                                dresserMenu = Menu(dresserOptions, "Dressers") # Make the menu
                                choice = dresserMenu.startMenu() # Start it
                                if choice == "Back": # They are done looking at dressers
                                    break # Bring them back to the categories menu
                                else: # They chose a product
                                    productPage(choice) # Load the product
                        
                        case "Dresses": # Dressers menu
                            while True: # Loop for menu
                                dressOptions = ["Mini Shirt Dress", "Shiny Mini Dress", "Satin Mermaid Dress", "Long Flower Print Dress", "Back"] # Options
                                dressMenu = Menu(dressOptions, "Dresses") # Make menu
                                choice = dressMenu.startMenu() # Start menu
                                if choice == "Back": # They want to leave
                                    break # Go back
                                else: # Chose a product
                                    productPage(choice) # LOADING...
                        
                        case "Underwear": # Underwear menu
                            while True: # Loop menu
                                underwearOptions = ["3 Pack Warface Camo Glow", "Christmas Briefs", "Caveman Leaf By Gooccii", "Back"] # Options
                                underwearMenu = Menu(underwearOptions, "Underwear") # Make menu
                                choice = underwearMenu.startMenu() # Start menu
                                if choice == "Back": # Go back
                                    break # Go back
                                else: # Product chosen
                                    productPage(choice) # Load product
                        
                        case "NFTs": # Why did I make this?
                            while True: # Loop (Captian Obvious to the rescue!)
                                NFTOptions = ["Totsugeki", "Neco-Arc", "Cat", "Spy", "Kasumi", "Fat Fuck", "Back"] # Options
                                NFTMenu = Menu(NFTOptions, "NFTs") # Make menu
                                choice = NFTMenu.startMenu() # Start menu
                                if choice == "Back": # Go back
                                    break # For the love of god! GO BACK!!!
                                else: # Product chosen (for some reason)
                                    productPage(choice) # Load it

                        case "Back": # They are done looking at the categories
                            break # Go back to main
            case "Cart": # They want to look at their cart
                while True: # Loop for the menu
                    itemsInCartCode = [] # They list of their items in the cart, but for the code to read
                    for i in itemsInCart: # Look at each item in their cart
                        itemsInCartCode.append(i) # Add it to the code version of the same list
                    count = 0 # Number to add spaces to choice (helps with not having multiples of a product not all be highlighted or be hidden (IDK why it was getting hidden...))
                    for i in itemsInCart: # Go through the list (they're both the same, doesn't matter which)
                        for a in range(count): # Count is used to index a choice and to add spaces.
                            itemsInCartCode[count] += " " # Add spaces according to the index
                        count += 1 # Add one to the count since we're moving forward in the list
                        # You might wonder "Why not just have 'itemsInCart.index(i)'?". Problem is, if there are multiples, it would go with the first instance, which is not what we want.
                    itemsInCartCode.append("Back") # Add the option to go back
                    itemsInCartCode.append("Checkout") # Add the option to checkout
                    totalCost = 0 # Cost of all the products
                    for i in itemsInCart: # Look at all the products
                        i = i.replace(" ", "-")
                        totalCost = totalCost + prices[i] # Check their prices
                    tax = totalCost*.07 # Get how much tax would add
                    totalCost += tax #  + tax
                    totalCost = int(totalCost*100)/100 # Only get 2 digits after the decimal
                    description = "Items:\n" # Start to display the items
                    for i in itemsInCart: # Look at all the products they chose
                        j = i.replace(" ", "-")
                        addString = f"  {i}: {prices[j]}\n" # Individual string for one item
                        description += addString # Add that string to the description
                    description += f"Total Cost: ${totalCost}" # Then add the total cost
                    cartMenu = Menu(itemsInCartCode, "Your Cart", description) # Make the menu
                    choice = cartMenu.startMenu() # Start the menu
                    if choice == "Back": # Go back
                        break # Go bck to the main menu
                    elif choice == "Checkout": # Checkout
                        if stylistCard == False:
                            # Stylist Card
                            cardOptions = ["Apply", "Continue to Checkout"] # Their options
                            cardMenu = Menu(cardOptions, "The Stylist Card", """ 'The Stylist Card' - Your Ultimate Fashion Accessory!

Unlock the Power of 'The Stylist Card' and Elevate Your Style Game:

 \u27A2 Shop up to $2000 in Fashion Boutique without interest for an entire year.
 \u27A2 Flexible payments that adapt to your lifestyle.
 \u27A2 Exclusive access to VIP discounts.
 \u27A2 Aesthetically pleasing card design that turns heads everywhere you go.

If you exceed the $2000 spending limit on 'The Stylist Card,' a fixed interest rate of 20% will be applied to the additional amount spent. Please manage your card responsibly to avoid any extra charges.                                        

Apply today and let your style shine with 'The Stylist Card.'""") # The discount is a 5% discount
                            choice = cardMenu.startMenu() # Start menu
                            if choice == "Apply": # They want to apply for the card
                                stylistCard = True # They now have the card
                                os.system("clear") # Clear the menu
                                print("Applying for 'The Stylist Card'", end="", flush=True) # Tell them that they are applying
                                for i in range(3): # loop to show it as loading
                                    sleep(1)
                                    print(".", end="", flush=True)
                                sleep(1)
                                print("\nYou have been approved for the card.") # Tell them that they have been approved
                                sleep(1)
                        # Recommend a product
                        recommendation = recommend(itemsInCart, ignoreList) # Find a recommendation for them
                        if recommendation != None: # There was a recommendation
                            recommendOptions = ["Check out Product", "Don't recommend this product to me", "Continue to Checkout"] # Their options
                            recommendMen = Menu(recommendOptions, recommendation, "We think you might like this product based on your current selections.") # Tekk them that this was reocmmended
                            choice = recommendMen.startMenu() # Get their choice
                            if choice == "Check out Product": # They want to check out the product
                                productPage(recommendation) # They either add it or move on
                            elif choice == "Don't recommend this product to me": # They don't want to see this product again
                                ignoreList.append(recommendation) # Add it to the ignore list
                        # Proceed to checkout
                        checkoutDict = {} # To store their products with the count of how many they bought
                        for i in itemsInCart: # Go through their cart
                            if i not in checkoutDict.keys(): # It isn't in the dictionary yet
                                checkoutDict[i] = 1 # Add it to the dictionary and set the value to 1
                            else: # It is in the dictionary
                                checkoutDict[i] += 1 # Add 1 to the value
                        checkoutDesc = f"Items:\n" # To show what they ordered and the costs
                        subtotal = 0 # Subtotal
                        for i in checkoutDict.keys(): # Look at all the products they ordered
                            j = i.replace(" ", "-") # Make a copy to get the price
                            productsPrice = prices[j]*(checkoutDict[i]) # Get the total price (The price times the amount they have in their cart)
                            subtotal += productsPrice # Add it to subtotal for the description
                            checkoutDesc += f" {i} {checkoutDict[i]}x  ${productsPrice}\n" # Add the item, the quantity, and the price in each line
                        if stylistCard == True: # They applied for the card
                            checkoutDesc += f"Subtotal: ${(int(subtotal*100))/100}\n\n  Tax: ${(int((subtotal*.07)*100))/100}\n  Discount: -${(int((subtotal*.05)*100))/100}\n\nTotal: ${(int(subtotal*100))/100+((int((subtotal*.07)*100))/100)-((int((subtotal*.05)*100))/100)}" # Tell them the subtotal, tax, discount, and total
                        else: # They don't have the card
                            checkoutDesc += f"Subtotal: ${(int(subtotal*100))/100}\n\n  Tax: ${(int((subtotal*.07)*100))/100}\n\nTotal: ${(int(subtotal*100))/100+((int((subtotal*.07)*100))/100)}" # Tell them the subtotal, tax, and total
                        options = ["Order Now", "Return to Cart"] # Their options
                        checkoutMen = Menu(options, "Checkout", checkoutDesc) # Make the menu
                        choice = checkoutMen.startMenu() # Get their choice
                        if choice == "Order Now": # They want to order it now
                            print("Thank you for shopping with us! Expect the products to arrive in 2-4 working days.") # Tell them that it's being ordered
                            exit() # End the program
                        # If they chose anything else, it would take them back to the cart menu.

                    else: # They chose a product
                        count = 0 # How far we've gone into a string
                        oldChoice = "" # What the choice was previously
                        oldChoice += choice # Get the choice
                        while True: # Loop to edit choice
                            if choice[-1] != " ": # It doesn't end in a space
                                break # Continue with the code
                            elif choice[count] != " " and choice[count + 1] == " ": # We found something that isn't a space with a space bfore it
                                choice = choice[:count+1] # Choice is now what choice was before, without the follwing spaces
                                break # End the loop
                            else: # Neither conditions were fulfilled
                                count -= 1 # Move further up the string
                        productPage(choice, itemsInCartCode) # load the product
            case "Exit": # They want to exit the store
                os.system("clear") # Clear the menu
                exit() # End the program

currentTime = time() # Get the current time
if currentTime >= 1696636740: # If the time is past October 6th, 2023
    print("\x1B[1mSorry, we're closed\x1B[0m") # Say that it's closed and end the program
else: # If it is before the end date
    main() # Run the program
