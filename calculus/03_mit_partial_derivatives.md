# MIT OCW practice — Partial derivatives

Source: MIT OpenCourseWare, 18.02SC Multivariable Calculus, Fall 2010, taught by Denis Auroux.

[Session 26 exercise](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/resources/mit18_02sc_pb_25_quest/)

[Published solution](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/resources/mit18_02sc_pb_25_comb/)

The tasks are paraphrased below. This AI-assisted explanation was checked against the published solution.

## Function and tasks

$$
f(x,y)=e^{x^2+y^2}+x^2+y^2+xy+2y+3
$$

Find the first partial derivatives, compare the mixed second partial derivatives and evaluate fₓ at (1, 3).

## 1. Partial derivative with respect to x

Hold y constant. Using the chain rule:

$$
\frac{\partial}{\partial x}e^{x^2+y^2}=2xe^{x^2+y^2}
$$

Including the remaining terms:

$$
\boxed{f_x=2xe^{x^2+y^2}+2x+y}
$$

## 2. Partial derivative with respect to y

Hold x constant:

$$
\boxed{f_y=2ye^{x^2+y^2}+2y+x+2}
$$

## 3. Mixed partial derivatives

Differentiate fₓ with respect to y:

$$
\frac{\partial}{\partial y}(f_x)
=2x(2ye^{x^2+y^2})+1
=4xye^{x^2+y^2}+1
$$

Differentiate fᵧ with respect to x:

$$
\frac{\partial}{\partial x}(f_y)
=2y(2xe^{x^2+y^2})+1
=4xye^{x^2+y^2}+1
$$

The results agree.

## 4. Evaluate at (1, 3)

$$
f_x(1,3)=2(1)e^{1^2+3^2}+2(1)+3
$$

$$
\boxed{f_x(1,3)=2e^{10}+5}
$$

## Questions to revisit

Why does xy contribute y to fₓ and x to fᵧ?

The variable not being differentiated is held constant.

Do mixed partial derivatives always agree?

Not without conditions. Here the second partial derivatives are continuous, so they agree.

## Attribution

Adapted from the MIT OCW exercise linked above. Explanatory steps and discussion questions were added.

This adapted note is shared under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
