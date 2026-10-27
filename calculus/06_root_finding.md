# Root finding: bisection and Newton's method

## The problem

Find a value of x for which:

f(x) = 0

Such a value is called a root.

We will compare two methods:

- Bisection: keep halving an interval containing a root.
- Newton's method: use a tangent line to calculate the next estimate.

The first example is:

f(x) = x² − 2

Its positive root is √2. This gives us a known answer against which to check the algorithms.

## 1. Find a starting interval

At x = 1:

f(1) = 1² − 2 = −1

At x = 2:

f(2) = 2² − 2 = 2

The function is continuous and changes sign between 1 and 2.

By the intermediate value theorem, at least one root lies in this interval.

Continuity matters. A sign change across a discontinuity does not necessarily indicate a root.

## 2. Bisection by hand

Calculate the midpoint:

m = (left + right)/2

Keep the half where the endpoint values have opposite signs.

| Step | Left | Right | Midpoint | f(midpoint) | Keep |
|---|---|---|---|---|---|
| 1 | 1 | 2 | 1.5 | 0.25 | [1, 1.5] |
| 2 | 1 | 1.5 | 1.25 | −0.4375 | [1.25, 1.5] |
| 3 | 1.25 | 1.5 | 1.375 | −0.109375 | [1.375, 1.5] |
| 4 | 1.375 | 1.5 | 1.4375 | 0.06640625 | [1.375, 1.4375] |

The root remains inside every retained interval.

This is the algorithm's invariant: a property that stays true after each update.

## 3. Decide when bisection should stop

Suppose the current interval is [a, b].

Its midpoint is at most half the interval width from any root inside it:

|midpoint − root| ≤ (b − a)/2

Therefore, stop when:

(b − a)/2 ≤ tolerance

For the starting interval [1, 2], the initial width is 1.

At the kth midpoint evaluation, after k − 1 previous halvings:

error bound = 1/2ᵏ

For a target error of 10⁻⁸:

1/2ᵏ ≤ 10⁻⁸

k ≥ log₂(10⁸)
k ≥ 26.575...

So 27 midpoint evaluations are enough.

This is an exact-arithmetic guarantee. Floating-point rounding can matter at very small tolerances.

## 4. Derive Newton's update

From the Taylor approximation lesson:

f(x + h) ≈ f(x) + f′(x)h

We want the approximation to equal zero:

0 = f(x) + f′(x)h

Solve for h:

h = −f(x)/f′(x)

Therefore:

next x = x − f(x)/f′(x)

Geometrically, the next estimate is where the tangent line crosses the x-axis.

The derivative must be nonzero for this update to be defined.

## 5. Newton's method for √2

For:

f(x) = x² − 2
f′(x) = 2x

The update becomes:

next x = x − (x² − 2)/(2x)
       = (x + 2/x)/2

Start at x₀ = 1.

First update:

x₁ = (1 + 2/1)/2
   = 1.5

Second update:

x₂ = (1.5 + 2/1.5)/2
   ≈ 1.416666667

Third update:

x₃ = (1.416666667 + 2/1.416666667)/2
   ≈ 1.414215686

Fourth update:

x₄ ≈ 1.414213562

Reference:

√2 ≈ 1.414213562

Newton approaches the answer quickly in this example.

## 6. Newton is not gradient ascent

Gradient ascent uses:

next x = x + step_size × score′(x)

It tries to increase a score.

Here, Newton uses:

next x = x − f(x)/f′(x)

It tries to solve f(x) = 0.

Both use derivatives, but their update rules and immediate objectives differ.

Newton's method can also be adapted for optimisation by applying root finding to a derivative. That is a later topic.

## 7. A case where Newton cycles

Now consider:

g(x) = x³ − 2x + 2
g′(x) = 3x² − 2

Start at x₀ = 0.

At zero:

g(0) = 2
g′(0) = −2

Therefore:

x₁ = 0 − 2/(−2)
   = 1

At one:

g(1) = 1
g′(1) = 1

Therefore:

x₂ = 1 − 1/1
   = 0

The sequence repeats:

0, 1, 0, 1, ...

Neither value is a root.

A nonzero derivative does not guarantee convergence. The starting point matters, and a program needs a step limit.

## 8. Solve the same cubic using bisection

At x = −2:

g(−2) = −8 + 4 + 2 = −2

At x = −1:

g(−1) = −1 + 2 + 2 = 3

The cubic is continuous and changes sign on [−2, −1].

Bisection can therefore locate a root in this interval:

root ≈ −1.76929235

Newton failed from our chosen starting point. The equation itself was still solvable.

## 9. Residual and root error are different

The residual is:

|f(estimated root)|

The root error is:

|estimated root − actual root|

A small residual does not always imply a small root error.

For example:

f(x) = 10⁻¹²(x − 1)

Its root is 1.

At x = 0:

|f(0)| = 10⁻¹²

The residual is tiny, but the root error is:

|0 − 1| = 1

The scale and slope of the function matter.

Our bisection implementation stops using an interval-width bound.

Our Newton implementation stops using a residual target. That is useful, but it is not a general guarantee on root error.

## 10. The algorithms

### Bisection

1. Evaluate the two interval endpoints.
2. Return immediately if either endpoint is a root.
3. Otherwise, require opposite signs.
4. Calculate the midpoint and evaluate the function there.
5. Stop if the midpoint is a root or the interval is sufficiently narrow.
6. Keep the half with opposite endpoint signs.
7. Repeat until the stopping condition or step limit is reached.

### Newton

1. Start from an initial estimate.
2. Evaluate the function.
3. Stop if the residual meets the target.
4. Evaluate the derivative.
5. Stop with an explanation if the derivative is zero.
6. Calculate the next estimate.
7. Repeat, subject to a step limit.

The script records the iterates so we can inspect what each method did.

## 11. Run the script

From the repository folder:

```bash
python calculus/root_finding.py
```

No additional packages are needed.

For the default examples, expect approximately:

- Bisection for √2: 1.4142135605
- Newton for √2: 1.4142135624
- Bisection for the cubic: −1.7692923471
- Newton for the cubic from zero: a cycle between 0 and 1

The script checks the known root, the cycle, a zero derivative and an invalid bisection interval.

## 12. Try another starting point

For the cubic, change Newton's starting point from 0 to −2.

Before running it, calculate the first update:

g(−2) = −2
g′(−2) = 10

next x = −2 − (−2)/10
       = −1.8

Now run it and inspect the later estimates.

Does this starting point behave differently from zero?

## Assumptions and limitations

- Bisection requires continuity and an initial sign-changing interval.
- An interval without opposite endpoint signs can still contain roots. This implementation simply cannot use it as a bracket.
- Newton requires a derivative and can fail from an unsuitable starting point.
- A very small derivative can cause a very large Newton step.
- The script assumes ordinary-scale inputs and finite function and derivative evaluations.
- Neither method searches for every root.
- The recorded histories use memory proportional to the number of iterations.
- This is a learning implementation, not a general numerical solver.

## Notes after running

To complete during study:

- Can I explain why bisection preserves a root in its interval?
- Can I derive Newton's update from a linear approximation?
- What changed when I started the cubic example at −2?
- Why is a small residual different from a small root error?
- Which stopping condition would I use if I needed a guaranteed interval?

## Support and sources

This is  not an MIT assignment.

The derivation builds on the Taylor approximation lesson in this repository.

MIT OpenCourseWare 18.01SC Single Variable Calculus is a reference for further study:

https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/
