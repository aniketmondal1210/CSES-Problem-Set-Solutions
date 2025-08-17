# Weird Algorithm (Collatz Sequence)

## Problem
Consider an algorithm that takes as input a positive integer `n`.  
- If `n` is even → divide it by 2.  
- If `n` is odd → multiply it by 3 and add 1.  

The algorithm repeats this process until `n` becomes `1`.  

Your task is to **simulate the execution** of the algorithm for a given value of `n`.

---

## Input
- A single integer `n` (1 ≤ n ≤ 10^6)

---

## Output
- Print all values of `n` during the algorithm, in a single line.

---

## Example

### Input

3


### Output

3 10 5 16 8 4 2 1


---

## Explanation
For `n = 3`, the sequence goes:  

3 → 10 → 5 → 16 → 8 → 4 → 2 → 1


---

## Constraints
- 1 ≤ `n` ≤ 10^6  
- Time Limit: **1.00 s**  
- Memory Limit: **512 MB**

---
