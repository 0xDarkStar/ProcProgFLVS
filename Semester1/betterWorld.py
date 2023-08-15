# Matthew Rojas
# 14/8/2023
# This script is meant to inform the user on how they can help make the world a better place.

'''
Ways the user can try to help make the world a better place:
 - Don't use disposable items
 - Be more empathetic
 - Lower your carbon footprint (and don't support companies that have high carbon emissions)
 - Walk, bicycle, or use public transit more to get to where you want to go
 - Make your city more human-centric
'''

denied = ["no", "n", "nope", "nah", "nuh-uh", "nuh uh"]

def main():
    name = input("Hello, user. Before I continue, may I ask for a name to refer to you by. ")
    if name.lower() in denied:
        print("Okay, Then I'll continue to refer to you as user.")
        name = "user"
    else:
        print(f"Okay, I'll refer to use as {name} from now on.")