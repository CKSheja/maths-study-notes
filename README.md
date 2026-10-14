# Maths study notes

I am revisiting mathematics alongside my software engineering studies, building on what I learned in high school and studying the concepts in more depth at university level.

I recently started Stanford's Probability for AI course to understand more of the mathematics behind AI. Some concepts are familiar, but I want to go beyond remembering formulas and understand how to derive, apply and connect them.

This repository brings together worked exercises, short explanations and Python experiments. It starts with some revision before moving into linear algebra, multivariable calculus and numerical methods.

## Study approach

I work through questions step by step and check the results where possible. Python is useful for testing calculations and exploring numerical methods.

The initial notes and scripts were prepared with AI assistance. I will add my own attempts, corrections and observations as I study.

## Current exercises

### Revision and introductory university topics

- [Functions, domains and exponential growth](precalculus/01_functions.md)
- [Linear systems, null spaces and eigenvalues](linear_algebra/01_vectors_and_matrices.md)
- [Derivatives, gradients and constrained optimisation](calculus/01_derivatives.md)
- [Integration and numerical approximation](calculus/02_integration.md)
- [Gaussian elimination: worked example and algorithm](linear_algebra/03_gaussian_elimination.md)

### Selected MIT OpenCourseWare exercises

- [18.06SC — Nullspaces, Problem 6.3](linear_algebra/02_mit_nullspaces.md)
- [18.02SC — Partial derivatives, Session 26](calculus/03_mit_partial_derivatives.md)

Each MIT exercise note identifies the exact source and links to the published solution.

## Python experiments

### Numerical integration

[Script](calculus/integration_experiment.py) · [Results and observations](calculus/integration_results.md)

Compares midpoint and trapezoidal approximations for:

- x² from 0 to 1
- sin(x) from 0 to π
- exp(x) from 0 to 1

The experiment increases the number of intervals and reports absolute errors against known exact answers.

The recorded results came from running the shared script in ChatGPT's Python environment. That execution context is documented in the results file.

### Gaussian elimination

[Script](linear_algebra/gaussian_elimination.py) · [Worked lesson](linear_algebra/03_gaussian_elimination.md)

Solves small square linear systems using elimination, partial pivoting and back substitution.

The script includes checks for known solutions, a system requiring a row swap and rejection of a singular matrix. It also reports the residual when the computed solution is substituted into the original equations.

This is a learning implementation. It rejects singular or numerically near-singular systems rather than classifying their solution sets.

## Running the scripts

Requires Python 3. No additional packages are needed.

Download or clone the repository, then open a terminal in the repository folder.

Run the integration experiment:

```bash
python calculus/integration_experiment.py
```

Run the Gaussian elimination example:

```bash
python linear_algebra/gaussian_elimination.py
```

On Windows, replace `python` with `py` if your installation uses the Python launcher.

GitHub displays the scripts but does not execute them.

## Topics to study next

### Linear algebra

- Bases, dimension and linear independence
- Linear transformations and change of basis
- Orthogonal projections and least squares
- Diagonalisation and positive definite matrices
- Conditioning and numerical error in linear systems

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

MIT-derived exercise notes include source links, adaptation notes and their applicable licence. The other exercises are not presented as MIT assignments.
