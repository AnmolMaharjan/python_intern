
# %%

a =[]


def func(n):
    i=2
    while True:
        
        prime = True
        
        for j in range(2,i):
            if i%j == 0:
                prime = False
                break
        if prime:
            a.append(i)
        if a.__len__() == n:
            break
        i +=1
        
func(5)
print(a)
