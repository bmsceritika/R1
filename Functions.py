def data():
	sname=input("Enter the servername")
	dbname=input("Enter the Dbname")
	uname=input("Enter your username")
	passw=input("Enter your password")
	a="servername="+sname+";"+"dbname="+dbname+";"+"userername="+uname+";"+"password="+passw
	return(a)
Data=data()
print(Data)
