def lot():
    s=input("Enter the string")
    x=s.split(sep=";")
    a=[]
    for i in x:
        y=i.split(sep="=")
        a.append(y)
    A=[]
    for i in a:
        x=tuple(i)
        A.append(x)
    return(A)
ca2lot=lot()
print(ca2lot)
