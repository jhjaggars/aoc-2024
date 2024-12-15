import sys

w = complex(0, -1)
e = complex(0, 1)
n = complex(-1, 0)
s = complex(1, 0)

move_mapping = {
    "<": w,
    ">": e,
    "^": n,
    "v": s,
}


def parse(moves, map):

    move_list = []
    for line in moves:
        for ch in line.strip():
            move_list.append(move_mapping[ch])

    game_map = {}
    robot_position = None
    rows, cols = 0, 0
    for row, line in enumerate(map):
        rows = row
        cols = len(line.strip())
        for col, ch in enumerate(line.strip()):
            if ch == "@":
                robot_position = complex(row, col)
                game_map[complex(row, col)] = ch
            elif ch in "#O.":
                game_map[complex(row, col)] = ch

    return move_list, game_map, robot_position, complex(rows, cols)


def move_ch(game_map, pos, mv):
    t = pos + mv

    match (game_map[t]):
        case ".":
            game_map[t], game_map[pos] = game_map[pos], game_map[t]
            return True
        case "#":
            return False
        case "O":
            if move_ch(game_map, t, mv):
                game_map[t], game_map[pos] = game_map[pos], game_map[t]
                return True
            return False


def calc_gps(game_map):

    gps = 0
    for k, v in game_map.items():
        if v == "O":
            gps += 100 * int(k.real) + int(k.imag)
    return gps


def viz(game_map, bounds):
    print(bounds)

    for row in range(int(bounds.real) + 1):
        for col in range(int(bounds.imag)):
            print(game_map[complex(row, col)], end="")
        print()


if __name__ == "__main__":
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    mapmap = {
        "input.txt": "input-map.txt",
        "small.txt": "small-map.txt",
        "medium.txt": "medium-map.txt",
    }

    with open(fname) as move_fp:
        with open(mapmap[fname]) as map_fp:
            move_list, game_map, robot_position, bounds = parse(move_fp, map_fp)

            # print(game_map)
            viz(game_map, bounds)
            for move in move_list:
                if move_ch(game_map, robot_position, move):
                    robot_position = robot_position + move
                # viz(game_map, bounds)
                # input()

            viz(game_map, bounds)
            print(calc_gps(game_map))
