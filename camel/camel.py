a = input("camelCase: ").strip()

j = 0

for i in a :

    if i.isupper() :
        a = a[:j] + "_" + a[j:].lower()
        j += 1

    j += 1

print("snake_case:",a)