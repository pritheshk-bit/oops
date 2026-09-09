class parrot:

    species = "brid"

    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = parrot("blu",10)
woo = parrot("woo",10)

print("blu is a ",blu.species)
print("woo is a ",woo.species)

print(f"{blu.name} is {blu.age} years old")
print(f"{woo.name} is {woo.age} years old")