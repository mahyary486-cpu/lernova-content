# Complement of a set

The complement of a set A is the set of all elements of the universal set that are not in A.

## Key ideas

- The universal set U is the large set that contains all the elements we are talking about in a problem. Every other set in the problem is a subset of U.
- The complement of A, written A' (some books write A^c), is the set of elements of U that are not in A. So A' = {x ∈ U | x ∉ A}.
- Facts about complements: A ∪ A' = U, A ∩ A' = ∅, (A')' = A, U' = ∅ and ∅' = U.
- For finite sets: n(A') = n(U) - n(A).
- The difference of two sets, A - B, is the set of elements that are in A but not in B. It can also be written A ∩ B'.
- De Morgan's laws connect complement, union and intersection: (A ∪ B)' = A' ∩ B' and (A ∩ B)' = A' ∪ B'.
- The complement always depends on the universal set. The same set A has a different complement if U changes.

## Worked examples

Example 1. Let U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10} and A = {2, 4, 6, 8, 10}. Find A' and check n(A') = n(U) - n(A).

Step 1: A' contains the elements of U that are not in A.
Step 2: Remove 2, 4, 6, 8, 10 from U. What remains is A' = {1, 3, 5, 7, 9}.
Step 3: n(U) = 10 and n(A) = 5, so n(U) - n(A) = 5. The set A' has 5 elements. Correct.

Example 2. Let U = {1, 2, 3, 4, 5, 6, 7, 8}, A = {1, 2, 3, 4} and B = {3, 4, 5, 6}. Check that (A ∪ B)' = A' ∩ B'.

Step 1: A ∪ B = {1, 2, 3, 4, 5, 6}. Then (A ∪ B)' = {7, 8}.
Step 2: A' = {5, 6, 7, 8} and B' = {1, 2, 7, 8}.
Step 3: The common elements of A' and B' are 7 and 8. So A' ∩ B' = {7, 8}.
Step 4: Both sides equal {7, 8}, so the law holds in this example.

Example 3. With the same U, A and B as in Example 2, find A - B, B - A and A ∩ B'. Then find (A ∩ B)' and A' ∪ B'.

Step 1: A - B contains elements of A that are not in B. Remove 3 and 4 from A to get {1, 2}.
Step 2: B - A contains elements of B that are not in A. Remove 3 and 4 from B to get {5, 6}.
Step 3: A ∩ B' = {1, 2, 3, 4} ∩ {1, 2, 7, 8} = {1, 2}. This equals A - B.
Step 4: A ∩ B = {3, 4}, so (A ∩ B)' = {1, 2, 5, 6, 7, 8}.
Step 5: A' ∪ B' = {5, 6, 7, 8} ∪ {1, 2, 7, 8} = {1, 2, 5, 6, 7, 8}. It equals (A ∩ B)', so the second law holds too.

## Common mistakes

- Finding a complement without knowing the universal set. Always read or write down U first.
- Confusing A' with A - B. The complement removes A from U, while A - B removes B from A.
- Assuming that A - B = B - A. In general they are different sets.
- Forgetting that elements of U outside both A and B still belong to (A ∪ B)'.

## Remember

- A ∪ A' = U and A ∩ A' = ∅.
- n(A') = n(U) - n(A).
- The complement of a union is the intersection of the complements, and the complement of an intersection is the union of the complements.
