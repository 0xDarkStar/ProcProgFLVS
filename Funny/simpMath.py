# This is for me to use in other scripts. Too lazy to download numpy and learn it.

def evenOrOdd(number):
    if number%2 == 0:
        return True
    else:
        return False

def mean(dataset: list):
    add = 0
    for i in dataset:
        add += i
    meanAns = add/len(dataset)
    return meanAns

def median(dataset: list):
    smallToBig = []
    smallest = 99999999999999999999999999
    indexOfSmallest = 0
    for a in range(len(dataset)):
        for i in dataset:
            if i < smallest:
                smallest = i
                indexOfSmallest = dataset.index(i)
        smallToBig.append(smallest)
        smallest = 99999999999999999999999
        del dataset[indexOfSmallest]
    if evenOrOdd(len(smallToBig)) == True:
        smaller = smallToBig[int(len(smallToBig)/2)-1]
        bigger = smallToBig[int((len(smallToBig)/2))]
        mid = (bigger+smaller)/2
        print(smallToBig)
        return mid
    else:
        mid = smallToBig[int(len(smallToBig)/2)]
        print(smallToBig)
        return mid

def mode(dataset: list):
    instances = {
    }
    for i in dataset:
        print("AAAAAAAAAAAA") # Test