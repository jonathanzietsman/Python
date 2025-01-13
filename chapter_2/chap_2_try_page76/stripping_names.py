# Variable with whitespace
name = "\t\n   John Doe   \n\t"

# Print the original name with whitespace
print("Original name with whitespace:")
print(name)

# Print the name with lstrip()
print("\nName with lstrip():")
print(name.lstrip())

# Print the name with rstrip()
print("\nName with rstrip():")
print(name.rstrip())

# Print the name with strip()
print("\nName with strip():")
print(name.strip())