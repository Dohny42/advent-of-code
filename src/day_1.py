import data_fetch

# data: list[str] = data_fetch.fetch_aoc_data(year=2025, day=1).splitlines()

data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()


def part_1() -> None:
    current = 50
    password = 0
    for line in data:
        dir, num = line[0], int(line[1:])
        num %= 100
        if dir == "R":
            current += num
            if current >= 100:
                current -= 100
        elif dir == "L":
            diff = current - num
            if diff < 0:
                current = 100 + diff
            else:
                current = diff

        password += 1 if current == 0 else 0

    print(password)


def part_2() -> None:
    current = 50
    password = 0
    for line in data:
        dir, num = line[0], int(line[1:])
        if dir == "R":
            mod, rem = divmod((current + num), 100)
            current = rem
            password += mod
        elif dir == "L":
            # if num > current:
            #     mod, rem = divmod((num + current), 100)
            #     current = 100 - rem
            #     password += mod

            mod, rem = divmod(abs((current - num)), 100)
            current = 100 - rem
            password += mod

    print(password)


if __name__ == "__main__":
    part_1()
    part_2()
