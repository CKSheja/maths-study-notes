# Maths study notes

I am revisiting mathematics alongside my software engineering studies. High school gave me a foundation in calculus, probability, statistics, algebra and mathematical logic. Some topics are still familiar; others need revision and practice.

I recently started Stanford's Probability for AI course. It has given me a reason to return to these ideas and explore how they are used in AI. Through this repository, I want to strengthen my understanding, work through more demanding problems and connect mathematical methods with code.

These notes bring together worked exercises, explanations and small Python experiments. They include revision alongside deeper study of linear algebra, multivariable calculus and numerical methods.

## Study approach

I work through questions step by step and check the results where possible. For selected topics, I also study an algorithm and its Python implementation.

The notes connect three things:

- The mathematical question and its assumptions
- The steps used to obtain an answer
- Checks that help establish whether the answer is correct

Python is useful for comparing methods, testing calculations and seeing how results change when the inputs change.

## Current exercises

### Revision and introductory university topics

- [Functions, domains and exponential growth](precalculus/01_functions.md)
- [Linear systems, null spaces and eigenvalues](linear_algebra/01_vectors_and_matrices.md)
- [Derivatives, gradients and constrained optimisation](calculus/01_derivatives.md)
- [Integration and numerical approximation](calculus/02_integration.md)
- [Gaussian elimination: worked example and algorithm](linear_algebra/03_gaussian_elimination.md)
- [Classifying linear systems: unique, infinite or no solution](linear_algebra/04_solution_types.md)
- [Numerical derivatives and approximation error](calculus/04_numerical_derivatives.md)
- [Least squares: when the equations do not agree](linear_algebra/05_least_squares.md)

### Selected MIT OpenCourseWare exercises

- [18.06SC — Nullspaces, Problem 6.3](linear_algebra/02_mit_nullspaces.md)
- [18.02SC — Partial derivatives, Session 26](calculus/03_mit_partial_derivatives.md)

Each MIT exercise note identifies the exact source and links to the published solution.

## Latest addition: least squares

The new lesson fits a straight line to three points that cannot all lie on the same line.

It derives the normal equations using partial derivatives, solves for the intercept and slope, and checks the residuals.

The Python script implements the centred straight-line fitting formula. It connects the matrix calculation to an algorithm and checks the condition Aᵀr = 0.

This follows the earlier work on linear systems: first finding exact solutions, then studying what to do when no exact solution exists.

## Python experiments

### Numerical integration

[Script](calculus/integration_experiment.py) · [Results and observations](calculus/integration_results.md)

Compares midpoint and trapezoidal approximations for:

- x² from 0 to 1
- sin(x) from 0 to π
- exp(x) from 0 to 1

The experiment increases the number of intervals and reports absolute errors against known exact answers.


### Gaussian elimination

[Script](linear_algebra/gaussian_elimination.py) · [Worked lesson](linear_algebra/03_gaussian_elimination.md)

Solves small square linear systems using elimination, partial pivoting and back substitution.

The script includes checks for known solutions, a system requiring a row swap and rejection of a singular matrix. It also reports the residual when the computed solution is substituted into the original equations.

This is a learning implementation. It rejects singular or numerically near-singular systems rather than classifying their solution sets.

### Classifying linear systems

[Script](linear_algebra/classify_systems.py) · [Worked lesson](linear_algebra/04_solution_types.md)

Uses row reduction with exact fractions to distinguish systems with one solution, infinitely many solutions or no solution.

For systems with free variables, it describes how the solutions depend on those variables.

### Numerical derivatives

[Script](calculus/numerical_derivatives.py) · [Worked lesson](calculus/04_numerical_derivatives.md)

Compares forward and central differences with known derivatives.

The examples explore how the step size affects approximation error and why continually reducing it does not always improve a floating-point calculation.

### Least-squares line fitting

[Script](linear_algebra/least_squares.py) · [Worked lesson](linear_algebra/05_least_squares.md)

Fits a line to observations that do not agree exactly.

The script reports the intercept, slope, predictions, residuals and sum of squared errors. It also checks that the residual vector is approximately orthogonal to the columns of the design matrix.

The examples include:

- Three points with no exact straight-line fit
- Points that lie exactly on a line
- Repeated x values
- Rejection of a fit where all x values are equal

This implementation fits a line with an intercept. It is not a general least-squares solver.

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

Run the linear-system classification examples:

```bash
python linear_algebra/classify_systems.py
```

Run the numerical derivative experiment:

```bash
python calculus/numerical_derivatives.py
```

Run the least-squares example:

```bash
python linear_algebra/least_squares.py
```

On Windows, replace `python` with `py` if your installation uses the Python launcher.

GitHub displays the scripts but does not execute them.

## Topics to study next

### Linear algebra

- Bases, dimension and linear independence in more depth
- Linear transformations and change of basis
- Orthogonal bases and Gram–Schmidt
- QR factorisation and its connection to least squares
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


Questions to return to in the least-squares lesson:

- Why does Aᵀr = 0 describe the best fit?
- Why do distinct x values give a unique fitted line?
- How does an outlier change the result?
- Why might forming AᵀA cause numerical difficulties in larger problems?

## Support and sources

- Stanford's Probability for AI — currently in progress. The exercises in this repository are separate from the course assignments.
- [MIT OCW 18.06 Linear Algebra, Spring 2010](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) — reference for further study.
- [MIT OCW 18.01SC Single Variable Calculus, Fall 2010](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) — reference for further study.
- Selected exercises from MIT OCW 18.06SC Fall 2011 and 18.02SC Fall 2010, credited in the individual files.

These are independent study notes, not coursework submitted for university credit.

## Attribution

MIT-derived exercise notes include source links, adaptation notes and their applicable licence. The other exercises are not presented as MIT assignments.
