# From derivatives to a numerical algorithm

## Exercise 1: start with a known derivative

Let:

$$
f(x)=x^2
$$

Then:

$$
f'(x)=2x
$$

At $x=2$:

$$
f'(2)=4
$$

We will use this exact answer to check numerical estimates.

The forward-difference formula is:

$$
D_f(h)=\frac{f(x+h)-f(x)}{h},\qquad h>0
$$

Choose $h=0.1$:

$$
D_f(0.1)=\frac{2.1^2-2^2}{0.1}
$$

$$
=\frac{4.41-4}{0.1}=4.1
$$

Absolute error:

$$
|4.1-4|=0.1
$$

For a general step $h$:

$$
\frac{(2+h)^2-4}{h}
=\frac{4h+h^2}{h}
=4+h
$$

Therefore, in exact arithmetic, the forward-difference error for this example is $h$.

## Exercise 2: use points on both sides

The central-difference formula is:

$$
D_c(h)=\frac{f(x+h)-f(x-h)}{2h}
$$

For the same function at $x=2$, with $h=0.1$:

$$
D_c(0.1)=\frac{2.1^2-1.9^2}{0.2}
$$

$$
=\frac{4.41-3.61}{0.2}=4
$$

Expanding algebraically:

$$
\frac{(2+h)^2-(2-h)^2}{2h}
=\frac{8h}{2h}
=4
$$

The central estimate is exact for this quadratic in exact arithmetic.

It is not exact for every function. A computer can also introduce rounding error.

## Exercise 3: a trigonometric function

Let:

$$
f(x)=\sin x
$$

Angles are measured in radians.

Since $f'(x)=\cos x$:

$$
f'(0)=1
$$

Using central differences with $h=0.1$:

$$
D_c(0.1)
=\frac{\sin(0.1)-\sin(-0.1)}{0.2}
$$

Because sine is odd:

$$
D_c(0.1)=\frac{\sin(0.1)}{0.1}
\approx0.9983341665
$$

Absolute error:

$$
|0.9983341665-1|
\approx0.0016658335
$$

At this particular point, forward and central differences give the same result because $\sin(0)=0$ and sine is odd.

That does not mean the methods always agree.

## Exercise 4: an exponential function

Let:

$$
f(x)=e^x
$$

Then:

$$
f'(1)=e\approx2.7182818285
$$

At $h=0.1$, forward differences give:

$$
D_f(0.1)=\frac{e^{1.1}-e}{0.1}
\approx2.8588419549
$$

Central differences give:

$$
D_c(0.1)=\frac{e^{1.1}-e^{0.9}}{0.2}
\approx2.7228145639
$$

The central estimate is closer for this step size.

The Python script repeats the calculation for progressively smaller steps.

## Why central differences often converge faster

For a sufficiently smooth function, Taylor expansion gives:

$$
f(x+h)
=f(x)+hf'(x)+\frac{h^2}{2}f''(x)+O(h^3)
$$

Subtracting $f(x)$ and dividing by $h$ gives:

$$
D_f(h)
=f'(x)+\frac{h}{2}f''(x)+O(h^2)
$$

The leading error is usually proportional to $h$.

For central differences, expanding at $x+h$ and $x-h$ and subtracting cancels the even-order terms:

$$
D_c(h)=f'(x)+O(h^2)
$$

This assumes sufficient smoothness and bounded derivatives nearby.

These statements describe truncation error before floating-point rounding is considered.

## Algorithm

1. Choose a function and an evaluation point.
2. Choose a positive step size.
3. Evaluate the function at the required nearby points.
4. Calculate forward and central differences.
5. Compare the estimates with a known derivative.
6. Repeat with smaller steps.
7. Inspect how the errors change.

The Python function accepts another function as an argument. The same implementation can therefore work with a polynomial, sine or an exponential.

## Run the script

[Open the Python script](numerical_derivatives.py).

From the repository root:

```bash
python calculus/numerical_derivatives.py
```

The output includes:

- Step size
- Forward estimate
- Central estimate
- Absolute error for each method

The examples are:

- $x^2$ at $x=2$
- $\sin x$ at $x=0$
- $e^x$ at $x=1$

## Why the smallest step is not always best

Smaller steps reduce truncation error.

However, a computer stores floating-point numbers with limited precision. Subtracting nearly equal values can lose useful precision. Dividing the resulting error by a tiny step can amplify it.

Eventually, the errors can increase or behave irregularly.

Look for this behaviour in the exponential example. Exact last digits may differ between computing environments.

A displayed error of zero does not establish that a numerical method is exact for arbitrary inputs.

## Further exercises and answers

### A. A straight line

Use:

$$
f(x)=3x+2
$$

The derivative is 3 everywhere.

Both difference formulas give 3 in exact arithmetic for any nonzero step.

### B. A cubic

Use:

$$
f(x)=x^3
$$

At $x=2$:

$$
f'(2)=3(2^2)=12
$$

Forward differences give:

$$
\frac{(2+h)^3-8}{h}
=12+6h+h^2
$$

Central differences give:

$$
\frac{(2+h)^3-(2-h)^3}{2h}
=12+h^2
$$

The formulas make their different error rates visible.

### C. A misleading answer

Use:

$$
f(x)=|x|
$$

At zero, central differences give:

$$
\frac{|h|-|-h|}{2h}=0
$$

But the derivative at zero does not exist. The left-hand slope is -1 and the right-hand slope is 1.

A plausible numerical answer does not establish differentiability.

## Implementation limits

The script rejects nonpositive or nonfinite steps. It also rejects steps too small to change the evaluation point in floating-point arithmetic.

It assumes the function is defined at the sampled points. It does not detect every domain problem or determine whether a derivative exists.

The known derivatives are used for verification. In a real problem, an exact answer may not be available.

## Support

Prepared with AI assistance. These are original study exercises, not MIT assignments.
