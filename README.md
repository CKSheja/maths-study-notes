# Maths study notes

I am revisiting mathematics alongside my software engineering studies, building on what I learned in high school and studying the concepts in more depth at university level.

I recently started Stanford's Probability for AI course to understand more of the mathematics behind AI. Some concepts are familiar, but I want to go beyond remembering formulas and understand how to derive, apply and connect them.

This repository brings together worked exercises, short explanations and Python checks. It starts with some revision before moving into linear algebra, multivariable calculus and numerical methods.

## Study approach

I work through each question step by step and check the result where possible. Python is useful for numerical checks and for exploring approximations.

The initial notes include AI-assisted worked solutions. I will add my own attempts, corrections and observations as I study.

## Current exercises

### Revision and introductory university topics

- [Functions, domains and exponential growth](precalculus/01_functions.md)
- [Linear systems, null spaces and eigenvalues](linear_algebra/01_vectors_and_matrices.md)
- [Derivatives, gradients and constrained optimisation](calculus/01_derivatives.md)
- [Integration and numerical approximation](calculus/02_integration.md)

### Selected MIT OpenCourseWare exercises

- [18.06SC — Nullspaces, Problem 6.3](linear_algebra/02_mit_nullspaces.md)
- [18.02SC — Partial derivatives, Session 26](calculus/03_mit_partial_derivatives.md)

Each MIT exercise note identifies the exact source and links to the published solution.

### Python experiment

- [Numerical integration experiment](calculus/integration_experiment.py)

The script compares midpoint and trapezoidal approximations for three integrals:

- x² from 0 to 1
- sin(x) from 0 to π
- eˣ from 0 to 1

It reports the approximations and their absolute errors against known exact answers, using increasing numbers of intervals.

Questions to investigate:

- How does doubling the number of intervals affect the error?
- Which method overestimates or underestimates each integral?
- Does one method consistently give a smaller error for these examples?

## Running the integration experiment

Requires Python 3. No additional packages are needed.

Download or clone the repository, then open a terminal in the repository folder and run:

```bash
python calculus/integration_experiment.py
```

On Windows, if Python is available through the `py` launcher, use:

```bash
py calculus/integration_experiment.py
```

For x² on [0, 1] with four intervals, the expected results are:

| Method | Approximation | Absolute error |
|---|---:|---:|
| Midpoint | 0.328125 | 0.005208333 |
| Trapezoidal | 0.343750 | 0.010416667 |

GitHub displays the script but does not execute it.

## Topics to study next

### Linear algebra

- Bases, dimension and linear independence
- Linear transformations and change of basis
- Orthogonal projections and least squares
- Diagonalisation and positive definite matrices

### Calculus

- Sequences, series and convergence
- Taylor approximations and error
- The multivariable chain rule
- Multiple integrals over nonrectangular regions
- Further constrained optimisation

### Engineering mathematics

- First-order and second-order differential equations
- Systems of differential equations
- Numerical root-finding
- Numerical methods for differential equations

## Exercises that need more practice

I will record exercises here after attempting them, noting where I got stuck and what I need to revisit.

## Support and sources

- Stanford's Probability for AI — currently in progress. These repository exercises are separate from the course assignments.
- [MIT OCW 18.06 Linear Algebra, Spring 2010](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — reference for further study.
- [MIT OCW 18.01SC Single Variable Calculus, Fall 2010](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) — reference for further study.
- Selected exercises from MIT OCW 18.06SC Fall 2011 and 18.02SC Fall 2010, credited in the individual files.
- AI assistance for preparing explanations, worked solutions and Python code.

These are independent study notes, not coursework submitted for university credit.

## Attribution

MIT-derived exercise notes include source links, adaptation notes and their applicable licence. The other exercises and the Python experiment are AI-assisted study examples and are not presented as MIT assignments.
