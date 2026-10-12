# Functions — revision before calculus

## Exercise 1 — Quadratic function

Find the roots, vertex, domain and range of:

$$
f(x)=x^2-4x+3
$$

### Roots

Set f(x) = 0 and factorise:

$$
x^2-4x+3=(x-1)(x-3)=0
$$

$$
\boxed{x=1\text{ or }x=3}
$$

### Vertex

Complete the square:

$$
f(x)=x^2-4x+4-1=(x-2)^2-1
$$

The squared term is smallest at x = 2.

$$
\boxed{\text{Vertex }=(2,-1)}
$$

### Domain and range

$$
\boxed{\text{Domain: }\mathbb R,\qquad\text{Range: }[-1,\infty)}
$$

### Python check

```python
def f(x):
    return x**2 - 4*x + 3


for x in range(5):
    print(x, f(x))
```

Expected values: 3, 0, -1, 0, 3.

## Exercise 2 — Domain restrictions

Simplify:

$$
q(x)=\frac{x^2-4}{x-2}
$$

The original denominator is zero at x = 2.

For x different from 2:

$$
q(x)=\frac{(x-2)(x+2)}{x-2}=x+2
$$

$$
\boxed{q(x)=x+2,\qquad x\ne2}
$$

The graph follows a line but excludes the point (2, 4). Its domain excludes 2 and its range excludes 4.

## Exercise 3 — Inverse function

Find the inverse of:

$$
f(x)=(x-2)^2,\qquad x\geq2
$$

Write:

$$
y=(x-2)^2
$$

Since x - 2 is nonnegative:

$$
\sqrt y=x-2
$$

$$
\boxed{f^{-1}(x)=2+\sqrt x,\qquad x\geq0}
$$

The inverse has range [2, ∞).

Check:

$$
f(5)=9,\qquad f^{-1}(9)=5
$$

Without the domain restriction, the original function is not one-to-one: f(1) = f(3) = 1.

## Exercise 4 — Compound interest

An investment earns 6% annually, compounded once per year. Find the theoretical doubling time.

$$
A=P(1.06)^t
$$

Set A = 2P:

$$
2=(1.06)^t
$$

Take logarithms:

$$
\ln2=t\ln1.06
$$

$$
\boxed{t=\frac{\ln2}{\ln1.06}\approx11.90\text{ years}}
$$

With annual crediting, the first annual balance at least twice the original investment occurs after 12 years.

```python
from math import log

print("Theoretical time:", round(log(2) / log(1.06), 2))
print("Growth factor after 11 years:", round(1.06**11, 3))
print("Growth factor after 12 years:", round(1.06**12, 3))
```

## Questions to revisit

- Why does cancelling a factor not restore an excluded input?
- Why does finding an inverse sometimes require a restricted domain?
- How would continuous compounding change the doubling-time calculation?
