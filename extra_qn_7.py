
# %%


z={}

for i in range(1, 11):
    y=1
    for j in range(1, i+1):
        y *= j 
    z[i] = y
print(z)
