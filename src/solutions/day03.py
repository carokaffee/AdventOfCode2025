from src.tools.loader import load_data

TESTING = False


def find_optimal_batteries(bank, amount):
    positions = [None] * amount
    indices = [None] * amount

    for idx in range(0, amount):
        for k in range(9, 0, -1):
            valid_bank = bank[: (-amount + idx + 1)] if idx != amount - 1 else bank
            for i, battery in enumerate(valid_bank):
                if (
                    battery == k
                    and (idx == 0 or positions[idx - 1] is not None)
                    and (positions[idx] is None)
                    and (idx == 0 or indices[idx - 1] < i)
                ):
                    positions[idx] = battery
                    indices[idx] = i
    return int("".join([str(el) for el in positions]))


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    banks = [[int(el) for el in banks] for banks in data]
    amount = 12

    new_values = []

    for bank in banks:
        optimal = find_optimal_batteries(bank, amount)
        new_values.append(optimal)

    print(sum(new_values))
