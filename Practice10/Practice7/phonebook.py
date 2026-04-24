# Example 1: Create a simple phonebook dictionary
phonebook = {"Alice": "123-456", "Bob": "987-654"}
print("Phonebook:", phonebook)

# Example 2: Add a new contact
phonebook["Charlie"] = "555-321"
print("After adding Charlie:", phonebook)

# Example 3: Search for a contact
name = "Bob"
if name in phonebook:
    print(f"{name}'s number is {phonebook[name]}")
else:
    print(f"{name} not found")