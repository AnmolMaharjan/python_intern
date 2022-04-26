
# %%
name = "Anmol Maharjan"
age = 26
full_name="I am Anmol Maharjan"
describe = 'He said,"I am Anmol Maharjan".'
essay = '''Strings are iterable set of characters enclosed within single-quotation marks '' or double-quotation marks. Multiline strings are enclosed with triple single-quotation marks  or triple double-quotation marks . Strings are generally immutable, but when we try to change the value of string to a variable, a completely new object is created and assigned to the variable. With strings created with single quotes ', we can use double quote" inside it without any escape characters. Some of the examples of strings are as follows:'''
print(essay)

# %%

content_1='first line.\nsecond line.'
print(content_1)
content_2='Everyone say,"I\'m a good guy". '
print(content_2)

# %%

first_name='Anmol'
last_name='Maharjan'
full_name=first_name + last_name
print(full_name)
print(full_name.__len__())

# %%

text='capitalization is the process of capitalizing the first character of the string'
print(text.capitalize())
text2=text.upper()
print(text2)
print(text2.lower())

# %%

name='Anmol'
age=16
print('My name is %s'%name)
print('I\'m %s & I\'m %d years old'%(name,age))
print('the value is:%10.3f'%12.345)
print("Hi {}, how're you doing? Are you {} now?".format(name,age))
print("Hi {n}, is the value {pi:10.2f}?".format(n=name,pi=3.1415))

# %%

hobbies='\n\n1.\tsinging\n2.\tdancing\n3.\tcoding'
print(hobbies)
first_name='Dawood'
last_name='Ibrahim'
full_name=first_name + " " + last_name
print(full_name)
print(full_name.__len__())

# %%

x='11'
y='12.23'
print(x.isdecimal())
print(y.isdecimal())