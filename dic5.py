# program to merge two or more dictionary together

num1 = {"name1":"ajayi"}
num2 = {"name2": "alabi"}
merge = num1.copy()
merge.update(num2)
print(merge)

# exercise2
# write a python program to sum all the items in a dictionary

person1_salary = {"income": 200, "credit": 100, "debit":30}
person2_salary = { "income2": 300, "credit": 150, "debit":40}
sum_of_both_salary = 0
for salary in (person1_salary.values(),person2_salary.values()):
	sum_of_both_salary = sum(salary)
	print("Total salary " + str(salary))

# write a python program to multiply all the values in a dictionary with 2

number = {1:2, 2:4, 3:9, 4:16}
for num in number.values():
	multiply = num * 2
	print(multiply)

# write a python program to remove a key from a dictionary
number = {1:2, 2:4, 3:9, 4:16}
if 1 in number:
	del number[1]
print(number)

