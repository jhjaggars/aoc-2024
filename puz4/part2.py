def valid(side):
    return side[0] in ("M", "S") and side[1] in ("M", "S") and side[0] == side[1]


def cmp(side_a, side_b):
    if valid(side_a) and valid(side_b):
        if side_a[0] != side_b[0]:
            return 1
    return 0


if __name__ == "__main__":
    grid = []
    with open("input.txt") as fp:
        for line in fp:
            grid.append(list(line.strip()))

    def scan(x, y):
        nw, ne = grid[x - 1][y - 1], grid[x + 1][y - 1]
        sw, se = grid[x - 1][y + 1], grid[x + 1][y + 1]

        top, bottom = (nw, ne), (sw, se)
        left, right = (nw, sw), (ne, se)

        return cmp(top, bottom) + cmp(left, right)

    matches = 0
    MXY = len(grid)
    MXX = len(grid[0])
    for x in range(1, MXX - 1):
        for y in range(1, MXY - 1):
            if grid[x][y] != "A":
                continue
            matches += scan(x, y)

    print(matches)
