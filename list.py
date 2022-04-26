
# %%

list_1=[10,11,12,13,14,15,16,17,18,19]
list_2=['aadvsdv','adcvsdd','fbsvgsdv','adda','gdgn','dfbgd','anhffgb','ijhfnh','sfgfb','gbb']
list_3=[1,'sfbdfb',2,'fhnh',3,'klkh',4,'sdf',5,'yukghn']
list_4=[
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j'
    ]
print(list_1)
print(list_2[0])
print(list_3[4])
print(list_4)
print(list_2[-1])
print(list_2[-5])
print(list_2[2:6])
print(list_2[1:])
print(list_2[:1])
print(list_2.__len__())

# %%

#updating the value of list
list_1[0]=20
list_1[2:4]=[18,20]
list_3.append("4")
list_4.insert(3,'k')
list_4.remove('a')
list_4_=['l','m','n']
list_4.extend(list_4_)
list_3.clear()
list_5=list_1.copy
list_2.sort()
list_4.reverse()
list_4.index('d')
list_4.index('d')
list_4.count('d')

# %%

x=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
xx=[
    [[1,2],[3,4]],
    [[5,6],[7,8]],
]
print(x[0][0])
print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_5)

# %%

r = [[[(x+a+b)for b in range(3)]for a in range(3)] for x in range(5)]
r=[[(x+a)for x in range(2)]for a in range(2)]
print(r)

# %%

arr=[]
for x in range(3):
    tmp=[]
    for y in range(3):
        tmp_2=[]
        for z in range(3):
            tmp_2.append(x+y+z)
        tmp.append(tmp_2)
    arr.append(tmp)
print(arr)

# %%

x=[]
for a in range(5):
    x.append(a)
print(x)