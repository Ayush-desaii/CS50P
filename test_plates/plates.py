def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    a = 0
    b = 0
    c = -1
    for i in s :
        if i.isalpha() :
            a += 1

        if i.isnumeric() :
            if b == 0 and i == '0' :

                return False
            b += 1

        if b == 1 :
            c = a

        if not (i.isalpha() or i.isnumeric()) :

            return False

    if a < 2 or a > 6 :

        return False

    if c != a and b > 0 :

        return False

    return True

if __name__ == "__main__":
    main()