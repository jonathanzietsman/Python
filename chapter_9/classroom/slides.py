""" Example ( Page 158-161 ) """

# Define a class called dog:
class Dog:
    """ A simple attempt to model a dog """
    # The __init__method is the constructor that gets called when we create an instance of Dog
    def __init__(self, name, age ):
        """ Initialize name and age attributes for the dog  """
        self.name = name    # Assign the given 'name' to the instances 'name' attribute
        self.age = age     # Assign the given 'name' to the instances 'name' attribute
        
    # Method that shows a dog sitting 
    def sit(self):
        print(f'{self.name} is now sitting.')\
    
    # Method that shows a dog rolling over 
    def roll_over(self):
        print(f'{self.name} rolled over.')
        
# 2. Creating an Insrance:
my_dog = Dog('Willie', 6)

print(f'My dogs name is {my_dog.name}.')
print(f'My dogs is {my_dog.age} years old.')

# Add a blank line between age calling methods
print()

# 3. Accesing attributes with dot notation
print(my_dog.name)
print(my_dog.age)

# Add a blank line between age calling methods
print()

# 4. Calling methods from the Dog class
my_dog.sit()
my_dog.roll_over()

# 5. Creating multiple instances 
my_dog = Dog('rex', 1 )
your_dog = Dog('Lucy', 3 )

print(f'\nMy dogs name is {my_dog.name}')
print(f'My dog is {my_dog.age} years old')
my_dog.sit()

print(f'\nYour dogs name is {your_dog.name}')
print(f'Your dog is {your_dog.age} years old')
your_dog.sit()