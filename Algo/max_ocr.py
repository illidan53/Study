from fractions import Fraction


def get_lazy_members(input_data: list, max_ocr_fraction=Fraction(1,3)):
    length = len(input_data)
    assert length != 0
    counter = {}
    result = []
    for e in input_data:
        try:
            counter[e] += 1
        except KeyError:
            counter[e] = 1

    threshold = length * max_ocr_fraction.numerator // max_ocr_fraction.denominator
    for k, v in counter.items():
        if v <= threshold:
            result.append(k)

    return result


if __name__ == "__main__":
    print(get_lazy_members([1, 2, 3, 4, 1, 2, 3, 3, 3, 3]))
    print(get_lazy_members([5, 6, 7, 8, 5, 6, 7, 8]))
    print(get_lazy_members([1, 1, 2, 2, 1, 1, 2, 2]))