def mdc(a: int, b: int) -> int:
    if a ==0 or b==0:
        return min(a,b)
    if a==b:
        return a
    elif a==1 or b==1:
        return min(a,b)
    else:
        return mdc(b, abs(a-b))

print(mdc(24,9))    

