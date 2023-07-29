def get_fraction():

    while True:
        n = input("Fraction: ")
        if "/" not in n :
            print ("invalid input, try again e.g. 'a/b' ")
            continue

        a, b = n.split("/")
        ans = ""
        try:
            c = (int(a)/int(b))*100

            if 0 <= c <= 1 :
                return "E"

            elif 99 <= c <= 100 :
                return "F"

            elif 1 < c < 99 :
                return f"{int(round(c))}%"

        except (ValueError, ZeroDivisionError):

            continue

print(get_fraction())