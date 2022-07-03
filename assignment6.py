#question 1
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
         sum+= x
    return sum == n
k=int(input("Write a number : "))
print(perfect_number(k))

#question 2
def palindrome(s):
 f_s = s.split()
 s_s = s[::-1].split()
 if ''.join(f_s) == ''.join(s_s):
    return 'YES, its palindrome'
 else:
    return 'NO, its not palindrome'
print(palindrome(input()))

#question 3
def pascal_triangle(n):
  trow = [1]
  y = [0]
  for x in range(max(n,0)):
    print(trow)
    trow=[l+r for l,r in zip(trow+y, y+trow)]
  return n>=1
pascal_triangle(6)

#question 4
import string
def ispangram(sentence, alphabet=string.ascii_lowercase):
  return set(alphabet) <= set(sentence.lower())
print(ispangram(input('Sentence: ')))

#question 5
items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))

#question 6
class student_data:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch

    def student_id(self):
        print(f'name : {self.name} ||| branch : {self.branch}')

s=student_data('VISHWASH','CIVIL')
s.student_id()

print('-->',s.name)
print('-->',s.branch)

#question 7
class Student:
  pass
class Marks:
  pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))

#question 8
def findTriplets(arr, n):
  found = True
  for i in range(0, n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n):
        if (arr[i] + arr[j] + arr[k] == 0):
          print(arr[i], arr[j], arr[k])
          found = True
# If no triplet with 0 sum
# found in array
  if (found == False):
    print(" not exist ")
arr = [-25, -10, -7, -3, 2, 4, 8, 10]
n = len(arr)
findTriplets(arr, n)


#question - 9
class validity:
  def f(str):
    a= ['()', '{}', '[]']
    while any(i in str for i in a):
      for j in a:
        str = str.replace(j, '')
    return not str
s = input("enter : ")
print(s, "-", "is balanced"
  if validity.f(s) else "is Unbalanced")


