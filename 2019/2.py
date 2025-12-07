def solve() -> int:
    with open("2.txt", "r") as f:
        f = f.read().strip().split(",")
        inp = [int(n) for n in f]

    inp[1], inp[2] = 12, 2
    print(inp)
    i = 0
    while i < len(inp):
        if inp[i] == 99:
            break
        elif inp[i] == 1:
            x, y = inp[inp[i + 1]], inp[inp[i + 2]]
            inp[inp[i + 3]] = x + y
            i += 4
        elif inp[i] == 2:
            x, y = inp[inp[i + 1]], inp[inp[i + 2]]
            inp[inp[i + 3]] = x * y
            i += 4
        else:
            i += 1
    return inp[0]


def solve2() -> int:
    with open("2.txt", "r") as f:
        f = f.read().strip().split(",")
        ff = [int(n) for n in f]
    for q in range(100):
        for w in range(100):
            inp = ff.copy()
            inp[1], inp[2] = q, w
            i = 0
            while i < len(inp):
                if inp[i] == 99:
                    break
                elif inp[i] == 1:
                    x, y = inp[inp[i + 1]], inp[inp[i + 2]]
                    inp[inp[i + 3]] = x + y
                    i += 4
                elif inp[i] == 2:
                    x, y = inp[inp[i + 1]], inp[inp[i + 2]]
                    inp[inp[i + 3]] = x * y
                    i += 4
                else:
                    i += 1
            if inp[0] == 19690720:
                return 100 * q + w


print(solve2())
