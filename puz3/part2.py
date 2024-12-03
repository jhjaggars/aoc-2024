import re

do_pat = re.compile(r"do\(\)")
dont_pat = re.compile(r"don't\(\)")
pat = re.compile(r"mul\((\d+),(\d+)\)")


def extract_product(puzzle_input):
    s = 0
    for m in pat.finditer(puzzle_input):
        product = int(m.group(1)) * int(m.group(2))
        s += product
    return s


if __name__ == "__main__":
    with open("input.txt") as fp:
        puzzle_input = fp.read()

    start = 0
    matching = True
    buf = []

    while start < len(puzzle_input):
        if matching:
            m = dont_pat.search(puzzle_input, start)
            if m:
                buf.append(puzzle_input[start : m.start()])
                matching = False
                start = m.end()
            else:
                buf.append(puzzle_input[start:])
                break
        else:
            m = do_pat.search(puzzle_input, start)
            if m:
                start = m.end()
                matching = True
            else:
                break

    print(extract_product("".join(buf)))
