import sys
import numpy as np


def parse(line):
    p, v = line.split()
    p = complex(*[int(x) for x in p.split("=")[1].split(",")])
    v = complex(*[int(x) for x in v.split("=")[1].split(",")])
    return p, v


def viz(arr):
    for r in np.transpose(arr):
        row = [" " if x == 0 else chr(215) for x in r]
        print("".join(row))


if __name__ == "__main__":
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    bounds = {"input.txt": complex(101, 103), "small.txt": complex(11, 7)}
    b = bounds[fname]
    A = np.zeros((int(b.real), int(b.imag)))
    robots = []
    sec = 6200
    with open(fname) as fp:
        for idx, line in enumerate(fp):
            (p, v) = parse(line)
            p = p + (v * sec)
            p = complex(p.real % b.real, p.imag % b.imag)
            robots.append((p, v))
            A[int(p.real), int(p.imag)] = 1

    viz(A)
    input()

    while True:
        A = np.zeros((int(b.real), int(b.imag)))
        for idx, (p, v) in enumerate(robots):
            p = p + v
            p = complex(p.real % b.real, p.imag % b.imag)
            robots[idx] = (p, v)
            A[int(p.real), int(p.imag)] = idx

        sec += 1
        viz(A)
        print(sec)
        input()

    # take 100 seconds of steps
    # t = p + (v * 100)
    # wrap
    # t = complex(t.real % b.real, t.imag % b.imag)
    # nw
    # if t.real < hmid and t.imag < vmid:
    # quadrants[0] += 1
    # sw
    # elif t.real < hmid and t.imag > vmid:
    # quadrants[1] += 1
    # se
    # elif t.real > hmid and t.imag < vmid:
    # quadrants[2] += 1
    # ne
    # elif t.real > hmid and t.imag > vmid:
    # quadrants[3] += 1

    # print(functools.reduce(operator.mul, quadrants, 1))
