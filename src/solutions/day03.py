from src.tools.loader import load_data

TESTING = True


def find_optimal_batteries(bank, amount):
    joltage = ""

    for idx in range(0, amount):
        valid_bank = bank[: (-amount + idx + 1)] if idx != amount - 1 else bank
        battery = max(valid_bank)
        joltage += str(battery)
        bank = bank[valid_bank.index(battery) + 1 :]

    return int(joltage)


def total_output_joltage(banks, amount):
    total_joltage = 0

    for bank in banks:
        optimal = find_optimal_batteries(bank, amount)
        total_joltage += optimal

    return total_joltage


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    banks = [[int(el) for el in banks] for banks in data]

    # PART 1
    # test:     357
    # answer: 17493
    print(total_output_joltage(banks, 2))

    # PART 2
    # test:     3121910778619
    # answer: 173685428989126
    print(total_output_joltage(banks, 12))
