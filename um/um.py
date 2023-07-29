import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    a = "(^|\W)um($|\W)"
    b = re.findall(a, s, re.IGNORECASE)
    if b:
        return len(b)

if __name__ == "__main__":
    main()