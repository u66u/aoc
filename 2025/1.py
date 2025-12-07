def inp():
    with open("inp.txt", "r") as f:
        r = []
        for l in f.readlines():
            r.append(l.strip())
    return r

def p1(arr: list) -> int:
    cur = 50
    res = 0
    for i in arr:
        direction = i[0]
        val = int(i[1:])
        if direction == "R":
            cur += val
        else:
            cur -= val
        cur %= 100
        if cur == 0: res += 1
    return res


def p2(arr: list) -> int:
    cur = 50
    res = 0
    for i in arr:
        direction = i[0]
        val = int(i[1:])
        if direction == "R":
            target = cur + val
            res += (target // 100) - (cur // 100)
            cur = target % 100
        else:
            target = cur - val
            res += ((cur - 1) // 100) - ((target - 1) // 100)
            cur = target % 100
    return res

print(p2(inp()))
