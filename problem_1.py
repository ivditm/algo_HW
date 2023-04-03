# id = 85070309


def find_zero_near(lenght: int, data: list) -> list:
    left_distance = 10**9
    left_answer = []
    right_distance = 10**9
    right_answer = []
    for i in range(lenght):
        if data[i] == 0:
            left_distance = i
            left_answer.append(0)
        else:
            left_answer.append(abs(i - left_distance))
    for i in range(lenght-1, -1, -1):
        if data[i] == 0:
            right_distance = i - len(data)-1
            right_answer.append(0)
        else:
            right_answer.append(abs(right_distance - (i-lenght-1)))
    return [min(i) for i in zip(left_answer, right_answer[::-1])]


if __name__ == '__main__':
    print(*find_zero_near(int(input()),
                          [int(i) for i in input().strip().split()]), sep=' ')
