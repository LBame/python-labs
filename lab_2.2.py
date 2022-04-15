#lab 2.2 
#var 8 Islamov

a=int(input( 'enter a five-digit number a ='))
b,ost= divmod(a,10000)
c= a-(b*10000)
a =c*10+b
print("the resulting number a =",a)
