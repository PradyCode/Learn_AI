from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'Pradyut', 'age':'35'}

print(new_person)