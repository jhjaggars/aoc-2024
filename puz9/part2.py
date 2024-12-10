from collections import namedtuple

File = namedtuple("File", ["fid", "loc", "size"])
Space = namedtuple("Space", ["loc", "size"])


def prep(data):
    free = []
    files = []

    fid = 0
    loc = 0
    for idx, v in enumerate(data):
        size = int(v)
        if idx % 2 != 0:
            free.append(
                Space(
                    loc,
                    size,
                )
            )
        else:
            files.append(File(fid, loc, size))
            fid += 1
        loc += size

    return free, files, [-1] * (loc + 1)


def checksum(disk):

    checksum = 0
    for blk, fid in enumerate(disk):
        if fid > -1:
            checksum += blk * fid
    return checksum


def write(file, disk):
    for offset in range(file.size):
        disk[file.loc + offset] = file.fid


def test(data):
    free, files, disk = prep(data)

    for file in reversed(files):
        for idx, space in enumerate(free):
            if space.loc > file.loc:
                # went too far write it where it stands
                write(file, disk)
                break

            if space.size >= file.size:
                # found a spot
                new_size = space.size - file.size
                free[idx] = Space(loc=space.loc + file.size, size=new_size)
                write(File(fid=file.fid, loc=space.loc, size=file.size), disk)
                break
        else:
            write(file, disk)

    return checksum(disk)


if __name__ == "__main__":
    # print(test("714892711") == 813)
    # print(test("12101") == 4)
    # print(test("12345") == 132)
    # print(test("233313312141413140211") == 2910)
    # print(test("1313165") == 169)
    # print(test("80893804751608292") == 1715)

    with open("small.txt") as fp:
        raw = fp.read().strip()

    # print(test(raw) == 2858)

    with open("input.txt") as fp:
        raw = fp.read().strip()

    print(test(raw))
