# 3-4 Guest list
guests = ["Abe Vigoda", "Bobby McFerrin", "Bjorn Borg"]

print(guests)

# 3-9 Print length of guests list
print(len(guests))

abe_invite = "Hi " + guests[0] + ", would you join me for dinner?"
bobby_invite = guests[1] + ", you are cordially invited to my dinner party."
bjorn_invite = "Hej " + guests[2] + ", skulle du gå med mig till middag?"

print(abe_invite)
print(bobby_invite)
print(bjorn_invite)

# 3-5 Changing guest list
print(guests[1] + " won't be able to make it.")

guests[1] = "Mama Cass" # Replace Bobby McFerrin with Mama Cass

cass_invite = "Salutations, " + guests[1] + ". Would you join us for dinner?"

print(cass_invite)

print("I have found a larger dinner table.")

# 3-6 Adding more guests
guests.insert(0, "Tomoe Gozen")
guests.insert(2, "Confucious")
guests.append("John Cleese")

tomoe_invite = guests[0] + ", please come to my party."
confucious_invite = guests[2] + ", I also want you to join my dinner party."
john_invite = guests[-1] + ", you are also invited."

print(tomoe_invite)
print(confucious_invite)
print (john_invite)

# 3-7 Shrinking guest list
print("Well, turns out that table won't arrive in time. So....")

first_uninvited_guest = guests.pop(0)
second_uninvited_guest = guests.pop(0)
third_uninvited_guest = guests.pop(0)
fourth_uninvited_guest = guests.pop(0)

print(first_uninvited_guest + ", would you mind not showing up?")
print(second_uninvited_guest + ", you too. You're dead, anyway.")
print(third_uninvited_guest + "... you know where I'm going with this...")
print(fourth_uninvited_guest + ", you are no longer invited, because I am a jerk.")

print(guests[0] + ", are you still coming?")
print(guests[1] + ", you are also still invited.")

del(guests[0])
del(guests[0])

 # no more guests :(
print(guests)




