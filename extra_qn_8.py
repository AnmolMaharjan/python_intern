
# %%

z={}

def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)


# fact(10)
print({i: fact(i) for i in range(1, 11)})
