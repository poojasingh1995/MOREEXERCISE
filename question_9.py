password=input("enter password")
if len(password)>=6 and len(password)<=16:
    if "$" in password:
        if "2" or "8"in password:
            print(password,"strong password")
        else:
            print(password,"weak password")
    else:
        print(password,"weak password")
else:
    print(password,"weak password")