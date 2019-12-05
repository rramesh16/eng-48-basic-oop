# OOP Basics 
This class is going to cover the basics of OOP

### Covered in this class:

**4 Pillars:**
- Abstraction
- Inheritance
- Polymorphism
- Encapsulation

Other learning outcomes:
- Git + GitHub
- Documentation with Markdown
- Best practices and organisation 

### Definitions
 
 **Class**
 - Is a blueprint of an object
 - It wraps methods and attributes 
 
 **Methods**
 - Like functions, they can take in arguments and run a block of code. 
 However, they can only be used by an instance of its' class.
 
 **Instance / object**
 - It is an occurrence of an object
 
 **Attributes**
 - Holds information about specific object. 
 - They are set in the ```` def__init__() ```` method with arguments like any other function.
 
 **def__init__()**
 - Also known as constructor or initializer 
 - This method runs every time an object is created. So when you do:
 
  ````
  animal = Animal('Fred', 10, 2)
 ````
 
 **self**
 - refers to the object / instance 
 
 **inheritance**
 - Ability of classes to inherit characteristics (parameters) and behaviours (methods) from parent class. 

**Polymorphism**
- Poly: many
- morph : forms
- Polymorphism : 'Many forms'
- Polymorphism in OOP is the ability to change methods and characteristics of instances of child classes. 
    - Method polymorphism (At method level)

**Abstraction**
- Hiding complexity from the user
- For example: If you want to turn on the TV, you just press the on button on the remote but detail of how it actually works is hidden 
- Specific to us, we will:
    - Write nice documentation for how to import and use our code
    - Use inheritance and importing to hide the code
    - Ultimately we can package it into a module that could be imported with PIP