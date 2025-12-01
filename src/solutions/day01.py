from src.tools.loader import load_data

TESTING = True


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    rotations = [(el[0], int(el[1:])) for el in data]

    dial_a = 50
    dial_b = 50
    count_a = 0
    count_b = 0

    for direction, num in rotations:
        step = num if direction == "R" else -num
        dial_a = (dial_a + step) % 100
        if dial_a == 0:
            count_a += 1

    for direction, num in rotations:
        step = 1 if direction == "R" else -1
        for _ in range(num):
            dial_b = (dial_b + step) % 100
            if dial_b == 0:
                count_b += 1

    # PART 1
    # test:      3
    # answer: 1165
    print(count_a)

    # PART 2
    # test:      6
    # answer: 6496
    print(count_b)
