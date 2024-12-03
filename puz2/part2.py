def without(lst, idx):
    cp = lst[:]
    cp.pop(idx)
    return cp


def test(values, retry):
    # print(values, retry)
    if retry < 0:
        return 0
    # if step is positive, then it should be sorted postive
    # otherwise it should be sorted negative
    dir = 1 if values[1] - values[0] > 0 else -1
    x, y = 0, 1

    while y < len(values):
        l, r = values[x], values[y]

        if (
            (r > l and dir == -1)
            or (r < l and dir == 1)
            or (abs(r - l) < 1 or abs(r - l) > 3)
        ):
            return min(
                1,
                retry * test(without(values, x), retry - 1)
                + test(without(values, y), retry - 1)
                + test(without(values, x - 1), retry - 1),
            )

        x, y = x + 1, y + 1

    return 1


if __name__ == "__main__":

    # values = [4, 2, 3, 5, 7]
    # r = test(values, 1)
    # print(r)

    with open("input.txt") as fp:
        safe = 0
        for line in fp:
            values = [int(v) for v in line.split()]
            r = test(values, 1)
            # print(values, r)
            safe += r
        print(safe)
