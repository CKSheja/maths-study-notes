# Maths study notes

I am revisiting mathematics alongside my software engineering studies. High school gave me a foundation in calculus, probability, statistics, algebra and mathematical logic. Some topics are still familiar; others need revision and practice.

I recently started Stanford's Probability for AI course. It has given me a reason to return to these ideas and explore how they are used in AI. Through this repository, I want to strengthen my understanding, work through more demanding problems and connect mathematical methods with code.

These notes bring together worked exercises, explanations and small Python experiments. They include revision alongside deeper study of linear algebra, multivariable calculus and numerical methods.

## Study approach

Each lesson connects a mathematical question with worked calculations and, where useful, a Python implementation. I want to understand why the method works, check its results and explore its limitations by changing the inputs.

## Current exercises

### Revision and further study

- [Functions, domains and exponential growth](precalculus/01_functions.md)
- [Quadratic functions](precalculus/01_quadratic_function.md)
- [Vectors and systems](linear_algebra/01_vectors_and_systems.md)
- [Linear systems, null spaces and eigenvalues](linear_algebra/01_vectors_and_matrices.md)
- [Derivatives, gradients and constrained optimisation](calculus/01_derivatives.md)
- [Integration and numerical approximation](calculus/02_integration.md)
- [Gaussian elimination: worked example and algorithm](linear_algebra/03_gaussian_elimination.md)

### Selected MIT OpenCourseWare exercises

- [18.06SC: Nullspaces, Problem 6.3](linear_algebra/02_mit_nullspaces.md)
- [18.02SC: Partial derivatives, Session 26](calculus/03_mit_partial_derivatives.md)

Each MIT exercise note identifies the exact source and links to the published solution.

## Next two study sessions

These are planned sessions. I will record completion and observations after working through them.

| Planned date | Lesson | Main question |
| --- | --- | --- |
| 16 October 2026 | [Linear systems: three possible outcomes](linear_algebra/04_solution_types.md) | How do row operations distinguish one, infinitely many or no solutions? |
| 16 October 2026 | [From derivatives to a numerical algorithm](calculus/04_numerical_derivatives.md) | How does step size affect a derivative approximation? |

Both lessons include worked answers, an algorithm, code and further examples to explore. The dates are a guide; I can spend longer on a lesson where needed.

## Python experiments

### Numerical integration

[Script](calculus/integration_experiment.py) · [Results and observations](calculus/integration_results.md)

Compares midpoint and trapezoidal approximations for:

- x² from 0 to 1
- sin(x) from 0 to π
- exp(x) from 0 to 1

The experiment increases the number of intervals and reports absolute errors against known exact answers.

The recorded integration results came from running the shared script in ChatGPT's Python environment. That execution context is documented in the results file.

### Gaussian elimination

[Script](linear_algebra/gaussian_elimination.py) · [Worked lesson](linear_algebra/03_gaussian_elimination.md)

Solves small square linear systems using elimination, partial pivoting and back substitution.

Checks include known solutions, a row swap and rejection of a singular matrix. The script also reports the residual when the computed solution is substituted into the original equations.

This earlier implementation rejects singular or numerically near-singular systems rather than classifying their solution sets.

### Classifying linear systems

[Script](linear_algebra/classify_systems.py) · [Worked lesson](linear_algebra/04_solution_types.md)

Uses exact fractions and Gauss–Jordan elimination to classify small systems and display row operations.

For consistent systems, it returns a particular solution and directions for any free variables. It checks these against the original equations.

This is a separate learning implementation. It does not replace the earlier floating-point solver or model uncertainty in measured inputs.

### Numerical derivatives

[Script](calculus/numerical_derivatives.py) · [Worked lesson](calculus/04_numerical_derivatives.md)

Compares forward and central differences for a quadratic, sine and an exponential.

It reports errors against exact derivatives over several step sizes, including very small steps where rounding can become important.

## Running the scripts

Requires Python 3. No additional packages are needed.

Download or clone the repository and open a terminal in its root folder.

Run the integration experiment:

```bash
python calculus/integration_experiment.py
```

Run the original Gaussian elimination example:

```bash
python linear_algebra/gaussian_elimination.py
```

Run the solution classification examples:

```bash
python linear_algebra/classify_systems.py
```

Run the numerical derivative experiment:

```bash
python calculus/numerical_derivatives.py
```

On Windows, replace `python` with `py` if your installation uses the Python launcher.

GitHub displays the scripts but does not execute them.

## Topics to revisit and extend

This is a study plan, not a list of completed topics. Some build on school mathematics; others introduce methods I have not yet worked through.

### Linear algebra

- Bases, dimension and linear independence
- Linear transformations and change of basis
- Orthogonal projections and least squares
- Diagonalisation and positive definite matrices
- Conditioning and numerical error in linear systems

### Calculus

- Sequences, series and convergence
- Taylor approximations and error bounds
- The multivariable chain rule
- Multiple integrals over nonrectangular regions
- Further constrained optimisation

### Engineering mathematics

- First-order and second-order differential equations
- Systems of differential equations
- Numerical root-finding
- Numerical methods for differential equations


## Support and sources

- Stanford's Probability for AI: currently in progress. These repository exercises are separate from the course assignments.
- [MIT OCW 18.06 Linear Algebra, Spring 2010](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/): reference for further study.
- [MIT OCW 18.01SC Single Variable Calculus, Fall 2010](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/): reference for further study.
- Selected exercises from MIT OCW 18.06SC Fall 2011 and 18.02SC Fall 2010, credited in the individual files.

These are independent study notes, not coursework submitted for university credit.

## Attribution

MIT-derived exercise notes include source links, adaptation notes and their applicable licence. The other exercises are not presented as MIT assignments.
