# Linear systems: three possible outcomes


## Exercise 1: one solution

Solve:

$$
x+y=5
$$

$$
2x-y=1
$$

Subtract twice the first equation from the second:

$$
(2x-y)-2(x+y)=1-2(5)
$$

$$
-3y=-9
$$

$$
y=3
$$

Substitute into the first equation:

$$
x+3=5
$$

$$
x=2
$$

Therefore:

$$
(x,y)=(2,3)
$$

Check both original equations:

$$
2+3=5
$$

$$
2(2)-3=1
$$

Both variables are determined, so there is one solution.

## Exercise 2: infinitely many solutions

Solve:

$$
x+y=5
$$

$$
2x+2y=10
$$

Subtract twice the first equation from the second:

$$
(2x+2y)-2(x+y)=10-2(5)
$$

$$
0=0
$$

The second equation adds no new restriction. We still have:

$$
x+y=5
$$

Let $y=t$, where $t$ is any real number. Then:

$$
x=5-t
$$

The full solution is:

$$
(x,y)=(5-t,t)
$$

Equivalently:

$$
(x,y)=(5,0)+t(-1,1)
$$

Check for every value of $t$:

$$
(5-t)+t=5
$$

$$
2(5-t)+2t=10
$$

Examples include $(5,0)$, $(4,1)$ and $(2,3)$.

There are infinitely many solutions because one variable is free.

## Exercise 3: no solution

Solve:

$$
x+y=5
$$

$$
2x+2y=12
$$

Subtract twice the first equation from the second:

$$
(2x+2y)-2(x+y)=12-2(5)
$$

$$
0=2
$$

This is impossible. No pair $(x,y)$ can satisfy both equations.

A row with zero coefficients does not decide the answer by itself. We also need to inspect its right-hand side.

## Comparing the results

| Final condition | Meaning |
| --- | --- |
| Every variable is determined | One solution |
| A redundant equation such as $0=0$, with free variables remaining | Infinitely many solutions |
| A contradiction such as $0=2$ | No solution |

A redundant equation does not always mean infinitely many solutions. Other equations could still determine every variable.

## Why row operations work

The algorithm uses three operations:

1. Swap two equations.
2. Divide an equation by a nonzero number.
3. Subtract a multiple of one equation from another.

These operations preserve the solution set because they are reversible.

For example, after subtracting twice the first equation from the second, we can recover the original second equation by adding twice the first equation back.

## From calculations to an algorithm

1. Form the augmented matrix containing the coefficients and constants.
2. Search a coefficient column for a nonzero pivot.
3. Swap the pivot row into position if necessary.
4. Divide the row by its pivot.
5. Subtract multiples of this row from every other row.
6. Repeat for the remaining columns.
7. Check for contradictions.
8. If the system is consistent, identify pivot variables and free variables.
9. Construct the solution.

Eliminating entries both above and below each pivot produces reduced row echelon form. This method is called Gauss–Jordan elimination.

It extends the earlier Gaussian elimination lesson, which used back substitution.

## Mathematical meaning of the code

[Open the Python script](classify_systems.py).

| Code decision | Mathematical reason |
| --- | --- |
| Find a nonzero pivot | We cannot divide by zero |
| Skip a column without an available pivot | That variable may be free |
| Check inconsistent rows first | One contradiction rules out all solutions |
| Set free variables to zero | Find one particular solution |
| Build a direction for each free variable | Describe the remaining freedom |

For a consistent system, the script returns a solution of the form:

$$
x=p+t_1v_1+\cdots+t_kv_k
$$

Here:

- $p$ is a particular solution.
- Each $v_i$ is a direction that can be added without changing $Ax$.
- Each $t_i$ is an arbitrary real number.

The script checks:

$$
Ap=b
$$

and:

$$
Av_i=0
$$

Therefore:

$$
A(p+t_1v_1+\cdots+t_kv_k)=b
$$

The free-variable construction describes all solutions, not just a few examples.

## Run the script

From the repository root:

```bash
python linear_algebra/classify_systems.py
```

Expected classifications:

```text
Exercise 1: unique
Exercise 2: infinite
Exercise 3: none
```

The script prints the row operations and checks consistent solutions by substitution.

## Further exercises and answers

### A. Change the constant

Replace 12 in Exercise 3 with 10.

The contradiction becomes $0=0$, so the system has infinitely many solutions.

### B. Change a coefficient

Solve:

$$
x+y=5,\qquad 2x+3y=10
$$

Subtract twice the first equation from the second:

$$
y=0
$$

Therefore $x=5$, giving $(5,0)$.

### C. Start with a zero coefficient

Solve:

$$
y=3,\qquad x+y=5
$$

A row swap provides a pivot in the first column.

The solution is $(2,3)$.

### D. Use three variables

Solve:

$$
x+y+z=4
$$

Let $y=s$ and $z=t$. Then:

$$
(x,y,z)=(4-s-t,s,t)
$$

Equivalently:

$$
(x,y,z)=(4,0,0)+s(-1,1,0)+t(-1,0,1)
$$

Try adding these examples to the script and compare its output with the worked answers.

## Implementation limits

The solver uses Python's Fraction type for exact rational arithmetic.

Use integers or strings such as `"0.1"` and `"1/3"` when exact inputs matter. The solver treats these values as exact numbers, not uncertain measurements.

This approach is useful for small learning examples. Fractions can become expensive for large systems.

The earlier floating-point solver remains in the repository for comparison.
