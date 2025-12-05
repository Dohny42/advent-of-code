import data_fetch

# data: list[str] = data_fetch.fetch_aoc_data(year=2025, day=4).splitlines()

data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()


def get_adjacent(x: int, y: int, data: list[list[str]]) -> int:
    # return number of adjacent (around) positions that are "@"
    adjacent_positions = [
        (x - 1, y),  # left
        (x + 1, y),  # right
        (x, y - 1),  # up
        (x, y + 1),  # down
        (x - 1, y - 1),  # up-left
        (x + 1, y - 1),  # up-right
        (x - 1, y + 1),  # down-left
        (x + 1, y + 1),  # down-right
    ]
    count = 0
    for pos in adjacent_positions:
        adj_x, adj_y = pos
        if 0 <= adj_y < len(data) and 0 <= adj_x < len(data[0]):
            if data[adj_y][adj_x] == "@":
                count += 1
    return count


def part_1() -> None:
    data_parsed = data
    total = 0
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == "@":
                n_adj = get_adjacent(x, y, data_parsed)
                if n_adj < 4:
                    total += 1

    print(f"Total: {total}")


def part_2() -> None:
    data_parsed = [list(line) for line in data]
    total = 0
    any_removable = True
    while any_removable:
        prev_total = total
        marks = []
        for y, line in enumerate(data_parsed):
            for x, char in enumerate(line):
                if char == "@":
                    n_adj = get_adjacent(x, y, data_parsed)
                    if n_adj < 4:
                        marks.append((x, y))
                        total += 1
        for x, y in marks:
            data_parsed[y][x] = "."
        print(f"Total so far: {total}")
        if total == prev_total:
            any_removable = False

    print(f"Final Total: {total}")


if __name__ == "__main__":
    part_1()
    part_2()
