from project import decision

def main():

    test_decision_1()


def test_decision_1():
    assert decision([10, 0.5, 100000000000, 0.9, 5]) == 1
    assert decision([17, 0.5, 100000000000, 0.9, 5]) == 0
    assert decision([10, 5, 100000000000, 0.9, 5]) == 0
    assert decision([10, 0.5, 1000, 0.9, 5]) == 0
    assert decision([10, 0.5, 100000000000, 6.9, 5]) == 0
    assert decision([10, 0.5, 100000000000, 0.9, -8]) == 0
    assert decision([10, "NA", 100000000000, 0.9, 5]) == 404

if __name__ == "__main__" :
    main()