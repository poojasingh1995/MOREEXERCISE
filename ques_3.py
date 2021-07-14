def is_harshad_number(num):
    x=num
    x_digits=list(str(x))
    i=0
    sum=0
    while i<len(x_digits):
        a=int(x_digits[i])
        sum=sum+a
        i=i+1
    if num%sum==0:
        return"true"
    else:
        return"false"
result=is_harshad_number(42)
print(result)
