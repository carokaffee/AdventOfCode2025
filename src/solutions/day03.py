from src.tools.loader import load_data

TESTING = False


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    batteries = [[int(el) for el in banks] for banks in data]
    print(batteries)
    values = []

    for bank in batteries:
        first = None
        first_index = None
        second = None
        n = len(bank)
        for k in range(9, 0, -1):
            for i, battery in enumerate(bank[:-1]):
                if (first is None) and battery == k:
                    first = battery
                    first_index = i
        for k in range(9, 0, -1):
            for i, battery in enumerate(bank):
                if (first is not None) and (second is None) and first_index < i and battery == k:
                    second = battery
        values.append(10 * first + second)

    print(values)
    print(sum(values))
