import bank

def main():

    test_hello()
    test_h()
    test_else()

def test_hello():



    assert bank.value("hello, world") == 0
    assert bank.value("HELLO, world") == 0



def test_h():

    assert bank.value("hi, friend") == 20
    assert bank.value("h") == 20
    assert bank.value("Hi, friend") == 20

def test_else():

    assert bank.value("cs50") == 100
    assert bank.value("programming with python") == 100
    assert bank.value("123456789") == 100

if __name__ == "__main__":
    main()