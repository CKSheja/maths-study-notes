# Linear algebra 01 — Vectors and simultaneous equations

## Exercise 1 — Vector operations

Let

$$
u=(2,1),\qquad v=(1,3)
$$

### Addition

Add corresponding components:

$$
u+v=(2+1,1+3)=\boxed{(3,4)}
$$

### Scalar multiplication

Multiply each component by 2:

$$
2u=(2\times2,2\times1)=\boxed{(4,2)}
$$

### Dot product

Multiply corresponding components and add:

$$
u\cdot v=(2)(1)+(1)(3)=\boxed{5}
$$

The result is a number, not a vector.

### Vector lengths

$$
\|u\|=\sqrt{2^2+1^2}=\boxed{\sqrt5}
$$

$$
\|v\|=\sqrt{1^2+3^2}=\boxed{\sqrt{10}}
$$

### Angle between the vectors

Use

$$
\cos\theta=\frac{u\cdot v}{\|u\|\|v\|}
$$

Then

$$
\cos\theta=\frac{5}{\sqrt5\sqrt{10}}
=\frac{1}{\sqrt2}
$$

Therefore

$$
\boxed{\theta=45^\circ}
$$

### Python check

```python
from math import sqrt, acos, degrees

u = (2, 1)
v = (1, 3)

vector_sum = tuple(a + b for a, b in zip(u, v))
twice_u = tuple(2*a for a in u)
dot_product = sum(a*b for a, b in zip(u, v))

length_u = sqrt(sum(a*a for a in u))
length_v = sqrt(sum(b*b for b in v))

cos_theta = dot_product / (length_u * length_v)
cos_theta = max(-1.0, min(1.0, cos_theta))
angle = degrees(acos(cos_theta))

print("u + v:", vector_sum)
print("2u:", twice_u)
print("Dot product:", dot_product)
print("Length of u:", round(length_u, 3))
print("Length of v:", round(length_v, 3))
print("Angle:", round(angle, 1), "degrees")
```

Expected output:

```text
u + v: (3, 4)
2u: (4, 2)
Dot product: 5
Length of u: 2.236
Length of v: 3.162
Angle: 45.0 degrees
```

## Exercise 2 — Solve simultaneous equations

Solve:

$$
2x+y=5
$$

$$
x-y=1
$$

Add the equations to eliminate y:

$$
3x=6
$$

$$
x=2
$$

Substitute into the second equation:

$$
2-y=1
$$

$$
y=1
$$

The solution is:

$$
\boxed{x=2,\qquad y=1}
$$

### Check both equations

$$
2(2)+1=5
$$

$$
2-1=1
$$

Both equations are satisfied.

### Matrix form

The same system can be written as:

$$
\begin{pmatrix}
2 & 1\\
1 & -1
\end{pmatrix}
\begin{pmatrix}
x\\
y
\end{pmatrix}
=
\begin{pmatrix}
5\\
1
\end{pmatrix}
$$

Each row represents one equation. Multiplying the matrix by the solution gives:

$$
\begin{pmatrix}
2 & 1\\
1 & -1
\end{pmatrix}
\begin{pmatrix}
2\\
1
\end{pmatrix}
=
\begin{pmatrix}
5\\
1
\end{pmatrix}
$$

### Python check

```python
matrix = [[2, 1], [1, -1]]
solution = [2, 1]

result = [
    sum(coefficient * value
        for coefficient, value in zip(row, solution))
    for row in matrix
]

print("Result:", result)
print("Matches [5, 1]:", result == [5, 1])
```

Expected output:

```text
Result: [5, 1]
Matches [5, 1]: True
```

This code checks the proposed solution. It does not solve the equations automatically.

## Practice

1. Repeat the vector calculations using u = (3, 0) and v = (0, 4).
2. Solve x + y = 7 and 2x - y = 2.
3. Write the second problem in matrix form and check your solution.
