from src.tools.loader import load_data

TESTING = False


if __name__ == "__main__":
    data = load_data(TESTING, "\n")
    batteries = [[int(el) for el in banks] for banks in data]
    values = []
    voltage = 12

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

    print(sum(values))

    new_values = []

    for bank in batteries:
        positions = [None] * 12
        indices = [None] * 12
        n = len(bank)

        for k in range(9, 0, -1):
            for i, battery in enumerate(bank[: (-voltage + 1)]):
                if (positions[0] is None) and battery == k:
                    positions[0] = battery
                    indices[0] = i

        for vol in range(1, 11):
            for k in range(9, 0, -1):
                for i, battery in enumerate(bank[: (-voltage + vol + 1)]):
                    if (
                        battery == k
                        and (positions[vol - 1] is not None)
                        and (positions[vol] is None)
                        and (indices[vol - 1] < i)
                    ):
                        positions[vol] = battery
                        indices[vol] = i

        for k in range(9, 0, -1):
            for i, battery in enumerate(bank):
                if (
                    battery == k
                    and (positions[voltage - 2] is not None)
                    and (positions[voltage - 1] is None)
                    and (indices[voltage - 2] < i)
                ):
                    positions[voltage - 1] = battery
                    indices[voltage - 1] = i

        new_values.append(int("".join([str(el) for el in positions])))

    print(sum(new_values))
