import data_fetch

data = data_fetch.fetch_aoc_data(year=2025, day=6)
# data = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """


def part_1() -> None:
    rows = data.splitlines()
    total = 0
    grid = []
    for line in rows:
        grid.append([el.strip() for el in line.split()])

    for x in range(len(grid[0])):
        col = 0
        for y in range(len(grid) - 1):
            # operation is the last row
            op = grid[-1][x]
            val = int(grid[y][x])
            if op == "+":
                col += val
            elif op == "*":
                if col == 0:
                    col = 1
                col *= val
        total += col
    print(f"Total: {total}")


def part_2() -> None:
    rows = data.splitlines()
    total = 0
    grid = []
    for line in rows:
        grid.append(line)

    curr_col_nums = []
    for x in range(len(grid[0]) - 1, -1, -1):
        col = 0
        num_in_col_str = ""
        curr_col_op = ""
        for y in range(len(grid) - 1):
            num_in_col_str += grid[y][x]
            if grid[-1][x] != " ":
                curr_col_op = grid[-1][x]
        # skip empty columns
        if num_in_col_str.strip() == "":
            continue
        curr_col_nums.append(int(num_in_col_str.strip()))
        if curr_col_op != "":
            # we can perform operation
            if curr_col_op == "+":
                for n in curr_col_nums:
                    col += n
            elif curr_col_op == "*":
                if col == 0:
                    col = 1
                for n in curr_col_nums:
                    col *= n
            # clear the curr col nums and op
            curr_col_nums = []
            curr_col_op = ""
        total += col
    print(f"Total: {total}")


if __name__ == "__main__":
    part_1()
    part_2()
