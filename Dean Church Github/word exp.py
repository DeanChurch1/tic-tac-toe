name = input("type in your first and last name:")
x = name.find(" ")
firstName = name[:x]
lastName = name[x+1:]
#lastName.trim(" ")
print(firstName)
print(lastName)

display_puzzle(puzzle)
