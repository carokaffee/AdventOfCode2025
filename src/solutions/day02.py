from src.tools.loader import load_data

TESTING = True


def is_invalid(num, longest_id, multiple):
    num = str(num)
    length = len(num)
    if multiple:
        possible_ks = range(longest_id // 2, 0, -1)
    else:
        if length % 2 != 0:
            return False
        else:
            possible_ks = [length // 2]

    for k in possible_ks:
        if length % k != 0 or length == k:
            continue

        parts = [num[k * i : k * (i + 1)] for i in range(length // k)]
        if len(set(parts)) == 1:
            return True

    return False


if __name__ == "__main__":
    data = load_data(TESTING, ",")

    id_ranges = [tuple(map(int, el.split("-"))) for el in data]
    longest_id = max([len(str(id2)) for (_, id2) in id_ranges])

    sum_invalid_a = 0
    sum_invalid_b = 0

    for start, end in id_ranges:
        midsum = 0
        for num in range(start, end + 1):
            if is_invalid(num, longest_id, multiple=False):
                sum_invalid_a += num
                midsum += 1
            if is_invalid(num, longest_id, multiple=True):
                sum_invalid_b += num

    # PART 1
    # test:    1227775554
    # answer: 56660955519
    print(sum_invalid_a)

    # PART 2
    # test:    4174379265
    # answer: 79183223243
    print(sum_invalid_b)
