# Common Python Syntax Examples

This guide covers common Python 3 syntax, with several comparisons to Java and examples useful for beginning LeetCode problems.

## 1. Comments

```python
# This is a single-line comment.

number = 10  # Comments can also follow code.
```

Python uses `#` rather than Java's `//` for single-line comments.

## 2. Variables

Python infers a variable's type, so you do not write `int`, `String`, and similar type names before variables.

```python
age = 22
price = 19.99
name = "Sebastian"
is_student = True
result = None
```

The comparable Java declarations would be:

```java
int age = 22;
String name = "Sebastian";
```

Multiple assignment and swapping:

```python
x, y = 10, 20
x, y = y, x
```

## 3. Printing

```python
print("Hello")
print(age)
print("Age:", age)
```

Formatted strings, called f-strings, let you insert expressions inside `{}`:

```python
name = "Sebastian"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

## 4. Arithmetic

```python
a = 10
b = 3

a + b    # 13: addition
a - b    # 7: subtraction
a * b    # 30: multiplication
a / b    # 3.333...: regular division
a // b   # 3: floor division
a % b    # 1: remainder
a ** b   # 1000: exponent
```

Updating variables:

```python
count += 1
count -= 1
total *= 2
```

Python does not have Java's `count++` or `count--` syntax.

## 5. Comparisons and Boolean operators

```python
x == y      # Equal values
x != y      # Unequal values
x < y
x <= y
x > y
x >= y
```

```python
age >= 18 and has_id
is_student or is_teacher
not is_closed
```

Python uses `and`, `or`, and `not` instead of Java's `&&`, `||`, and `!`.

## 6. Conditions

```python
age = 22

if age >= 21:
    print("Can enter")
elif age >= 18:
    print("Adult, but under 21")
else:
    print("Minor")
```

Python uses indentation instead of braces to define the contents of each branch. A condition ends with a colon (`:`).

A one-line conditional expression looks like this:

```python
status = "adult" if age >= 18 else "minor"
```

## 7. `for` loops

Loop through the values in a list:

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

Loop through a sequence of integers:

```python
for i in range(5):
    print(i)
```

`range(5)` produces `0, 1, 2, 3, 4`. The ending value is excluded.

```python
range(5)          # 0 through 4
range(2, 6)       # 2 through 5
range(0, 10, 2)   # 0, 2, 4, 6, 8
range(5, 0, -1)   # 5, 4, 3, 2, 1
```

Loop using indexes:

```python
for i in range(len(numbers)):
    print(i, numbers[i])
```

Get the index and value more cleanly with `enumerate()`:

```python
for i, number in enumerate(numbers):
    print(i, number)
```

## 8. `while` loops

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

Controlling a loop:

```python
for number in numbers:
    if number < 0:
        continue  # Skip the rest of this iteration.

    if number == 100:
        break     # Exit the entire loop.

    print(number)
```

## 9. Functions

```python
def add(a, b):
    return a + b

answer = add(5, 3)
```

With type hints:

```python
def add(a: int, b: int) -> int:
    return a + b
```

- `a: int` says that `a` is expected to be an integer.
- `b: int` says that `b` is expected to be an integer.
- `-> int` says that the function is expected to return an integer.

A default parameter supplies a value when the caller does not provide one:

```python
def greet(name="friend"):
    print(f"Hello, {name}")

greet()             # Hello, friend
greet("Sebastian")  # Hello, Sebastian
```

## 10. Lists

A Python list is similar to Java's `ArrayList`.

```python
numbers = [10, 20, 30]
```

Access and change elements:

```python
numbers[0]      # First element: 10
numbers[-1]     # Last element: 30
numbers[0] = 15
```

Common list operations:

```python
numbers.append(40)      # Add to the end.
numbers.pop()           # Remove and return the last value.
numbers.pop(0)          # Remove and return index 0.
numbers.insert(1, 17)   # Insert 17 at index 1.
numbers.remove(20)      # Remove the first matching value.

len(numbers)
sum(numbers)
min(numbers)
max(numbers)
```

Membership test:

```python
if 20 in numbers:
    print("Found it")
```

List slicing:

```python
numbers = [10, 20, 30, 40, 50]

numbers[1:4]   # [20, 30, 40]
numbers[:3]    # [10, 20, 30]
numbers[2:]    # [30, 40, 50]
numbers[::-1]  # Reversed copy
```

## 11. List comprehensions

A list comprehension is a compact way to create a list:

```python
squares = [number * number for number in range(5)]
# [0, 1, 4, 9, 16]
```

With a condition:

```python
evens = [number for number in numbers if number % 2 == 0]
```

The longer equivalent is:

```python
evens = []

for number in numbers:
    if number % 2 == 0:
        evens.append(number)
```

## 12. Dictionaries

A dictionary is Python's built-in hash map. It stores key-value pairs.

```python
student = {
    "name": "Sebastian",
    "age": 22,
    "major": "Computer Science"
}
```

Accessing and changing values:

```python
student["name"]
student["age"] = 23
student["school"] = "CPP"
```

Check whether a key exists:

```python
if "major" in student:
    print(student["major"])
```

Safely retrieve a value:

```python
student.get("gpa")        # None when missing
student.get("gpa", 0.0)   # 0.0 when missing
```

Loop through a dictionary:

```python
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)
```

Frequency-counting pattern:

```python
counts = {}

for number in numbers:
    counts[number] = counts.get(number, 0) + 1
```

## 13. Sets

A set stores unique values and offers fast average-time membership checks.

```python
seen = set()

seen.add(10)
seen.add(20)
seen.add(10)  # A duplicate is not added.

if 10 in seen:
    print("Already encountered")
```

Removing values:

```python
seen.remove(10)   # Raises an error if 10 is missing.
seen.discard(10)  # Safe when 10 is missing.
```

Remove duplicate values from a list:

```python
numbers = [1, 1, 2, 3, 3]
unique_numbers = set(numbers)
```

## 14. Tuples

A tuple is an immutable sequence, meaning its contents cannot be changed after creation.

```python
point = (10, 20)

x = point[0]
y = point[1]
```

Tuple unpacking:

```python
x, y = point
```

Tuples are frequently used for coordinates and directions:

```python
directions = [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
```

## 15. Strings

```python
word = "leetcode"

word[0]     # "l"
word[-1]    # "e"
len(word)   # 8
```

Common methods:

```python
word.upper()
word.lower()
word.startswith("leet")
word.endswith("code")
word.replace("leet", "road")
```

Split and join:

```python
sentence = "Python is useful"
words = sentence.split()
# ["Python", "is", "useful"]

result = "-".join(words)
# "Python-is-useful"
```

Loop through characters:

```python
for character in word:
    print(character)
```

Strings are immutable, so this is invalid:

```python
word[0] = "L"  # Error
```

Instead, create a new string:

```python
word = "L" + word[1:]
```

## 16. Sorting

Modify an existing list:

```python
numbers.sort()
numbers.sort(reverse=True)
```

Create a new sorted list:

```python
ordered = sorted(numbers)
```

Custom sorting:

```python
words = ["cat", "elephant", "dog"]
words.sort(key=len)
# ["cat", "dog", "elephant"]
```

Do not assign the result of `.sort()`:

```python
ordered = numbers.sort()  # Wrong: ordered becomes None.
```

## 17. Classes

```python
class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def describe(self):
        return f"{self.year} {self.make}"
```

Creating and using an object:

```python
car = Car("Honda", 2018)

print(car.make)
print(car.describe())
```

- `__init__` is similar to a Java constructor.
- `self` is similar to Java's `this`.
- Python fields do not have to be declared separately before assignment.

## 18. Common LeetCode syntax

LeetCode usually supplies a class and method header:

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for number in nums:
            if number in seen:
                return True

            seen.add(number)

        return False
```

Other frequently used patterns:

```python
# Index and value
for index, value in enumerate(nums):
    print(index, value)

# Values from two lists
for first, second in zip(list1, list2):
    print(first, second)

# Stack
stack = []
stack.append(value)
top = stack.pop()
```

A queue should use `deque` so removing from the front is efficient:

```python
from collections import deque

queue = deque()
queue.append(value)
value = queue.popleft()
```

## Java-to-Python translation

| Java | Python |
|---|---|
| `true`, `false` | `True`, `False` |
| `null` | `None` |
| `&&`, `||`, `!` | `and`, `or`, `not` |
| `else if` | `elif` |
| `ArrayList<Integer>` | `list[int]` |
| `HashMap<K, V>` | `dict` |
| `HashSet<T>` | `set` |
| `this` | `self` |
| `System.out.println(x)` | `print(x)` |
| `x++` | `x += 1` |
| `{ }` blocks | Indentation |
| `;` | Usually omitted |

## What to learn first

For introductory LeetCode problems, prioritize:

1. Variables and comparisons
2. Conditions
3. `for` and `while` loops
4. Functions and return values
5. Lists
6. Dictionaries
7. Sets
8. `range()`, `len()`, and `enumerate()`

These features are enough to begin solving array, string, hash-map, and set problems in Python.
