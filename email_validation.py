import re

email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email=input("enter your email please :")
if re.search(email_condition,email):
    print("Right email")
else:
    print("Wrong email")
    