class Person1:
    def __init__(self, name):
        self.name = name

p = Person1('Nihal')
print(p.name)

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} old. He lives in {self.city}, {self.country}"

p = Person('Nihal', 'Sayyad', 26, 'India', 'Pune')
print(p.person_info())