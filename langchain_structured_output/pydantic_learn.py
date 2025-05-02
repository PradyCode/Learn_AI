from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str 
    age: Optional[int] = None
    email: EmailStr
    gpa: float = Field(gt=0,lt=4,default = 2, description= 'gpa of a studen' )

new_student = {'name': 'Pradyut', 'age': 35 , 'email': 'pradyutpratik@gmail.com', 'gpa' : 3.82}

student = Student(**new_student)

#print(student.email)

student_dict = dict(student)

print(student_dict['email'])