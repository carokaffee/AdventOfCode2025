from src.tools.loader import load_data

TESTING = True


def count_fresh_ids_in_list(id_ranges, ingredients):
    count = 0

    for ing_id in ingredients:
        if any([start <= ing_id and ing_id <= end for start, end in id_ranges]):
            count += 1

    return count


def count_all_fresh_ids(id_ranges):
    endpoints = {el for pair in id_ranges for el in pair}
    cut_id_ranges = set()

    for a, b in id_ranges:
        cuts = sorted(el for el in endpoints if a <= el and el <= b)
        cut_id_ranges.update((el, el) for el in cuts)
        cut_id_ranges.update((cuts[i] + 1, cuts[i + 1] - 1) for i in range(len(cuts) - 1))

    count = sum(b - a + 1 for a, b in cut_id_ranges)

    return count


if __name__ == "__main__":
    raw_ranges, raw_ingredients = load_data(TESTING, "\n\n")

    id_ranges = [tuple(map(int, el.split("-"))) for el in raw_ranges.split("\n")]
    ingredients = list(map(int, raw_ingredients.split("\n")))

    # PART 1
    # test:     3
    # answer: 529
    print(count_fresh_ids_in_list(id_ranges, ingredients))

    # PART 2
    # test:                14
    # answer: 344260049617193
    print(count_all_fresh_ids(id_ranges))
