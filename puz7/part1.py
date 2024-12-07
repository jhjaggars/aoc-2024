import itertools
import operator


def calc(operators, operands):
    acc = operators[0](operands[0], operands[1])
    for op, nd in zip(operators[1:], operands[2:]):
        acc = op(acc, nd)
    return acc


if __name__ == "__main__":
    result = 0
    # with open("small.txt") as fp:
    with open("input.txt") as fp:
        for line in fp:
            target, operands = line.strip().split(":")

            target = int(target)
            operands = [int(o) for o in operands.split()]
            print(f"{target} <- {operands}")

            slots = len(operands) - 1
            ops = list(itertools.product((operator.add, operator.mul), repeat=slots))
            for op_set in ops:
                v = calc(op_set, operands)
                print(f"{op_set} -> {v}")
                if v == target:
                    result += target
                    break

    print(result)
