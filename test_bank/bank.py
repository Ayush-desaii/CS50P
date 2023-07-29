def main():

    a = input("Greeting: ").strip()
    print(value(a))

def value(greeting):



    if "hello" in greeting.lower() :
        return 0

    elif greeting[0].lower() == "h" :
        return 20

    else :
        return 100

if __name__ == "__main__":
    main()