import pprint
from dataclasses import dataclass
from collections import defaultdict
from itertools import combinations

antennas = defaultdict(list)


@dataclass
class Location:
    x: int
    y: int

    def in_bounds(self, mxx, mxy, mnx=0, mny=0):
        return mnx <= self.x <= mxx and mny <= self.y <= mxy

    def __hash__(self):
        return hash((self.x, self.y))


def get_antinodes(a: Location, b: Location, bounds):
    rise = b.y - a.y
    run = b.x - a.x

    antinodes = set([a, b])

    proposed = Location(b.x + run, b.y + rise)
    while proposed.in_bounds(bounds[0], bounds[1]):
        antinodes.add(proposed)
        proposed = Location(proposed.x + run, proposed.y + rise)

    proposed = Location(a.x - run, a.y - rise)
    while proposed.in_bounds(bounds[0], bounds[1]):
        antinodes.add(proposed)
        proposed = Location(proposed.x - run, proposed.y - rise)

    return antinodes


if __name__ == "__main__":
    mxx = 0
    mxy = 0
    map = []
    with open("input.txt") as fp:
        # with open("small.txt") as fp:
        # with open("simple.txt") as fp:
        for y, line in enumerate(fp):
            mxy = y
            map.append(list(line.strip()))
            for x, ch in enumerate(line.strip()):
                mxx = x
                if ch != ".":
                    antennas[ch].append(Location(x, y))

    antinodes = set()
    for freq, antenna_set in antennas.items():
        for a, b in combinations(list(antenna_set), 2):
            for n in get_antinodes(a, b, (mxx, mxy)):
                map[n.y][n.x] = "#"
                antinodes.add(n)

    # pprint.pprint(antennas)
    # pprint.pprint(antinodes)
    # for row in map:
    #     print(" ".join(row))
    print(len(antinodes))
