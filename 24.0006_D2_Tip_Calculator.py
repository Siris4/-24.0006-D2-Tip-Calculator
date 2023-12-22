original_bill = 150.00
print(type(original_bill))
total_people = 5
print(type(total_people))
tip_percentage = 1.12
print(type(tip_percentage))
math = float((original_bill/total_people)*tip_percentage)
two_decimal_math = float(round(math, 2))
# format() .2f (shown below) will force exacty 2 decimal places, .2f is used as
# 2nd parameter being passed into it.
print("The bill for each person is $"+(format(two_decimal_math, ".2f")))