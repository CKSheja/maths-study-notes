# Linear algebra — vectors and matrices

## Exercise 1 — Vectors

Let u = (2, 1) and v = (1, 3).

### Addition and dot product

$$
u+v=(2+1,1+3)=\boxed{(3,4)}
$$

$$
u\cdot v=2(1)+1(3)=\boxed{5}
$$

### Lengths and angle

$$
\|u\|=\sqrt5,\qquad\|v\|=\sqrt{10}
$$

$$
\cos\theta=\frac{u\cdot v}{\|u\|\|v\|}
=\frac5{\sqrt5\sqrt{10}}=\frac1{\sqrt2}
$$

$$
\boxed{\theta=45^\circ}
$$

## Exercise 2 — A linear system

Solve:

$$
2x+y=5,\qquad x-y=1
$$

Add the equations:

$$
3x=6\quad\Rightarrow\quad x=2
$$

Substitute:

$$
2-y=1\quad\Rightarrow\quad y=1
$$

$$
\boxed{(x,y)=(2,1)}
$$

Check: 2(2) + 1 = 5 and 2 - 1 = 1.

The matrix form is:

$$
\begin{pmatrix}2&1\\1&-1\end{pmatrix}
\begin{pmatrix}x\\y\end{pmatrix}
=
\begin{pmatrix}5\\1\end{pmatrix}
$$

## Exercise 3 — Rank and null space

Find the rank and a null-space basis for:

$$
A=\begin{pmatrix}1&2&1\\2&4&2\end{pmatrix}
$$

Subtract twice row 1 from row 2:

$$
\begin{pmatrix}1&2&1\\0&0&0\end{pmatrix}
$$

There is one pivot:

$$
\boxed{\operatorname{rank}(A)=1}
$$

To solve Ax = 0:

$$
x_1+2x_2+x_3=0
$$

Let x₂ = s and x₃ = t. Then x₁ = -2s - t:

$$
x=
s\begin{pmatrix}-2\\1\\0\end{pmatrix}
+t\begin{pmatrix}-1\\0\\1\end{pmatrix}
$$

These two vectors span the null space. They are independent because their second and third components force both coefficients to be zero in a zero combination.

A basis is:

$$
\boxed{
\left\{
\begin{pmatrix}-2\\1\\0\end{pmatrix},
\begin{pmatrix}-1\\0\\1\end{pmatrix}
\right\}
}
$$

The nullity is 2.

Rank-nullity check:

$$
1+2=3
$$

This equals the number of columns.

## Exercise 4 — No solution or infinitely many?

### System A

$$
x+y=2,\qquad2x+2y=4
$$

The second equation repeats the first. There are infinitely many solutions:

$$
\boxed{(x,y)=(s,2-s),\qquad s\in\mathbb R}
$$

### System B

$$
x+y=2,\qquad2x+2y=5
$$

Subtracting twice the first equation from the second gives 0 = 1.

$$
\boxed{\text{No solution}}
$$

## Exercise 5 — Matrix multiplication order

Let:

$$
A=\begin{pmatrix}1&2\\0&1\end{pmatrix},
\qquad
B=\begin{pmatrix}2&0\\1&3\end{pmatrix}
$$

Using row-by-column multiplication:

$$
AB=
\begin{pmatrix}
1(2)+2(1)&1(0)+2(3)\\
0(2)+1(1)&0(0)+1(3)
\end{pmatrix}
=
\boxed{\begin{pmatrix}4&6\\1&3\end{pmatrix}}
$$

$$
BA=
\begin{pmatrix}
2(1)+0(0)&2(2)+0(1)\\
1(1)+3(0)&1(2)+3(1)
\end{pmatrix}
=
\boxed{\begin{pmatrix}2&4\\1&5\end{pmatrix}}
$$

Therefore AB ≠ BA.

## Exercise 6 — Eigenvalues and eigenvectors

Let:

$$
M=\begin{pmatrix}2&1\\1&2\end{pmatrix}
$$

Find the values λ for which Mv = λv has a nonzero solution.

$$
\det(M-\lambda I)=(2-\lambda)^2-1
$$

$$
=\lambda^2-4\lambda+3=(\lambda-1)(\lambda-3)
$$

Hence:

$$
\boxed{\lambda=1,\qquad\lambda=3}
$$

For λ = 3, solving (M - 3I)v = 0 gives v₂ = v₁. Choose:

$$
v=\begin{pmatrix}1\\1\end{pmatrix}
$$

For λ = 1, solving (M - I)v = 0 gives v₂ = -v₁. Choose:

$$
v=\begin{pmatrix}1\\-1\end{pmatrix}
$$

Check:

$$
M\begin{pmatrix}1\\1\end{pmatrix}
=3\begin{pmatrix}1\\1\end{pmatrix}
$$

$$
M\begin{pmatrix}1\\-1\end{pmatrix}
=\begin{pmatrix}1\\-1\end{pmatrix}
$$

## Questions to revisit

- Why does a basis need both spanning and independence?
- How do pivots and free variables determine a solution set?
- Why is the zero vector excluded from the definition of an eigenvector?
- Why can reversing matrix multiplication change the result?
