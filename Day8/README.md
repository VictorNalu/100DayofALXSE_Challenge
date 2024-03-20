# Day 8

Hi there,

Today is Day 8 of the 100days of AlxSE challenge. Today, I did my first task in the Airbnb clone: The console project.

Here is the task:

> Write a class BaseModel that defines all common attributes/methods for other classes:
> models/base_model.py
> Public instance attributes:
> id: string - assign with an uuid when an instance is created:
> you can use uuid.uuid4() to generate unique id but don’t forget to convert to a string
> the goal is to have unique id for each BaseModel
> created_at: datetime - assign with the current datetime when an instance is created
> updated_at: datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
> **str**: should print: [<class name>] (<self.id>) <self.**dict**>
> Public instance methods:
> save(self): updates the public instance attribute updated_at with the current datetime
> to_dict(self): returns a dictionary containing all keys/values of **dict** of the instance:
> by using self.**dict**, only instance attributes set will be returned
> a key **class** must be added to this dictionary with the class name of the object
> created_at and updated_at must be converted to string object in ISO format:
> format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
> you can use isoformat() of datetime object
> This method will be the first piece of the serialization/deserialization process: create a dictionary representation with “simple object type” of our BaseModel

## You can find the solution here: [base_model][def]

[def]: https://github.com/VictorNalu/AirBnB_clone/blob/4093d226cb21a85beee1c654ae8bc51bdf2e6b90/models/base_model.py
