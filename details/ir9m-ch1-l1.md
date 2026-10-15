# Sets and subsets

A set is a well-defined collection of objects, and a subset is a set whose members all belong to another set.

## Key ideas

- A set is a collection of objects where it is always clear whether an object belongs or not. The objects are called elements or members. We usually name sets with capital letters such as A, B, C.
- We write a ∈ A to say "a is an element of A", and a ∉ A to say "a is not an element of A".
- Roster method: list the elements inside braces, for example A = {2, 4, 6, 8}. Order does not matter and we do not repeat an element.
- Set-builder method: describe the rule, for example B = {x | x is a natural number and x < 5}. Read it as "the set of all x such that x is a natural number less than 5".
- The empty set, written ∅ or { }, has no elements.
- A is a subset of B, written A ⊆ B, if every element of A is also an element of B. The empty set is a subset of every set, and every set is a subset of itself.
- If A ⊆ B but A ≠ B, then A is a proper subset of B.
- A set with n elements has 2^n subsets. This includes ∅ and the set itself.
- Common number sets: N = {1, 2, 3, ...} are the natural numbers, Z = {..., -2, -1, 0, 1, 2, ...} are the integers.

## Worked examples

Example 1. Write A = {x | x is a natural number and x < 5} by the roster method. Then decide whether 4 ∈ A and 5 ∈ A.

Step 1: Natural numbers start at 1. The natural numbers less than 5 are 1, 2, 3, 4.
Step 2: So A = {1, 2, 3, 4}.
Step 3: 4 is in the list, so 4 ∈ A. 5 is not in the list, so 5 ∉ A.

Example 2. List all subsets of {a, b, c}.

Step 1: Subsets with 0 elements: ∅. That is 1 subset.
Step 2: Subsets with 1 element: {a}, {b}, {c}. That is 3 subsets.
Step 3: Subsets with 2 elements: {a, b}, {a, c}, {b, c}. That is 3 subsets.
Step 4: Subsets with 3 elements: {a, b, c}. That is 1 subset.
Step 5: Total = 1 + 3 + 3 + 1 = 8. This agrees with 2^3 = 8.

Example 3. Let A = {1, 2, 3, 4, 5, 6} and B = {2, 4, 6}. Is B ⊆ A? Is A ⊆ B? How many subsets and proper subsets does B have?

Step 1: Check each element of B. 2 ∈ A, 4 ∈ A, 6 ∈ A. So B ⊆ A.
Step 2: Check A. The element 1 is in A but not in B. So A is not a subset of B.
Step 3: B has 3 elements, so it has 2^3 = 8 subsets.
Step 4: A proper subset cannot be B itself. So B has 8 - 1 = 7 proper subsets.

## Common mistakes

- Mixing up ∈ and ⊆. Use ∈ between an element and a set (2 ∈ A), and ⊆ between two sets ({2} ⊆ A).
- Writing 0 ∈ N. In this course the natural numbers start at 1, so 0 is not a natural number.
- Forgetting the empty set and the set itself when listing subsets.
- Repeating elements, such as {1, 1, 2}. Each element is written once, so this set is just {1, 2}.

## Remember

- ∅ ⊆ A and A ⊆ A for every set A.
- A set with n elements has 2^n subsets and 2^n - 1 proper subsets.
- The order of elements in a set does not matter.
