
m = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

while True:

    d = input("Date: ")

    try :

        if "/" in d :
            mm,dd,yy = d.split("/")
        elif "," in d :
            mmdd,yy = d.split(", ")
            mm,dd = mmdd.split(" ")
            mm = m.index(mm) + 1

        if int(mm) > 12 or int(dd) > 31:
            raise ValueError

    except (AttributeError, ValueError, NameError, KeyError):
        pass

    else:
        print(f"{int(yy)}-{int(mm):02}-{int(dd):02}")
        break