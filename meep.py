from __future__ import division
from random import *

print ("insert current grades and desires for future grades. This program will calculate your potential GPA and requirements in finals. Put in random answers for classes you are not taking in the select catagories")
class_grades = input("Grade 1:"),input("Grade 2:"),input("Grade 3:"),input("Grade 4:"),input("Grade 5:"),input("Grade 6:"),input("Grade 7:")
grade_desires = input("Desired grade 1:"),input("Desired grade 2:"),input("Desired grade 3:"),input("Desired grade 4:"),input("Desired grade 5:"),input("Desired grade 6:"),input("Desired grade 7:")

print grade_desires





class_weights = input("Class final weight 1:"),input("Class final weight 2:"),input("Class final weight 3:"),input("Class final weight 4:"),input("Class final weight 5:"),input("Class final weight 6:"),input("Class final weight 7:")


class_numbers = input("Number of classes:")



def number_grade_and_GPA(class_grades):
   class_index = 0
   grade = ''
   GPA = 0
   while class_index < class_numbers:
       if class_grades[class_index] >= 90:
           grade = grade + ' A '
           GPA = GPA + 4
           class_index = class_index + 1
       elif class_grades[class_index] >= 80:
           grade = grade + ' B '
           GPA = GPA + 3
           class_index = class_index + 1
       elif class_grades[class_index] >= 70:
           grade = grade + ' C '
           GPA = GPA + 2
           class_index = class_index + 1
       elif class_grades[class_index] >= 60:
           grade = grade + ' D '
           GPA = GPA + 1
           class_index = class_index + 1
       else:
           grade = grade + ' F '
           GPA = GPA + 0
           class_index = class_index + 1
   GPA = GPA / class_numbers
   print "Your GPA"
   print round(GPA,2)
   return grade   
number_grade_and_GPA(class_grades)

def finals_requirements():
   final = 0
   class_index = 0
   grade_index = 0
   test_needed_grades = ''
   while class_index < class_numbers:
       final = 0
       final = ((grade_desires[grade_index])/100 - (1 - (class_weights[grade_index])/100)* (class_grades[grade_index]/100)) / (class_weights[grade_index]/100)
       final = final * 100
       grade_index= grade_index + 1
       test_needed_grades =test_needed_grades + " Class " + str(class_index) + " " + str(final)
       class_index = class_index + 1
   return test_needed_grades
print "Final requirements:"
print finals_requirements()

def ideal_GPA(grade_desires):
   class_index = 0
   grade = ''
   GPA = 0
   while class_index < class_numbers:
       if grade_desires[class_index] >= 90:
           grade = grade + ' A '
           GPA = GPA + 4
           class_index = class_index + 1
       elif grade_desires[class_index] >= 80:
           grade = grade + ' B '
           GPA = GPA + 3
           class_index = class_index + 1
       elif grade_desires[class_index] >= 70:
           grade = grade + ' C '
           GPA = GPA + 2
           class_index = class_index + 1
       elif grade_desires[class_index] >= 60:
           grade = grade + ' D '
           GPA = GPA + 1
           class_index = class_index + 1
       else:
           grade = grade + ' F '
           GPA = GPA + 0
           class_index = class_index + 1
   GPA = GPA / class_numbers
   print "Your ideal GPA"
   print round(GPA,2)
   return grade
print ideal_GPA(grade_desires)

