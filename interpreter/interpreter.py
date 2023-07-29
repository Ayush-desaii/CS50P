a = input("Expression: ").strip()

x, y, z = a.split(" ")

x = int(x)
z = int(z)

if y == "+" :
    print(float(x + z))

elif y == "*" :
    print(float(x * z))

elif y == "/" :
    print(float(x / z))

elif y == "-" :
    print(float(x - z))