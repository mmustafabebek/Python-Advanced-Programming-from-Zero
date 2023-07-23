"""
Calculate the letter grade according to the grades of the user's midterm1, midterm2, final grades.

     Midterm1 will affect 30% of the total grade.

     Midterm2 will affect 30% of the total grade.

     The final will affect 40% of the total grade.


     Total Grade >= 90 -----> AA

     Total Grade >= 85 -----> BA

     Total Grade >= 80 -----> BB

     Total Grade >= 75 -----> CB

     Total Grade >= 70 -----> CC

     Total Grade >= 65 -----> DC

     Total Grade >= 60 -----> DD

     Total Grade >= 55 -----> FD

     Total Grade < 55 -----> FF
"""

midterm1 = float(input("Your first midterm grade:"))
midterm2 = float(input("Your second midterm grade:"))
final = float(input("Your final grade:"))

total_grade = (midterm1 * 0.3) + (midterm2 * 0.3) + (final * 0.4)

if(total_grade >= 90):
    print("AA")
elif(total_grade >= 85):
    print("BA")
elif(total_grade >= 80):
    print("BB")
elif(total_grade >= 75):
    print("CB")
elif(total_grade >= 70):
    print("CC")
elif(total_grade >= 65):
    print("DC")
elif(total_grade >= 60):
    print("DD")
elif(total_grade >= 55):
    print("FD")
elif(total_grade < 55):
    print("FF")
