# defining a variable to store a message 
message = "Hello Python world!"

# printing the message
print(message)

# changing the message and printing it again
message = "Hello Python Crash Course world!"
print(message)

# concatenation: combining two or more strings into one
greeting = "Hello"
name = "Alice"
print(greeting + " " + name)

# Repetition: repeating a string multiple times
print("Hello" * 5)

# slicing: extracting a part of a string
print("hello, world!"[7:12])

# escaping characters: using special characters like newline (\n) and tab (\t)
print("Line 1\nLine 2\n\tIndented line")

# string length: using the len() function to get the length of a string
print(len("Hello, world!"))

# indexing: accessing individual characters in a string
message = "Hello, world!"
print(message[0])

# negative indexing: accessing characters from the end of a string
message = "Hello, world!"
print(message[-1])

# string comparison: comparing strings using comparison operators
print("apple" == "apple")

# upper(): converts all characters to uppercase
message = "hello, world!"
print(message.upper())

# lower(): converts all characters to lowercase
message = "HELLO, WORLD!"
print(message.lower())

# strip(): removes leading and trailing whitespace
name = "\t\n   John Doe   \n\t"
print(name.strip())

# replace(): replaces a substring with another substring
message = "Hello, world!"
print(message.replace("world", "Python"))

# find(): finds the index of a substring
message = "Hello, world!"
print(message.find("world"))

# split(): splits a string into a list(array) based on a delimiter
message = "apple,banana,orange"
print(message.split(","))