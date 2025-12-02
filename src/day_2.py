from typing import Generator

from aocd import get_data

data: list[str] = get_data(day=2, year=2025).split(",")
# data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(
#     ","
# )


def generate_range(start: int, end: int) -> Generator[int, None, None]:
    for i in range(start, end + 1):
        yield i


def part_1() -> None:
    total = 0

    for id_range in data:
        start, end = map(int, id_range.split("-"))
        for id_int in generate_range(start, end):
            id_str = str(id_int)
            if len(id_str) % 2 != 0:
                continue

            # both halves have same digits
            mid = len(id_str) // 2
            first_half = id_str[:mid]
            second_half = id_str[mid:]
            if first_half == second_half:
                total += id_int

    print(total)


def check_one_digit_repeat(id_str: str) -> bool:
    first = id_str[0]
    return all(char == first for char in id_str)


def check_two_digit_repeat(id_str: str) -> bool:
    for i in range(0, len(id_str), 2):
        pair = id_str[i : i + 2]
        if pair != id_str[0:2]:
            return False
    return True


def check_three_digit_repeat(id_str: str) -> bool:
    for i in range(0, len(id_str), 3):
        triplet = id_str[i : i + 3]
        if triplet != id_str[0:3]:
            return False
    return True


def part_2() -> None:
    total = 0

    for id_range in data:
        start, end = map(int, id_range.split("-"))
        for id_int in generate_range(start, end):
            id_str = str(id_int)
            if len(id_str) < 2:
                continue
            if len(id_str) % 2 != 0:
                check = check_one_digit_repeat(id_str)
                if check:
                    total += id_int
                # total += id_int if check else 0
                if not check and len(id_str) == 9:
                    check = check_three_digit_repeat(id_str)
                    if check:
                        total += id_int
                continue
            # both halves have same digits
            same = False
            mid = len(id_str) // 2
            first_half = id_str[:mid]
            second_half = id_str[mid:]
            if first_half == second_half:
                same = True
            if (
                not same and not len(id_str) == 2
            ):  # skip two digit check for two digits (pair check for 24 fails since 2 != 4)
                same = check_two_digit_repeat(id_str)
            if same:
                total += id_int

    print(total)


if __name__ == "__main__":
    # part_1()
    part_2()
