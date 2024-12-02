def test(values):
    # if step is positive, then it should be sorted postive
    # otherwise it should be sorted negative
    dir = 1 if values[1] - values[0] > 0 else -1
    
    for l, r  in zip(values[:-1], values[1:]):

        if r > l and dir == -1:
            return 0

        if r < l and dir == 1:
            return 0

        if abs(r - l) < 1 or abs(r - l) > 3:
            return 0

    return 1
        

if __name__ == "__main__":
    with open("input.txt") as fp:
        print(sum(test([int(v) for v in line.split()]) for line in fp))
