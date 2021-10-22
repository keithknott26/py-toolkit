# How to use the super() method

Using a base class we create two more classes where we add only what makes the derived class unique. We make use of `super()` to get a delegate object of the parent class in order to call its method directly.

* _Individual_: a base class to represent a person
* _Student_: it **extends** the base class adding a new method
* _Teacher_: it **overrides** a method of the parent class.

## How to run the code:
```
pipenv shell
cd samples/oop
python demo.py
```
