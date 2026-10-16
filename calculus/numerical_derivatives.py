"""Compare numerical derivatives with known exact derivatives.

Python standard library only.
"""

import math


def derivative(function, x, h, method="central"):
    """Approximate a derivative using a positive step size."""
    if not math.isfinite(h) or h <= 0:
        raise ValueError("h must be positive and finite.")

    if method not in ("forward", "central"):
        raise ValueError("Choose forward or central.")

    if x + h == x or (
        method == "central" and x - h == x
    ):
        raise ValueError(
            "h is too small to change x "
            "in floating-point arithmetic."
        )

    if method == "forward":
        return (function(x + h) - function(x)) / h

    return (
        function(x + h) - function(x - h)
    ) / (2 * h)


def run_checks():
    # A line has a constant derivative.
    line_result = derivative(
        lambda x: 3 * x + 2, 1, 0.01
    )
    assert math.isclose(
        line_result, 3, abs_tol=1e-10
    )

    # Central differences are exact for a quadratic
    # in exact arithmetic; allow floating-point error.
    quadratic_result = derivative(
        lambda x: x * x, 2, 0.1
    )
    assert math.isclose(
        quadratic_result, 4, abs_tol=1e-10
    )

    sine_result = derivative(
        math.sin, 0, 1e-3
    )
    assert math.isclose(
        sine_result, 1, abs_tol=2e-7
    )

    for invalid_step in (0, -1, float("inf")):
        try:
            derivative(math.sin, 0, invalid_step)
        except ValueError:
            pass
        else:
            raise AssertionError(
                "An invalid step was accepted."
            )

    print("Derivative checks passed.")


if __name__ == "__main__":
    run_checks()

    cases = [
        (
            "x^2 at x=2",
            lambda x: x * x,
            2.0,
            4.0,
        ),
        (
            "sin(x) at x=0 (radians)",
            math.sin,
            0.0,
            1.0,
        ),
        (
            "exp(x) at x=1",
            math.exp,
            1.0,
            math.e,
        ),
    ]

    steps = [
        1e-1,
        1e-2,
        1e-3,
        1e-5,
        1e-7,
        1e-9,
        1e-12,
        1e-15,
    ]

    for label, function, x, exact in cases:
        print(
            "\n" + label
            + f"; exact derivative = {exact:.12g}"
        )

        print(
            f"{'h':>10} "
            f"{'forward':>15} "
            f"{'central':>15} "
            f"{'forward error':>15} "
            f"{'central error':>15}"
        )

        for h in steps:
            forward = derivative(
                function, x, h, "forward"
            )
            central = derivative(
                function, x, h, "central"
            )

            forward_error = abs(forward - exact)
            central_error = abs(central - exact)

            print(
                f"{h:10.1e} "
                f"{forward:15.9g} "
                f"{central:15.9g} "
                f"{forward_error:15.6e} "
                f"{central_error:15.6e}"
            )
