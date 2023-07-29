import sys

if len(sys.argv) < 2:
    sys.exit("too few command-line argument")

elif len(sys.argv) > 2:
    sys.exit("too many command-line argument")

elif sys.argv[1][-3:] != ".py" :
    sys.exit("file is not python file")

else :

    try :

        c = 0
        with open(sys.argv[1], "r") as a:
            for line in a :
                if line.lstrip().startswith("#") or line.strip() == "" :
                    continue
                else :
                    c += 1
        print(c)

    except FileNotFoundError:
        sys.exit("file not found")
