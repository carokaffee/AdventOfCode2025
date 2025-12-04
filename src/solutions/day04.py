from src.tools.loader import load_data

TESTING = True
DIR = tuple((dx, dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1) if dx != 0 or dy != 0)


def prepare_grid(data):
    len_padded = len(data) + 2
    empty = ["."]
    rolls = []
    rolls.append(empty * len_padded)
    rolls += [empty + [el for el in row] + empty for row in data]
    rolls.append(["."] * len_padded)

    return rolls


def find_accessible_rolls(rolls, iterate=False):
    num_rows = len(rolls)
    num_cols = len(rolls[0])

    counter = 0
    change = True

    while change:
        change = False
        for x in range(1, num_rows - 1):
            for y in range(1, num_cols - 1):
                if rolls[x][y] == ".":
                    continue
                num_near_rolls = 0
                for dx, dy in DIR:
                    num_near_rolls += rolls[x + dx][y + dy] == "@"
                if num_near_rolls < 4:
                    counter += 1
                    if iterate:
                        rolls[x][y] = "."
                        change = True

    return counter


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    rolls = prepare_grid(data)

    # PART 1
    # test:     13
    # answer: 1370
    print(find_accessible_rolls(rolls))

    # PART 2
    # test:     43
    # answer: 8437
    print(find_accessible_rolls(rolls, iterate=True))
