data = "475449 2599064 213 0 2 65 5755 51149"


def process(item):
    if item == "0":
        yield "1"
    elif len(item) % 2 == 0:
        yield item[: len(item) // 2]
        yield str(int(item[len(item) // 2 :]))
    else:
        yield str(int(item) * 2024)


def blink(times, data):
    data = data.split()
    for _ in range(times):
        tmp = []
        for item in data:
            for output in process(item):
                tmp.append(output)
        data = tmp
        # print(data)
        # input()
    return len(data)


if __name__ == "__main__":
    test = "125 17"

    assert blink(25, test) == 55312

    print(blink(25, data))
