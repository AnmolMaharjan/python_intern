
# %%

from unittest import result



l = [1, 2, 3, -3, -5, 7, 6, -4, 8, -8]
nl = []
for (i, v) in enumerate(l):
    for x in l[i + 1:]:
        ts = x + v
        for n in l:
            if ts + n == 0:
                nl = [*nl, [v, x, n]]
print(nl)

