import sys
import csv

if len(sys.argv) < 3 :
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3 :
    sys.exit("Too many command-line arguments")

else :
    try :
        with open(sys.argv[1], "r") as a:
            with open(sys.argv[2], "w") as b:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(b, fieldnames=fieldnames)
                reader = csv.DictReader(a)
                writer.writeheader()
                for row in reader:
                    x, y = row["name"].split(", ")
                    n = row["house"]
                    writer.writerow({'first' : y, 'last' : x, 'house': n})

    except FileNotFoundError:
        sys.exit("file does not exists")