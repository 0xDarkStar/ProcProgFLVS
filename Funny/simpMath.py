# This is for me to use in other scripts. Too lazy to download numpy and learn it.
import copy

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
    datasetMod = copy.copy(dataset)
    smallToBig = []
    smallest = 99999999999999999999999999
    indexOfSmallest = 0
    for a in range(len(datasetMod)):
        for i in datasetMod:
            if i < smallest:
                smallest = i
                indexOfSmallest = datasetMod.index(i)
        smallToBig.append(smallest)
        smallest = 99999999999999999999999
        del datasetMod[indexOfSmallest]
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
    datasetMod = copy.copy(dataset)
    instances = {
    }
    while len(datasetMod) > 0:
        matching = datasetMod[0]
        matches = 0
        for i in datasetMod:
            if i == matching:
                remove = datasetMod.index(i)
                del datasetMod[remove]
                matches += 1
        instances[matching] = matches
    mostInstances = 0
    mostFrequent = "hi :)"
    for value, instance in instances.items():
        if instance > mostInstances:
            mostInstances = instance
            mostFrequent = value
    return mostFrequent
