# dictionary comprehension
number = {num: num**2 for num in [1,2,3,4,5,6,7]}
print(number)

# exercise2

str1 = "ABC"
str2 = "123"
combo = {str1[num]:str2[num] for num in range(0, len(str1))}
print(combo)