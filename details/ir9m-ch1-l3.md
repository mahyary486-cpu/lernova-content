# Union and intersection

The union of two sets combines all their elements, and the intersection keeps only the elements they share.

## Key ideas

- The union of A and B, written A ∪ B, is the set of all elements that belong to A, or to B, or to both. Each element is listed once.
- The intersection of A and B, written A ∩ B, is the set of all elements that belong to both A and B.
- If A and B have no common element, then A ∩ B = ∅. We say that A and B are disjoint sets.
- Useful facts: A ∪ A = A, A ∩ A = A, A ∪ ∅ = A, A ∩ ∅ = ∅. Also A ∩ B ⊆ A ⊆ A ∪ B.
- Both operations are commutative: A ∪ B = B ∪ A and A ∩ B = B ∩ A.
- If A ⊆ B, then A ∪ B = B and A ∩ B = A.
- Counting rule for finite sets: n(A ∪ B) = n(A) + n(B) - n(A ∩ B). We subtract n(A ∩ B) because the shared elements were counted twice.
- If A and B are disjoint, the rule becomes n(A ∪ B) = n(A) + n(B).
- Word clues: "or" usually means union, and "and" usually means intersection.

## Worked examples

Example 1. Let A = {1, 2, 3, 4} and B = {3, 4, 5, 6}. Find A ∪ B and A ∩ B.

Step 1: Put all elements together and write each once: A ∪ B = {1, 2, 3, 4, 5, 6}.
Step 2: Find the elements in both sets. Only 3 and 4 appear in both. So A ∩ B = {3, 4}.
Step 3: Check the counting rule: n(A) + n(B) - n(A ∩ B) = 4 + 4 - 2 = 6. This equals n(A ∪ B) = 6.

Example 2. Let A be the multiples of 2 that are at most 12, and B be the multiples of 3 that are at most 12. Find A ∪ B and A ∩ B.

Step 1: A = {2, 4, 6, 8, 10, 12} and B = {3, 6, 9, 12}.
Step 2: The common elements are 6 and 12. So A ∩ B = {6, 12}.
Step 3: Combine and remove repeats: A ∪ B = {2, 3, 4, 6, 8, 9, 10, 12}.
Step 4: Check: 6 + 4 - 2 = 8, and A ∪ B has 8 elements.

Example 3. In a class of 30 students, 18 play football, 15 play volleyball, and 7 play both. How many students play at least one of the two sports? How many play neither?

Step 1: Let F be the football players and V the volleyball players. Then n(F) = 18, n(V) = 15, n(F ∩ V) = 7.
Step 2: Students who play at least one sport: n(F ∪ V) = 18 + 15 - 7 = 26.
Step 3: Students who play neither: 30 - 26 = 4.
Step 4: Check: only football = 18 - 7 = 11, only volleyball = 15 - 7 = 8, both = 7. Then 11 + 8 + 7 = 26. Correct.

## Common mistakes

- Writing a repeated element in a union. In {1, 2, 3} ∪ {3, 4}, the number 3 appears once: {1, 2, 3, 4}.
- Adding n(A) + n(B) for a union without subtracting the common elements.
- Mixing up the symbols ∪ and ∩. A helpful picture: ∪ looks like a cup that collects everything.
- Writing A ∩ B = 0 for disjoint sets. The correct answer is the empty set, A ∩ B = ∅.

## Remember

- Union means everything in either set; intersection means only what is in both.
- n(A ∪ B) = n(A) + n(B) - n(A ∩ B).
- Disjoint sets have an empty intersection.
