
# %%

m = [1, 2, 3, 4, 5]
j = []


for i in m:
    k = int(i) ** 2
    j.append(k)
# or
print([k ** 2 for k in m])

print(sum(j))