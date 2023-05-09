

"""
In this example, we define a Address, Contact, and Employee class that inherits from pydantic.BaseModel. The Employee class has attributes for id, name, age, address, and contacts, which are defined using Pydantic's field types. We define two validator methods to validate the age and contacts attributes.

We create an Employee object using the Employee class constructor and pass in values for all of the attributes. We assign the object to the variable employee.

We then use Pydantic's dict() method to convert the employee object to a dictionary, and then create a new Employee object from the dictionary. This step validates the incoming data and ensures that it conforms to the data model.

We define two custom methods on the Employee class: get_personal_data() and get_contact_data(). These methods extract subsets of data from the employee object and return them as dictionaries.

We call the get_personal_data() and get_contact_data() methods on the employee object to extract subsets of data, and assign the results to the variables personal_data and contact_data.

Finally, we print the extracted data to the console.

This example demonstrates how to use Pydantic to define complex data models with validators and custom methods, and how to extract subsets of data from those models.
"""


from pydantic import BaseModel, validator
from typing import List

class Address(BaseModel):
    street: str
    city: str
    state: str
    zipcode: str
        
class Contact(BaseModel):
    name: str
    phone: str
    email: str
        
class Employee(BaseModel):
    id: int
    name: str
    age: int
    address: Address
    contacts: List[Contact]
        
    @validator('age')
    def validate_age(cls, age):
        if age < 18:
            raise ValueError('Employee must be at least 18 years old')
        return age
    
    @validator('contacts')
    def validate_contacts(cls, contacts):
        if len(contacts) == 0:
            raise ValueError('Employee must have at least one contact')
        return contacts
    
    def get_personal_data(self):
        return {"name": self.name,
                "age": self.age,
                "address": self.address}
    
    def get_contact_data(self):
        return [{"name": c.name,
                 "phone": c.phone,
                 "email": c.email} for c in self.contacts]

# Create an Employee object
employee = Employee(id=123,
                    name="John",
                    age=30,
                    address=Address(street="123 Main St.",
                                     city="Anytown",
                                     state="CA",
                                     zipcode="12345"),
                    contacts=[Contact(name="Jane",
                                       phone="555-1234",
                                       email="jane@example.com"),
                              Contact(name="Bob",
                                       phone="555-5678",
                                       email="bob@example.com")])

# Validate the Employee object
employee_dict = employee.dict()
employee = Employee(**employee_dict)

# Extract subsets of data from the Employee object
personal_data = employee.get_personal_data()
contact_data = employee.get_contact_data()

# Print the extracted data
print(personal_data)
print(contact_data)


