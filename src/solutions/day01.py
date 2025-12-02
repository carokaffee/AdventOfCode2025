from src.tools.loader import load_data

TESTING = True


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    rotations = [(el[0], int(el[1:])) for el in data]

    dial_a = dial_b1 = dial_b2 = 50
    count_a = count_b1 = count_b2 = 0

    # part 1
    for direction, num in rotations:
        step = num if direction == "R" else -num
        dial_a = (dial_a + step) % 100
        if dial_a == 0:
            count_a += 1

    # part 2 (rather dumb but works because input is small enough)
    for direction, num in rotations:
        step = 1 if direction == "R" else -1
        for _ in range(num):
            dial_b1 = (dial_b1 + step) % 100
            if dial_b1 == 0:
                count_b1 += 1

    # part 2 (more efficient version that wasn't written half asleep at 6am :D)
    for direction, num in rotations:
        step = num if direction == "R" else -num
        count_b2 += abs(dial_b2 + step) // 100
        if dial_b2 != 0 and dial_b2 + step <= 0:
            count_b2 += 1

        dial_b2 = (dial_b2 + step) % 100

    # PART 1
    # test:      3
    # answer: 1165
    print(count_a)

    # PART 2
    # test:      6
    # answer: 6496
    print(count_b1, count_b2)
