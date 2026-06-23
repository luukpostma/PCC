countries: list[str] = ["germany", "austria", "turkey"]

# Accessing elements in a list:
print(countries[1].title())

# Index position starts at 0 not 1

# -1 zorgt er altijd voor dat je het laatste item in de list krijgt:
print(countries[-1].title())

# Het gebruiken van items in een list:
print(f"Ik wou graag een keer naar {countries[0].title()} willen gaan!")

# Het veranderen van items op een specifieke plek in een list.
countries[0] = "netherlands"
print(countries)

# Het toevoegen van items aan een list:
countries.append("belgium")
print(countries)

# Het toevoegen van een item op een specifieke plek:
countries.insert(0, "england")
print(countries)

# Het verwijderen van items in een list:
del countries[0]
print(countries)

# Het verwijderen van items met pop(), dit verwijderd altijd het laatste item.
countries.pop()
print(countries)

# Het verwijderen van items met pop(), je kunt ook een specifieke item verwijderen.
countries.pop(1)
print(countries)

# Het verwijderen van items bij waarde:
countries.remove("turkey")
print(countries)

##
countries.append("sweden")
print(countries)
##

# Het verwijderen van een variable met de remove()
remove_country = "sweden"
countries.remove(remove_country)
print(countries)

##
countries.append("brazil")
countries.append("canada")
countries.append("china")
print(countries)
##

# Met de sort functie kun je de list alfabetisch-volgorde maken.
countries.sort()
print(countries)

# Reverse alfabetische volgorde:
countries.sort(reverse=True)
print(countries)

# Met sorted() pas je de originele lijst niet aan, er word achter de schermen een kopie gemaakt.
print(countries)
print(sorted(countries))

# Een list reversen
countries.reverse()
print(countries)