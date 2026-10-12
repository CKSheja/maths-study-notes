# MIT OCW practice — Nullspaces

Source: MIT OpenCourseWare, 18.06SC Linear Algebra, Fall 2011, taught by Gilbert Strang.

[Problem sheet — Problem 6.3](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/resources/mit18_06scf11_ses1-6prob/)

[Published solutions](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/resources/mit18_06scf11_ses1-6sol/)

The task is paraphrased below. This AI-assisted explanation was checked against the published solution.

## Question

Matrices A and B have the same number of columns. Form C by stacking A above B.

How does N(C) relate to N(A) and N(B)?

## Solution

$$
C=\begin{pmatrix}A\\B\end{pmatrix}
$$

For any compatible vector x:

$$
Cx=\begin{pmatrix}Ax\\Bx\end{pmatrix}
$$

This equals zero exactly when both Ax = 0 and Bx = 0.

Therefore x must belong to both nullspaces:

$$
\boxed{N(C)=N(A)\cap N(B)}
$$

## Example

Let:

$$
A=\begin{pmatrix}1&1\end{pmatrix},
\qquad
B=\begin{pmatrix}1&-1\end{pmatrix}
$$

Belonging to both nullspaces requires:

$$
x_1+x_2=0,\qquad x_1-x_2=0
$$

Adding gives x₁ = 0, then x₂ = 0.

Thus the stacked matrix has nullspace containing only the zero vector.

## Question to revisit

Why intersection rather than union?

The vector must satisfy both equations. Satisfying only one is insufficient.

## Attribution

Adapted from the MIT OCW exercise linked above. Explanatory steps and the numerical example were added.

This adapted note is shared under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
