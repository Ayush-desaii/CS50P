import random


while True :

    try :

        i = int(input("Level: "))
        a = random.randint(1,i)
        b = int(input("Guess: "))

        if b > a :
            print("Too large!")

        elif b < a :
            print("Too small!")
        elif b == a :
            print("Just right!")
            break
    except ValueError :
        pass
