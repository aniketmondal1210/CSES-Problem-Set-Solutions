# Exponentiation

## Problem
Your task is to efficiently calculate values `a^b mod (10^9+7)`.

> **Note:** In this task, we assume that `0^0 = 1`.

---

## Input
- The first input line contains an integer `n`: the number of calculations.  
- After this, there are `n` lines, each containing two integers `a` and `b`.

---

## Output
- Print each value `a^b mod (10^9+7)`.

---

## Constraints
- 1 ≤ n ≤ 2·10^5  
- 0 ≤ a, b ≤ 10^9  
- Time Limit: **1.00 s**  
- Memory Limit: **512 MB**

---

## Example

### Input

3
3 4
2 8
123 123


### Output

81
256
921450052


---

## Explanation
- 3^4 = 81  
- 2^8 = 256  
- 123^123 = 921450052 (after modulo 1e9+7)  

---
