# Write a program to swap the values of two variables using arithmetic operators.
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = a
a = a + b - a
print("swaped value is :" )
print("a :" ,a)
print("b :" ,c)