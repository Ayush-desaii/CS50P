import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("too few command-line argument")

elif len(sys.argv) > 3:
    sys.exit("too many command-line argument")

a = (sys.argv[1]).lower().split(".")
c = (sys.argv[2]).lower().split(".")
b = ["jpg", "jpeg", "png"]

if a[1] not in b:
    sys.exit("file is not image file")

elif a[1] != c[1] :
    sys.exit("file formate is not same")

else :

    try:
        shirt = Image.open("shirt.png")
        with Image.open(sys.argv[1]) as m:
            n = ImageOps.fit(m, shirt.size)
            n.paste(shirt, shirt)
            n.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("file does not exists")
