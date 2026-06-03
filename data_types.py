#String data type

firstname = ' Imona'
lastname = 'Prosper '

print(type(firstname))
print(type(lastname) == str)
print(isinstance(firstname, str))

#string method
print(firstname.upper() + " " + lastname.lower())
print(firstname.title() + " " + lastname.lower())
print(len(firstname.strip()))
print(len(lastname.strip()))
print(len(firstname.lstrip()))
print(len(lastname.rstrip()))

age = 15
print(type(age))
print(type(age) == str)
print(isinstance(age, str))
print("\n")

title = "menu".upper()

print(title.center(16, "="))
print("Cofee".ljust(14, ".") + "$2")
print("Tea".ljust(16, ".") + "$2")
print("Milk".ljust(15, ".") + "$3")
print("\n")

print(title.endswith("U"))
print(title.startswith("f"))
print("\n")

price = 100
best_price = 80
print(type(price))
print(isinstance(best_price, str))
print("\n")

gpa = 3.45
