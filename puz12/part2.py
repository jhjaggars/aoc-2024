import sys

hdirs = (complex(0, 1), complex(0, -1))
vdirs = (complex(1, 0), complex(-1, 0))
dirs = hdirs + vdirs


def parse(fp):
    data = {}
    for row, line in enumerate(fp):
        for col, ch in enumerate(line.strip()):
            data[complex(row, col)] = ch
    return data


def test(data, cell, seen, perimeters):
    area = 1
    seen.add(cell)
    for dir in dirs:

        pdir = cell + dir

        # grid boundary, increment perimeter of cell
        if pdir not in data:
            perimeters.add((cell, pdir))
            continue

        # already processed this cell
        if pdir in seen:
            continue

        # another plot type, incr perimeters
        if data[pdir] != data[cell]:
            perimeters.add((cell, pdir))
            continue

        area += test(data, pdir, seen, perimeters)

    return area


def trace(cell, adjacent, dir, perimeters):
    traced = (cell + dir, adjacent + dir)

    if traced not in perimeters:
        return

    perimeters.remove(traced)
    trace(cell + dir, adjacent + dir, dir, perimeters)


def calculate_walls(perimeters):
    walls = 0
    while perimeters:
        perimeter = perimeters.pop()
        cell, adjacent = perimeter
        walls += 1
        # real is the row
        # imag is the col
        dirs = vdirs if cell.real == adjacent.real else hdirs
        for dir in dirs:
            trace(cell, adjacent, dir, perimeters)

    return walls


if __name__ == "__main__":
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    with open(fname) as fp:
        data = parse(fp)
        total = 0
        all_seen = set()
        for cell in data:
            cv = data[cell]
            if cell in all_seen:
                continue
            seen = set()
            perimeters = set()
            area = test(data, cell, seen, perimeters)
            all_seen = all_seen.union(seen)
            walls = calculate_walls(perimeters)
            total += walls * area
        print(total)
