# LuxDev Python Assignments - Week 4

This repository contains a set of beginner-friendly Python scripts, each focusing on a fundamental programming concept. The scripts are organized under `week4/assignment/` and are designed for hands-on learning and practice.

## Table of Contents

- [Overview](#overview)
- [Directory Structure](#directory-structure)
- [File Descriptions](#file-descriptions)
  - [variable.py](#variablepy)
  - [data_types.py](#data_typespy)
  - [data_structures.py](#data_structurespy)
  - [control_flows.py](#control_flowspy)
  - [loops.py](#loopspy)
  - [funcs.py](#funcspy)
- [Usage Notes](#usage-notes)
- [Contact](#contact)

## Overview

Each script demonstrates core Python concepts through exercises and small challenges. The code is suitable for beginners and those looking to reinforce their understanding of Python basics.

## Directory Structure

```
luxdev/
  week4/
    assignment/
      control_flows.py
      data_structures.py
      data_types.py
      funcs.py
      loops.py
      variable.py
```

## File Descriptions

### variable.py

- **Focus:** Variables and basic input/output.
- **Exercises:**
  - Assigns and prints integer variables.
  - Demonstrates string assignment and printing.
- **Challenge:**
  - Prompts the user for their name and age, then prints a personalized greeting.

### data_types.py

- **Focus:** Python data types and type conversion.
- **Exercises:**
  - Prints the type of various literals (int, float, str).
  - Demonstrates type conversion from string to int.
  - Shows arithmetic operations between different types.
  - Demonstrates string multiplication.
- **Challenge:**
  - Prompts the user for two numbers, adds them, and prints the result and its type.

### data_structures.py

- **Focus:** Lists, dictionaries, tuples, and sets.
- **Exercises:**
  - Accesses elements in a list.
  - Demonstrates dictionary usage.
  - Shows tuple immutability (with a commented-out error line).
  - Handles lists with duplicate values and converts them to sets.
- **Challenge:**
  - Collects user input into a list, converts it to a set, and prints the set.

### control_flows.py

- **Focus:** Conditional statements and logical operators.
- **Exercises:**
  - Checks if a number is positive, negative, or zero.
  - Determines voting eligibility based on age.
  - Finds the largest of three numbers.
  - Demonstrates `and`, `or`, and `not` operators.
- **Challenge:**
  - Implements a grading system that assigns a letter grade based on a numeric score.

### loops.py

- **Focus:** For and while loops, loop control statements.
- **Exercises:**
  - Prints numbers 1 to 10 using a for loop.
  - Repeats user input until 'stop' is entered (while loop).
  - Prints even numbers from 1 to 20.
  - Explains `break` and `continue` (with comments).
- **Challenge:**
  - Implements a number guessing game using a while loop and random number generation.

### funcs.py

- **Focus:** Functions, parameters, return values, and function calls.
- **Exercises:**
  - Defines and calls functions for greeting and addition (with even/odd check).
- **Challenge:**
  - Implements a calculator function supporting +, -, \*, and / (with error handling).
  - Demonstrates calling functions from within another function.
  - Includes a main block to test and demonstrate all functions.

## Usage Notes

- **Python Version:** These scripts are compatible with Python 3.x.
- **User Input:** Many scripts require user input via the terminal. Run them individually using:
  ```bash
  python week4/assignment/<filename>.py
  ```
- **Error Handling:** Some scripts intentionally include lines that will raise errors (e.g., attempting to modify a tuple) for educational purposes. Read comments for guidance.
- **Randomness:** The guessing game in `loops.py` uses the `random` module.

## Contact

For questions or feedback, please contact me.
