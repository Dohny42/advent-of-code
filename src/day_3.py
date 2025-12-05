import data_fetch

# data: list[str] = data_fetch.fetch_aoc_data(year=2025, day=3).splitlines()

data = """987654321111111
811111111111119
234234234234278
818181911112111
""".splitlines()


def part_1() -> None:
    total = 0
    for line in data:
        curr_left_idx = 0
        curr_right_idx = len(line) - 1
        left_max = -1
        left_max_idx = 0
        right_max = -1
        right_max_idx = len(line) - 1

        # process left side
        while curr_left_idx < len(line) - 1:
            curr = int(line[curr_left_idx])
            if curr > left_max:
                left_max = curr
                left_max_idx = curr_left_idx
            if curr == 9:
                break
            curr_left_idx += 1

        # process right side (from end to left idx + 1)
        while curr_right_idx > left_max_idx:
            curr = int(line[curr_right_idx])
            if curr > right_max:
                right_max = curr
                right_max_idx = curr_right_idx
            if curr == 9:
                break
            curr_right_idx -= 1

        conc = int(f"{left_max}{right_max}")
        print(conc)
        total += conc

        print(total)

        print(
            f"Line: {line} Max 1: {left_max} at {left_max_idx}, Max 2: {right_max} at {right_max_idx}"
        )

    print(f"Total: {total}")


def get_max_data(line: str, skip: list[int]) -> tuple[int, int]:
    max_digit = -1
    max_idx = -1
    for idx, char in enumerate(line):
        curr = int(char)
        if curr > max_digit:
            max_digit = curr
            max_idx = idx
    return max_digit, max_idx


def part_2() -> None:
    total = 0
    for line in dummy_data:
        # 12 passes
        for i in range(12):
            print(f"Pass {i + 1}")
            max_digit, max_idx = get_max_data(line)
        curr_left_idx = 0
        curr_right_idx = len(line) - 1
        left_max = -1
        left_max_idx = 0
        right_max = -1
        right_max_idx = len(line) - 1

        # process left side
        while curr_left_idx < len(line) - 1:
            curr = int(line[curr_left_idx])
            if curr > left_max:
                left_max = curr
                left_max_idx = curr_left_idx
            if curr == 9:
                break
            curr_left_idx += 1

        # process right side (from end to left idx + 1)
        while curr_right_idx > left_max_idx:
            curr = int(line[curr_right_idx])
            if curr > right_max:
                right_max = curr
                right_max_idx = curr_right_idx
            if curr == 9:
                break
            curr_right_idx -= 1

        conc = int(f"{left_max}{right_max}")
        print(conc)
        total += conc

        print(total)

        print(
            f"Line: {line} Max 1: {left_max} at {left_max_idx}, Max 2: {right_max} at {right_max_idx}"
        )

    print(f"Total: {total}")


if __name__ == "__main__":
    part_1()
