def main():

    n = input("Fraction: ")
    a = convert(n)
    b = gauge(a)
    print(b)

def convert(fraction):

        a, b = fraction.split("/")

        c = int((int(a)/int(b))*100)

        if int(a) > int(b):
            raise ValueError

        if int(b) == 0:
            raise ZeroDivisionError

        return c




def gauge(percentage):



        if 0 <= percentage and percentage <= 1 :
            return "E"

        elif 99 <= percentage and percentage <= 100 :
            return "F"

        elif 1 < percentage and percentage < 99 :
            return f"{int(round(percentage))}%"


if __name__ == "__main__":
    main()