
def main():

    a = input("Input:")
    print(shorten(a))


def shorten(word):

    v = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']

    for i in word :

        if i in v :
            word = word.replace(i, "")

    return word

if __name__ == "__main__":
    main()