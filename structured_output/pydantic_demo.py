# create a dictionary storing names of student and make sure it should always be in string
from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    # name: str 
    name : str = 'Pragya' #using default value
    age: Optional[int]  = None
    email: EmailStr #validating email format
    # applyingg consatraint
    cgpa:float = Field(gt=0, lt=10,default=5,description='A decimal value representing the cgpa of the student')
# new_student = {'age':32}
new_student = {'age':'32','email':'abc@gmail.com'}  #pydantic type coercing feature
# new_student = {'name':'Pragya'}
# new_student = {'name':32}  # for trial check using other data type getting error
student = Student(**new_student)
print(student)

# converting pydantic object into dict-json format
student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)