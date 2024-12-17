import sys
from heapq import heappop, heappush
from math import inf

dirs = [
    complex(1, 0),  # S
    complex(0, 1),  # E
    complex(-1, 0),  # N
    complex(0, -1),  # W
]

EAST = 1

BOUNDS = complex(0, 0)

HEADING_VIZ = {
    complex(1, 0): "v",
    complex(0, 1): ">",
    complex(-1, 0): "^",
    complex(0, -1): "<",
}


def parse(fp):
    global BOUNDS
    map = {}
    start = complex(0, 0)
    end = complex(0, 0)
    for row, line in enumerate(fp):
        for col, ch in enumerate(line.strip()):
            BOUNDS = complex(row, col)
            if ch == "S":
                start = complex(row, col)
            if ch == "E":
                end = complex(row, col)
            map[complex(row, col)] = ch
    return map, start, end


def viz(game_map, pos, heading):
    for row in range(int(BOUNDS.real) + 1):
        for col in range(int(BOUNDS.imag) + 1):

            tmp = game_map[pos]
            if pos == complex(row, col):
                game_map[pos] = HEADING_VIZ[heading]

            print(game_map[complex(row, col)], end="")

            if pos == complex(row, col):
                game_map[pos] = tmp

        print()


def path_viz(game_map, path):
    game_map = dict(game_map)
    for elem in path:
        p, _ = elem
        game_map[p] = "o"

    for row in range(int(BOUNDS.real) + 1):
        for col in range(int(BOUNDS.imag) + 1):
            print(game_map[complex(row, col)], end="")
        print()


def uncomplex(c):
    return (c.real, c.imag)


def dijkstra(map, start, end):
    highscore = inf
    queue = []
    visited = {}
    heappush(queue, (0, uncomplex(start), EAST))

    while queue:
        score, pos, heading = heappop(queue)
        pos = complex(*pos)

        if score > highscore:
            return

        if (pos, heading) in visited and visited[(pos, heading)] < score:
            continue

        visited[(pos, heading)] = score

        if pos == end:
            return score

        if map[pos + dirs[heading]] != "#":
            heappush(queue, (score + 1, uncomplex(pos + dirs[heading]), heading))

        heappush(
            queue,
            (score + 1000, uncomplex(pos), (heading + 1) % len(dirs)),
        )
        heappush(
            queue,
            (score + 1000, uncomplex(pos), (heading - 1) % len(dirs)),
        )


if __name__ == "__main__":
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    with open(fname) as fp:
        map, start, end = parse(fp)
        print(dijkstra(map, start, end))
