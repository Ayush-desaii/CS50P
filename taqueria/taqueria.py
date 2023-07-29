
def taq():

    d = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    m = 0

    while True:

        try :
            a = input("Item: ").title()

            if a not in d:
                continue

            else :
                m = m + d[a]
                print(f"Total: ${'{:.2f}'.format(m)}")

        except EOFError:
            print()
            break

taq()