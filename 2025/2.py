def inp(innp: str):
    ranges = []
    for part in innp.replace("\n", "").split(","):
        part = part.strip()
        if part:
            l, h = map(int, part.split("-"))
            ranges.append((l, h))
    return ranges


def ceildiv(a, b):
    return (a + b - 1) // b


def p1(ranges: list) -> int:
    res = 0
    for l, h in ranges:
        k = 1
        while 1:
            b = 10**k
            min_k, max_k = b // 10 or 1, b - 1
            m = b + 1
            if min_k * m > h:
                break
            lo = max(min_k, ceildiv(l, m))
            hi = min(max_k, h // m)
            if lo <= hi:
                cnt = hi - lo + 1
                res += m * cnt * (lo + hi) // 2
            k += 1
    return res

def repeating_mult(k, r):
        res, power = 0, 1
        for _ in range(r):
            res += power
            power *= 10**k
        return res

def p2(ranges: list) -> int:
    ids = set()
    for l, h in ranges:
        k = 1
        while 1:
            b = 10**k
            min_k, max_k = b // 10 or 1, b - 1
            if min_k * (b + 1) > h:
                break
            r = 2
            while 1:
                m = repeating_mult(k, r)
                if min_k * m > h:
                    break
                lo = max(min_k, ceildiv(l, m))
                hi = min(max_k, h // m)
                for p in range(lo, hi + 1):
                    ids.add(p * m)
                r += 1
            k += 1
    return sum(ids)


with open("inp.txt", "r") as f:
    x = inp(f.read())
    print(p1(x))
    print(p2(x))
