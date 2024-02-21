def firstmethod():
    secondmethod()
    print("I am first method")

def secondmethod():
    thirdmethod()
    print("I am second method")

def thirdmethod():
    forthmethod()
    print("Hi I am third method")

def forthmethod():
    print("Hi I am forth method")

firstmethod()