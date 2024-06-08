Certainly! Here's a similar template tailored for Python exception handling questions:

---

# Python Exception Handling

This repository contains a set of Python exercises focusing on exception handling.

## Questions

### 1. Handling Multiple Exceptions with a Single `except` Block

- **Question:** Explain and demonstrate how you can handle multiple exceptions with a single `except` block in Python. Provide an example where a block of code might raise a `ValueError` or a `ZeroDivisionError`, and show how you would handle these exceptions together.

### 2. File Reading with Exception Handling

- **Question:** Write a Python function that attempts to open and read a file. If the file does not exist, handle the exception and return a specific message. If any other exception occurs, return a generic error message.

### 3. The Role of the `finally` Block

- **Question:** Describe the role of the `finally` block in Python exception handling. Provide an example where the `finally` block ensures that certain cleanup actions are always performed, regardless of whether an exception occurs.

### 4. Using `raise` to Propagate Exceptions

- **Question:** Demonstrate how the `raise` statement can be used to propagate an exception up the call stack. Write a function that raises an exception and another function that calls this function and handles the exception.

### 5. Simulating a Simple Transaction System

- **Question:** Write a program that simulates a simple banking transaction system. The program should raise a custom exception if a withdrawal amount exceeds the available balance and handle this exception appropriately to ensure the program does not crash.
