import sys

WEST = complex(0, -1)
EAST = complex(0, 1)
NORTH = complex(-1, 0)
SOUTH = complex(1, 0)

move_mapping = {
    "<": WEST,
    ">": EAST,
    "^": NORTH,
    "v": SOUTH,
}

BOUNDS = complex(0, 0)


def parse(moves, map):
    global BOUNDS

    move_list = []
    for line in moves:
        for ch in line.strip():
            move_list.append(move_mapping[ch])

    game_map = {}
    robot_position = None
    rows, cols = 0, 0
    for row, line in enumerate(map):
        rows = row
        cols = len(line.strip()) * 2
        for col, ch in enumerate(line.strip()):
            col *= 2
            if ch == "@":
                robot_position = complex(row, col)
                game_map[complex(row, col)] = ch
                game_map[complex(row, col + 1)] = "."
            elif ch == "O":
                game_map[complex(row, col)] = "["
                game_map[complex(row, col + 1)] = "]"
            elif ch in "#.":
                game_map[complex(row, col)] = ch
                game_map[complex(row, col + 1)] = ch

    BOUNDS = complex(rows, cols)
    return move_list, game_map, robot_position


def calc_gps(game_map):

    gps = 0
    for k, v in game_map.items():
        if v == "[":
            gps += 100 * int(k.real) + int(k.imag)
    return gps


def viz(game_map):
    for row in range(int(BOUNDS.real) + 1):
        for col in range(int(BOUNDS.imag)):
            print(game_map[complex(row, col)], end="")
        print()


def swap(game_map, l, r, tl, tr):
    gtl, gtr = game_map[tl], game_map[tr]
    gl, gr = game_map[l], game_map[r]
    game_map[tl], game_map[tr] = gl, gr
    game_map[l], game_map[r] = gtl, gtr


def move_box(game_map, l, r, mv, test=False):
    tl = l + mv
    tr = r + mv

    # print(f"{game_map[tl]=}{game_map[tr]=}")

    if mv in (NORTH, SOUTH):
        match (game_map[tl], game_map[tr]):
            case (".", "."):
                # print(f"pushing the box {mv=}")
                # print(
                #     f"swapping {game_map[tl], game_map[tr]} and {game_map[l], game_map[r]}"
                # )
                # viz(game_map)
                # input()
                if not test:
                    swap(game_map, l, r, tl, tr)
                # viz(game_map)
                # input()
                return True
            case (".", "["):
                if move_box(game_map, tr, tr + EAST, mv, test):
                    if not test:
                        swap(game_map, l, r, tl, tr)
                    return True
                return False
            case ("]", "."):
                if move_box(game_map, tl + WEST, tl, mv, test):
                    if not test:
                        swap(game_map, l, r, tl, tr)
                    return True
                return False
            case ("[", "]"):
                # print(f"pushing a whole box")
                if move_box(game_map, tl, tr, mv, test):
                    if not test:
                        swap(game_map, l, r, tl, tr)
                    return True
                return False
            case ("]", "["):
                # print(f"pushing two boxes")
                if move_box(game_map, tl + WEST, tl, mv, True) and move_box(
                    game_map, tr, tr + EAST, mv, True
                ):
                    move_box(game_map, tl + WEST, tl, mv, test)
                    move_box(game_map, tr, tr + EAST, mv, test)
                    if not test:
                        swap(game_map, l, r, tl, tr)
                    return True
                return False
            case ("#", "#"):
                return False

    if mv == WEST:
        if game_map[tl] == ".":
            game_map[tl], game_map[l], game_map[r] = (
                game_map[l],
                game_map[r],
                game_map[tl],
            )
            return True
        elif game_map[tl] == "]" and move_box(game_map, tl + WEST, tl, mv):
            game_map[tl], game_map[l], game_map[r] = (
                game_map[l],
                game_map[r],
                game_map[tl],
            )
            return True

    elif mv == EAST:
        if game_map[tr] == ".":
            game_map[l], game_map[r], game_map[tr] = (
                game_map[tr],
                game_map[l],
                game_map[r],
            )
            return True
        if game_map[tr] == "[" and move_box(game_map, tr, tr + EAST, mv):
            game_map[l], game_map[r], game_map[tr] = (
                game_map[tr],
                game_map[l],
                game_map[r],
            )
            return True

    return False


def move_ch(game_map, pos, mv):
    t = pos + mv

    match (game_map[t]):
        case ".":
            game_map[t], game_map[pos] = game_map[pos], game_map[t]
            return True
        case "#":
            return False
        case "[":
            if move_box(game_map, t, t + EAST, mv):
                game_map[t], game_map[pos] = game_map[pos], game_map[t]
                return True
            return False
        case "]":
            if move_box(game_map, t + WEST, t, mv):
                game_map[t], game_map[pos] = game_map[pos], game_map[t]
                return True
            return False


if __name__ == "__main__":
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    mapmap = {
        "input.txt": "input-map.txt",
        "small.txt": "small-map.txt",
        "medium.txt": "medium-map.txt",
        "tiny.txt": "tiny-map.txt",
        "test1.txt": "test1-map.txt",
        "test2.txt": "test2-map.txt",
        "test3.txt": "test3-map.txt",
        "test4.txt": "test4-map.txt",
        "test5.txt": "test5-map.txt",
        "test6.txt": "test6-map.txt",
    }

    with open(fname) as move_fp:
        with open(mapmap[fname]) as map_fp:
            move_list, game_map, robot_position = parse(move_fp, map_fp)

            viz(game_map)
            for move in move_list:
                if move_ch(game_map, robot_position, move):
                    robot_position = robot_position + move
                    game_map[robot_position] = "@"
                # viz(game_map)
                # input()

        viz(game_map)
        print(calc_gps(game_map))
