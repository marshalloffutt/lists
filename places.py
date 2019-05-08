places = ["Mars", "Egypt", "Venice", "Tokyo", "Vancouver"]

# Print places
print(places)

# Print sorted places in alphabetical order
print(sorted(places))

# Print original places
print(places)

# Print sorted places in reverse alphabetical order
print(sorted(places, reverse=True))

# Show that original list is unchanged
print(places)

# Use reverse() to change the order of the list
places.reverse()
print(places)

# Use reverse() to change the order of list again
places.reverse()
print(places)

# Use sort() to alphabetize the list
places.sort()
print(places)

#Use sort() to to  to reverse alphabetize
places.sort(reverse = True)
print(places)