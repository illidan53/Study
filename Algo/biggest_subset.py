from copy import copy


# rule 001: number of 0 and 1 are the same
def get_biggest_subset_rule_001(input_list: list) -> list:
    l = list(map(lambda x:x if x == 1 else -1, input_list))
    sum_by_index = []
    previous = 0
    for i in l:
        previous += i
        sum_by_index.append(previous)

    sum_occurrences = {}
    for index, value in enumerate(sum_by_index):
        try:
            sum_occurrences[value].append(index)
        except KeyError:
            sum_occurrences[value] = [index]

    biggest_length = 0
    start_index, end_index = (0, 0)

    for k, v in sum_occurrences.items():
        current_length = v[-1] - v[0]
        if current_length >= biggest_length:
            biggest_length = current_length
            start_index = v[0]
            end_index = v[-1]

    return l[start_index + 1: end_index + 1]


if __name__ == "__main__":
    list1 = [0, 1, 0, 0, 1, 1, 0, 0, 0]
    result = list(map(lambda x:x if x == 1 else 0, get_biggest_subset_rule_001(list1)))
    print(result)
