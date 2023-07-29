import validators

a = input("What's your email address? ")

if validators.email(a) == True:
    print("Valid")
else:
    print("Invalid")