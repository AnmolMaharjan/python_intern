
# %%

a =[]

def func1(n):
    for i in range(2,n):
        for j in range(2,i):
            if i%j == 0:
                break
            else:
                a.append(i)
                break
        

        
func1(20)
print(a)