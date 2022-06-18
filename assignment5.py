#21102077
#Vishwash Shukla

#question-1
string=input("Enter the the string :")
print(string[::-1])
 

#question-2
x=int(input("Enter the minimum value :"))
y=int(input("Enter the maximum value: "))
num=int(input("Enter the number for divisibility check :"))
i=x
while i<=y:
    if i%num==0 :
        print(i)
    i+=1

#question-3
a=float(input("Enter the length of side:"))
b=float(input("Enter the length of side:"))
c=float(input("Enter the length of side:"))
if a+b>c and a+c>b and b+c>a :
    s=(a+b+c)/2
    ar_tri=(s*(s-a)*(s-b)*(s-c))**(0.5)
    print(ar_tri)
else :
    print("Error")

#question-4
n=int(input("Enter the no. of rows :"))
t=(n//2)+1
l=n//2
for i in range(1,t+1):
    for j in range(1,i+1):
        print("*",end="")
    print()
for q in range(l,0,-1):
    for r in range(q,0,-1):
        print("*",end="")
    print()

#question-5
row=int(input("Enter the number of rows"))
n=0

for i in range(0,row+1):
      
      for j in range(i): 
            if n==26:
                n=0 
            else:
                pass
            y=chr(65+n) 
            print(y, end="")
            n+=1
      print("")


#question-6

lower_value = int(input("Enter the Lowest Range Value : "))  
upper_value = int(input("Enter the Upper Range Value : "))    # input from user the lowest and the upper range
  
print ("The Prime Numbers in this range are : ")  
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):                           # Check for each number if it has any factor between 1 and itself
            if (number % i) == 0:                             # if YES, the code will move on
                break       
        else:  
            print (number)                                    # if NO, the code prints the number



#question-7
accum=[]
for i in range(1,500):
    if i%7==0 and i%11==0 :
        accum.append(i)
print("The numbers divisible by 11 and are multiple of 7 are :",accum)        



#question-8
pos=[]
neg=[]
odd=[]
even=[]
times={}
li=[]
for i in range(10):
    num=int(input("Enter the number "))
    li.append(num)
    if num>=0:
        pos.append(num)
    elif num<0 :
        neg.append(num)
    if num%2==0 :
        even.append(num)
    else :
        odd.append(num)
    if num not in times :
            times[num]=1
    else:
        times[num]+=1
print("Positive numbers are: ",pos)
print("Negative numbers are: ",neg)
print("Even numbers are: ",even)
print("Odd numbers are: ",odd)
print("Number of times each number occurs in the List",times)





#question-9
n=int(input("Number of words: "))
li=[]
for i in range(n):
    word=input("Enter the word: ")
    li.append(word)
times={}
for i in li :
    if i not in times :
        times[i]=1
    else :
        times[i]+=1
print("Number of occurences: ",times)
