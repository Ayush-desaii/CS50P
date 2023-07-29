def gro():
    b = {}
    while True:
        try :
            a = input().upper()

            if a in b:
                b[a] += 1
            else :
                b[a] = 1


        except EOFError:

            for i, j in sorted(b.items()):
                print(j, i)

            break


gro()