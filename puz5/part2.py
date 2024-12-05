from collections import defaultdict

rules = defaultdict(set)


def is_out_of_order(update):
    for idx, v in enumerate(update):
        before = set(update[:idx])

        # if there is any intersection of the rule for v
        # and before, that means that this is out of order
        # since v has to appear before the items in the rules
        if before.intersection(rules[v]):
            return True
    return False


def fix(update):
    while is_out_of_order(update):
        for idx, v in enumerate(update):
            before = update[:idx]

            # find the first item in the before list that v needs to appear
            # prior to and move v in front of it
            for bidx, i in enumerate(before):
                if i in rules[v]:
                    update.pop(idx)
                    update.insert(bidx, v)
                    break

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
            if not is_out_of_order(update):
                continue

            answer += fix(update)
    print(answer)
