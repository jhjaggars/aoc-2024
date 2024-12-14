import sys
import functools
import operator


def parse(line):
    p, v = line.split()
    p = complex(*[int(x) for x in p.split("=")[1].split(",")])
    v = complex(*[int(x) for x in v.split("=")[1].split(",")])
    return p, v


if __name__ == "__main__":
    fname = "input.txt" if len(sys.argv) < 2 else sys.argv[1]
    bounds = {"input.txt": complex(101, 103), "small.txt": complex(11, 7)}
    with open(fname) as fp:
        b = bounds[fname]
        hmid = b.real // 2
        vmid = b.imag // 2
        quadrants = [0] * 4
        for line in fp:
            p, v = parse(line)
            # take 100 seconds of steps
            t = p + (v * 100)
            # wrap
            t = complex(t.real % b.real, t.imag % b.imag)
            # nw
            if t.real < hmid and t.imag < vmid:
                quadrants[0] += 1
            # sw
            elif t.real < hmid and t.imag > vmid:
                quadrants[1] += 1
            # se
            elif t.real > hmid and t.imag < vmid:
                quadrants[2] += 1
            # ne
            elif t.real > hmid and t.imag > vmid:
                quadrants[3] += 1

        print(functools.reduce(operator.mul, quadrants, 1))
