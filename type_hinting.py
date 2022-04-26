

import math
from typing import Dict, List

# %%

a6: int = 5
x6: str = 'abcde'
b6: float = 12.34
print(b6, type(b6))

# %%

c6: str = 'fghij klmno'
d6: list = [1, 2, 3, 4, 5, 'abc']
print(d6)

# %%

e6: tuple = (1, 2, 3)
print(type(e6))

# %%

f6: List['int'] = [5, 2]
print(f6)

# %%

g6: List = ['cde', 11]
h6: Dict[str, str] = {'k': 'v'}
print(h6)

# %%

def add_int(x, y):
    return(math.floor(x)+y)


print(add_int(5, 6))