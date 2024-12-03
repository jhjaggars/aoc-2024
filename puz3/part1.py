import re

pat = re.compile(r"mul\((\d+),(\d+)\)")

if __name__ == "__main__":
    with open("input.txt") as fp:
        puzzle_input = fp.read()

    s = 0
    for m in pat.finditer(puzzle_input):
        product = int(m.group(1)) * int(m.group(2))
        s += product

    print(s)
