# Gaussian elimination — from equations to an algorithm

## Goal

Solve a system by eliminating variables, then implement the same steps in Python.

[Runnable script](gaussian_elimination.py)

This lesson and its code were prepared with AI assistance.

## Problem

Solve:

$$
2x+y-z=8
$$

$$
-3x-y+2z=-11
$$

$$
-2x+y+2z=-3
$$

## 1. Write the augmented matrix

The last column contains the right-hand sides.

$$
\left[
\begin{array}{ccc|c}
2&1&-1&8\\
-3&-1&2&-11\\
-2&1&2&-3
\end{array}
\right]
$$

## 2. Eliminate x from the second equation

Use:

$$
R_2\leftarrow R_2+\frac32R_1
$$

This gives:

$$
\left[
\begin{array}{ccc|c}
2&1&-1&8\\
0&\frac12&\frac12&1\\
-2&1&2&-3
\end{array}
\right]
$$

## 3. Eliminate x from the third equation

Use:

$$
R_3\leftarrow R_3+R_1
$$

Then:

$$
\left[
\begin{array}{ccc|c}
2&1&-1&8\\
0&\frac12&\frac12&1\\
0&2&1&5
\end{array}
\right]
$$

## 4. Eliminate y from the third equation

Use:

$$
R_3\leftarrow R_3-4R_2
$$

The matrix becomes upper triangular:

$$
\left[
\begin{array}{ccc|c}
2&1&-1&8\\
0&\frac12&\frac12&1\\
0&0&-1&1
\end{array}
\right]
$$

## 5. Back substitution

From the third row:

$$
-z=1\quad\Rightarrow\quad z=-1
$$

From the second row:

$$
\frac12y+\frac12(-1)=1
$$

$$
y=3
$$

From the first row:

$$
2x+3-(-1)=8
$$

$$
x=2
$$

Therefore:

$$
\boxed{x=2,\qquad y=3,\qquad z=-1}
$$

## 6. Check all three equations

$$
2(2)+3-(-1)=8
$$

$$
-3(2)-3+2(-1)=-11
$$

$$
-2(2)+3+2(-1)=-3
$$

All three equations are satisfied.

## How the script follows this method

1. Form an augmented matrix.
2. Choose a pivot in each column.
3. Swap rows if needed.
4. Eliminate entries below the pivot.
5. Work backwards to obtain the solution.
6. Substitute the answer into the original system.

The script uses partial pivoting: it chooses the remaining row with the largest absolute entry in the current column.

Its intermediate rows may therefore differ from the hand calculation, but the solution should agree.

## Running it

From the repository folder:

```bash
python linear_algebra/gaussian_elimination.py
```

The script includes a system that requires a row swap and a singular system that it rejects.

It is a small learning implementation for square systems with unique solutions. It does not classify singular systems as inconsistent or having infinitely many solutions.

## Questions to revisit

### Why do row operations preserve the solution?

Swapping equations or adding a multiple of one equation to another preserves the same constraints. These operations can also be reversed.

### Why swap rows?

A zero pivot cannot be used for division. Choosing a larger available pivot also helps limit some numerical errors.

### Does a small residual prove the solution is accurate?

It shows that the computed answer nearly satisfies the equations. For an ill-conditioned system, a small residual does not necessarily imply a small error in the solution.

### What should happen if the matrix is singular?

This script stops. A more general solver would examine the reduced system to distinguish no solution from infinitely many solutions.
