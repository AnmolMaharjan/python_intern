
# %%

x = ['atanasoff', 'berry', 'computer', ]
y = {}
# {
#   'atanasoff': 9,
#   'berry': 5,
#   'computer': 8
# }

# for i in x:
#     y[i]= i.__len__()
print({i: i.__len__() for i in x})