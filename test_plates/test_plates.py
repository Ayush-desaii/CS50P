from plates import is_valid

def main():

    test_1()
    test_2()
    test_3()
    test_4()


def test_1():

    assert is_valid("aa") == True
    assert is_valid("AAA") == True
    assert is_valid("A123") == False

def test_2():

    assert is_valid("a") == False
    assert is_valid("AAABBB") == True
    assert is_valid("AAABBBCCC23") == False

def test_3():

    assert is_valid("aa023") == False
    assert is_valid("AAA333") == True
    assert is_valid("AB12CD") == False

def test_4():

    assert is_valid("aa.") == False
    assert is_valid("AAA,c") == False
    assert is_valid("A12 3") == False
    assert is_valid("ABC333") == True


if __name__ == "__main__":
    main()