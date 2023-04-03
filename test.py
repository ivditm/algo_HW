from problem_1 import find_zero_near
from problem_2 import calculate_points


def test_problem_1(func):
    data_1 = (5, [0, 1, 4, 9, 0])
    data_2 = (6, [0, 7, 9, 4, 8, 20])
    assert func(*data_1) == [0, 1, 2, 1, 0]
    assert func(*data_2) == [0, 1, 2, 3, 4, 5]


def test_problem_2(func):
    data_1 = (6, '12312..22..22..2')
    data_2 = (8, '1111999911119911')
    data_3 = (8, '1111111111111111')
    assert func(*data_1) == 2
    assert func(*data_2) == 1
    assert func(*data_3) == 0


if __name__ == '__main__':
    test_problem_1(find_zero_near)
    test_problem_2(calculate_points)
