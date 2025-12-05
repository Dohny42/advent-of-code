import pathlib

import requests


def fetch_aoc_data(year: int, day: int) -> str:
    token_path = pathlib.Path.home() / ".config" / "aocd" / "token"
    try:
        with open(token_path, "r") as f:
            token = f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Token file not found at {token_path}")

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": token}
    response = requests.get(url, cookies=cookies)
    response.raise_for_status()
    return response.text
