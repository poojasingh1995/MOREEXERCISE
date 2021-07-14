i=0
while i<=1000:
    if i%3==0 and i%7==0 and i%21==0:
        print(i,"navgurukul")
    elif i%3==0:
        print(i,"nav")
    elif i%7==0:
        print(i,"gurukul")
    else:
        print(i)
    i=i+1