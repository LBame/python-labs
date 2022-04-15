#lab 1.1 
#var 8 Islamov

a=int(input('the byte size a = '))
b,ost = divmod(a,1024)
c,ost=divmod(b,1024)
print("size = ",b , "Kb" )
print("size = ",c , "Mb" )
