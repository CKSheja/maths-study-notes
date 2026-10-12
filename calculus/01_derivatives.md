# Calculus — derivatives and gradients

## Exercise 1 — First principles

For f(x) = x²:

$$
f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}h
$$

$$
=\lim_{h\to0}\frac{(x+h)^2-x^2}h
$$

$$
=\lim_{h\to0}(2x+h)
$$

$$
\boxed{f'(x)=2x}
$$

## Exercise 2 — Chain rule

Differentiate:

$$
f(x)=(3x^2+1)^3
$$

The outer derivative is 3(3x² + 1)². The inner derivative is 6x.

$$
\boxed{f'(x)=18x(3x^2+1)^2}
$$

## Exercise 3 — Partial derivatives

Find the gradient of:

$$
f(x,y)=x^2+xy+y^2
$$

Hold y constant when differentiating with respect to x:

$$
f_x=2x+y
$$

Hold x constant when differentiating with respect to y:

$$
f_y=x+2y
$$

$$
\boxed{\nabla f=(2x+y,\ x+2y)}
$$

At (1, 2):

$$
\boxed{\nabla f(1,2)=(4,5)}
$$

## Exercise 4 — Classify a stationary point

For the same function, solve:

$$
2x+y=0,\qquad x+2y=0
$$

From the first equation, y = -2x. Substituting into the second gives x = 0 and y = 0.

Rewrite the function:

$$
f(x,y)=\left(x+\frac y2\right)^2+\frac34y^2
$$

Both terms are nonnegative. They are simultaneously zero only at (0, 0).

$$
\boxed{\text{Unique global minimum at }(0,0),\quad f=0}
$$

## Exercise 5 — Constrained optimisation

Maximise xy subject to:

$$
x+y=6,\qquad x,y\geq0
$$

### Substitution

Use y = 6 - x:

$$
p(x)=x(6-x),\qquad0\leq x\leq6
$$

$$
p'(x)=6-2x=0\quad\Rightarrow\quad x=3
$$

Then y = 3.

Since p''(x) = -2, the function is concave down. The endpoint products are zero.

$$
\boxed{\text{Maximum product }=9\text{ at }(3,3)}
$$

### Lagrange multipliers

Let f(x,y) = xy and g(x,y) = x + y - 6.

For an interior constrained extremum:

$$
\nabla f=\lambda\nabla g
$$

$$
(y,x)=\lambda(1,1)
$$

Thus x = y. With x + y = 6, we obtain x = y = 3.

Checking the boundary again gives zero, so the maximum is 9.

## Questions to revisit

- Does a zero gradient always indicate a minimum? No: it may indicate a maximum or saddle point.
- Why check boundary points in constrained optimisation?
- What changes when differentiating with respect to one variable while holding another constant?
