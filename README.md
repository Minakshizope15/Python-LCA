print("To find the largest number")
a=float(input("Enter first number a:"))
b=float(input("Enter second number b:"))
c=float(input("enter third number c:"))

if a==b==c:
   print("all are equal")
elif a==b and a>c:
   largest=a and b
   else largest=c 
elif b==c and b>a:
   largest=b and c
   else largest=a
elif c==a and c>b
  largest=c and b 
  else largest=b
if a>b and a>c
   largest=a
elif b>c and b>a
   largest=b
elif c>a and c>b
   largest=c
print("largest number is:", largest)

  
