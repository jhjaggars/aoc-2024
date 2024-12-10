import sys


def load(raw):
    map = {}
    for r, row in enumerate(raw):
        for c, v in enumerate(row.strip()):
            map[complex(r, c)] = int(v)
    return map


dirs = (
    complex(0, 1),
    complex(1, 0),
    complex(0, -1),
    complex(-1, 0),
)


def dfs(pt, height, found):
    if pt not in map:
        return 0
    v = map[pt]
    if v != height:
        return 0

    if v == 9:
        found.add(pt)
    for dir in dirs:
        dfs(pt + dir, v + 1, found)


if __name__ == "__main__":
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    with open(fname) as fp:
        map = load(fp)

    score = 0
    for pt, v in map.items():
        if v == 0:
            found = set()
            dfs(pt, v, found)
            score += len(found)
    print(score)
