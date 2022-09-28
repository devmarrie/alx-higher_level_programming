>Inharitance is the ability of a class to pick the attributes of another class and use them as its own.The class which is being inherited from is defined as the *parent, base or super class* while the class which inherits is defined as the *sub class, derived class  or the child class*.Below is the syntax for inheritance in python.

```
class ChildClass(ParentClass):
     #Class defination
```

>So in this case when the child class is being structured the parent class is remembered.When an attribute reffernce is not found in the child class it is searched for in the parent class.This rule is applied recursively if the parent class is derived from another class.A derived class may override methods of the base class. **Overriding** simply means the derived class inherits the attributes(fields and methods) of the parent class and extend or replace its outlook in the child class.

```
class Person():
     def __init__(self,name,age=20):
         self.name = name
         self.age = age
     def eats(self):
        print("{}, eats alot".format(self.name))

class Human(Person):
     def __init__(self,name):
         self.name = name
     def eats(self):
         print("{},eats and is {} years old".format(self.name, self.age))

Marrie = Human("Marrie")
Marrie.eats()

```

>Python has the follwing methods that work well with inheritance
*isinstance() - used to check an instance type.It returns true if the first argument is an instance of the second argument

```
isinstance(obj, int)
# return true if the object type is an integer or is derived from a class that is derived from int
```

*issubclass() - checks for class inheritance

#### Multiple ineritance 
>This ussually happens when a sub class inherits from **more than one** base class. The inheritance happens from left to right,not searching twice if the attributes overlap in the hierachy. Multiple inheritance provide more than one way to rech the parent class.

```
class DerivedClass(BaseClass1, BaseClass2, BaseClass3):
   #class definition

```

>If we do not inherit from any class, just as a single class implementation is , the class is bound to inherit from the  object  it creates after instaniation.

####The super function
>This magic method calls the method in the parent class.It can be called inside any method but mostly called in the  __init__  method.It enables one to avoid redundant code. 
