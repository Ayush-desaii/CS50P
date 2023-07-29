d = 50
denom = [25, 10, 5]

while d >= 1 :
    print("Amount Due:",d)
    c = int(input("Insert Coin: "))
    if c in denom :
        d = d - c

if d == 0 :
    print("Change Owed:",d)

else :
    print("Change Owed:",0 - d)
