import pytest
import fuel

def main():

    test_convert()
    test_gauge()

def test_convert():

    assert fuel.convert("4/8") == 50
    assert fuel.convert("1/4") == 25
    assert fuel.convert("1/10") == 10

    with pytest.raises(ValueError):
        fuel.convert("5/2")

    with pytest.raises(ZeroDivisionError):
        fuel.convert("5/0")

def test_gauge():

    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(99) == "F"


if __name__ == "__main__":
    main()