import csv
from tabulate import tabulate
import sys

if len(sys.argv) < 2:
    sys.exit("too few command-line argument")

elif len(sys.argv) > 2:
    sys.exit("too many command-line argument")

elif sys.argv[1][-4:] != ".csv" :
    sys.exit("file is not csv file")

else :

    try :

        with open(sys.argv[1]) as a:
            r = csv.reader(a, delimiter=',')

            print(tabulate(r,headers="firstrow",tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("file not found")
