# https://www.youtube.com/watch?v=jBsC34PxzoM
# https://www.chilimath.com/lessons/advanced-algebra/cramers-rule-with-two-variables/

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
                int(x.split("=")[1]) + 10000000000000,
                int(y.split("=")[1]) + 10000000000000,
            )

    yield a_button, b_button, target


def ugg_math(target, a, b):
    det = a.real * b.imag - a.imag * b.real
    calc_a = int((target.real * b.imag - target.imag * b.real) // det)
    calc_b = int((a.real * target.imag - a.imag * target.real) // det)
    if (
        complex(a.real * calc_a + b.real * calc_b, a.imag * calc_a + b.imag * calc_b)
        == target
    ):
        return calc_a * 3 + calc_b
    return 0


if __name__ == "__main__":
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    with open(fname) as fp:
        gen = parse(fp.readlines())

    total = 0
    for a, b, target in gen:
        total += ugg_math(target, a, b)
    print(total)
