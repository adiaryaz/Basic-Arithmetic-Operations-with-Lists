# Basic Arithmetic Operations with Lists

A program to perform fundamental arithmetic calculations using functions and list manipulation.

## 📝 Description

This program demonstrates the use of Python functions and lists to handle basic arithmetic. It takes two integer inputs from the user, stores them in a list, and passes them to a function. This function calculates the difference (subtraction), sum (addition), and product (multiplication) of the two numbers. The results are returned and stored in a specific order within a result list.

-----

## 🎯 Problem Statement

### Input:

  * **Input 1:** An integer (First number, let's call it `a`).
  * **Input 2:** An integer (Second number, let's call it `b`).

### Output:

  * A single list containing three integers in the following order: `[Subtraction, Addition, Multiplication]`.

### Rules:

1.  The program must use a function defined as `aritmatika(angka1, angka2)`.
2.  The arithmetic operations must be calculated as follows:
      * **Subtraction:** `angka1 - angka2`
      * **Addition:** `angka1 + angka2`
      * **Multiplication:** `angka1 * angka2`
3.  The inputs must be stored in a list (`inputUser`) before processing.
4.  The results must be assigned to specific indices in the `hasilAritmatika` list:
      * Index 0: Subtraction result.
      * Index 1: Addition result.
      * Index 2: Multiplication result.

-----

## 💡 Examples

### Example 1

**Input:**

```
10
5
```

**Output:**

```
[5, 15, 50]
```

**Explanation:**

  * Subtraction: $10 - 5 = 5$
  * Addition: $10 + 5 = 15$
  * Multiplication: $10 \times 5 = 50$

### Example 2

**Input:**

```
3
4
```

**Output:**

```
[-1, 7, 12]
```

**Explanation:**

  * Subtraction: $3 - 4 = -1$
  * Addition: $3 + 4 = 7$
  * Multiplication: $3 \times 4 = 12$

### Example 3

**Input:**

```
0
5
```

**Output:**

```
[-5, 5, 0]
```

**Explanation:**

  * Subtraction: $0 - 5 = -5$
  * Addition: $0 + 5 = 5$
  * Multiplication: $0 \times 5 = 0$

-----

## 🚀 How to Use

1.  **Clone this repository**

    ```bash
    git clone https://github.com/adiaryaz/basic-arithmetic-lists.git
    cd basic-arithmetic-lists
    ```

2.  **Run the program** (assuming the file is `Array Season2.py`):

    ```bash
    python "Array Season2.py"
    ```

    Enter two integers on separate lines when prompted to see the result list.
