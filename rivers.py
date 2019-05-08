rivers = ["Mississippi River", "Ohio River", "Cumberland River", "Tennessee River", "Potomac River"]

print(rivers)

# Change Ohio River to Saginaw River
rivers[1] = "Saginaw River"

# Add Fox River to end of list
rivers.append("Fox River")

# Insert "Rio Grande" at beginning of list
rivers.insert(0, "Rio Grande")

# Remove index 3 (Cumberland River)
del rivers[3]

# Pop method to remove Fox River
rivers.pop(-1)

# Remove Tennessee River by naming it
rivers.remove("Tennessee River")

# Sort list permanently with sort()
rivers.sort()

# Reverse the order
rivers.reverse()

# Find length of list
print(len(rivers))

print(rivers)

# Intentional error, index out of range
rivers.pop(4)
