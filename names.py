names = ['larry', 'barry', 'gary', 'jerry']

print (names[0].title())
print (names[1].title())
print (names[2].title())
print (names[3].title())

message = "Don't mess with " + names[0].title() + ", or " + names[-1].title() + "!"

message_for_barry = "You're a good man, " + names[1].title() + "."

print(message)
print(message_for_barry)