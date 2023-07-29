def main():

    a = input("What time is it? ").strip()

    b = convert(a)

    if b <= 8 and b >= 7 :
        print("breakfast time")

    elif b <= 13 and b >= 12 :
        print("lunch time")

    elif b <= 19 and b >= 18 :
        print("dinner time")

def convert(time):

    a, b = time.split(":")

    a = float(a)

    b = float(b)/60

    return a + b



if __name__ == "__main__":
    main()