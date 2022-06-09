#Question 1

a=int(input("Enter a number you want to convert into binary: "))
print("Binary form of",a,"is: ",bin(a))

#Output 1

#Enter a number you want to convert into binary: 56
#Binary form of 56 is:  0b111000

#Question 2

num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
op=input("Enter the calculation you want to perform:(+,-,*,/):")
a=max(num1,num2)
b=min(num1,num2)
if op=="+":
    print("Sum=",a+b)
elif op=="-":
    print("Difference=",a-b)
elif op=="*":
    print("Product=",a*b)
elif op=="/":
    print("Division=",a/b)
else:
    print("Enter a proper operator.")
