import sys
import random
from pyfiglet import Figlet

figlet = Figlet()


b = ["-f", "--font"]

if len(sys.argv) < 2:
    i = input("Input: ")
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(i))
elif len(sys.argv) > 2 and (sys.argv[1] in b) and (sys.argv[2] in figlet.getFonts()):
    i = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(i))
else :
    sys.exit("Invalid usage")

