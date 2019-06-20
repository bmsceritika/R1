def lot(s):
    a=[]
    for i in s.split(sep=";"):
        a.append(tuple(i.split(sep="=")))
    return(a)
str=input("Enter the string")
ca2lot=lot(str)
print(ca2lot)
               
