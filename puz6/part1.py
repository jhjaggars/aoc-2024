map = []
pos = 0, 0

up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)
dirs = (up, right, down, left)
heading = 0


def getNextXY(heading):
    return dirs[heading][0] + pos[0], dirs[heading][1] + pos[1]


def turn(heading):
    return (heading + 1) % len(dirs)


if __name__ == "__main__":
    with open("input.txt") as fp:
        for y, line in enumerate(fp):
            row = list(line.strip())
            try:
                pos = y, row.index("^")
            except ValueError:
                pass
            map.append(row)

    mxy = len(map)
    mxx = len(map[0])

    spaces = set()

    while True:
        # mark current
        # map[pos[0]][pos[1]] = "X"
        spaces.add((pos[0], pos[1]))

        # get the test cell
        x, y = getNextXY(heading)

        # check for edge of map
        if x >= mxx or y >= mxy:
            break

        # turn if needed
        if map[x][y] == "#":
            heading = turn(heading)
        else:
            # step
            pos = x, y

    # print(sum(row.count("X") for row in map))
    print(len(spaces))
