# Taylor approximations: choosing enough terms

## Question

Approximate e using a polynomial for eˣ around x = 0.

How many terms are enough to guarantee an approximation error below 0.001?

This lesson connects derivatives to numerical approximation. The aim is to calculate an approximation and give a mathematical reason to trust its accuracy.

## 1. Build the polynomial from derivatives

A Taylor polynomial of degree n around zero is:

Pₙ(x) = f(0) + f′(0)x + f″(0)x²/2! + ... + f⁽ⁿ⁾(0)xⁿ/n!

For f(x) = eˣ, every derivative is also eˣ.

Therefore:

f(0) = f′(0) = f″(0) = ... = 1

So:

Pₙ(x) = 1 + x + x²/2! + ... + xⁿ/n!

For example:

P₃(x) = 1 + x + x²/2 + x³/6

The coefficients are chosen so the polynomial and eˣ have the same value and first n derivatives at zero.

## 2. First approximation of e

Set x = 1:

P₃(1) = 1 + 1 + 1/2 + 1/6
      = 8/3
      ≈ 2.666666667

Using e ≈ 2.718281828 as a reference:

absolute error ≈ |2.718281828 − 2.666666667|
               ≈ 0.051615162

This is larger than our target of 0.001.

## 3. Add more terms

For degree 5:

P₅(1) = 1 + 1 + 1/2 + 1/6 + 1/24 + 1/120
      = 163/60
      ≈ 2.716666667

Absolute error:

|e − P₅(1)| ≈ 0.001615162

Still too large.

For degree 6:

P₆(1) = P₅(1) + 1/720
      = 1957/720
      ≈ 2.718055556

Absolute error:

|e − P₆(1)| ≈ 0.000226273

This meets the target.

Degree 6 means seven terms, including the constant term.

## 4. Establish an error bound

Comparing with a reference value tells us the observed error. Taylor's theorem gives a bound without needing the exact value of the remainder.

The Lagrange remainder is:

Rₙ(x) = f⁽ⁿ⁺¹⁾(ξ)xⁿ⁺¹/(n + 1)!

Here, ξ lies between zero and x.

For f(x) = eˣ:

|Rₙ(x)| = e^ξ |x|ⁿ⁺¹/(n + 1)!

Because eˣ is increasing:

e^ξ ≤ e^max(0,x)

Therefore:

|Rₙ(x)| ≤ e^max(0,x) |x|ⁿ⁺¹/(n + 1)!

At x = 1:

|Rₙ(1)| ≤ e/(n + 1)!

For degree 5:

|R₅(1)| ≤ e/720
         ≈ 0.003775391

This bound does not guarantee error below 0.001.

For degree 6:

|R₆(1)| ≤ e/5040
         ≈ 0.000539342

This does guarantee error below 0.001 in exact arithmetic.

We can even avoid using a precise value of e in this argument. Since e < 3:

|R₆(1)| < 3/5040
         ≈ 0.000595238
         < 0.001

## 5. A bound is not the actual error

For degree 6 at x = 1:

Actual error ≈ 0.000226273
Error bound  ≈ 0.000539342

The bound is larger because it uses an upper limit for the derivative throughout the interval.

A bound above the target does not prove that an approximation fails. It means this particular bound cannot certify it.

In this example, the reference calculation separately confirms that degree 5 fails.

## 6. Why increasing the degree eventually works here

For a fixed x, define:

Bₙ = e^max(0,x) |x|ⁿ⁺¹/(n + 1)!

The ratio of consecutive bounds is:

Bₙ₊₁ / Bₙ = |x|/(n + 2)

For |x| ≤ 1, this ratio is at most 1/(n + 2).

The bound therefore tends to zero as n increases. This establishes convergence of these Taylor polynomials to eˣ on the interval used in the experiment.

This conclusion relies on the remainder shrinking. Merely writing a Taylor series does not establish convergence to the original function for every possible function.

## 7. Turn the polynomial into an algorithm

The terms are:

1, x, x²/2!, x³/3!, ...

Instead of calculating every power and factorial separately, use the previous term.

If:

tₖ₋₁ = xᵏ⁻¹/(k − 1)!

then:

tₖ = tₖ₋₁ × x/k

For x = 1:

t₀ = 1
t₁ = 1 × 1/1 = 1
t₂ = 1 × 1/2 = 1/2
t₃ = (1/2) × 1/3 = 1/6

Algorithm:

1. Start with term = 1.
2. For k from 1 to n, multiply the previous term by x/k.
3. Add the terms.
4. Compare the approximation with Python's math.exp.
5. Calculate the theoretical remainder bound.

The script uses math.fsum to reduce summation error.

Generating and summing n + 1 terms takes O(n) time. This implementation stores the terms in a list, so it also uses O(n) memory.

## 8. Choose the degree automatically

To find a degree for a target error:

1. Start at degree zero.
2. Calculate the remainder bound.
3. Stop at the first degree whose bound is at most the target.
4. Otherwise, increase the degree.

This selects the smallest degree certified by this bound within the search range. It does not necessarily select the smallest degree whose actual error meets the target.

The script searches degrees 0 through 20.

## 9. Worked exercise: approximate e⁻¹

Using degree 3:

P₃(−1) = 1 − 1 + 1/2 − 1/6
       = 1/3
       ≈ 0.333333333

Reference value:

e⁻¹ ≈ 0.367879441

Absolute error:

|e⁻¹ − P₃(−1)| ≈ 0.034546108

On the interval from −1 to 0, the largest value of eˣ is 1.

Therefore:

|R₃(−1)| ≤ 1/4!
          = 1/24
          ≈ 0.041666667

The observed error is below the bound.

The negative input makes the polynomial terms alternate in sign. This gives a useful contrast with the positive-input examples.

## 10. Run the experiment

From the repository folder:

```bash
python calculus/taylor_exp.py
```

No additional packages are needed.

The script compares approximations at x = −1, 0.5 and 1 for several polynomial degrees.

For x = 1 and a target error of 0.001, it should report:

```text
Selected degree: 6
Number of terms: 7
Approximation:   2.718055556
Absolute error:  0.000226273
Error bound:     0.000539342
```

## 11. Try another tolerance

Change:

```python
tolerance = 0.001
```

to:

```python
tolerance = 0.0001
```

For x = 1:

Degree 6 has bound:

e/7! ≈ 0.000539342

Degree 7 has bound:

e/8! ≈ 0.0000674177

The script should therefore select degree 7, which uses eight terms.

## Limits of the experiment

- The polynomial is centred at zero.
- Inputs are restricted to −1 ≤ x ≤ 1.
- Python's math.exp provides a numerical reference, not an exact symbolic value.
- The remainder bound describes polynomial truncation error in exact arithmetic.
- Floating-point rounding introduces an additional error.
- The degree selector does not guarantee the final floating-point error for extremely small tolerances.
- This script is for studying Taylor approximation. It is not a replacement for math.exp.

## Notes after running

To complete during study:

- Can I derive the term recurrence without looking at the code?
- What is the difference between degree and number of terms?
- Why is the bound different for x = −1 and x = 1?
- Why can the actual error meet a target even when a bound does not?
- How did changing the tolerance affect the selected degree?

## Support and sources

This is not an MIT assignment.

MIT OpenCourseWare 18.01SC Single Variable Calculus is a reference for further study of Taylor polynomials and series:

https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/
