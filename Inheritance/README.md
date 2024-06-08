# Python Inheritance Coding Questions

This repository contains Python coding questions related to inheritance, categorized into different types of inheritance.

## Questions:

### 1. Single Inheritance:
   - **Problem Statement:** Write a Python program that demonstrates single inheritance. Define a superclass called `Shape` with a method `area()` to calculate the area of the shape. Then, create a subclass called `Rectangle` that inherits from `Shape` and adds a method `perimeter()` to calculate the perimeter of the rectangle.
   - **File:** `single_inheritance.py`

### 2. Multiple Inheritance:
   - **Problem Statement:** Create a Python program that showcases multiple inheritance. Define two parent classes `A` and `B`. Class `A` has a method `method_A()` that prints "Method A". Class `B` has a method `method_B()` that prints "Method B". Then, create a child class `C` that inherits from both `A` and `B` and has a method `method_C()` that prints "Method C".
   - **File:** `multiple_inheritance.py`

### 3. Multilevel Inheritance:
   - **Problem Statement:** Implement a Python program to demonstrate multilevel inheritance. Define three classes: `Person`, `Employee`, and `Manager`. `Person` should have attributes `name` and `age`, while `Employee` should inherit from `Person` and include additional attributes like `emp_id` and `salary`. Finally, `Manager` should inherit from `Employee` and have an additional attribute `department`.
   - **File:** `multilevel_inheritance.py`

### 4. Hierarchical Inheritance:
   - **Problem Statement:** Write a Python script that illustrates hierarchical inheritance. Create a superclass `Animal` with a method `sound()` that prints the sound of the animal. Then, create two subclasses `Dog` and `Cat` that inherit from `Animal` and each override the `sound()` method to print "Bark" and "Meow" respectively.
   - **File:** `hierarchical_inheritance.py`

### 5. Hybrid Inheritance:
   - **Problem Statement:** Develop a Python program showcasing hybrid inheritance. Create a class `Vehicle` with methods `start()` and `stop()`. Then, create two subclasses `Car` and `Motorcycle` that inherit from `Vehicle`. Additionally, create another subclass `HybridCar` that inherits from both `Car` and `Motorcycle` and adds a method `charge_battery()`.
   - **File:** `hybrid_inheritance.py`
