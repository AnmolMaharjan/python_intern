
# %% 

odd_even = lambda x: 'Even' if x%2 == 0 else 'Odd'
print(odd_even(3))
print(odd_even(6))

# %%

l = [1,2,3,4,5]

d = lambda a:[x**2 for x in l]
print(d(l))