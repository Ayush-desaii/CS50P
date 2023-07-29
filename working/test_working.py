from working import convert
import pytest

def main():
    test_convert1()
    test_convert2()


def test_convert1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

def test_convert2():
    with pytest.raises(ValueError):
        convert("90 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM TO 5:00 PM")
    with pytest.raises(ValueError):
        convert("12 AM - 12 PM")
    with pytest.raises(ValueError):
        convert("9 to 5")

if __name__ == "__main__":
    main()