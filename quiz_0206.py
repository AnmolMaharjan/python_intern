
# %%

my_list = []
my_list.append(5)
my_list.append(9)

print(my_list)

a=int(input('Enter the number:'))
my_list.append(a)
print(my_list)

more_items = [
    2,
    3,
    4
]
my_list.extend(more_items)
print(my_list)
ass=my_list.__len__()
print(f'The length of the list is {ass}')
my_list.pop(1)
print(my_list)