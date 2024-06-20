# Program to manage data types

## Problem:

We want you to model and implement, in the language of your choice, a virtual method table handler for an object-oriented system with simple inheritance and dynamic method dispatch:

a. It must know how to deal with class definitions, potentially with simple inheritance. These definitions will only have the names of the methods it will have.

b. Once the program is started, it will repeatedly ask the user for an action to proceed. Such action can be:
  1. ```CLASS <type> [<name>]```<br>
    Defines a new type that will have methods with names set in the provided list. The <type> can be:<br>
      - A name, which establishes a type that does not inherit from any other.<br>
      - An expression of the form <name> : <super>, which states the name of the type and the fact that this type inherits from the type with name <super>.<br>
    For example: ```CLASS A f g``` and ```CLASS B : A f h```.<br>
    Let's note that it is possible to replace definitions of a super class in classes that inherit it.<br>
    The program should report an error and ignore the action if the name of the new class already exists, if the super class does not exist, if there are repeated definitions in the list of method names, or if a loop occurs in the inheritance hierarchy.
  2. ```DESCRIBIR <name>```<br>
    It should display the virtual method table for the type with the proposed name.<br>
    For example: ```DESCRIBIR B```.<br>
    This should show:<br>
      f -> B :: f<br>
      g -> A :: g<br>
      h -> B :: h<br>
    The program should report an error and ignore the action if the type name does not exist.
  3. ```SALIR```<br>
    It must exit the simulator.

At the end of each action, the program must ask the user for the next action.

## Requirements:
To run this program, you must have the following installed:<br>
- Python

## How to install the project
Follow these steps to install the project:
1. **Clone the repository**: Clone the repository using the following git command:<br>
   ```git clone https://github.com/PanquecaFuriosa/Table-and-Virtual_method-handler```

## How to run the project
Follow these steps to run the project:
1. **Run the following bash command**:<br>
   ```python ManejadorDeTipos.py```
