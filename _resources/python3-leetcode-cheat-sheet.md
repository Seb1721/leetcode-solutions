# Python 3 + LeetCode Quick Reference

Use **Python3** on LeetCode. This guide assumes Python 3.14 syntax, but nearly all of it works on Python 3.9+.

## 1. Variables and basic types

```python
age = 22                 # int
price = 9.99             # float
name = "Sebastian"       # str
active = True            # bool
nothing = None           # NoneType

type(age)                # <class 'int'>
int("42")                # 42
str(42)                  # "42"
float("3.5")             # 3.5
```

Python variables do not require type declarations. Names are case-sensitive.

```python
count = 1
Count = 2                # different variable

x, y = 10, 20            # multiple assignment
x, y = y, x              # swap values
```

## 2. Arithmetic and comparisons

```python
a + b                    # addition
a - b                    # subtraction
a * b                    # multiplication
a / b                    # decimal division: 5 / 2 == 2.5
a // b                   # floor division: 5 // 2 == 2
a % b                    # remainder
a ** b                   # exponent: 2 ** 3 == 8

a == b                   # equal values
a != b                   # not equal
a < b
a <= b
a > b
a >= b

x and y
x or y
not x
```

Useful numeric helpers:

```python
abs(-5)                  # 5
min(4, 8)                # 4
max(4, 8)                # 8
round(3.14159, 2)        # 3.14
pow(2, 3)                # 8
divmod(17, 5)            # (3, 2): quotient and remainder
```

## 3. Conditions

```python
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

status = "adult" if age >= 18 else "minor"
```

Python uses indentation instead of braces.

Falsy values include `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, and `set()`.

```python
if nums:                  # true when nums is not empty
    print("has values")
```

## 4. Loops

```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 6):     # 2, 3, 4, 5
    print(i)

for i in range(10, 0, -1):
    print(i)

for value in nums:
    print(value)

for i, value in enumerate(nums):
    print(i, value)

while left < right:
    left += 1

for x in nums:
    if x < 0:
        continue          # skip this iteration
    if x == target:
        break             # exit loop
```

Loop through two collections together:

```python
for a, b in zip(list1, list2):
    print(a, b)
```

## 5. Functions

```python
def add(a: int, b: int) -> int:
    return a + b

def greet(name="friend"):
    return f"Hello, {name}"
```

LeetCode commonly supplies this structure:

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Write your solution here.
        return []
```

- `self` refers to the current `Solution` object.
- Do not normally call the method yourself; LeetCode does that.
- Return the requested answer instead of printing it.

## 6. Lists (dynamic arrays)

```python
nums = [10, 20, 30]
nums[0]                   # 10
nums[-1]                  # 30
nums[1:3]                 # [20, 30]
nums[::-1]                # reversed copy

nums.append(40)           # add at end: O(1) amortized
nums.pop()                # remove/return last: O(1)
nums.insert(1, 15)        # insert by index: O(n)
nums.pop(1)               # remove by index: O(n)
nums.remove(20)           # remove first matching value: O(n)

len(nums)
sum(nums)
min(nums)
max(nums)
target in nums            # O(n)
```

Sorting:

```python
nums.sort()                       # modifies nums
nums.sort(reverse=True)
ordered = sorted(nums)            # returns new list
words.sort(key=len)               # shortest first
pairs.sort(key=lambda pair: pair[1])
```

List comprehensions:

```python
squares = [x * x for x in range(5)]
evens = [x for x in nums if x % 2 == 0]
matrix = [[0] * cols for _ in range(rows)]
```

Do not create a matrix with `[[0] * cols] * rows`; the rows would reference the same list.

## 7. Strings

Strings are immutable: operations produce new strings.

```python
s = "leetcode"
s[0]                      # "l"
s[-1]                     # "e"
s[1:4]                    # "eet"
s[::-1]                   # reverse
len(s)

s.lower()
s.upper()
s.strip()                  # remove surrounding whitespace
s.startswith("leet")
s.endswith("code")
s.find("code")             # index or -1
s.replace("leet", "road")
s.split()                  # split on whitespace
"a,b,c".split(",")         # ["a", "b", "c"]
"-".join(["a", "b"])      # "a-b"

s.isalpha()
s.isdigit()
s.isalnum()
```

Characters and ASCII/Unicode values:

```python
ord("a")                  # 97
chr(97)                   # "a"
```

Efficiently build a string:

```python
characters = []
characters.append("a")
characters.append("b")
result = "".join(characters)
```

## 8. Dictionaries (hash maps)

Use a dictionary to map a key to a value. Average lookup, insertion, and deletion are `O(1)`.

```python
ages = {"Ana": 20, "Ben": 22}
ages["Ana"]               # 20
ages["Cal"] = 19

"Ana" in ages             # checks keys
ages.get("Dan", 0)        # return 0 if missing
ages.pop("Ana")

for key in ages:
    print(key)

for value in ages.values():
    print(value)

for key, value in ages.items():
    print(key, value)
```

Frequency counter:

```python
counts = {}
for value in nums:
    counts[value] = counts.get(value, 0) + 1
```

Or:

```python
from collections import Counter

counts = Counter(nums)
counts[value]
counts.most_common(1)
```

## 9. Sets

A set stores unique values. Average membership, insertion, and deletion are `O(1)`.

```python
seen = set()
seen.add(5)
seen.remove(5)             # error if missing
seen.discard(5)            # safe if missing
5 in seen

unique = set(nums)
```

Set operations:

```python
a | b                      # union
a & b                      # intersection
a - b                      # difference
a ^ b                      # values in one set but not both
```

## 10. Tuples

Tuples are immutable and can be dictionary keys or set elements.

```python
point = (3, 4)
x, y = point

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = {(0, 0), (1, 0)}
```

## 11. Stack, queue, and deque

### Stack: last in, first out

```python
stack = []
stack.append(value)        # push
value = stack.pop()        # pop
top = stack[-1]            # peek
```

### Queue: first in, first out

```python
from collections import deque

queue = deque()
queue.append(value)        # add right
value = queue.popleft()    # remove left: O(1)
```

Do not repeatedly use `list.pop(0)` for a queue; it is `O(n)`.

`deque` can operate at both ends:

```python
d.append(x)
d.appendleft(x)
d.pop()
d.popleft()
```

## 12. Heaps / priority queues

Python's `heapq` is a min-heap.

```python
import heapq

heap = []
heapq.heappush(heap, 5)     # O(log n)
heapq.heappush(heap, 2)
smallest = heapq.heappop(heap)
smallest = heap[0]          # peek

heapq.heapify(nums)         # convert list in O(n)
```

Simulate a max-heap with negative numbers:

```python
heapq.heappush(heap, -value)
largest = -heapq.heappop(heap)
```

For priority plus data, push tuples:

```python
heapq.heappush(heap, (priority, value))
priority, value = heapq.heappop(heap)
```

## 13. Useful standard-library tools

```python
from collections import Counter, defaultdict, deque
from math import ceil, floor, gcd, inf, sqrt
from bisect import bisect_left, bisect_right
```

`defaultdict`:

```python
graph = defaultdict(list)
graph["A"].append("B")

counts = defaultdict(int)
counts["x"] += 1
```

Infinity:

```python
best = float("inf")
worst = float("-inf")
# or: from math import inf
```

Binary-search insertion positions:

```python
i = bisect_left(nums, target)     # first index >= target
j = bisect_right(nums, target)    # first index > target
```

## 14. Common LeetCode patterns

### Hash-map lookup: Two Sum

```python
seen = {}

for i, number in enumerate(nums):
    needed = target - number
    if needed in seen:
        return [seen[needed], i]
    seen[number] = i
```

### Two pointers

```python
left, right = 0, len(nums) - 1

while left < right:
    if nums[left] + nums[right] < target:
        left += 1
    else:
        right -= 1
```

### Sliding window

```python
left = 0
window_sum = 0

for right, value in enumerate(nums):
    window_sum += value

    while window_sum > target:
        window_sum -= nums[left]
        left += 1

    window_length = right - left + 1
```

### Binary search

```python
left, right = 0, len(nums) - 1

while left <= right:
    middle = left + (right - left) // 2

    if nums[middle] == target:
        return middle
    if nums[middle] < target:
        left = middle + 1
    else:
        right = middle - 1

return -1
```

### Breadth-first search (BFS)

```python
from collections import deque

queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```

### Depth-first search (DFS)

```python
def dfs(node):
    if node in visited:
        return

    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor)
```

### Grid traversal

```python
rows, cols = len(grid), len(grid[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for dr, dc in directions:
    new_row, new_col = row + dr, col + dc

    if 0 <= new_row < rows and 0 <= new_col < cols:
        pass
```

### Prefix sums

```python
prefix = [0]

for number in nums:
    prefix.append(prefix[-1] + number)

# Sum from index left through right, inclusive:
range_sum = prefix[right + 1] - prefix[left]
```

## 15. Complexity quick reference

| Operation | Typical complexity |
|---|---:|
| List access by index | `O(1)` |
| List append/pop from end | `O(1)` amortized |
| List insert/delete near beginning | `O(n)` |
| Search a list/string | `O(n)` |
| Dictionary/set lookup | `O(1)` average |
| Heap push/pop | `O(log n)` |
| Sort | `O(n log n)` |
| Binary search in sorted data | `O(log n)` |
| Nested loop over all pairs | `O(n²)` |

Common input-size intuition:

- `n <= 20`: exponential/backtracking may be possible.
- `n <= 1,000`: `O(n²)` may be possible.
- `n <= 100,000`: usually aim for `O(n)` or `O(n log n)`.
- Very large `n`: often aim for `O(n)` or `O(log n)`.

These are guidelines, not guarantees; constant factors and time limits matter.

## 16. Common mistakes

```python
# Assignment versus comparison
x = 5                     # assign
x == 5                    # compare

# None comparison
if value is None:         # preferred
    pass

# Copy versus alias
b = a                     # same list object
b = a.copy()              # shallow copy
b = a[:]                  # shallow copy

# Sorting
result = nums.sort()       # WRONG: result becomes None
nums.sort()                # modifies nums
result = sorted(nums)      # creates new list

# Off-by-one
range(n)                   # 0 through n - 1
```

Do not modify a dictionary or set's size while directly iterating through it. Iterate over a copy if necessary.

## 17. Problem-solving checklist

1. Restate the input and required output.
2. Work through one small example manually.
3. Identify the brute-force solution first.
4. Check whether a hash map, set, two pointers, sliding window, stack, queue, or binary search removes repeated work.
5. State your expected time and space complexity.
6. Test empty/minimum input, one element, duplicates, negatives, and boundary indices.
7. Submit only after you can explain why the solution works.

## 18. Minimal starting template

```python
class Solution:
    def solve(self, nums: list[int]) -> int:
        # 1. Initialize data structures.
        answer = 0

        # 2. Process the input.
        for value in nums:
            pass

        # 3. Return, do not merely print.
        return answer
```

The goal is not to memorize every method. Learn which data structure fits the problem, then refer back to the exact syntax until it becomes automatic.
