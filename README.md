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

### Precalculus and revision

- [Functions, domains and exponential growth](precalculus/01_functions.md)
- [Quadratic functions](precalculus/01_quadratic_function.md)

### Linear algebra

- [Vectors and systems of equations](linear_algebra/01_vectors_and_systems.md)
- [Linear systems, null spaces and eigenvalues](linear_algebra/01_vectors_and_matrices.md)
- [Gaussian elimination: worked example and algorithm](linear_algebra/03_gaussian_elimination.md)
- [Classifying linear systems: unique, infinite or no solution](linear_algebra/04_solution_types.md)
- [Least squares: when the equations do not agree](linear_algebra/05_least_squares.md)

### Calculus and numerical methods

- [Derivatives, gradients and constrained optimisation](calculus/01_derivatives.md)
- [Integration and numerical approximation](calculus/02_integration.md)
- [Numerical derivatives and approximation error](calculus/04_numerical_derivatives.md)
- [Taylor approximations: choosing enough terms](calculus/05_taylor_approximations.md)
- [Root finding: bisection and Newton's method](calculus/06_root_finding.md)
- [Euler's method: how fast does a cup cool?](calculus/07_euler_cooling.md)

### Selected MIT OpenCourseWare exercises

- [18.06SC: Nullspaces, Problem 6.3](linear_algebra/02_mit_nullspaces.md)
- [18.02SC: Partial derivatives, Session 26](calculus/03_mit_partial_derivatives.md)

Each note identifies the original exercise and links to its published solution.

## Latest addition: Euler's method

The [cooling exercise](calculus/07_euler_cooling.md) starts with a cup at 80°C in a room at 20°C. The first two steps can be checked by hand. The [Python experiment](calculus/euler_cooling.py) then compares four step sizes against the exact temperature at ten minutes.

The last example keeps the time fixed at twelve minutes. One large step predicts 8°C; two smaller steps predict 29.6°C. Rewriting the calculation in terms of the difference from room temperature explains why the first estimate crosses below 20°C.

## Python experiments

| Script | What it explores |
| --- | --- |
| [Numerical integration](calculus/integration_experiment.py) | Compares midpoint and trapezoidal estimates with exact integrals. [Results and observations](calculus/integration_results.md) |
| [Gaussian elimination](linear_algebra/gaussian_elimination.py) | Solves small square systems using partial pivoting and checks the residual. Includes a row swap and a singular system. |
| [Classifying linear systems](linear_algebra/classify_systems.py) | Uses exact fractions to distinguish one solution, infinitely many solutions and no solution. |
| [Numerical derivatives](calculus/numerical_derivatives.py) | Compares forward and central differences and investigates when reducing the step stops helping. |
| [Least-squares line fitting](linear_algebra/least_squares.py) | Fits a line with an intercept and checks whether the residuals are orthogonal to the columns of the design matrix. |
| [Taylor approximation](calculus/taylor_exp.py) | Approximates the exponential function and compares actual errors with Taylor remainder bounds. |
| [Bisection and Newton's method](calculus/root_finding.py) | Estimates a square root and examines a cubic for which Newton's method cycles from the chosen starting point. |
| [Euler cooling experiment](calculus/euler_cooling.py) | Estimates a cup's temperature and checks how step size affects the error and whether the estimate crosses room temperature. |

## Running the scripts

The scripts use Python 3 and need no additional packages. Open a terminal in the repository folder and choose a command:

```bash
python calculus/integration_experiment.py
python linear_algebra/gaussian_elimination.py
python linear_algebra/classify_systems.py
python calculus/numerical_derivatives.py
python linear_algebra/least_squares.py
python calculus/taylor_exp.py
python calculus/root_finding.py
python calculus/euler_cooling.py
```

On Windows, use `py` instead of `python` if you use the Python launcher.

## Topics to study next

### Linear algebra

- Bases, dimension and linear independence in more depth
- Linear transformations and change of basis
- Orthogonal bases and Gram–Schmidt
- QR factorisation and its connection to least squares
- Diagonalisation and positive definite matrices
- Conditioning and numerical error in linear systems

### Calculus

- Sequences, series and convergence tests
- Taylor expansions around points other than zero
- Using Taylor expansions to analyse numerical methods
- The multivariable chain rule
- Multiple integrals over nonrectangular regions
- Further constrained optimisation

### Engineering mathematics

- Solving other separable first-order differential equations
- Comparing Euler's method with the midpoint method for differential equations
- Stability: when numerical errors shrink and when they grow
- Second-order equations and systems of differential equations

## Exercises that need more practice

Questions to return to:

- Why does Aᵀr = 0 describe a least-squares solution?
- How does an outlier change a fitted line?
- What is the difference between an error bound and the actual error?
- When does increasing a Taylor polynomial's degree stop helping?
- Why does bisection need continuity to guarantee a root?
- Why can Newton's method cycle even when its derivative is nonzero at each step?
- How does a small function residual differ from a small error in the estimated root?
- In the cooling example, can an estimate cross room temperature and still get closer to it on the next step?

## Support and sources

- Stanford's Probability for AI, currently in progress. The exercises in this repository are separate from the course assignments.
- [MIT OCW 18.06 Linear Algebra, Spring 2010](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) is a reference for further study.
- [MIT OCW 18.01SC Single Variable Calculus, Fall 2010](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) is a reference for further study.
- Selected exercises from MIT OCW 18.06SC Fall 2011 and 18.02SC Fall 2010 are credited in the individual notes.

## Attribution
The MIT exercise notes include source links, adaptation notes and their applicable licence. These are independent study notes, not coursework submitted for university credit.
