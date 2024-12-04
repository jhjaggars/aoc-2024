MXX = 0
MXY = 0


if __name__ == "__main__":
    grid = []
    with open("input.txt") as fp:
        for line in fp:
            grid.append(list(line.strip()))

    MXY = len(grid)
    MXX = len(grid[0])

    def scan(x, y, vx, vy):
        steps = 0
        buf = []
        while steps < 4:
            if 0 <= x < MXX and 0 <= y < MXY:
                buf.append(grid[x][y])
            else:
                return 0
            steps += 1
            x += vx
            y += vy

        if buf == ["X", "M", "A", "S"]:
            print(x, y, buf)
            return 1
        else:
            return 0

    matches = 0
    for x in range(MXX):
        for y in range(MXY):
            if grid[x][y] != "X":
                continue
            matches += sum(
                (
                    scan(x, y, 1, 0),
                    scan(x, y, -1, 0),
                    scan(x, y, 0, 1),
                    scan(x, y, 0, -1),
                    scan(x, y, 1, 1),
                    scan(x, y, 1, -1),
                    scan(x, y, -1, 1),
                    scan(x, y, -1, -1),
                )
            )

    print(matches)
