import re

char_8=re.compile(r'.{8,}')
upper_char=re.compile(r'[A-Z]')
lower_char=re.compile(r'[a-z]')
digit=re.compile(r'[0-9]')

password=str(input("Enter a password to check wether it is strong or not:"))

charcheck=char_10.search(password)
uppercheck=upper_char.search(password)
lowercheck=lower_char.search(password)
digitcheck=digit.search(password)



if (charcheck and uppercheck and lowercheck and digitcheck):
    print("Your password is strong")
else:
    print("Your password is not strong. Try to change")
    
