"""Compare midpoint and trapezoidal integration with exact results.

AI-assisted study experiment.
Run: python calculus/integration_experiment.py
"""

import math


def midpoint_rule(function, start, end, intervals):
    """Approximate an integral using rectangle midpoint heights."""
    if intervals <= 0:
        raise ValueError("The number of intervals must be positive.")

    width = (end - start) / intervals

    heights = (
        function(start + (index + 0.5) * width)
        for index in range(intervals)
    )

    return width * math.fsum(heights)


def trapezoidal_rule(function, start, end, intervals):
    """Approximate an integral using trapezoids."""
    if intervals <= 0:
        raise ValueError("The number of intervals must be positive.")

    width = (end - start) / intervals

    interior_heights = (
        function(start + index * width)
        for index in range(1, intervals)
    )

    return width * (
        (function(start) + function(end)) / 2
        + math.fsum(interior_heights)
    )


def run_experiment(name, function, start, end, exact):
    print(f"\n{name}")
    print(f"Interval: [{start:.6f}, {end:.6f}]")
    print(f"Exact integral: {exact:.9f}\n")

    print(
        f"{'Intervals':>9} "
        f"{'Midpoint':>13} "
        f"{'Abs. error':>13} "
        f"{'Trapezoidal':>13} "
        f"{'Abs. error':>13}"
    )

    for intervals in [4, 8, 16, 32, 64]:
        midpoint = midpoint_rule(function, start, end, intervals)
        trapezoidal = trapezoidal_rule(
            function, start, end, intervals
        )

        print(
            f"{intervals:9d} "
            f"{midpoint:13.9f} "
            f"{abs(midpoint - exact):13.9f} "
            f"{trapezoidal:13.9f} "
            f"{abs(trapezoidal - exact):13.9f}"
        )


def main():
    experiments = [
        ("Integral of x^2", lambda x: x**2, 0.0, 1.0, 1 / 3),
        ("Integral of sin(x)", math.sin, 0.0, math.pi, 2.0),
        ("Integral of exp(x)", math.exp, 0.0, 1.0, math.e - 1),
    ]

    for experiment in experiments:
        run_experiment(*experiment)


if __name__ == "__main__":
    main()
