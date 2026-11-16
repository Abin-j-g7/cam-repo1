import sys

import requests
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding="utf-8")


def decode_secret_message(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")
    if table is None:
        raise ValueError("No table found in the page content")

    data = []

    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")

        if len(cells) >= 3:
            x = int(cells[0].text.strip())
            char = cells[1].text.strip()
            y = int(cells[2].text.strip())
            data.append((x, y, char))

    if not data:
        raise ValueError("No grid data found in the table")

    max_x = max(item[0] for item in data)
    max_y = max(item[1] for item in data)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, y, char in data:
        grid[y][x] = char

    for row in grid:
        print("".join(row))


decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub")