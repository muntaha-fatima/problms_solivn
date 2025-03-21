﻿# pPoblms_solivng
# Python Utility Functions

This project contains three useful Python functions:

1. **Reverse a String** 🌀
2. **Count Vowels in a String** 🔤
3. **Find the Sum of Digits in a Number** 🔢

---

## 🔄 1. Reverse a String
This function takes a string and returns the reversed version of it.

### ✨ Code:
```python
def reverse_string(s):
    return s[::-1]  # String ko reverse karna

# Example Use
print(reverse_string("hello"))  # Output: "olleh"
```
### 📌 Explanation:
- **Slicing technique (`[::-1]`)** ka use karke string ko reverse kiya jata hai.

---

## 🔢 2. Count Vowels in a String
This function counts the number of vowels (a, e, i, o, u) in a given string.

### ✨ Code:
```python
def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}  # Set of vowels
    count = sum(1 for char in s.lower() if char in vowels)  # Counting vowels
    return count

# Example Use
print(count_vowels("Apple"))  # Output: 2
```
### 📌 Explanation:
- **String ko lowercase mein convert kiya jata hai** taake uppercase vowels bhi detect ho sakein.
- **Set (`{}`) ka use** kiya gaya vowels ko efficiently check karne ke liye.

---

## 🔢 3. Sum of Digits in a Number
This function takes a non-negative integer and returns the sum of its digits.

### ✨ Code:
```python
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))  # Digits ka sum lena

# Example Use
print(sum_of_digits(1234))  # Output: 10
```
### 📌 Explanation:
- **Number ko string mein convert kiya** taake uske digits ko loop se extract kar sakein.
- **`sum(int(digit) for digit in str(n))`** har digit ko integer banake uska sum nikalta hai.

---

## 🚀 **How to Run?**
1. Copy and paste the code into a Python file.
2. Run the script and test different inputs.

🎯 **These functions can be used in various applications like data processing, text analysis, and more!** 😃






