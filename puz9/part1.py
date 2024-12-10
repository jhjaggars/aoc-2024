# with open("small.txt") as fp:
with open("input.txt") as fp:
    data = [int(ch) for ch in fp.read().strip()]

# field id starting from the left
fid = 0
# field id starting from the right
rfid = len(data) // 2


# logical file block being written
block = 0

# running checksum of file blocks
# field * block
checksum = 0

# pointers to the data
idx = 0
ridx = len(data) - 1

# if idx equals the ridx then I'm done


def right_generator(data):
    global ridx
    global rfid
    while ridx > 0:
        while data[ridx] > 0:
            # print(f"{data[ridx]=} yielding {rfid} from {ridx}")
            data[ridx] -= 1
            yield rfid, ridx
        rfid -= 1
        ridx -= 2


right = right_generator(data)

viz = []

print(data)
while True:
    while data[idx] > 0:
        # print(f"{data[idx]=} yielding {fid} from {idx}")
        checksum += fid * block
        viz.append(fid)
        data[idx] -= 1
        block += 1
    fid += 1

    if idx > ridx:
        break

    # fill free space
    while data[idx + 1] > 0:
        try:
            rfid, ridx = next(right)
            checksum += rfid * block
            viz.append(rfid)
            data[idx + 1] -= 1
            block += 1
        except StopIteration:
            break

    idx += 2

    if ridx < idx:
        break

print(block, checksum)
# print(viz)
