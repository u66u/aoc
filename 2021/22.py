from os import getenv
from pathlib import Path
from aocd import get_data

session = getenv("AOC_SESSION")
file_path = Path(__file__)
day = int(file_path.stem)
year = int(file_path.parent.name)

d = get_data(session, day, year).split("\n")
d = [s.split(" ") for s in d]


def p1(inp: list) -> int:
    on_s = set()
    for i in inp:
        on = i[0].startswith("on")
        arr = [val for val in i[1].split(",")]

        xr = arr[0][2:].split("..")
        yr = arr[1][2:].split("..")
        zr = arr[2][2:].split("..")

        x1, x2 = int(xr[0]), int(xr[1])
        y1, y2 = int(yr[0]), int(yr[1])
        z1, z2 = int(zr[0]), int(zr[1])

        # x1, x2 = max(-50, x1), min(50, x2)
        # y1, y2 = max(-50, y1), min(50, y2)
        # z1, z2 = max(-50, z1), min(50, z2)

        if x1 > x2 or y1 > y2 or z1 > z2:
            continue
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                for z in range(z1, z2 + 1):
                    if on:
                        on_s.add((x, y, z))
                    else:
                        on_s.discard((x, y, z))
    return len(on_s)


print(p1(d))
