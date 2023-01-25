class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 

'''
p1 = Person('Kwesi', 39)
print(p1.name)
print(p1.age)
'''
name = input('Enter your name: ')
age = input('Enter your age: ')
p1 = Person(name, age)
print(p1.name)
print(p1.age)
