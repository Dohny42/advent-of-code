import data_fetch

data = data_fetch.fetch_aoc_data(year=2025, day=5)

# data = """3-5
# 10-14
# 16-20
# 12-18

# 1
# 5
# 8
# 11
# 17
# 32"""


def part_1() -> None:
    ranges, ids = data.split("\n\n")
    ranges = ranges.splitlines()
    ids = ids.splitlines()

    total = 0
    for id in ids:
        for range in ranges:
            start, end = map(int, range.split("-"))
            value = int(id)
            if start <= value <= end:
                total += 1
                break
    print(f"Total: {total}")


def part_2() -> None:
    ranges, ids = data.split("\n\n")
    ranges = ranges.splitlines()

    total = 0
    for i in range(len(ranges)):
        start_i, end_i = map(int, ranges[i].split("-"))
        total_i = end_i - start_i + 1
        for j in range(len(ranges)):
            if i == j:
                continue
            start_j, end_j = map(int, ranges[j].split("-"))
            # check if ranges overlap
            if start_i <= end_j and start_j <= end_i:
                overlap_n = min(end_i, end_j) - max(start_i, start_j) + 1
                if i < j:
                    total -= overlap_n
        total += total_i
    print(f"Total: {total}")


if __name__ == "__main__":
    # part_1()
    part_2()
