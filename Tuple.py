def lot():
    s=input("Enter the string")
    x=s.split(sep=";")
    A=[]
    for i in x:
        A.append(tuple(i.split(sep="=")))
    return(A)
ca2lot=lot()
print(ca2lot)
               
