import sys
from collections import Counter

l_list = []
r_list = []
for line in sys.stdin:
    l, r = line.split()
    l_list.append(int(l))
    r_list.append(int(r))

r_counter = Counter(r_list)
l_list.sort()
r_list.sort()

diff = sum(abs(y -x) for x, y in zip(l_list, r_list))
sim_score = sum(x * r_counter.get(x, 0) for x in l_list)

print(diff)
print(sim_score)
