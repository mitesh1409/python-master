# Classes

When we think we need to define a new class, we work though a series of questions in  
an effort to convince ourselves we actually need one. Here’s what we ask:

#1 Will a dictionary do instead?  
If all you need is a way to bundle named data values together,  
use a dictionary not a class.  
You’ll be much happier.

#2 What about defining a class using the built-in `dataclass`?  
The PSL contains a module called `dataclass`. This module exists to make it easy to  
create a custom class in Python with the minimum of effort.

#3 What about using the third-party `attrs` package?  
PyPI contains the very highly regarded `attrs`, which can be considered to be a  
superset of the built-in `dataclass`. Like the latter, it works hard to help you  
avoid writing all the boilerplate code required to create your own custom class.  

If you end up answering no, no, and no to these three questions,  
feel free to create your own custom class.  

The Python documentation (especially [Chapter 9 of The Python
Tutorial](https://docs.python.org/3/tutorial/classes.html)) is a good starting point.

---

## Example #1

Building a BetterDate Class

You are developing a time series package and want to define your own class for working with dates, BetterDate.

The attributes of the class will be year, month, and day. You want to have a constructor that creates BetterDate objects given the values for year, month, and day, but you also want to be able to create BetterDate objects from strings, such as 2021-04-30.

```python

class BetterDate:
  def __init__(self, year, month, day):
    self.year, self.month, self.day = year, month, day
    
  # Define a class method from_str
  @classmethod
  def from_str(cls, datestr):
    # Split the string at "-"
    parts = datestr.split("-")
    year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
    # Return the class instance
    return cls(year, month, day)

# Create the xmas object      
xmas = BetterDate.from_str("2024-12-25")   
print(xmas.year)
print(xmas.month)
print(xmas.day)

```

---

## Example #2

Create a subclass

The purpose of child classes, or sub-classes, is to customize and extend the functionality of the parent class.

Recall the Employee class from earlier in the course. In most organizations, managers have more privileges and responsibilities than regular employees. So it would make sense to introduce a Manager class that has more functionality than Employee.

But a Manager is still an employee, so the Manager class should be inherited from the Employee class.

In this exercise, you'll create a Manager child class and, later in the course, you'll add specific functionality to the class.

```python

class Employee:
    MIN_SALARY = 30000

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY
        
    def give_raise(self, amount):
        self.salary += amount

# Define a new class Manager inheriting from Employee
class Manager(Employee):
    # Add a keyword to leave this class empty
    pass

# Define a Manager object
mng = Manager("Debbie Lashko", 86500)

# Print mng's name
print(mng.name)

```

---

## Example #3

Customize a subclass

Inheritance is powerful because it allows us to reuse and customize code without rewriting existing code. By calling methods of the parent class within the child class, we reuse all the code in those methods, making our code concise and manageable.

In this exercise, you'll continue working with the Manager class that is inherited from the Employee class. You'll add a constructor that builds on the Employee constructor, taking an additional argument where you can specify the project that the manager is working on.

A simplified version of the Employee class, as well as the beginning of the Manager class you previously created, has been provided for you in script.py.

```python

class Employee:
  def __init__(self, name, salary=30000):
    self.name = name
    self.salary = salary

  def give_raise(self, amount):
    self.salary += amount

class Manager(Employee):
  # Add a constructor 
  def __init__(self, name, salary=50000, project=None):
    # Call the parent's constructor
    Employee.__init__(self, name, salary)
    # Assign project attribute
    self.project = project

  def display(self):
    print("Manager ", self.name)

```

---

## Example #4

Method inheritance

In this exercise, you'll extend the Manager class (which is inherited from the Employee class), created in the previous exercise, by creating a method called give_raise(). It will be similar to the method of the same name in the Employee class, but include an additional argument called bonus.

The Manager class you previously created has been provided for you in script.py.

```python

class Employee:
  def __init__(self, name, salary=30000):
    self.name = name
    self.salary = salary

  def give_raise(self, amount):
    self.salary += amount

class Manager(Employee):
  def display(self):
    print("Manager ", self.name)

  def __init__(self, name, salary=50000, project=None):
    Employee.__init__(self, name, salary)
    self.project = project

  # Add a give_raise method
  def give_raise(self, amount, bonus=1.05):
    new_amount = amount * bonus 
    Employee.give_raise(self, new_amount)

mngr = Manager("Ashta Dunbar", 78500)
mngr.give_raise(2000, bonus=1.03)
print(mngr.salary)

```

---

## Example #5

Inheritance of class attributes
Earlier in the course, you learned about class attributes and methods that are shared among all the instances of a class. How do they work with inheritance?

In this exercise, you'll create a subclass of the Player class you worked with earlier in the chapter and explore the inheritance of class attributes and methods.

The `Player` class has been defined for you, and the code provided here:

```python

class Player:
    MAX_POSITION = 10

    def __init__(self):
      self.position = 0

    def move(self, steps):
      if self.position + steps < Player.MAX_POSITION:
        self.position += steps 
      else:
        self.position = Player.MAX_POSITION

# Create a Racer class inheriting from Player
class Racer(Player):
    # Create MAX_POSITION with a value of 15
    # MAX_POSITION = 15 # This will overwrite parent class attribute.
    pass

# Create a Player and a Racer objects
p = Player()
r = Racer()

print("p.MAX_POSITION = ", p.MAX_POSITION)
print("r.MAX_POSITION = ", r.MAX_POSITION)

```

Class attributes CAN be inherited, and the value of class attributes CAN be overwritten in the child class.

---

## Example #6

Overloading equality

When comparing two objects of a custom class using ==, Python by default compares just the memory chunks that the objects point to, not the data contained in the objects. To override this behavior, the class can implement a special method, which accepts two arguments, the objects to be compared, and returns True or False. This method will be implicitly called when two objects are compared.

The BankAccount class from the previous chapter is available for you in the script.py. It has two attributes, balance and number, and a withdraw() method. Two bank accounts with the same balance are not necessarily the same account, but a bank account usually has an account number, and two accounts with the same account number should be considered the same.

```python

class BankAccount:
    # Modify to initialize a number attribute
    def __init__(self, number, balance=0):
        self.balance = balance
        self.number = number

    def withdraw(self, amount):
        self.balance -= amount

    # Define __eq__ that returns True if the number attributes are equal 
    def __eq__(self, other):
        return self.number == other.number

# Create accounts and compare them
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)

```

---

## Example #7

Checking class equality

In the previous exercise, you defined a BankAccount class with a number attribute that was used for comparison. But if you were to compare a BankAccount object to an object of another class that also has a number attribute, you could end up with unexpected results.

For example, consider two classes

```python

class Phone:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number

pn = Phone(873555333)

class BankAccount:
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number == other.number

acct = BankAccount(873555333)

```

Running acct == pn will return True, even though it compares a phone number with a bank account number.

It is good practice to check the class of objects passed to the __eq__() method to make sure the comparison makes sense.

```python

class BankAccount:
    def __init__(self, number, balance=0):
        self.number, self.balance = number, balance

    def withdraw(self, amount):
        self.balance -= amount 

    # Modify to add a check for the class type
    def __eq__(self, other):
        return (self.number == other.number) and (type(self) == type(other))

acct = BankAccount(873555333)
pn = Phone(873555333)

# Check if the two objects are equal
print(acct == pn)

```
