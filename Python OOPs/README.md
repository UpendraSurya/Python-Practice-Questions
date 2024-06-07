# Python OOP Concepts: Inheritance and Abstraction

This repository contains a set of Python exercises focusing on object-oriented programming (OOP) concepts, particularly inheritance and abstraction.

## Questions

### 1. Book and EBook Classes (Inheritance)    

- **Question:** Create a class `Book` with attributes `title` and `author`, and a method `get_info()` that returns a string with the book's title and author. Then create a subclass `EBook` that adds an attribute `file_size` and overrides the `get_info()` method to include the file size in the returned string. Write code to demonstrate this functionality.

### 2. Transport, Car, and Bicycle Classes (Abstraction, Inheritance)

- **Question:** Define an abstract class `Transport` with an abstract method `move()`. Create two subclasses `Car` and `Bicycle`, each implementing the `move()` method to print specific messages. Also, add an attribute `speed` to each subclass and a method `get_speed()` to return the speed. Write a program to create instances of `Car` and `Bicycle` and demonstrate their functionality.

### 3. BankAccount and SavingsAccount Classes (Inheritance)

- **Question:** Implement a class `BankAccount` with attributes `account_number` and `balance`. Create a subclass `SavingsAccount` that adds an attribute `interest_rate` and a method `apply_interest()` to update the balance by applying the interest rate. Write a program to create an instance of `SavingsAccount`, deposit an amount, apply interest, and print the updated balance.

### 4. Shape, Square, and Triangle Classes (Abstraction, Inheritance)

- **Question:** Implement a class hierarchy with an abstract class `Shape` and concrete subclasses `Square` and `Triangle`. Each subclass should implement a method `perimeter()` to calculate the perimeter of the shape. Write a program to create instances of `Square` and `Triangle` and calculate their perimeters.

### 5. Employee and Manager Classes (Inheritance)

- **Question:** Define a class `Employee` with attributes `name` and `salary`. Implement a method `give_raise()` to increase the salary by a given percentage. Create a subclass `Manager` that adds an attribute `bonus` and overrides the `give_raise()` method to also add the bonus to the salary. Demonstrate the functionality by creating instances of `Employee` and `Manager` and applying raises.

### 6. VowelConsonantCount (static)

Write a Python class named "StringAnalyzer" with a static method named "count_vowels" that takes a string as input and prints the count of vowels (a, e, i, o, u) in the string. Additionally, add another static method named "count_consonants" that takes a string as input and prints the count of consonants (non-vowel alphabets) in the string. Test both methods with sample strings.   give the anwer and give a name to it
