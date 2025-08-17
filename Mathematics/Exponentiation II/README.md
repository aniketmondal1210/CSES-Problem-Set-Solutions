# Exponentiation II

## Problem
Your task is to efficiently calculate values `a^(b^c) mod (10^9+7)`.

> **Note:** In this task, we assume that `0^0 = 1`.

---

## Input
- The first input line contains an integer `n`: the number of calculations.  
- After this, there are `n` lines, each containing three integers `a, b, c`.

---

## Output
- Print each value `a^(b^c) mod (10^9+7)`.

---

## Constraints
- 1 ≤ n ≤ 10^5  
- 0 ≤ a, b, c ≤ 10^9  
- Time Limit: **1.00 s**  
- Memory Limit: **512 MB**

---

## Example

### Input

3

3 7 1

15 2 2

3 4 5


### Output

2187

50625

763327764


---

## Explanation
1. `3^(7^1) = 3^7 = 2187`  
2. `15^(2^2) = 15^4 = 50625`  
3. `3^(4^5) = 3^1024 mod 1e9+7 = 763327764`  

---
