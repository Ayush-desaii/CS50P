from um import count

def main():
    test_count()


def test_count():
    assert count("um") == 1
    assert count("um, how are you ?") == 1
    assert count("um, oh, um, naruto-kun") == 2
    assert count("yummy") == 0
    assert count("UM") == 1

if __name__ == "__main__":
    main()