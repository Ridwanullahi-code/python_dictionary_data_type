# conditional logic with dictionaries

number = {
	1:2, 2:4, 3:9,4:16
}

condition = {k: ("even" if k % 2 == 0 else "odd") for k in number.values()}
print(condition)