from src.tools.loader import load_data
from math import prod

TESTING = True


def calculate_total(grouped_nums, operators):
    total = 0

    for nums, op in zip(grouped_nums, operators):
        value = sum(nums) if op == "+" else prod(nums)
        total += value

    return total


def solve_part_1(data):
    operators = data[-1].split()
    grouped_nums = zip(*[list(map(int, line.split())) for line in data[:-1]])

    return calculate_total(grouped_nums, operators)


def solve_part_2(data):
    operators = data[-1].split()
    cols = list(zip(*data[:-1]))
    nums = ["".join(col).strip() for col in cols]

    grouped_nums = [[]]
    for num in nums:
        if not num:
            grouped_nums.append([])
        else:
            grouped_nums[-1].append(int(num))

    return calculate_total(grouped_nums, operators)


if __name__ == "__main__":
    data = load_data(TESTING, "\n")

    # PART 1
    # test:         4277556
    # answer: 5733696195703
    print(solve_part_1(data))

    # PART 2
    # test:          3263827
    # answer: 10951882745757
    print(solve_part_2(data))
