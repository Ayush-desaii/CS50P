from seasons import num_to_word
import pytest

def main():
    test_1()


def test_1():
    assert num_to_word(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert num_to_word(366) == "Five hundred twenty-seven thousand forty minutes"


if __name__ == "__main__":
    main()