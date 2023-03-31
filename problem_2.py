# id = 84915543
# задача № 2 - пока так, но тесты прошли

def read_input():
    return int(input())*2, input() + input() + input() + input()


def make_dictionary(obj):
    dict_ = {}
    for part in obj:
        if dict_.get(part) is None:
            dict_[part] = 1
        else:
            dict_[part] += 1
    return dict_


def solution(max_pas, string):
    good_data = []
    i = 0
    data = make_dictionary(string)
    data.pop('.', None)
    for i in data.values():
        if i <= max_pas:
            good_data.append(i)
    return len(good_data)


print(solution(*read_input()))
