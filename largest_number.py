print("To find the largest number")
a = float(input("Enter first number a: "))
b = float(input("Enter second number b: "))
c = float(input("Enter third number c: "))

if a == b == c:
    print("All are equal")

elif a == b and a > c:
    largest = a

elif b == c and b > a:
    largest = b

elif c == a and c > b:
    largest = c

if a > b and a > c:
    largest = a

elif b > c and b > a:
    largest = b

else:
    largest = c

print("Largest number is:", largest)

  
