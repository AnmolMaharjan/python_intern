
import traceback

import re

# txt = "Malai yo jindagi le kaha puryayo 1 Kahile hasayo kahile ruwayo 2 Afnai sanga chhutaera eklo banayo 3 Malai yo jindagile kaha puryayo"
# x_search = re.search("^M.*o$", txt)
# x_findall = re.findall(r"o", txt)
# x_findall1 = re.findall(r"\d", txt)
# x_split = re.split(r"1|2|3", txt)
# x_sub = re.sub(r"\s","@", txt)
# x_split1 = re.split(r"@", x_sub)
# x_findall2 = re.findall("[@]", x_sub)
# # a = re.search("[a-zA-Z]",txt)
# # b = re.search('\d',txt)

# if x_search:
#     print("x pass vo.")
# else:
#     print("Timile khojeko vetiyena.")
# print(x_findall)
# print(x_findall1)
# print(x_split)
# print(x_sub)
# print(x_split1)
# print(x_findall2)

# if a:print("a pass vo")
# if b:print("b pass vo")

# a = re.findall(r"[a-zA-Z][aA]",txt)
# print(a)

# txt = "ebeeceeefjbeeejbeafleebeeecwlaeeebweelabfwheeeedjgveeeeejhejeeee"

# x = re.findall(r"[eE]+", txt)
# print(x)

# txt="John,Penny,Jane,Lenny,Jenifer,Jenny,Joan,Jqxbon,nny"

# # x=re.findall("[a-zA-Z]*nny", txt)
# x=re.findall(r"[jJ][a-zA-Z]{1,2}n", txt)
# print(x)

txt = input("Enter E-mail Address:")
# txt = "anmol.maharjan@cdts.com.np"
x = re.search(r"^[a-zA-Z0-9\._]+@[a-zA-Z]+[\.][a-zA-Z]+[[\.][a-zA-Z]*]?$", txt)

if x:
    print("valid")
else:
    print("not valid")
