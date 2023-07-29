import twttr

def main():

    test_word()


def test_word():

    assert twttr.shorten("cs50") == "cs50"
    assert twttr.shorten("programming with python") == "prgrmmng wth pythn"
    assert twttr.shorten("hello, world") == "hll, wrld"
    assert twttr.shorten("HELLO, friEnd") == "HLL, frnd"
    assert twttr.shorten("123456789") == "123456789"

if __name__ == "__main__":
    main()