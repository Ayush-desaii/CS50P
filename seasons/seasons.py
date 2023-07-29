import inflect
from datetime import date
import sys
import operator

p = inflect.engine()

def main():

    d = input("Date of Birth: ")

    try:
        m = operator.sub(date.today(), date.fromisoformat(d))
        n = m.days
        print(num_to_word(n))

    except ValueError:
        sys.exit("invalid date")

def num_to_word(n):

     mi = n * 24 * 60
     b = (f"{(p.number_to_words(mi, andword='')).capitalize()} minutes")
     return b

if __name__ == "__main__":
    main()