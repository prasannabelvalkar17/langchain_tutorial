from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = "Sachin"
    age: Optional[int] = None
    grade: str
    email: Optional[EmailStr] = None
    cgpa: Optional[float] = Field(None, ge=0.0, le=10.0, description="CGPA must be between 0.0 and 10.0")

new_student = Student(name="John Doe", age=20, grade="A", email="john.doe@example.com", cgpa=8.5)
# name='John Doe' age=20 grade='A'

print(new_student)

# new_student2 = Student(name=55, age=20, grade="A")
# print(new_student2)  
# Input should be a valid string [type=string_type, input_value=55, input_type=int]

new_student3 = Student(age=20, grade="A")
print(new_student3)
# name='Sachin' age=20 grade='A'

# new_student4 = Student(age=20, grade="A", email="invalid_email")
# print(new_student4)
#  not a valid email address: An email address must have an @-sign. [type=value_error, input_value='invalid_email', input_type=str]

# new_student5 = Student(age=20, grade="A", cgpa=12)
# print(new_student5)
# Input should be less than or equal to 10 [type=less_than_equal, input_value=12.0, input_type=float]


# we can convert pydantic object into dictionary using .dict() method
student_dict = new_student.dict()
print(student_dict)   #{'name': 'John Doe', 'age': 20, 'grade': 'A', 'email': 'john.doe@example.com', 'cgpa': 8.5}
print(student_dict['name'])  # Output: John Doe

# we can convert pydantic object into JSON using .json() method
student_json = new_student.json()  # method is deprecated in Pydantic v2
studeent_json_new = new_student.model_dump_json()  # New method in Pydantic v2
print(student_json)  
print(studeent_json_new)

# {"name":"John Doe","age":20,"grade":"A","email":"john.doe@example.com","cgpa":8.5}