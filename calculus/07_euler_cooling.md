# Euler's method: how fast does a cup cool?

A cup starts at 80°C in a room that stays at 20°C. If we know how fast the cup is cooling right now, how can we estimate its temperature ten minutes later?

In the [root-finding exercise](06_root_finding.md), Newton's method used the slope at one point to estimate where a curve crosses zero. Here the slope tells us how temperature changes with time. We use it to move forward a few minutes, then calculate the slope again.

## 1. Set up the cooling model

Let T be the cup's temperature in °C and t the time in minutes. Assume the cooling rate is proportional to the difference between the cup and room temperatures. For this exercise, use a cooling constant of 0.1 per minute.

$$
\frac{dT}{dt}=-0.1(T-20), \qquad T(0)=80.
$$

Two quick checks:

- At 80°C, the rate is −0.1 × (80 − 20) = −6°C/min. The cup cools.
- At 20°C, the rate is zero. A cup already at room temperature stays there.

These values are chosen for the exercise. They are not measurements from a real cup.

## 2. Work out the first two steps

Euler's rule is:

$$
T_{\text{next}} = T_{\text{current}} + h \times \text{current rate},
$$

where h is the step size in minutes. Start with h = 2 minutes.

| Time at start | Temperature | Rate at start | Estimate two minutes later |
| --- | ---: | ---: | --- |
| 0 min | 80°C | −6°C/min | 80°C + (2 min)(−6°C/min) = **68°C** |
| 2 min | 68°C | −4.8°C/min | 68°C + (2 min)(−4.8°C/min) = **58.4°C** |

The second step is smaller even though both steps cover two minutes. At 68°C the cup is closer to room temperature, so it cools more slowly.

## 3. Check the ten-minute estimate

Let D = T − 20, the temperature difference between the cup and the room. It starts at 60°C and satisfies D′ = −0.1D. An exponential fits that equation:

$$
D(t)=60e^{-0.1t}, \qquad T(t)=20+60e^{-0.1t}.
$$

We can check this by substitution: it gives T(0) = 80, and its derivative is −0.1 times the temperature difference.

At ten minutes the exact temperature **under this model** is 20 + 60/e, about **42.073°C**. That gives us something to compare the Python estimates with.

| Step size | Steps to reach 10 min | Euler estimate | Absolute error |
| ---: | ---: | ---: | ---: |
| 2 min | 5 | 39.661°C | 2.412°C |
| 1 min | 10 | 40.921°C | 1.152°C |
| 0.5 min | 20 | 41.509°C | 0.564°C |
| 0.25 min | 40 | 41.794°C | 0.279°C |

Why are all the estimates too cold? During each step the cooling slows down, but Euler keeps using the faster rate from the start of that step. A shorter step lets it update the rate sooner. In this example, halving the step roughly halves the error at ten minutes.

## 4. Same cup, same twelve minutes, different answers

**One 12-minute step:** the initial rate is −6°C/min, so Euler gives 80 + 12(−6) = **8°C**. That is below the 20°C room temperature, which the exact model never crosses.

**Two 6-minute steps:**

1. At 6 minutes: 80 + 6(−6) = **44°C**.
2. The new rate is −0.1 × (44 − 20) = −2.4°C/min.
3. At 12 minutes: 44 + 6(−2.4) = **29.6°C**.

Both calculations cover twelve minutes. The second one gets a chance to update the cooling rate halfway through. It still underestimates the exact value of about 38.07°C, but it no longer crosses below room temperature.

## A way to predict the overshoot

Writing Euler's update in terms of the temperature difference gives:

$$
D_{\text{next}} = (1-0.1h)D_{\text{current}}.
$$

For a 6-minute step, the multiplier is 0.4, so the difference stays positive. For a 12-minute step, it is −0.2, so the difference changes sign. That explains the 8°C result before we even run the script.

**Question to revisit:** What happens when h is exactly 10 minutes? Compare what Euler predicts after one step with the exact ten-minute temperature above.

[Run the Python experiment](euler_cooling.py)
