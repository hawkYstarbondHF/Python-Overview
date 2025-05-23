import pytest
import os
import python_overview as po

def test_exercise1(capfd):
    po.exercise1()
    out, _ = capfd.readouterr()
    assert out == "The sum is: 62790\n"

def test_exercise2(capfd):
    po.exercise2()
    out, _ = capfd.readouterr()
    lines = out.splitlines()
    assert lines[0] == "HB"
    assert lines[1] == "HB"
    assert lines[2] == "a1"
    assert lines[3] == "a1"
    assert lines[4] == "a1"
    assert lines[5] == "1a"
    assert len(lines) == 6

def test_first_longer_shorter(capfd):
    with pytest.raises(ValueError):
        po.first_longer_shorter("","Test")

    with pytest.raises(ValueError):
        po.first_longer_shorter("Test","")

    with pytest.raises(ValueError):
        po.first_longer_shorter(None,"Test")

    with pytest.raises(ValueError):
        po.first_longer_shorter("Test",None)

    assert "xs" == po.first_longer_shorter("x x x x x x x x x x x x x x x x x x x x x x x x s x s sdasf dsfsdf sdf sdf sdfewfasf fsakkkasdfkwa o93 2", "sad")
    assert "\n\t" == po.first_longer_shorter("\taddasdad \n\n we", "\n \t\n\n\n\t\tx x x x x x x x x x x x x x x x x x x x x x x x s x s sdasf dsfsdf sdf sdf sdfewfasf fsakkkasdfkwa o93 2")

    out, _ = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 0  # Should be no console output from first_longer_shorter

def test_exercise3(capfd):
    po.exercise3()
    out, _ = capfd.readouterr()
    assert out == "1, 2, 3, 4, 6, 7, 8, 9, 10, 5\n"

def test_move_to_end(capfd):
    one_to_ten = [1,2,3,4,5,6,7,8,9,10]
    po.move_to_end(one_to_ten, 0)
    assert one_to_ten == [2,3,4,5,6,7,8,9,10,1]
    po.move_to_end(one_to_ten, 9)
    assert one_to_ten == [2,3,4,5,6,7,8,9,10,1]
    po.move_to_end(one_to_ten, 1)
    assert one_to_ten == [2,4,5,6,7,8,9,10,1,3]
    po.move_to_end(one_to_ten, 8)
    assert one_to_ten == [2,4,5,6,7,8,9,10,3,1]
    po.move_to_end(one_to_ten, 2)
    assert one_to_ten == [2,4,6,7,8,9,10,3,1,5]
    po.move_to_end(one_to_ten, 7)
    assert one_to_ten == [2,4,6,7,8,9,10,1,5,3]
    po.move_to_end(one_to_ten, 3)
    assert one_to_ten == [2,4,6,8,9,10,1,5,3,7]
    po.move_to_end(one_to_ten, 6)
    assert one_to_ten == [2,4,6,8,9,10,5,3,7,1]
    po.move_to_end(one_to_ten, 4)
    assert one_to_ten == [2,4,6,8,10,5,3,7,1,9]
    po.move_to_end(one_to_ten, 5)
    assert one_to_ten == [2,4,6,8,10,3,7,1,9,5]

    shorter = [10000,-243,32,367845]
    po.move_to_end(shorter, 2)
    assert shorter == [10000,-243,367845, 32]
    po.move_to_end(shorter, 3)
    assert shorter == [10000,-243,367845, 32]
    po.move_to_end(shorter, 0)
    assert shorter == [-243,367845, 32, 10000]
    po.move_to_end(shorter, 1)
    assert shorter == [-243,32, 10000, 367845]

    duplicates = [1,2,3,1,2,3,4,4,3,2]
    po.move_to_end(duplicates, 0)
    assert duplicates == [2,3,1,2,3,4,4,3,2,1]
    po.move_to_end(duplicates, 2)
    assert duplicates == [2,3,2,3,4,4,3,2,1,1]
    po.move_to_end(duplicates, 2)
    assert duplicates == [2,3,3,4,4,3,2,1,1,2]
    po.move_to_end(duplicates, 5)
    assert duplicates == [2,3,3,4,4,2,1,1,2,3]
    po.move_to_end(duplicates, 7)
    assert duplicates == [2,3,3,4,4,2,1,2,3,1]
    po.move_to_end(duplicates, 1)
    assert duplicates == [2,3,4,4,2,1,2,3,1,3]

    out, _ = capfd.readouterr()
    lines = out.splitlines()
    assert len(lines) == 0  # Should be no console output from move_to_end

def test_exercise4(capfd):
    po.exercise4()
    out, _ = capfd.readouterr()
    lines = out.splitlines()
    assert lines[0] == "9"
    assert lines[1] == "9"
    assert lines[2] == "28"
    assert lines[3] == "28"
    assert lines[4] == "406"
    assert lines[5] == "406"
    assert len(lines) == 6

def test_recursive_seq():
    with pytest.raises(ValueError):
        po.recursive_seq(-30)
    with pytest.raises(ValueError):
        po.recursive_seq(-5)
    with pytest.raises(ValueError):
        po.recursive_seq(-1)

    assert 1 == po.recursive_seq(0)
    assert 2 == po.recursive_seq(1)
    assert 3 == po.recursive_seq(2)
    assert 4 == po.recursive_seq(3)
    assert 6 == po.recursive_seq(4)
    assert 9 == po.recursive_seq(5)
    assert 13 == po.recursive_seq(6)
    assert 19 == po.recursive_seq(7)
    assert 28 == po.recursive_seq(8)
    assert 41 == po.recursive_seq(9)
    assert 60 == po.recursive_seq(10)
    assert 2745 == po.recursive_seq(20)
    assert 125491 == po.recursive_seq(30)
    assert 5736961 == po.recursive_seq(40)
    assert 178955183 == po.recursive_seq(49)

def test_dynamic_seq():
    with pytest.raises(ValueError):
        po.dynamic_seq(-30)
    with pytest.raises(ValueError):
        po.dynamic_seq(-5)
    with pytest.raises(ValueError):
        po.dynamic_seq(-1)

    assert 1 == po.dynamic_seq(0)
    assert 2 == po.dynamic_seq(1)
    assert 3 == po.dynamic_seq(2)
    assert 4 == po.dynamic_seq(3)
    assert 6 == po.dynamic_seq(4)
    assert 9 == po.dynamic_seq(5)
    assert 13 == po.dynamic_seq(6)
    assert 19 == po.dynamic_seq(7)
    assert 28 == po.dynamic_seq(8)
    assert 41 == po.dynamic_seq(9)
    assert 60 == po.dynamic_seq(10)
    assert 88 == po.dynamic_seq(11)
    assert 129 == po.dynamic_seq(12)
    assert 189 == po.dynamic_seq(13)
    assert 277 == po.dynamic_seq(14)
    assert 406 == po.dynamic_seq(15)
    assert 595 == po.dynamic_seq(16)
    assert 872 == po.dynamic_seq(17)
    assert 1278 == po.dynamic_seq(18)
    assert 1873 == po.dynamic_seq(19)
    assert 2745 == po.dynamic_seq(20)
    assert 4023 == po.dynamic_seq(21)
    assert 5896 == po.dynamic_seq(22)
    assert 8641 == po.dynamic_seq(23)
    assert 12664 == po.dynamic_seq(24)
    assert 18560 == po.dynamic_seq(25)
    assert 27201 == po.dynamic_seq(26)
    assert 39865 == po.dynamic_seq(27)
    assert 58425 == po.dynamic_seq(28)
    assert 85626 == po.dynamic_seq(29)
    assert 125491 == po.dynamic_seq(30)
    assert 183916 == po.dynamic_seq(31)
    assert 269542 == po.dynamic_seq(32)
    assert 395033 == po.dynamic_seq(33)
    assert 578949 == po.dynamic_seq(34)
    assert 848491 == po.dynamic_seq(35)
    assert 1243524 == po.dynamic_seq(36)
    assert 1822473 == po.dynamic_seq(37)
    assert 2670964 == po.dynamic_seq(38)
    assert 3914488 == po.dynamic_seq(39)
    assert 5736961 == po.dynamic_seq(40)
    assert 8407925 == po.dynamic_seq(41)
    assert 12322413 == po.dynamic_seq(42)
    assert 18059374 == po.dynamic_seq(43)
    assert 26467299 == po.dynamic_seq(44)
    assert 38789712 == po.dynamic_seq(45)
    assert 56849086 == po.dynamic_seq(46)
    assert 83316385 == po.dynamic_seq(47)
    assert 122106097 == po.dynamic_seq(48)
    assert 178955183 == po.dynamic_seq(49)
    assert 262271568 == po.dynamic_seq(50)
    assert 384377665 == po.dynamic_seq(51)
    assert 563332848 == po.dynamic_seq(52)
    assert 825604416 == po.dynamic_seq(53)
    assert 1209982081 == po.dynamic_seq(54)
    assert 1773314929 == po.dynamic_seq(55)
    assert 2598919345 == po.dynamic_seq(56)
    assert 3808901426 == po.dynamic_seq(57)
    assert 5582216355 == po.dynamic_seq(58)
    assert 8181135700 == po.dynamic_seq(59)
    assert 11990037126 == po.dynamic_seq(60)
    assert 17572253481 == po.dynamic_seq(61)
    assert 25753389181 == po.dynamic_seq(62)
    assert 37743426307 == po.dynamic_seq(63)
    assert 55315679788 == po.dynamic_seq(64)
    assert 81069068969 == po.dynamic_seq(65)
    assert 118812495276 == po.dynamic_seq(66)
    assert 174128175064 == po.dynamic_seq(67)
    assert 255197244033 == po.dynamic_seq(68)
    assert 374009739309 == po.dynamic_seq(69)
    assert 548137914373 == po.dynamic_seq(70)
    assert 803335158406 == po.dynamic_seq(71)
    assert 1177344897715 == po.dynamic_seq(72)
    assert 1725482812088 == po.dynamic_seq(73)
    assert 2528817970494 == po.dynamic_seq(74)
    assert 3706162868209 == po.dynamic_seq(75)
    assert 5431645680297 == po.dynamic_seq(76)
    assert 7960463650791 == po.dynamic_seq(77)
    assert 11666626519000 == po.dynamic_seq(78)
    assert 17098272199297 == po.dynamic_seq(79)
    assert 25058735850088 == po.dynamic_seq(80)
    assert 36725362369088 == po.dynamic_seq(81)
    assert 53823634568385 == po.dynamic_seq(82)
    assert 78882370418473 == po.dynamic_seq(83)
    assert 115607732787561 == po.dynamic_seq(84)
    assert 169431367355946 == po.dynamic_seq(85)
    assert 248313737774419 == po.dynamic_seq(86)
    assert 363921470561980 == po.dynamic_seq(87)
    assert 533352837917926 == po.dynamic_seq(88)
    assert 781666575692345 == po.dynamic_seq(89)
    assert 1145588046254325 == po.dynamic_seq(90)
    assert 1678940884172251 == po.dynamic_seq(91)
    assert 2460607459864596 == po.dynamic_seq(92)
    assert 3606195506118921 == po.dynamic_seq(93)
    assert 5285136390291172 == po.dynamic_seq(94)
    assert 7745743850155768 == po.dynamic_seq(95)
    assert 11351939356274689 == po.dynamic_seq(96)
    assert 16637075746565861 == po.dynamic_seq(97)
    assert 24382819596721629 == po.dynamic_seq(98)
    assert 35734758952996318 == po.dynamic_seq(99)

def test_exercise5(capfd):
    po.exercise5()
    out, _ = capfd.readouterr()
    lines = out.splitlines()
    assert lines[0] == "Maximum value: 201"
    assert lines[1] == "Average value: 8.688524590163935"
    assert len(lines) == 2

def test_exercise5_different_file(capfd):
    os.rename("numbers.txt", "numbers.cpy")
    try:
        with open('numbers.txt', 'w') as f:
            f.write('-34\n')
            f.write('-12312\n')
            f.write('-200\n')
            f.write('-3\n')
            f.write('-145\n')
            f.write('-57\n')
            f.write('-9494\n')
            f.write('-90909\n')

        po.exercise5()
        out, _ = capfd.readouterr()
        lines = out.splitlines()
        assert lines[0] == "Maximum value: -3"
        assert lines[1] == "Average value: -14144.25"
        assert len(lines) == 2
    finally:
        os.remove("numbers.txt")
        os.rename("numbers.cpy", "numbers.txt")

def test_exercise5_no_file(capfd):
    os.rename("numbers.txt", "numbers.cpy")
    try:
        po.exercise5()
        out, _ = capfd.readouterr()
        assert out == "The file \"numbers.txt\" does not exist. Exiting.\n"
    finally:
        os.rename("numbers.cpy", "numbers.txt")

def test_exercise6(capfd):
    po.exercise6()
    out, _ = capfd.readouterr()
    lines = out.splitlines()
    assert lines[0] == "Employee 1 earns $330.00 for 40 hours of work."
    assert lines[1] == "Employee 1 earns $214.50 for 26 hours of work."
    assert lines[2] == "Employee 2 earns $604.00 for 40 hours of work."
    assert len(lines) == 3
