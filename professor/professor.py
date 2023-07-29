import random


def main():

    l = get_level()
    score = 0

    for i in range(0,10):

        a, b = generate_integer(l)

        i = 0
        while True :

            c = int(input(f"{a} + {b} = "))
            if c == (a + b):
                score += 1
                break
            elif i == 2 :
                print("EEE")
                print(f"{a} + {b} = {a + b}")
                break
            else :
                print("EEE")
                i += 1

    print("Score: ", score)

def get_level():

    n = 0
    while n > 3 or n < 1 :
        try :
            n = int(input("Level: "))
        except ValueError :
            n = 0
            pass
    return n

def generate_integer(level):

    if level == 1 :

        a = random.randint(0,9)
        b = random.randint(0,9)

    elif level == 2 :

        a = random.randint(10,99)
        b = random.randint(10,99)

    else :

        a = random.randint(100,999)
        b = random.randint(100,999)

    return a,b

if __name__ == "__main__":
    main()