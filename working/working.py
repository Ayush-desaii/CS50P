import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    a = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    b = re.search(r"^" + a + " to " + a + "$", s)
    if b:
        t1 = formate(b.group(1), b.group(2), b.group(3))
        t2 = formate(b.group(4), b.group(5), b.group(6))
        return f"{t1} to {t2}"
    else :
        raise ValueError

def formate(h, m, p):

    if p == "PM":
        if h == "12":
            hr = "12"
        else:
            hr = f"{int(h) + 12}"
    else :
        if h == "12":
            hr = "00"
        else:
            hr = f"{int(h):02}"

    if m == None:
        mi = "00"
    else:
        mi = f"{int(m):02}"

    return f"{hr}:{mi}"


if __name__ == "__main__":
    main()