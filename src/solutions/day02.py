from src.tools.loader import load_data

TESTING = False


def is_invalid(num):
    num = str(num)

    if len(num) % 2 == 1:
        return False
    if num[: len(num) // 2] == num[len(num) // 2 :]:
        return True
    return False


def is_invalid2(num):
    num = str(num)
    length = len(num)
    for k in range(5, 0, -1):
        if length % k != 0 or length == k:
            continue

        parts = [num[k * i : k * (i + 1)] for i in range(length // k)]
        if len(set(parts)) == 1:
            return True

    return False


if __name__ == "__main__":
    data = load_data(TESTING, ",")
    ranges = [tuple(map(int, el.split("-"))) for el in data]

    sum_invalid = 0

    for i, (start, end) in enumerate(ranges):
        print(i, start, end)
        for num in range(start, end + 1):
            if is_invalid2(num):
                sum_invalid += num

    print(sum_invalid)
