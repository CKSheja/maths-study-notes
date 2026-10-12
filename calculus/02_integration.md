# Calculus — integration and accumulation

## Exercise 1 — Antiderivative

Evaluate:

$$
\int(3x^2-4x+2)\,dx
$$

Integrating each term:

$$
\boxed{x^3-2x^2+2x+C}
$$

Differentiating the answer returns the original integrand.

## Exercise 2 — Substitution

Evaluate:

$$
\int2x(x^2+1)^3\,dx
$$

Let u = x² + 1, so du = 2x dx.

$$
\int u^3\,du=\frac{u^4}4+C
$$

Substitute back:

$$
\boxed{\frac{(x^2+1)^4}4+C}
$$

## Exercise 3 — Displacement and distance

A particle has velocity v(t) = 2t - 2 m/s, with t measured in seconds.

Find displacement and distance from t = 0 to t = 3 s.

### Displacement

$$
\int_0^3(2t-2)\,dt=[t^2-2t]_0^3
$$

$$
\boxed{\text{Displacement}=3\text{ m}}
$$

### Distance

Velocity changes sign at t = 1.

$$
\text{Distance}
=-\int_0^1(2t-2)\,dt+\int_1^3(2t-2)\,dt
$$

$$
\boxed{\text{Distance}=1+4=5\text{ m}}
$$

## Exercise 4 — Double integral

Evaluate:

$$
\int_0^1\int_0^2(x+y)\,dy\,dx
$$

Integrate with respect to y, holding x constant:

$$
\int_0^2(x+y)\,dy
=\left[xy+\frac{y^2}2\right]_0^2
=2x+2
$$

Then:

$$
\int_0^1(2x+2)\,dx=[x^2+2x]_0^1
$$

$$
\boxed{3}
$$

Reverse the order to check:

$$
\int_0^2\int_0^1(x+y)\,dx\,dy
=\int_0^2\left(\frac12+y\right)\,dy=3
$$

The continuous integrand over this rectangle permits either order.

## Exercise 5 — Midpoint approximation

Approximate:

$$
\int_0^1x^2\,dx
$$

using four equal midpoint rectangles.

$$
\Delta x=\frac14
$$

The midpoints are 0.125, 0.375, 0.625 and 0.875.

$$
\text{Approximation}
=0.25(0.125^2+0.375^2+0.625^2+0.875^2)
$$

$$
\boxed{0.328125}
$$

The exact value is 1/3. The absolute error is approximately 0.005208.

### Python exploration

```python
def midpoint_integral(f, a, b, n):
    width = (b - a) / n
    total = 0.0

    for i in range(n):
        midpoint = a + (i + 0.5) * width
        total += f(midpoint)

    return total * width


for n in [4, 10, 100]:
    estimate = midpoint_integral(lambda x: x**2, 0, 1, n)
    error = abs(estimate - 1/3)
    print(f"n={n}: estimate={estimate:.6f}, error={error:.6f}")
```

Expected output:

```text
n=4: estimate=0.328125, error=0.005208
n=10: estimate=0.332500, error=0.000833
n=100: estimate=0.333325, error=0.000008
```

For this function and interval, the absolute error is exactly 1/(12n²). Doubling n divides the error by four.

## Questions to revisit

- Why does an indefinite integral include C?
- Why can displacement differ from total distance?
- How do integration bounds change for a nonrectangular region?
- How can we assess numerical error when an exact integral is unavailable?
