user = int (input("Type in a number"))
#number = num

one = "This is your number as an integer {:,}"
print(one.format(user))

one = "This is your number as a float {:.4f}"
print(one.format(user))

one = "This is your number as a perentage {:.0%}"
print(one.format(user))

one = "This is your number in a dollar amount ${:.2f}"
print(one.format(user))