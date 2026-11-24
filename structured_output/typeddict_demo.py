from typing import TypedDict

class Person(TypedDict):
    name:str
    age:int

new_person:Person = {'name':'Pragya','age':'35'}
print(new_person)

# even though we have passed age as str value code fir v chl gya