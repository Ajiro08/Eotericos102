p = float(input ('what is p'))
r = float(input('what is r'))
t = float(input('what is t'))


a = p*(1.0+(r/100.0)*t)
print(a)

#project 1 subsection b
p = float(input(' what is p:'))
r = float(input('what is r:'))
n = float(input('what is n:'))
t = float(input("what is t:"))
nt = float(input("what is nt:"))
A = p*(1+r/n)**nt

print(A)


# subsection 3
p = float(input('what is p:'))
m = float(input('what is m:'))
r = float(input('what is r:'))
n = float(input('what is n:'))
nt = float(input("what is nt:"))
t = float(input('what is t:'))
A = p*m*t*((1+r/n)**(nt)-1)/(r/n)
print(A)