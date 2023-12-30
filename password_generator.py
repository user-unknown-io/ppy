from string import (
    digits,
    punctuation,
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase
)

def GenPwd(l:int)->str:
     from random import choice
     asc = digits + punctuation + ascii_letters + ascii_uppercase + ascii_lowercase
     nwd:str = ""
     for i in range(l):
          a = choice(asc)
          nwd = nwd + a

     return nwd


a = GenPwd(40)
print(a)
