
# %%

tuple = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(tuple.index(3))
x = enumerate(tuple)
for (i, tuple) in x:
    print(f'{i+1}. {tuple}')