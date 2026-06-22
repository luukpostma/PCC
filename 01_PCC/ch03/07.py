guest_list = ["justin", "michael", "drake"]

print(f"Hey {guest_list[0].title()}, would you like to come to my dinner?")
print(f"Hey {guest_list[1].title()}, would you like to come to my dinner?")
print(f"Hey {guest_list[2].title()}, would you like to come to my dinner?")

print(f"Oh, {guest_list[1].title()} can't make it to the dinner!")

# Langzame manier voor het veranderen van een item in een list.
# del guest_list[1]
# guest_list.append("jay-z")

# Snelle manier voor het veranderen van een item in een list.
guest_list[1] = "jay-z"

print(f"Hey {guest_list[0].title()}, would you like to come to my dinner?")
print(f"Hey {guest_list[1].title()}, would you like to come to my dinner?")
print(f"Hey {guest_list[2].title()}, would you like to come to my dinner?")

print("I found a bigger dining table!")

guest_list.insert(0, "rihanna")
guest_list.insert(2, "pablo")
guest_list.append("beyonce")

print(guest_list)

print(f"Hey {guest_list[0].title()} ,would you like to come to my dinner?")
print(f"Hey {guest_list[1].title()}, would you like to come to my dinner?")
print(f"Hey {guest_list[2].title()}, would you like to come to my dinner?")
print(f"Hey {guest_list[3].title()}, would you like to come to my dinner?")
print(f"Hey {guest_list[4].title()}, would you like to come to my dinner?")
print(f"Hey {guest_list[5].title()}, would you like to come to my dinner?")

print("Oh, I can only invite 2 people to dinner.")

print(f"I'm sorry {guest_list.pop().title()}, I can only invite 2 people.")
print(f"I'm sorry {guest_list.pop().title()}, I can only invite 2 people.")
print(f"I'm sorry {guest_list.pop().title()}, I can only invite 2 people.")
print(f"I'm sorry {guest_list.pop().title()}, I can only invite 2 people.")

print(guest_list)

print(f"Hey {guest_list[0].title()}, your are still invited!")
print(f"Hey {guest_list[1].title()}, your are still invited!")