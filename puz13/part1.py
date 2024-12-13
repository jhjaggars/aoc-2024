import sys


def parse_plus(line):
    _, r = line.split(":")
    x, y = r.split(",")
    return complex(int(x.split("+")[1]), int(y.split("+")[1]))


def parse(lines):
    a_button = None
    b_button = None
    target = None
    for line in lines:
        if line.strip() == "":
            yield a_button, b_button, target
        elif line.strip().startswith("Button A"):
            a_button = parse_plus(line)
        elif line.strip().startswith("Button B"):
            b_button = parse_plus(line)
        elif line.strip().startswith("Prize"):
            x, y = line.split(":")[1].split(",")
            target = complex(
                int(x.split("=")[1]),
                int(y.split("=")[1]),
            )

    yield a_button, b_button, target


if __name__ == "__main__":
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    with open(fname) as fp:
        gen = parse(fp.readlines())

    total = 0
    for a, b, target in gen:
        solutions = []
        for i in range(100):
            for j in range(100):
                if a * i + b * j == target:
                    solutions.append(i * 3 + j)
        if solutions:
            total += min(solutions)
    print(total)
