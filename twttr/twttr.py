a = input("Input:")

v = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

for i in a :

    if i in v :
        a = a.replace(i, "")

print(a)