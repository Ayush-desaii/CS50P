import inflect

p = inflect.engine()
b = []

while True:

    try :
        i = input("Name: ").strip()
        b.append(i)
    except EOFError :
        print("Adieu, adieu, to", p.join(b))
        break
