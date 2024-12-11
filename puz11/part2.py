from functools import cache

data = tuple("475449 2599064 213 0 2 65 5755 51149".split())


@cache
def process(item):
    if item == "0":
        return ("1",)
    elif len(item) % 2 == 0:
        return (item[: len(item) // 2], str(int(item[len(item) // 2 :])))
    else:
        return (str(int(item) * 2024),)


@cache
def rblink(times, data):
    if times == 0:
        return len(data)

    return sum(rblink(times - 1, process(i)) for i in data)


if __name__ == "__main__":
    test = tuple("125 17".split())

    assert rblink(25, test) == 55312

    print(rblink(75, data))
