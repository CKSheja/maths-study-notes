"""Solve small square linear systems using Gaussian elimination.

AI-assisted learning implementation with partial pivoting.

Run from the repository folder:
    python linear_algebra/gaussian_elimination.py

Singular or numerically near-singular systems are rejected.
"""

import math


def solve_system(matrix, rhs, tolerance=1e-12):
    """Return the unique solution of a square system Ax = b."""
    size = len(matrix)

    if size == 0:
        raise ValueError("The matrix must not be empty.")

    if len(rhs) != size or any(len(row) != size for row in matrix):
        raise ValueError("Use a square matrix and a matching right-hand side.")

    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("Tolerance must be finite and positive.")

    augmented = [
        [float(value) for value in row] + [float(rhs[index])]
        for index, row in enumerate(matrix)
    ]

    if not all(
        math.isfinite(value)
        for row in augmented
        for value in row
    ):
        raise ValueError("All inputs must be finite numbers.")

    scale = max(
        abs(value)
        for row in augmented
        for value in row[:size]
    )

    if scale == 0:
        raise ValueError("The system has no unique solution.")

    threshold = tolerance * scale

    # Forward elimination.
    for column in range(size):
        pivot_row = max(
            range(column, size),
            key=lambda row: abs(augmented[row][column]),
        )

        if abs(augmented[pivot_row][column]) <= threshold:
            raise ValueError(
                "The matrix is singular or numerically near-singular."
            )

        augmented[column], augmented[pivot_row] = (
            augmented[pivot_row],
            augmented[column],
        )

        for row in range(column + 1, size):
            factor = (
                augmented[row][column] / augmented[column][column]
            )
            augmented[row][column] = 0.0

            for entry in range(column + 1, size + 1):
                augmented[row][entry] -= (
                    factor * augmented[column][entry]
                )

    # Back substitution.
    solution = [0.0] * size

    for row in range(size - 1, -1, -1):
        known_terms = math.fsum(
            augmented[row][column] * solution[column]
            for column in range(row + 1, size)
        )

        solution[row] = (
            augmented[row][size] - known_terms
        ) / augmented[row][row]

    return solution


def maximum_residual(matrix, rhs, solution):
    """Largest absolute difference between Ax and b."""
    return max(
        abs(
            math.fsum(a * x for a, x in zip(row, solution))
            - target
        )
        for row, target in zip(matrix, rhs)
    )


def run_checks():
    """Check known solutions, a required row swap and singular rejection."""
    cases = [
        (
            [[2, 1], [1, -1]],
            [5, 1],
            [2, 1],
        ),
        (
            [[0, 2], [1, 1]],
            [4, 3],
            [1, 2],
        ),
        (
            [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]],
            [8, -11, -3],
            [2, 3, -1],
        ),
    ]

    for matrix, rhs, expected in cases:
        actual = solve_system(matrix, rhs)

        if not all(
            math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
            for a, b in zip(actual, expected)
        ):
            raise AssertionError(
                f"Expected {expected}, received {actual}"
            )

    try:
        solve_system([[1, 2], [2, 4]], [3, 6])
    except ValueError:
        pass
    else:
        raise AssertionError("A singular matrix should be rejected.")

    print("All built-in checks passed.")


def main():
    run_checks()

    matrix = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2],
    ]
    rhs = [8, -11, -3]

    solution = solve_system(matrix, rhs)

    print("\nSolution:")
    for name, value in zip(["x", "y", "z"], solution):
        print(f"{name} = {value:.6f}")

    residual = maximum_residual(matrix, rhs, solution)
    print(f"\nMaximum absolute residual: {residual:.3e}")


if __name__ == "__main__":
    main()
