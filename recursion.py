def fac (a):
    if(a==1 or a==0):
        return 1
    else:
        return a*fac(a-1)
print(fac(5))    