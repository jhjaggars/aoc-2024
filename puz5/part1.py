from collections import defaultdict

rules = defaultdict(set)


def test(update):
    for idx, v in enumerate(update):
        before = set(update[:idx])
        # after = set(update[idx + 1 :])

        # if there is any intersection of the rule for v
        # and before, that means that this is out of order
        # since v has to appear before the items in the rules
        if before.intersection(rules[v]):
            return 0

    # return the middle one? weird
    return int(update[len(update) // 2])


if __name__ == "__main__":

    with open("rules.txt") as fp:
        for line in fp:
            l, r = line.strip().split("|")
            rules[l].add(r)

    answer = 0
    with open("input.txt") as fp:
        for line in fp:
            update = line.strip().split(",")
            answer += test(update)
    print(answer)
