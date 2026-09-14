from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    email: str


new_person: Person = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}

new_person2: Person = {
    "name": "John Doe",
    "age": "30",    ## this will not give an error, but it is not type safe
    "email": "john.doe@example.com"
}


print(new_person)
print(new_person2)