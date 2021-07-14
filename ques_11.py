def break_into_word(sentence):
    a=[]
    b=""
    for i in sentence:
        if i==" ":
            a.append(b)
            b=" "
        else:
            b=b+1
    if b:
        a.append(b)
    print(a)
break_into_word("Navgurukul is an alternative to higher education reducing the barries of currnt formal education system")