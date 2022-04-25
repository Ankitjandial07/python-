#Question 1

a=float(input("Enter 1st number : "))
b=float(input("Enter 2nd number : "))
c=float(input("Enter 3rd number : "))
print("Average of the numbers : ",(a+b+c)/3)


#output

#Enter 1st number : 7
#Enter 2nd number : 7
#Enter 3rd number : 7
#Average of the numbers :  7.0




#Question 2

a=int(input("Enter Gross Income : "))
b=int(input("Enter the number of dependents :"))
c=a-10000-(3000*b)
d=c*0.2
print("Tax to be paid : ",d)


#output

#Enter Gross Income : 500000
#Enter the number of dependents :3
#Tax to be paid :  96200.0



#Question 3

a=str(input("Enter the name of the person : "))
b=int(input("Enter the age of the person : "))
c=float(input("Enter the marks obatined by the person : "))
d=str(input("Enter the name of the course peson wants to take : "))
e=int(input("Enter the SID of the students : "))
f=[a,b,c,d,e]
print("Information about the person :",f)



#output

#Enter the name of the person : abc
#Enter the age of the person : 16
#Enter the marks obatined by the person : 89.8
#Enter the name of the course peson wants to take : civil
#Enter the SID of the students : 2110215675
#Information about the person : ['abc', 16, 89.8, 'civil', 2110215675]



#Question 4


a=int(input("Enter the marks of 1st student : "))
b=int(input("Enter the marks of 2nd student : "))
c=int(input("Enter the marks of 3rd student : "))
d=int(input("Enter the marks of 4th student : "))
e=int(input("Enter the marks of 5th student : "))
f=[a,b,c,d,e]
print("Marks of the students : ",f)
f.sort()
print("Marks of the students in the sorted manner : ",f)




#output

#Enter the marks of 1st student : 94
#Enter the marks of 2nd student : 75
#Enter the marks of 3rd student : 78
#Enter the marks of 4th student : 35
#Enter the marks of 5th student : 41
#Marks of the students :  [94, 75, 78, 35, 41]
#Marks of the students in the sorted manner :  [35, 41, 75, 78, 94]



#Question 5


a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
a.pop(3)
print(a)


#output

#['Red', 'Green', 'White', 'Pink', 'Yellow']


b=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
b=["Purple" if(i=="Black")or(i=="Pink")else i for i in b]
print(b)


#Output

#['Red', 'Green', 'White', 'Purple', 'Purple', 'Yellow']



