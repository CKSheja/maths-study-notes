"""Classify small linear systems using exact row reduction.

Python standard library only.

Use integers or strings such as "0.1" and "1/3" for exact inputs.
This is a learning implementation, not a large-scale numerical solver.
"""

from fractions import Fraction


def solve_system(coefficients, constants, show_steps=False):
    """Return the solution type, reduced matrix and solution family."""
    if not coefficients or not coefficients[0]:
        raise ValueError("Provide at least one equation and one unknown.")

    number_of_variables = len(coefficients[0])

    if (
        len(constants) != len(coefficients)
        or any(len(row) != number_of_variables for row in coefficients)
    ):
        raise ValueError("Matrix dimensions and constants do not match.")

    # Build a new augmented matrix, leaving the original inputs unchanged.
    matrix = [
        [Fraction(str(value)) for value in row]
        + [Fraction(str(constant))]
        for row, constant in zip(coefficients, constants)
    ]

    number_of_equations = len(matrix)

    def display(label):
        if show_steps:
            print(label)
            for row in matrix:
                left = " ".join(str(value) for value in row[:-1])
                print(f"  {left} | {row[-1]}")

    display("Augmented matrix:")

    pivot_columns = []
    pivot_row = 0

    for column in range(number_of_variables):
        candidate = next(
            (
                row
                for row in range(pivot_row, number_of_equations)
                if matrix[row][column] != 0
            ),
            None,
        )

        if candidate is None:
            continue

        if candidate != pivot_row:
            matrix[pivot_row], matrix[candidate] = (
                matrix[candidate],
                matrix[pivot_row],
            )
            display(f"Swap R{pivot_row + 1} and R{candidate + 1}")

        pivot = matrix[pivot_row][column]

        matrix[pivot_row] = [
            value / pivot for value in matrix[pivot_row]
        ]
        display(f"Divide R{pivot_row + 1} by {pivot}")

        # Eliminate above and below the pivot.
        for row in range(number_of_equations):
            if row == pivot_row:
                continue

            factor = matrix[row][column]

            if factor != 0:
                matrix[row] = [
                    value - factor * pivot_value
                    for value, pivot_value in zip(
                        matrix[row], matrix[pivot_row]
                    )
                ]

                display(
                    f"R{row + 1} <- R{row + 1}"
                    f" - ({factor}) R{pivot_row + 1}"
                )

        pivot_columns.append(column)
        pivot_row += 1

        if pivot_row == number_of_equations:
            break

    # A contradiction takes priority over counting free variables.
    inconsistent = any(
        all(value == 0 for value in row[:-1]) and row[-1] != 0
        for row in matrix
    )

    if inconsistent:
        return {
            "kind": "none",
            "rref": matrix,
            "particular": None,
            "basis": [],
        }

    free_columns = [
        column
        for column in range(number_of_variables)
        if column not in pivot_columns
    ]

    # One particular solution: set all free variables to zero.
    particular = [
        Fraction(0) for _ in range(number_of_variables)
    ]

    for row, column in enumerate(pivot_columns):
        particular[column] = matrix[row][-1]

    # Construct one null-space direction for each free variable.
    basis = []

    for free_column in free_columns:
        direction = [
            Fraction(0) for _ in range(number_of_variables)
        ]
        direction[free_column] = Fraction(1)

        for row, column in enumerate(pivot_columns):
            direction[column] = -matrix[row][free_column]

        basis.append(direction)

    return {
        "kind": "infinite" if free_columns else "unique",
        "rref": matrix,
        "particular": particular,
        "basis": basis,
    }


def multiply(matrix, vector):
    """Multiply a matrix by a vector using exact arithmetic."""
    return [
        sum(
            Fraction(str(coefficient)) * value
            for coefficient, value in zip(row, vector)
        )
        for row in matrix
    ]


def verify_family(matrix, constants, result):
    """Check A*p=b and A*v=0 for each solution direction."""
    if result["kind"] == "none":
        return False

    expected = [
        Fraction(str(constant)) for constant in constants
    ]

    particular_is_valid = (
        multiply(matrix, result["particular"]) == expected
    )

    directions_are_valid = all(
        multiply(matrix, direction) == [0] * len(matrix)
        for direction in result["basis"]
    )

    return particular_is_valid and directions_are_valid


def format_vector(vector):
    return "(" + ", ".join(map(str, vector)) + ")"


def run_checks():
    cases = [
        # One solution.
        ([[1, 1], [2, -1]], [5, 1], "unique"),

        # Infinitely many solutions.
        ([[1, 1], [2, 2]], [5, 10], "infinite"),

        # No solution.
        ([[1, 1], [2, 2]], [5, 12], "none"),

        # A row swap is required.
        ([[0, 1], [1, 1]], [3, 5], "unique"),

        # A zero equation leaves both variables free.
        ([[0, 0]], [0], "infinite"),

        # A zero coefficient row with a nonzero constant.
        ([[0, 0]], [1], "none"),

        # Two free variables.
        ([[1, 1, 1]], [4], "infinite"),

        # More equations than unknowns, but consistent.
        ([[1], [2]], [3, 6], "unique"),

        # More equations than unknowns, but inconsistent.
        ([[1], [2]], [3, 7], "none"),
    ]

    for matrix, constants, expected_kind in cases:
        result = solve_system(matrix, constants)

        assert result["kind"] == expected_kind

        if expected_kind != "none":
            assert verify_family(matrix, constants, result)

    known_solution = solve_system(
        [[1, 1], [2, -1]], [5, 1]
    )
    assert known_solution["particular"] == [2, 3]

    print(f"{len(cases)} system checks passed.")


if __name__ == "__main__":
    run_checks()

    examples = [
        ("Exercise 1", [[1, 1], [2, -1]], [5, 1]),
        ("Exercise 2", [[1, 1], [2, 2]], [5, 10]),
        ("Exercise 3", [[1, 1], [2, 2]], [5, 12]),
    ]

    for name, matrix, constants in examples:
        print("\n" + name)

        result = solve_system(
            matrix, constants, show_steps=True
        )

        print("Classification:", result["kind"])

        if result["kind"] == "none":
            print(
                "A row asserts that zero equals "
                "a nonzero constant."
            )
        else:
            expression = format_vector(
                result["particular"]
            )

            for index, direction in enumerate(
                result["basis"], start=1
            ):
                expression += (
                    f" + t{index} * "
                    f"{format_vector(direction)}"
                )

            print("Solution:", expression)
            print(
                "Exact substitution check:",
                verify_family(matrix, constants, result),
            )
