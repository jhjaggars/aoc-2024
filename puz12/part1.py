import sys

dirs = (
    complex(0, 1),
    complex(1, 0),
    complex(0, -1),
    complex(-1, 0),
)


def parse(fp):
    data = {}
    for row, line in enumerate(fp):
        for col, ch in enumerate(line.strip()):
            data[complex(row, col)] = ch
    return data


def test(data, cell, seen):
    perimeters = 0
    area = 1
    val = data[cell]
    seen.add(cell)
    for dir in dirs:

        pdir = cell + dir

        # grid boundary, increment perimeter of cell
        if pdir not in data:
            perimeters += 1
            continue

        peek = data[pdir]
        # already processed this cell
        if pdir in seen:
            continue

        # flood to the cell
        if peek == val:
            p, v = test(data, pdir, seen)
            perimeters += p
            area += v
        else:  # another plot type, incr perimeters
            perimeters += 1

    return perimeters, area


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
            p, a = test(data, cell, seen)
            # print(f"{cv=} {p=} {a=}|{seen=} {all_seen=}")
            all_seen = all_seen.union(seen)
            total += p * a
        print(total)
