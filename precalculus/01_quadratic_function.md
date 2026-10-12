# Precalculus 01 — A quadratic function

## Question

For the function

$$
f(x)=x^2-4x+3
$$

find its roots, vertex and range. Check some values using Python.

## 1. Evaluate the function

At x = 0:

$$
f(0)=0^2-4(0)+3=3
$$

At x = 2:

$$
f(2)=2^2-4(2)+3=4-8+3=-1
$$

At x = 4:

$$
f(4)=4^2-4(4)+3=16-16+3=3
$$

## 2. Find the roots

Set the function equal to zero:

$$
x^2-4x+3=0
$$

Factorise:

$$
(x-1)(x-3)=0
$$

Therefore the roots are:

$$
\boxed{x=1\text{ or }x=3}
$$

## 3. Find the vertex

Complete the square:

$$
x^2-4x+3=(x-2)^2-1
$$

The squared term cannot be negative. Its smallest value is zero, when x = 2.

The vertex is therefore:

$$
\boxed{(2,-1)}
$$

The graph opens upwards and is symmetric about x = 2.

## 4. Domain and range

The polynomial is defined for every real x.

$$
\text{Domain: }\mathbb{R}
$$

Its smallest output is -1.

$$
\text{Range: }[-1,\infty)
$$

## 5. Python check

```python
def f(x):
    return x**2 - 4*x + 3


for x in range(5):
    print(f"x = {x}, f(x) = {f(x)}")
```

Expected output:

```text
x = 0, f(x) = 3
x = 1, f(x) = 0
x = 2, f(x) = -1
x = 3, f(x) = 0
x = 4, f(x) = 3
```

The equal values at x = 0 and x = 4, and at x = 1 and x = 3, agree with the symmetry about x = 2.

## Practice

Repeat the calculations for:

$$
g(x)=x^2-6x+5
$$

Find the roots, vertex, domain and range before checking with Python.
