places = ["america", "japan", "sint maarten", "australia", "antartica"]
print(places)

print(sorted(places))

print(places)

# Met de sorted() hou je de originele list in tact en word en achter de schermen een nieuwe kopie gemaakt.
print(sorted(places, reverse=True))
print(places)

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

# met de sort() pas je de huidige list aan.
places.sort(reverse=True)
print(places)

