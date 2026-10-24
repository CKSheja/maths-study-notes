"""Explore Taylor polynomials for exp(x) on [-1, 1]."""

import math


def taylor_exp(x, degree):
    if not isinstance(degree, int) or degree < 0:
        raise ValueError("Degree must be a nonnegative integer.")

    if not math.isfinite(x) or abs(x) > 1:
        raise ValueError(
            "This experiment uses finite x values from -1 to 1."
        )

    term = 1.0
    terms = [term]

    for k in range(1, degree + 1):
        term *= x / k
        terms.append(term)

    return math.fsum(terms)


def error_bound(x, degree):
    """Lagrange bound for truncation error, excluding rounding error."""
    return (
        math.exp(max(0, x))
        * abs(x) ** (degree + 1)
        / math.factorial(degree + 1)
    )


def degree_for_tolerance(x, tolerance):
    if not math.isfinite(x) or abs(x) > 1:
        raise ValueError("Use x between -1 and 1.")

    if not math.isfinite(tolerance) or tolerance <= 0:
        raise ValueError("Tolerance must be positive and finite.")

    for degree in range(21):
        if error_bound(x, degree) <= tolerance:
            return degree

    raise ValueError("No degree up to 20 meets this bound.")


def check_examples():
    assert taylor_exp(0, 6) == 1
    assert math.isclose(taylor_exp(1, 3), 8 / 3)
    assert math.isclose(taylor_exp(-1, 3), 1 / 3)
    assert degree_for_tolerance(1, 0.001) == 6

    for x in (-1.0, 0.5, 1.0):
        for degree in (0, 1, 2, 3, 4, 6, 8, 10):
            approximation = taylor_exp(x, degree)
            error = abs(math.exp(x) - approximation)

            # Allow a small margin for floating-point rounding.
            assert error <= error_bound(x, degree) + 1e-14

    print("Example checks passed.")


def show_comparison(x):
    reference = math.exp(x)

    print()
    print(f"x = {x:g}, reference = {reference:.9f}")
    print(
        f"{'Degree':>6} {'Terms':>6} {'Approximation':>15} "
        f"{'Abs. error':>13} {'Error bound':>13}"
    )

    for degree in (0, 1, 2, 3, 4, 6, 8, 10):
        approximation = taylor_exp(x, degree)
        error = abs(reference - approximation)
        bound = error_bound(x, degree)

        print(
            f"{degree:6d} {degree + 1:6d} "
            f"{approximation:15.9f} {error:13.6e} "
            f"{bound:13.6e}"
        )


def main():
    check_examples()

    for x in (-1.0, 0.5, 1.0):
        show_comparison(x)

    x = 1.0
    tolerance = 0.001

    degree = degree_for_tolerance(x, tolerance)
    approximation = taylor_exp(x, degree)
    error = abs(math.exp(x) - approximation)
    bound = error_bound(x, degree)

    print()
    print(f"Choosing a degree for x = {x:g}")
    print(f"Target error:    {tolerance:g}")
    print(f"Selected degree: {degree}")
    print(f"Number of terms: {degree + 1}")
    print(f"Approximation:   {approximation:.9f}")
    print(f"Absolute error:  {error:.9f}")
    print(f"Error bound:     {bound:.9f}")
    print()
    print("The bound covers truncation error, not floating-point rounding.")


if __name__ == "__main__":
    main()
