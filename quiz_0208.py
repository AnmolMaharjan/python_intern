
# %%

multi = [
    [12,52,37],
    [46,51,16],
    [71,82,39]
]
print(multi[1][1])
print(multi[-1][-2])

multi.append([40,61,10])
print(multi)

for x in multi:
    for y in x:
        print(y, end=' ')

multi.clear()
print(multi)