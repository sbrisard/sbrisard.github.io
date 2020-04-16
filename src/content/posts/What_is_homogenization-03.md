Title: What is homogenization? Part 3: ensemble averages vs. volume averages
Date: 2020-04-15
Category: Homogenization
UseKaTeX: True

In the [previous instalment]({filename}20200408-What_is_homogenization-02.md) of
this series on homogenization, we discussed homogenization of a distribution of
black dots on a white background to a uniform shade of gray. In that example,
homogenization boils down to evaluating the fraction of the total are occupied
by the dots: this is the so-called *rule of mixtures*. Of course, in most
real-case applications, the homogenization process is much more complex than
merely evaluating a surface (or volume) fraction. However, before we move onto
such more difficult homogenization processes, we will discuss in more detail
volume fractions in the present post, where we will introduce *periodic* and
*random* homogenization.

In the halftoning example that we used
[previously]({filename}20200408-What_is_homogenization-02.md), computing the
effective gray-level was fairly easy owing to the fact that the dots were
regularly spaced. The pattern is in fact periodic: the whole plane (or space)
can be paved with one single *unit-cell* (a hexagon in the present case).

![The unit-cell]({static}What_is_homogenization/unit-cell.png){.fig30p100}

Once the unit-cell had been identified, the effective gray-level was computed as
the following surface fraction

$$\text{effective gray level} = \frac{surface area of white region}{surface area of unit-cell}.$$

This is an example of what is called *periodic homogenization*, meaning that the
heterogeneities are laid out in a periodic pattern. Homogenization in the
periodic case is generally a three-step process

1. identify the unit-cell,
2. solve an auxiliary problem on the unit-cell,
3. post-process the solution to the auxiliary problem to compute the effective
   properties.

In the above example

1. the unit-cell (point 1) is a hexagon,
2. the auxiliary problem reads: “compute the surface area of the unit-cell and
   the surface area of the white region”,
3. post-processing reduces to forming the surface ratio.

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- coding: utf-8 -->
<!-- End: -->
