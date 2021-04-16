""" you have two dictionaries 
The first is one contains the student marks in the mathematics course:
The second dictionary contains the student marks in the programming course:
Where the key is the student Id and the value is the mark
Write a python code to find all the students(students id) who achieved more than 80 in both courses. 
"""
stu_over80_in_math = []
stu_over80_in_program = []


d1 = {1:80, 2:90, 3:90, 4:80, 5:60, 6:70, 7:58, 8:66, 9:79}

d2 = {1:88, 2:77, 3:95, 4:80, 5:66, 6:77, 7:88, 8:90, 9:88}

for key, value in d1.items():
	if value > 80:
		stu_over80_in_math = key
		print(stu_over80_in_math)

for key, value in d2.items():
	if value > 80:
		stu_over80_in_program = key
		print(stu_over80_in_program)
