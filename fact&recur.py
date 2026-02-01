def fa(n):
    if n==0:
        return(1)
    return n * fa(n-1)
n=int(input('ener no:'))

#res=fa(n)
print(fa(n))