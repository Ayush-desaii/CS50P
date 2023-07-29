from jar import Jar
import pytest

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(30)
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(50)


def test_withdraw():
    jar = Jar(30)
    jar.deposit(15)
    jar.withdraw(5)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.withdraw(50)

if __name__ == "__main__":
    main()