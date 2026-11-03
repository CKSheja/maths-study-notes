from math import exp, isclose


def euler(slope, initial_value, duration, steps):
    """Estimate the final value using equally spaced Euler steps."""
    if not isinstance(steps, int) or steps < 1:
        raise ValueError("steps must be a positive integer")

    step_size = duration / steps
    value = initial_value

    for step in range(steps):
        time = step * step_size
        value += step_size * slope(time, value)

    return value


def cooling_rate(time, temperature):
    return -0.1 * (temperature - 20)


def exact_temperature(minutes):
    return 20 + 60 * exp(-0.1 * minutes)


if __name__ == "__main__":
    
    assert isclose(euler(cooling_rate, 80, 4, 2), 58.4)
    assert euler(cooling_rate, 20, 10, 5) == 20

    exact = exact_temperature(10)
    print("Step (min)   Temperature at 10 min (C)   Absolute error (C)")

    for steps in (5, 10, 20, 40):
        estimate = euler(cooling_rate, 80, 10, steps)
        error = abs(estimate - exact)
        print(f"{10 / steps:10.2f}   {estimate:25.3f}   {error:18.3f}")

    print(f"\nExact at 10 min: {exact:.3f} C")

    print("\nSame cup, same 12 minutes:")
    for steps in (1, 2):
        estimate = euler(cooling_rate, 80, 12, steps)
        print(f"{steps} step(s) of {12 / steps:g} min: {estimate:.1f} C")

    print(f"Exact at 12 min: {exact_temperature(12):.2f} C")
