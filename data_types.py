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

