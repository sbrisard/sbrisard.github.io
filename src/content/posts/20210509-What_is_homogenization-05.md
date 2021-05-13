Title: What is homogenization? Part 5: introducing the representative volume element
Date: 2021-05-09
Category: Homogenization
UseKaTeX: True

In the [previous instalment]({filename}20201208-What_is_homogenization-04.md) of
this series on homogenization, we derived the homogenized properties of a
rectangular spring mesh. Our goal in this post is to analyse the “convergence”
towards the homogenized stiffness; meanwhile, we will discuss the size of the
so-called representative volume element (RVE).

## In the previous episode…

The system considered in this post is shown below. The length of the diagonal
springs is $\ell$; they make an angle $θ$ with the $x$-axis ($Δx=\ell\cosθ$,
$Δy=\ell\sinθ$: grid spacing along the $x$ and $y$ axes). The stiffness of the
diagonal springs is $k$; the stiffnesses of the horizontal and vertical springs
are $χ\_x\,k$ and $χ\_y\,k$, respectively.

![The spring mesh considered here]({static}What_is_homogenization/spring_mesh.png){.fig60p100}

We showed that, in the homogenization limit, this spring mesh behaves as a plate
loaded in its plane only. The effective constitutive law of the equivalent plate
reads

$$N\_{xx}=A\_x^\text{eff}ε\_{xx}+ν\_{xy}^\text{eff}A\_y^\text{eff}ε\_{yy},$$
$$N\_{yy}=A\_y^\text{eff}ε\_{yy}+ν\_{yx}^\text{eff}A\_x^\text{eff}ε\_{xx},$$
$$N\_{xy}=A\_{xy}^\text{eff}ε\_{xy},$$

where $N\_{xx}$, $N\_{yy}$ and $N\_{xy}$ are the membrane stresses (these are
internal forces per unit-length). The effective stiffnesses $A\_x^\text{eff}$,
$A\_y^\text{eff}$ and $A\_{xy}^\text{eff}$ are given by the following
expressions

$$A\_x^\text{eff}=k\operatorname{cotan}θ\bigl(1+\cos2θ+χ\_x\bigr),$$
$$A\_y^\text{eff}=k\tanθ\bigl(1-\cos2θ+χ\_y\bigr),$$
$$A\_{xy}^\text{eff}=2ν\_{xy}^\text{eff}A\_y^\text{eff}
=2ν\_{yx}^\text{eff}A\_x^\text{eff}=2k\sin2θ.$$

In the present post, we will show through numerical experiments that, for
sufficiently large meshes, the set of springs indeed behaves as a continuous
flat membrane.

## A uniaxial tension experiment

We consider a simple uniaxial tension experiment (see below). The system is a
$\mathcal N\_x×\mathcal N\_y$ grid. Except for corner nodes, nodes that are
located on the vertical boundaries are subjected to horizontal forces $Q$ (on
the right-hand side) and $-Q$ (on the left-hand side). For large systems, this
is equivalent to a uniformly distributed load $q=Q/Δy$. Corner nodes pick only
the load applied to half the $y$-spacing: therefore, they are subjected to
$±Q/2$.

![The uniaxial tension experiment]({static}What_is_homogenization/uniaxial_tension.png){.fig60p100}

In the homogenization limit, the system should behave as a plate under uniaxial
tension, for which we should have $N\_{xx}=q$, $N\_{yy}=0$ and
$N\_{xy}=0$. Plugging into the constitutive equations, we find that
$N\_{xx}=\tilde{A}\_x^\text{eff}ε\_{xx}$, where the uniaxial stiffness
$\tilde{A}\_x^\text{eff}$ is defined as follows

$$\tilde{A}\_x^\text{eff}
=A\_x^\text{eff}\bigl(1-ν\_{xy}^\text{eff}ν\_{yx}^\text{eff}\bigr).$$

For “large” (but finite) spring models, we therefore expect the average strain
$⟨ε\_{xx}⟩$ to be related to $q$ through the following formula:
$q=\tilde{A}\_x^\text{eff}⟨ε\_{xx}⟩$.

In order to assess the validity of the above approximation, we need to evaluate
the average strain $⟨ε\_{xx}⟩$ in the spring model. To do so, we draw
inspiration from the following formula that relates (for continuous systems) the
average strain $⟨\tens ε⟩$ in $Ω$ to a boundary integral of the displacement
$\vec u$

$$⟨\tens ε⟩ =\frac1V∫\_{∂Ω}\tfrac12\bigl(\vec u⊗\vec n+\vec n⊗\vec u\bigr),$$

where $\vec n$ denotes the outer normal to $∂Ω$. In the present case, $\vec
e\_x⋅\vec n=0$ on the top and bottom boundaries. On the left and right
boundaries, the integrals are discretized as follows

$$⟨ε\_{xx}⟩\simeq\frac1{\mathcal N\_x\mathcal N\_yΔx}
\sum\_{j=0}^{\mathcal N\_y}w\_j\vec e\_x
⋅\bigl(\vec u\_{\mathcal N\_x,j}-\vec u\_{0, j}\bigr),$$

where $\vec u\_{i,j}$ denotes the displacement of the $(i, j)$ node, located at
$x=iΔx$, $y=jΔy$. In the above formula, the weights $w\_j$ are $w\_j=1$ for
off-corner nodes and $w\_j=\frac12$ for corner nodes.

The average strain $⟨ε\_{xx}⟩$ being defined, we introduce the *apparent*
uniaxial stiffness $\tilde{A}\_{x}^{\text{app}}=q/⟨ε\_{xx}⟩$ and check that
$\tilde{A}\_{x}^{\text{app}}→\tilde{A}\_x^{\text{eff}}$ as the size of the
system grows to infinity.

Now that the stage is set, let us look at the results. In the remainder of this
post, we will consider the following simple case: $θ=π/4$ (square cells),
$χ\_x=χ\_y=χ$ (horizontal and vertical springs are identical), $\mathcal
N\_x=\mathcal N\_y=\mathcal N$ (square mesh). From the general expressions of
the effective stiffnesses, we find in that case

$$A\_x^\text{eff}=A\_y^\text{eff}=k\bigl(1+χ\bigr),\quad
ν\_{xy}=ν\_{yx}=\frac1{1+χ}$$

and

$$\frac{\tilde{A}\_x^\text{eff}}{k}=\frac{χ\bigl(χ+2\bigr)}{χ+1}.$$

## Apparent stiffness of a small system

For small systems, the apparent stiffness can be computed analytically. More
details can be found in a companion post on the [symbolic analysis of a spring
mesh]({filename}20210512-Symbolic_analysis_of_a_spring_mesh.md). We find, for a
1×1 system:

$$\frac{\tilde{A}\_x^\text{app}}k=\frac{4χ\bigl(χ+1\bigr)}{2χ+1},$$

then, for a 2×2 system:

$$\frac{\tilde{A}\_x^\text{app}}k
=\frac{8χ\bigl(χ+1\bigr)\bigl(χ+2\bigr)}{\bigl(2χ+3\bigr)\bigl(3χ+2\bigr)},$$

finally, for a 3×3 system:

$$\frac{\tilde{A}\_x^\text{app}}k
=\frac{144χ\bigl(χ+1\bigr)\bigl(4χ^4+24χ^3+41χ^2+24χ+4\bigr)}
{480χ^5+2888χ^4+5616χ^3+4771χ^2+1800χ+236}.$$

The above expressions of the *apparent* stiffnesses are plotted below. More
precisely, we plot the relative error

$$\frac{\tilde{A}\_x^\text{app}-\tilde{A}\_x^\text{eff}}{\tilde{A}\_x^\text{eff}}$$

against the stiffness ratio $\chi$.

![Apparent stiffness vs. χ]({static}What_is_homogenization/apparent_stiffness_vs_chi.png){.fig60p100}

It is observed that, for a given value of $\chi$, the error tends to decrease
with the size of the system. However, even for 3×3 systems, the difference
between apparent and effective siffnesses (about 20%) remains too high to
conclude about convergence. This means that we need to explore larger systems.

## Apparent stiffness of larger systems

For larger systems, it is no longer practical to establish closed-form
expressions of the apparent stiffness. We must resort to numerical simulations,
that are presented in a 
[companion post]({filename}20210513-Numerical_analysis_of_a_spring_mesh.md).

The simulations are carried out for the set of parameters for which an isotropic
effective behavior is expected, namely $χ\_x=χ\_y=2$ and $θ=π/4$. Then
$A\_x^\text{eff}=A\_y^\text{eff}=3k$ and $A\_{xy}^\text{eff}=2k$. Therefore,
$\tilde{A}\_x^\text{eff}=\frac83k$.

In the figure below, we plot in log-log scale the relative error on the
effective stiffness as a function of the size of the system.

![Apparent stiffness vs. system size]({static}What_is_homogenization/apparent_stiffness_vs_number_of_cells.png){.fig60p100}

From this plot, convergence (as a power of the system size) is quite clear. In
other words, for large enough systems, the network of springs indeed behaves as
a continuous membrane.

Convergence is quite slow, though: for the apparent stiffness to be within 1% of
the effective stiffness, we need a 64×64 system.

## Conclusion

In this post, we have verified (for a specific loading) that the homogenization
procedure developed in the [previous
post]({filename}20201208-What_is_homogenization-04.md) was indeed correct.

We have shown that the size of the system under consideration is important:
remember that, for homogenization to be meaningful, [scales must be
separated]({filename}20200402-What_is_homogenization-01.md).

The convergence plot presented above can be used to introduce what is commonly
–but somewhat confusingly– called the *representative volume element* (RVE). A
system can be considered as a RVE if the relative error between the apparent and
effective values of a specific property are below a given tolerance ([Kanit *et
al.*, 2003](https://doi.org/10.1016/S0020-7683(03)00143-4)).

From the above definition, it should be clear that there is no such thing as
**the** RVE. At best, it is possible to define **a** RVE, for a specific
quantity of interest (in the present case, the homogenized stiffness) and a
user-specified tolerance.

In the next instalment of this series, we will introduce a little bit of
randomness.

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- coding: utf-8 -->
<!-- End: -->
