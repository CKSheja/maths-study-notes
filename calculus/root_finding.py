"""Compare bisection and Newton's method on two equations."""

import math


def bisection(f, left, right, tolerance=1e-8, max_steps=100):
    if not left < right or tolerance <= 0 or max_steps < 1:
        raise ValueError("Check the interval, tolerance and step limit.")

    f_left, f_right = f(left), f(right)

    if f_left == 0:
        return left, []

    if f_right == 0:
        return right, []

    if (f_left > 0) == (f_right > 0):
        raise ValueError("The endpoint values must have opposite signs.")

    history = []

    for step in range(1, max_steps + 1):
        midpoint = left + (right - left) / 2
        value = f(midpoint)
        bound = (right - left) / 2

        history.append((step, midpoint, value, bound))

        if value == 0 or bound <= tolerance:
            return midpoint, history

        if midpoint == left or midpoint == right:
            raise RuntimeError(
                "Floating-point resolution prevents further bisection."
            )

        if (value > 0) == (f_left > 0):
            left, f_left = midpoint, value
        else:
            right = midpoint

    raise RuntimeError("Bisection reached its step limit.")


def newton(
    f, derivative, start, residual_tolerance=1e-10, max_steps=20
):
    if residual_tolerance <= 0 or max_steps < 1:
        raise ValueError("Tolerance and step limit must be positive.")

    x = float(start)
    history = []

    for step in range(max_steps + 1):
        value = f(x)
        history.append((step, x, value))

        if abs(value) <= residual_tolerance:
            return x, history, "Residual target reached"

        if step == max_steps:
            break

        slope = derivative(x)

        if slope == 0:
            return x, history, "Stopped: zero derivative"

        next_x = x - value / slope

        if not math.isfinite(next_x):
            return x, history, "Stopped: non-finite next iterate"

        if next_x == x:
            return (
                x,
                history,
                "Stopped: no change in floating-point arithmetic",
            )

        x = next_x

    return x, history, "Stopped: step limit reached"


def quadratic(x):
    return x * x - 2


def quadratic_derivative(x):
    return 2 * x


def cubic(x):
    return x**3 - 2 * x + 2


def cubic_derivative(x):
    return 3 * x * x - 2


def check_examples():
    root, _ = bisection(quadratic, 1, 2)
    assert abs(root - math.sqrt(2)) <= 1e-8

    root, _, status = newton(quadratic, quadratic_derivative, 1)
    assert status == "Residual target reached"
    assert abs(root - math.sqrt(2)) < 1e-10

    _, _, status = newton(quadratic, quadratic_derivative, 0)
    assert status == "Stopped: zero derivative"

    _, history, status = newton(
        cubic, cubic_derivative, 0, max_steps=6
    )
    assert [row[1] for row in history] == [0, 1, 0, 1, 0, 1, 0]
    assert status == "Stopped: step limit reached"

    try:
        bisection(quadratic, 2, 3)
    except ValueError:
        pass
    else:
        raise AssertionError("The invalid bracket should be rejected.")

    print("Example checks passed.")


def print_newton_history(history):
    print(f"{'Update':>6} {'x':>16} {'f(x)':>16}")

    for step, x, value in history:
        print(f"{step:6d} {x:16.10f} {value:16.6e}")


def main():
    check_examples()

    print("\nExample 1: x^2 - 2 = 0")

    root, history = bisection(quadratic, 1, 2)

    print("\nBisection:")
    print(f"Root estimate:       {root:.10f}")
    print(f"Midpoint evaluations: {len(history)}")
    print(f"Final interval bound: {history[-1][3]:.3e}")
    print(f"Reference root error: {abs(root - math.sqrt(2)):.3e}")

    root, history, status = newton(
        quadratic, quadratic_derivative, 1
    )

    print("\nNewton:")
    print_newton_history(history)
    print(status)
    print(f"Reference root error: {abs(root - math.sqrt(2)):.3e}")

    print("\nExample 2: x^3 - 2x + 2 = 0")

    _, history, status = newton(
        cubic, cubic_derivative, 0, max_steps=6
    )

    print("\nNewton starting at zero:")
    print_newton_history(history)
    print(status)

    root, _ = bisection(cubic, -2, -1)

    print("\nBisection on [-2, -1]:")
    print(f"Root estimate: {root:.10f}")
    print(f"Residual:      {abs(cubic(root)):.3e}")


if __name__ == "__main__":
    main()
