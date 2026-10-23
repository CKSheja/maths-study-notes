"""Fit a straight line by least squares using only the standard library."""

from math import fsum, isclose


def fit_line(points):
    """Return intercept and slope for y ≈ intercept + slope*x."""
    points = list(points)

    if len(points) < 2:
        raise ValueError("Provide at least two points.")

    mean_x = fsum(x for x, _ in points) / len(points)
    mean_y = fsum(y for _, y in points) / len(points)

    denominator = fsum((x - mean_x) ** 2 for x, _ in points)

    if denominator == 0:
        raise ValueError(
            "A unique line needs at least two distinct x values."
        )

    numerator = fsum(
        (x - mean_x) * (y - mean_y)
        for x, y in points
    )

    slope = numerator / denominator
    intercept = mean_y - slope * mean_x

    return intercept, slope


def check_examples():
    points = [(0, 1), (1, 2), (2, 2)]
    intercept, slope = fit_line(points)

    assert isclose(intercept, 7 / 6)
    assert isclose(slope, 1 / 2)

    residuals = [
        y - (intercept + slope * x)
        for x, y in points
    ]

    assert isclose(fsum(r * r for r in residuals), 1 / 6)
    assert isclose(fsum(residuals), 0, abs_tol=1e-12)
    assert isclose(
        fsum(
            x * r
            for (x, _), r in zip(points, residuals)
        ),
        0,
        abs_tol=1e-12,
    )

    intercept, slope = fit_line([(0, 1), (1, 3), (2, 5)])
    assert isclose(intercept, 1)
    assert isclose(slope, 2)

    intercept, slope = fit_line([(0, 1), (0, 3), (1, 4)])
    assert isclose(intercept, 2)
    assert isclose(slope, 2)

    try:
        fit_line([(1, 2), (1, 5)])
    except ValueError:
        pass
    else:
        raise AssertionError("Identical x values should be rejected.")

    print("Example checks passed.")


def main():
    check_examples()

    points = [(0, 1), (1, 2), (2, 2)]
    intercept, slope = fit_line(points)

    predictions = [
        intercept + slope * x
        for x, _ in points
    ]

    residuals = [
        y - predicted
        for (_, y), predicted in zip(points, predictions)
    ]

    squared_error = fsum(r * r for r in residuals)
    residual_sum = fsum(residuals)
    weighted_residual_sum = fsum(
        x * r
        for (x, _), r in zip(points, residuals)
    )

    print()
    print(f"Intercept: {intercept:.6f}")
    print(f"Slope:     {slope:.6f}")
    print()
    print(f"{'x':>8} {'Observed':>10} {'Predicted':>10} {'Residual':>10}")

    for (x, y), predicted, residual in zip(
        points, predictions, residuals
    ):
        print(
            f"{x:8.3f} {y:10.3f} "
            f"{predicted:10.6f} {residual:10.6f}"
        )

    print()
    print(f"SSE:       {squared_error:.6f}")
    print(f"Sum r:     {residual_sum:.3e}")
    print(f"Sum x*r:   {weighted_residual_sum:.3e}")
    print("Both residual sums should be close to zero.")


if __name__ == "__main__":
    main()
