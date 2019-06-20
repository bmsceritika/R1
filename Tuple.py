def lot():
    s=input("Enter the string")
    A=[]
    for i in s.split(sep=";"):
        A.append(tuple(i.split(sep="=")))
    return(A)
ca2lot=lot()
print(ca2lot)
               
