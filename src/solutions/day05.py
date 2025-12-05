from src.tools.loader import load_data
import time

TESTING = False


if __name__ == "__main__":
    s = time.time()
    data = load_data(TESTING, "\n\n")

    ranges = [tuple(map(int, tuple(el.split("-")))) for el in data[0].split("\n")]
    ingredients = list(map(int, data[1].split("\n")))

    count = 0

    for ing in ingredients:
        spoiled = 0
        for start, end in ranges:
            if start <= ing and ing <= end:
                spoiled = True
        count += spoiled

    print(count)

    points = sorted(list(set([point for pair in ranges for point in pair])))

    new_ranges = []
    for a, b in ranges:
        special = [num for num in points if a <= num and num <= b]
        new_ranges += [(num, num) for num in special]
        for i in range(len(special) - 1):
            new_ranges.append((special[i] + 1, special[i + 1] - 1))

    new_ranges = set(new_ranges)

    count2 = 0
    for a, b in new_ranges:
        if a <= b:
            count2 += b - a + 1

    print(count2)

    e = time.time()
    print(e - s)
