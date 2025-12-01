from src.tools.loader import load_data

TESTING = False


if __name__ == "__main__":
    data = load_data(TESTING, "\n")

    code = [(el[0], int(el[1:])) for el in data]

    dial = 50
    count = 0

    for direction, el in code:
        if direction == "R":
            dial = (dial + el) % 100
        elif direction == "L":
            dial = (dial - el) % 100
        else:
            raise ValueError
        if dial == 0:
            count += 1

    print(count)

    dial = 50
    count2 = 0

    for direction, el in code:
        if direction == "R":
            for _ in range(el):
                dial = (dial + 1) % 100
                if dial == 0:
                    count2 += 1
        if direction == "L":
            for _ in range(el):
                dial = (dial - 1) % 100
                if dial == 0:
                    count2 += 1

    print(count2)
