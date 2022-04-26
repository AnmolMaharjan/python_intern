
# %%

from calendar import different_locale


rich: set = {'USA', 'China', 'Japan', 'Germany', 'France', 'Austarlia', 'Italy', 'Nepal'}
europe: set = {'Germany', 'France', 'England', 'Switzerland', 'Italy', 'Portugal', 'Sweden'}

print(rich-europe)
print(europe-rich)
print(rich & europe)
print(rich-europe ^ europe-rich)
print(rich | europe)

print(rich.isdisjoint(europe))

rich.difference_update(europe)
print(rich.isdisjoint(europe))