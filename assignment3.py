print("QUESTION 1")
print()
# Python program to convert Decimal to Binary Number
 
number = int(input("ENTER A NUMBER : "))
 
print("the binary number is :", bin(number)[2::])  # using the inbuilt function

print()
print("QUESTION 2")
print()

choice = input('''
Please select the type of operation you want to perform:
+ for addition
- for subtraction
* for multiplication
/ for division
''')
 
num_1 = int(input('Enter your first number: '))
num_2 = int(input('Enter your second number: '))
 
if choice == '+':
    print('{} + {} = '.format(num_1, num_2))
    print(num_1 + num_2)
 
elif choice == '-':
    print('{} - {} = '.format(num_1, num_2))
    print(num_1 - num_2)
 
elif choice == '*':
    print('{} * {} = '.format(num_1, num_2))
    print(num_1 * num_2)
 
elif choice == '/':
    print('{} / {} = '.format(num_1, num_2))
    print(num_1 / num_2)
 
else:
    print('Enter a valid operator, please run the program again.')


print()
print("QUESTION 3")
print()

#question 3(a.)
#   (3+4)*5

#question 3(b.)
#   n*(n-1)/2

#question 3(c.)
#   4*math.pi*r**2

#question 3(d.)
#   math.sqrt(r*(math.cos(a))**2+r*(math.sin(a))**2)

#question 3(e.)
#   (y2-y1)/(x2-x1)

print()
print("QUESTION 4")
print()

for i in range(5):
    print(i, end=" ")
print()
 
for i in range(3, 10):
    print(i, end=" ")
print()
 
for i in range(4, 13, 3):
    print(i, end=" ")
print()

for i in range(15, 5, -2):
    print(i, end=" ")
print()

for i in range(5, 3):
    print(i, end=" ")
print()

print()
print("QUESTION 5")
print()
atom1=int(input("Carbon Atoms -> "))
atom2=int(input("Hydrogen Atoms -> "))
atom3=int(input("Oxygen Atoms -> "))

print("The Molecular weight of the compound is -> ",atom1*1.00794+atom2*12.0107+atom3*15.9994)
