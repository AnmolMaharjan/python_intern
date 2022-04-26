
# %%

def s_add(x11, y11):
    return x11+y11


print(s_add(3, 4))

# %%

print("Aashish", end=' ---> ')
print("Roshan")
print("Aashish", "Mohammad", "Roshan", sep=' > ')

# %%

# empty function


def ss():
    pass

# %%


def add(x, y, z=0):
    return x + y + z


print(add(2, 3))

# %%


def a(d, b, c):
    data = {
        'd1':
        {
            'f':
            {
                'g': 'h1',
                'i': 'j1',
                'k': 'l1'
            },
            'm':
            {
                'n': 'o1',
                'p': 'q1',
                'r': 's1'
            },
            't':
            {
                'u': 'v1',
                'w': 'x1',
                'y': 'z1'
            }
        },
        'd2':
        {
            'f':
            {
                'g': 'h2',
                'i': 'j2',
                'k': 'l2'
            },
            'm':
            {
                'n': 'o2',
                'p': 'q2',
                'r': 's2'
            },
            't':
            {
                'u': 'v2',
                'w': 'x2',
                'y': 'z2'
            }
        }
    }
    return data[d][b][c]


# print([d][b][c])

aaa = 'd1'
print(a(aaa, 't', 'u'))


# %%

def aldjbhcdgkvkdsjbc(x,y):
    return x*y

g=aldjbhcdgkvkdsjbc
g(2,3)

# %%