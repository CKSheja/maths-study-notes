# Numerical integration — results and observations

## Experiment

Compare midpoint and trapezoidal integration for:

- x² on [0, 1], with exact integral 1/3
- sin(x) on [0, π], with exact integral 2
- exp(x) on [0, 1], with exact integral e - 1

[Python script](integration_experiment.py)

The version of the script shared in the study conversation was run in ChatGPT's Python environment on 14 October 2026. It was not downloaded from GitHub for that run.

The results and explanation below were prepared with AI assistance.

## 1. Integral of x²

Exact value: 0.333333333...

| Intervals | Midpoint | Absolute error | Trapezoidal | Absolute error |
|---:|---:|---:|---:|---:|
| 4 | 0.328125000 | 0.005208333 | 0.343750000 | 0.010416667 |
| 8 | 0.332031250 | 0.001302083 | 0.335937500 | 0.002604167 |
| 16 | 0.333007812 | 0.000325521 | 0.333984375 | 0.000651042 |
| 32 | 0.333251953 | 0.000081380 | 0.333496094 | 0.000162760 |
| 64 | 0.333312988 | 0.000020345 | 0.333374023 | 0.000040690 |

## 2. Integral of sin(x)

Exact value: 2.

| Intervals | Midpoint | Absolute error | Trapezoidal | Absolute error |
|---:|---:|---:|---:|---:|
| 4 | 2.052344306 | 0.052344306 | 1.896118898 | 0.103881102 |
| 8 | 2.012909086 | 0.012909086 | 1.974231602 | 0.025768398 |
| 16 | 2.003216378 | 0.003216378 | 1.993570344 | 0.006429656 |
| 32 | 2.000803416 | 0.000803416 | 1.998393361 | 0.001606639 |
| 64 | 2.000200812 | 0.000200812 | 1.999598389 | 0.000401611 |

## 3. Integral of exp(x)

Exact value: 1.718281828...

| Intervals | Midpoint | Absolute error | Trapezoidal | Absolute error |
|---:|---:|---:|---:|---:|
| 4 | 1.713815280 | 0.004466549 | 1.727221905 | 0.008940076 |
| 8 | 1.717163665 | 0.001118163 | 1.720518592 | 0.002236764 |
| 16 | 1.718002192 | 0.000279636 | 1.718841129 | 0.000559300 |
| 32 | 1.718211913 | 0.000069915 | 1.718421660 | 0.000139832 |
| 64 | 1.718264349 | 0.000017479 | 1.718316787 | 0.000034958 |

## Observations

### More intervals reduced the error

Both methods became more accurate as the number of intervals increased.

Doubling the number of intervals reduced the error by approximately a factor of four. This is consistent with second-order convergence for these smooth functions.

For x², the reduction is exactly a factor of four in exact arithmetic.

### Midpoint was more accurate in these examples

Midpoint had a smaller absolute error in every case tested.

This does not establish that midpoint is better for every possible function.

### The direction of error changed with the curve

For x² and exp(x), midpoint underestimated while trapezoidal overestimated.

Both functions are convex on the intervals used: their graphs curve upwards.

For sin(x) on [0, π], the graph is concave. Midpoint overestimated and trapezoidal underestimated.

## Questions for further practice

- What happens with a linear function?
- Does the same error pattern hold for a function with a sharp corner?
- How does Simpson's rule compare?
- At what point might floating-point rounding limit further improvement?
