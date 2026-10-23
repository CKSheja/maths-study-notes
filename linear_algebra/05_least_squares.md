# Least squares: when the equations do not agree

## Question

Find the straight line that best fits these points:

| x | y |
|---|---|
| 0 | 1 |
| 1 | 2 |
| 2 | 2 |

Write the line as:

y ≈ a + bx

Here, a is the intercept and b is the slope.

“Best fit” means the line with the smallest sum of squared vertical errors.

## 1. Can one line pass through all three points?

Substitute each point:

a = 1
a + b = 2
a + 2b = 2

The first two equations give a = 1 and b = 1.

But the third equation would then give:

1 + 2(1) = 3

The observed value is 2, so there is no exact solution.

Gaussian elimination can detect this inconsistency. Least squares answers a different question: which line comes closest under our chosen error measure?

## 2. Write the error function

For each point:

residual = observed value − predicted value

The sum of squared errors is:

S(a, b) = (1 − a)² + (2 − a − b)² + (2 − a − 2b)²

Squaring prevents positive and negative residuals from cancelling.

It also makes large residuals contribute more strongly.

## 3. Differentiate

Set both partial derivatives equal to zero.

With respect to a:

∂S/∂a = −2(1 − a) − 2(2 − a − b) − 2(2 − a − 2b)

0 = 5 − 3a − 3b

Therefore:

3a + 3b = 5

With respect to b:

∂S/∂b = −2(2 − a − b) − 4(2 − a − 2b)

0 = (2 − a − b) + 2(2 − a − 2b)

Therefore:

3a + 5b = 6

## 4. Solve the two equations

3a + 3b = 5
3a + 5b = 6

Subtract the first equation from the second:

2b = 1
b = 1/2

Substitute into the first equation:

3a + 3/2 = 5
3a = 7/2
a = 7/6

The fitted line is:

y ≈ 7/6 + x/2

## 5. Check the predictions and errors

| x | Observed y | Predicted y | Residual |
|---|---|---|---|
| 0 | 1 | 7/6 | −1/6 |
| 1 | 2 | 5/3 | 1/3 |
| 2 | 2 | 13/6 | −1/6 |

Sum of squared errors:

S = (−1/6)² + (1/3)² + (−1/6)²
  = 1/36 + 4/36 + 1/36
  = 1/6

For comparison, the line through the first two points is y = 1 + x.

Its predictions are 1, 2 and 3.

Its squared error is:

0² + 0² + (−1)² = 1

The least-squares line has the smaller error: 1/6 instead of 1.

This comparison checks one alternative. The minimisation argument establishes the result for all lines.

## 6. Where the matrices come in

Write the equations as Aθ ≈ y:

```text
A = [[1, 0],
     [1, 1],
     [1, 2]]

θ = [a, b]

y = [1, 2, 2]
```

The first column of A multiplies the intercept.
The second column multiplies the slope.

The normal equations are:

AᵀAθ = Aᵀy

Here:

```text
AᵀA = [[3, 3],
       [3, 5]]

Aᵀy = [5, 6]
```

These give the same equations we obtained by differentiating:

3a + 3b = 5
3a + 5b = 6

## 7. Why this is the unique minimum

For any proposed coefficient change h:

hᵀAᵀAh = ||Ah||²

The columns of A are linearly independent, so Ah cannot be zero unless h is zero.

Therefore AᵀA is positive definite. The error function is a strictly convex quadratic, and its stationary point is the unique global minimum.

This connects the calculation to positive definite matrices, which I will study in more detail later.

## 8. The projection check

Let r = y − Aθ be the residual vector.

At the least-squares solution:

Aᵀr = 0

Check the first column:

(−1/6) + (1/3) + (−1/6) = 0

Check the second column:

0(−1/6) + 1(1/3) + 2(−1/6) = 0

The residual is perpendicular to both columns of A.

The prediction vector Aθ is the orthogonal projection of y onto the column space of A. The vector being projected is the list of observed y values.

## 9. Turn the calculation into an algorithm

For n points, the normal equations become:

na + bΣx = Σy
aΣx + bΣx² = Σxy

The first equation gives:

a = mean(y) − b × mean(x)

Substituting this into the second equation gives:

b = Σ[(x − mean(x))(y − mean(y))] / Σ[(x − mean(x))²]

Then:

a = mean(y) − b × mean(x)

The Python script uses this centred formula. It solves the same straight-line least-squares problem without explicitly forming or inverting a matrix.

Algorithm:

1. Find the mean of x and the mean of y.
2. Find the sum of squared deviations of x from its mean.
3. If that sum is zero, all x values are equal and the slope is not uniquely determined.
4. Calculate the slope.
5. Calculate the intercept.
6. Calculate predictions, residuals and squared error.
7. Check that Σr and Σxr are approximately zero.

The fitting calculation takes O(n) time.

## 10. Run the script

From the repository folder:

```bash
python linear_algebra/least_squares.py
```

No additional packages are needed.

For the original points, the main results should be:

```text
Intercept: 1.166667
Slope:     0.500000
SSE:       0.166667
```

The script also checks an exact line, repeated x values and a case where the slope cannot be determined uniquely.

Small nonzero residual sums can occur because Python uses floating-point arithmetic.

## 11. Change one observation

Replace the original points with:

```python
points = [(0, 1), (1, 2), (2, 4)]
```

Before running it, predict whether the slope will increase.

Worked check:

3a + 3b = 7
3a + 5b = 10

Subtract:

2b = 3
b = 3/2

Then:

3a + 9/2 = 7
a = 5/6

The new line is:

y ≈ 5/6 + 3x/2

The slope increases from 1/2 to 3/2.

The residuals are now:

1/6, −1/3, 1/6

The squared error is still 1/6. Different fitted lines can have the same total error.

## Assumptions and limitations

- This method fits one straight line with an intercept.
- It minimises squared errors in y, not perpendicular distances to the line.
- All observations receive equal weight.
- At least two distinct x values are needed for a unique intercept and slope.
- A small fitting error does not establish that the line will predict new data well.
- Squared error is sensitive to outliers.
- The script assumes finite numeric inputs at ordinary scales. It is a learning implementation, not a general numerical library.
- For larger least-squares problems, QR or SVD methods are usually preferable to explicitly solving normal equations.

## Notes after running

To complete during study:

- Which part of the calculation could I explain without looking back?
- Why can repeated x values be allowed, but all x values being equal is a problem?
- What happened when I changed one observation?
- Can I explain Aᵀr = 0 in words?

## Support and sources

This is not an MIT assignment.

MIT OpenCourseWare 18.06 Linear Algebra is a reference for further study of projections and least squares:

https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
