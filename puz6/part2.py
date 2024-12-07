import time

map = []

up = (-1, 0)
right = (0, 1)
down = (1, 0)
left = (0, -1)
dirs = (up, right, down, left)
heading = 0
MXX = 0
MXY = 0


def getNextYX(heading, coord):
    return dirs[heading][0] + coord[0], dirs[heading][1] + coord[1]


def turn(heading):
    return (heading + 1) % len(dirs)


def mark(heading):
    match heading:
        case 0:
            return "^"
        case 1:
            return ">"
        case 2:
            return "v"
        case 3:
            return "<"


def show_map(pos, heading, block=()):

    if block:
        try:
            orig_path = map[block[0]][block[1]]
        except IndexError:
            return
        map[block[0]][block[1]] = "O"

    orig_guard = map[pos[0]][pos[1]]
    map[pos[0]][pos[1]] = mark(heading)

    for r in map:
        print("".join(r))

    map[pos[0]][pos[1]] = orig_guard

    if block:
        map[block[0]][block[1]] = orig_path


def get_spaces(pos, heading):
    spaces = set()

    while True:
        # mark current
        spaces.add((pos[0], pos[1]))

        # get the test cell
        y, x = getNextYX(heading, (pos[0], pos[1]))

        # check for edge of map
        if x >= MXX or x < 0 or y >= MXY or y < 0:
            return spaces

        # turn if needed
        if map[y][x] == "#":
            heading = turn(heading)
        else:
            # step
            pos = y, x


def is_loop(pos, heading, block):

    visited = set((pos[0], pos[1], heading))
    while True:
        y, x = getNextYX(heading, (pos[0], pos[1]))

        if x >= MXX or x < 0 or y >= MXY or y < 0:
            return False

        if (y, x, heading) in visited:
            # show_map(pos, heading, block)
            # input()
            return True

        if map[y][x] == "#" or (y, x) == block:
            heading = turn(heading)
        else:
            visited.add((y, x, heading))
            pos = y, x


if __name__ == "__main__":
    initial = 0, 0

    with open("input.txt") as fp:
        # with open("small.txt") as fp:
        for y, line in enumerate(fp):
            row = list(line.strip())
            try:
                initial = y, row.index("^")
            except ValueError:
                pass
            map.append(row)

    MXY = len(map)
    MXX = len(map[0])
    map[initial[0]][initial[1]] = "."

    spaces = get_spaces(initial, heading)
    loops = 0

    for y, x in spaces:

        # cannot place a temporary block on the initial space
        if (y, x) == initial:
            continue

        if is_loop((initial[0], initial[1]), 0, (y, x)):
            loops += 1

    print(loops)
