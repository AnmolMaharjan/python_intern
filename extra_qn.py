
# %%

x = set(range(1, 100))
y = []
for k in x:
    if k % 2 == 0:
        y.append(k//2)
    else:
        y.append(k*2)
print(y)