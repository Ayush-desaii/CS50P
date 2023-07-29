a = input("File name: ").lower().strip()
e = a.split(".",2)

b = 0

if len(e) == 2 :
    b = 1

elif len(e) == 3 :
    b = 2

match e[b] :
    case ("jpg") :
        print("image/jpeg")

    case ("pdf") :
        print("application/pdf")

    case ("jpeg") :
        print("image/jpeg")

    case ("txt") :
        print("text/plain")

    case ("gif") :
        print("image/gif")

    case ("zip") :
        print("application/zip")

    case ("png") :
        print("image/png")

    case ("octet-stream") :
        print("application/octet-stream")

    case ("bin") :
        print("application/octet-stream")

    case _ :
        print("application/octet-stream")