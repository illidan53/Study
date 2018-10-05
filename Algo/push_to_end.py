from copy import copy


def push_to_end(input_data: list, value=0) -> list:
    assert input_data != ''
    counter = 0
    input_data_copy = copy(input_data)
    for i in range(len(input_data)):
        if input_data[i] == value:
            del input_data_copy[i - counter]
            counter += 1

    input_data_copy.extend([value] * counter)

    print(input_data_copy)
    return input_data_copy


if __name__ == "__main__":
    push_to_end([3,2,1,0,4,2,0,0,12,23])
    push_to_end([0,0,0,1,2,3,0,0,0,4,5,6])