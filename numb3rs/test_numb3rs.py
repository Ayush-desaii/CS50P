from numb3rs import validate

def main():
    test_validate_1()
    test_validate_2()


def test_validate_1():

    assert validate("hello") == False
    assert validate("1234") == False
    assert validate("a.b.c.d") == False
    assert validate("hello") == False

def test_validate_2():

    assert validate("1.2.3.4") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("198.34.4.91") == True
    assert validate("1.256.3.4") == False
    assert validate("255.255.456.255") == False
    assert validate("0.0.1000.0") == False
    assert validate("198.34.4.911") == False

if __name__ == "__main__":
    main()