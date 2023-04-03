# id = 85076430


def create_counter(string: str) -> dict[str, int]:
    counter = {}
    for symbol in string:
        if symbol in counter:
            counter[symbol] += 1
        else:
            counter[symbol] = 1
    return counter


def calculate_points(max_pas: int, string: str) -> int:
    number_of_points = 0
    data = create_counter(string.replace('.', ''))
    for i in data.values():
        if i <= max_pas:
            number_of_points += 1
    return number_of_points


if __name__ == '__main__':
    max_pass = int(input())*2
    matrix = ''.join(input() for _ in range(4))
    print(calculate_points(max_pass, matrix))
