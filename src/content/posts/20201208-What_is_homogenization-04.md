Title: What is homogenization? Part 4: a first example
Date: 2020-12-08
Category: Homogenization
UseKaTeX: True

In the [previous instalment]({filename}20200421-What_is_homogenization-03.md) of
this series on homogenization, we discussed volume and ensemble averages for
random heterogeneous materials. In view of introducing *statistical* and
*representative* volume elements, we will introduce in this post our first
homogenization example, namely a two-dimensional, rectangular mesh of springs
that is loaded in its plane only. We will show that this system can be
homogenized as a plate, the [extensional
stiffnesses](https://en.wikipedia.org/wiki/Plate_theory#Stress–strain_relations)
of which we will derive in closed-form.

Note that this example is fully deterministic and in fact, periodic. *Periodic
homogenization* provides a rigorous framework for the derivation of its
effective properties. The derivation presented here is more heuristic and does
not rely on this framework.

The figure below shows the spring mesh considered in this post; $\ell$ is the
length of the diagonal springs. These springs make an angle $\theta$ with the
$x$-axis. The grid spacing is therefore $\Delta x=\ell\cos\theta$ along the
$x$-axis and $\Delta y=\ell\sin\theta$ along the $y$-axis. The stiffness of the
diagonal springs is $k$; the stiffnesses of the horizontal and vertical springs
are $\chi\_x\,k$ and $\chi\_y\,k$, respectively ($\chi\_x$, $\chi\_y$:
dimensionless numbers).

![The spring mesh considered here]({static}What_is_homogenization/spring_mesh.png){.fig60p100}

It will be convenient to introduce the radius-vector of the mesh nodes

$$\vec x\_{ij}=i\Delta x\,\vec e\_x+j\Delta y\,\vec e\_y.$$

Similarly, we introduce the mid-points $\vec x\_{i+1/2, j}$, $\vec x\_{i,
j+1/2}$ and $\vec x\_{i+1/2, j+1/2}$.

Seen from far away, this mesh behaves as a plate that would be loaded in its
plane only. In particular, we will show that when $\theta=\pi/4$ (square mesh)
and $\chi\_x=\chi\_y=2$, the homogenized plate is isotropic, with Poisson ratio
$\nu=1/3$ and membrane stiffness

$$A=\frac{Eh}{1-\nu^2}=3k.$$

## Outline of the homogenization strategy

Our strategy relies on the approximation of the elastic energy of the spring
mesh. It is recalled that the [elastic energy of a
spring]({filename}20201125-On_the_stiffness_matrix_of_a_linear_spring.md) is
fully defined by the displacements of the end-points. In the present case, the
end-points are the vertices $\vec x\_{ij}$ of the grid, with displacement $\vec
u\_{ij}$. Our aim is to replace the discrete set of springs with a continuous
structure. It is natural to assume that the nodal displacements $\vec u\_{ij}$
are the trace of a smooth displacement field, $\vec u$: $\vec u\_{ij}\simeq\vec
u(\vec x\_{ij})$.

Owing to the separation of scales, we will also assume that the typical size of
the microstructure (namely, the size $\ell$ of a spring) is small, compared to
the typical length scale over which the smooth displacement field $\vec u$
varies. **The first element of our strategy** is to perform Taylor expansions of
$\vec u$ with respect to the powers of $\ell$.

**The second element of our strategy** is the fact that the elastic energy of
the mesh is additive. More precisely, it is the sum of the energies of each
spring

$$W=\sum\_{i, j}\bigl(W\_{i+1/2, j}+W\_{i, j+1/2}+W\_{i+1/2, j+1/2}\bigr),$$

where $W\_{i+1/2, j}$ (resp. $W\_{i, j+1/2}$, $W\_{i+1/2, j+1/2}$) denote the
elastic energy of the horizontal (resp. vertical, diagonal) spring centered at
$\vec x\_{i, j+1/2}$ (resp. $\vec x\_{i, j+1/2}$, $\vec x\_{i+1/2,
j+1/2}$). Note that $W\_{i+1/2, j+1/2}$ is the energy of *two* diagonal springs.

Each spring of a specific type (horizontal, vertical or diagonal) covers a
rectangular “influence zone”. For the horizontal spring centered at $\vec
x\_{i+1/2, j}$, the influence zone is the area: $i\Delta x\leq
x\leq\bigl(i+1\bigr)\Delta x$ and $\bigl(j-1/2\bigr)\Delta y\leq
y\leq\bigl(j+1/2\bigr)\Delta y$

![“Influence zone” of horizontal springs]({static}What_is_homogenization/influence_zone-horizontal.png){.fig30p100}

For the vertical spring centered at $\vec x\_{i, j+1/2}$, the influence zone
is the area: $\bigl(i-1/2\bigr)\Delta x\leq x\leq\bigl(i+1/2\bigr)\Delta x$ and
$j\Delta y\leq y\leq\bigl(j+1\bigr)\Delta y$

![“Influence zone” of vertical springs]({static}What_is_homogenization/influence_zone-vertical.png){.fig30p100}

Finally, for the diagonal springs centered at $\vec x\_{i+1/2, j+1/2}$, the influence
zone is the area: $i\Delta x\leq x\leq\bigl(i+1\bigr)\Delta x$
and $j\Delta y\leq y\leq\bigl(j+1\bigr)\Delta y$

![“Influence zone” of vertical springs]({static}What_is_homogenization/influence_zone-diagonal.png){.fig30p100}

In all three cases, the “influence zone” has the same area, $\Delta x\,\Delta
y=\ell^2\cos\theta\sin\theta$. We write the elastic energy

$$W=\sum\_{i, j}\bigl(\frac{W\_{i+1/2, j}}{\ell^2\cos\theta\sin\theta}+\frac{W\_{i, j+1/2}}{\ell^2\cos\theta\sin\theta}+\frac{W\_{i+1/2, j+1/2}}{\ell^2\cos\theta\sin\theta}\bigr)\Delta x\,\Delta y,$$

with $\Delta x=\ell\cos\theta$ and $\Delta y=\ell\sin\theta$.

We will show that, when the size of the springs $\ell$ tends to zero, the
various terms of this sum have a limit

$$\frac{W\_{i+1/2, j}}{\ell^2\cos\theta\sin\theta}
\to w\_x[\tens\varepsilon(\vec x\_{i+1/2, j})],
\quad\frac{W\_{i, j+1/2}}{\ell^2\cos\theta\sin\theta}
\to w\_y[\tens\varepsilon(\vec x\_{i, j+1/2})]$$
and
$$\frac{W\_{i+1/2, j+1/2}}{\ell^2\cos\theta\sin\theta}\to w\_{xy}[\tens\varepsilon(\vec x\_{i+1/2, j+1/2})],$$

where it is noted that the various $w\_\star$ are functions of
$\tens\varepsilon=\sym\tgrad\vec u$. The elastic energy of the spring then reads

$$W=\sum\_{i, j}\bigl\\{w\_x[\tens\varepsilon(\vec x\_{i+1/2, j})]+w\_y[\tens\varepsilon(\vec x\_{i, j+1/2})]+w\_{xy}[\tens\varepsilon(\vec x\_{i+1/2, j+1/2})]\bigr\\}\Delta x\,\Delta y,$$

which can be interpreted as a [Riemann sum](https://en.wikipedia.org/wiki/Riemann_sum)

$$W=\int\bigl\\{w\_x[\tens\varepsilon(\vec x)]+w\_y[\tens\varepsilon(\vec x)]+w\_{xy}[\tens\varepsilon(\vec x)]\bigr\\}\D x\,\D y.$$

In other words, homogenization of the spring mesh leads to a continuous
mechanical system with elastic energy density $w=w\_x+w\_y+w\_{xy}$. Note that
$w$ is a function of the strain tensor $\tens\varepsilon$. Therefore, the
homogenized spring mesh behaves as a plate that deforms in its plane only. The
expression of the plate effective stiffness will be discussed in the next
section.

## Elastic energy of the mesh

It is shown in the <a href="#appendix">appendix</a> below that the elastic
energy densities of each type of springs have the following expressions

$$w\_x=\tfrac12k\,\chi\_x \operatorname{cotan}\theta\,\varepsilon\_{xx}^2,
\quad w\_y=\tfrac12k\,\chi\_y\tan\theta\,\varepsilon\_{yy}^2$$

and

$$\begin{aligned}w\_{xy}={}&\tfrac12k\operatorname{cotan}\theta\bigl(1+\cos2\theta\bigr)\varepsilon\_{xx}^2+\tfrac12k\tan\theta\bigl(1-\cos2\theta\bigr)\,\varepsilon\_{yy}^2\\\\&+k\sin2\theta\bigl(\varepsilon\_{xx}\,\varepsilon\_{yy}+2\,\varepsilon\_{xy}^2\bigr).\end{aligned}$$

Summing all three contributions, we find the strain energy density of an
orthotropic plate that is loaded in its plane only, namely

$$w=\tfrac12A\_x\,\varepsilon\_{xx}^2+\tfrac12A\_y\,\varepsilon\_{yy}^2+\tfrac12\bigl(\nu\_{xy}\,A\_y+\nu\_{yx}\,A\_x\bigr)\varepsilon\_{xx}\,\varepsilon\_{yy}+A\_{xy}\varepsilon\_{xy}^2,$$

with

$$A\_x=k\operatorname{cotan}\theta\bigl(1+\cos2\theta+\chi\_x\bigr),$$
$$A\_y=k\tan\theta\bigl(1-\cos2\theta+\chi\_y\bigr),$$
$$\nu\_{xy}\,A\_y=\nu\_{yx}\,A\_x=k\sin2\theta,$$
$$A\_{xy}=2k\sin2\theta.$$

The Poisson ratios can be expressed as follows
$$\nu\_{xy}=\frac{1+\cos2\theta}{1-\cos2\theta+\chi\_y}
\quad\text{and}\quad
\nu\_{yx}=\frac{1-\cos2\theta}{1+\cos2\theta+\chi\_x}.$$

It is interesting to find the conditions under which the above equivalent
membrane is isotropic. We must have

$$A=A\_x=A\_y,\quad\nu=\nu\_{xy}=\nu\_{yx}\quad\text{and}\quad A\_{xy}=\bigl(1-\nu\bigr)A,$$

where $\nu$ is the unique Poisson ratio and $A=Eh/(1-\nu^2)$ is the classical
membrane stiffness. Since $A\_{xy}=2\nu\_{xy}\,A\_y=2\nu\_{yx}\,A\_x$, the third
identity leads to $\nu=1/3$. From the expressions of the Poisson ratios, we
deduce that

$$\chi\_x=2-4\cos2\theta\quad\text{and}\quad\chi\_y=2+4\cos2\theta.$$

Plugging into the expressions of $A\_x$ and $A\_y$, we find

$$A=A\_x=A\_y=3k\sin2\theta.$$

For a square mesh, $\theta=\pi/4$, and isotropy requires that
$\chi\_x=\chi\_y=2$. In other words, if the horizontal and vertical springs are
twice as stiff as the diagonal springs, then the mesh behaves as an *isotropic*
plane membrane, with membrane stiffness $A=3k$ and Poisson ratio $\nu=1/3$.

## Conclusion

We have encountered our first homogenization example. A rectangular mesh of
springs can be homogenized as a continuous plate loaded in its plane only. We
saw the conditions on the geometry of the mesh and the stiffnesses of the
springs for the homogenized plate to behave isotropically.

In the [next instalment]({filename}20210509-What_is_homogenization-05.md) of
this series, we will discuss size effects in a deterministic setting.

<a id="appendix"></a>
## Appendix: derivation of the effective elastic energy

In this appendix, we derive the expression of the effective elastic energy of
the mesh of springs. We first express the elastic energy of one spring as a
function of the strain $\tens\varepsilon$ (assuming that the homogenized
displacement field $\vec u$ is smooth enough to allow for Taylor expansions).

Then, the general expression of the elastic energy is specialized to each type
of springs (horizontal, vertical and diagonal). In all three cases, it is shown
that the energy per unit area does not depend on the size $\ell$ of the spring,
which makes evaluation of the limit when $\ell\to0$ straightforward.

### Contribution of one spring

We consider one of the springs of the mesh, located between the end-points $A$
and $B$, with radius-vectors $\vec x\_A$ and $\vec x\_B$. We introduce the radius-vector $\vec x\_{AB}$ of the mid-point

$$\vec x\_{AB}=\tfrac12\bigl(\vec x\_A+\vec x\_B\bigr)$$

and we have

$$\vec x\_A=\vec x\_{AB}-\tfrac12\ell\_{AB}\,\vec n\_{AB}
\quad\text{and}\quad
\vec x\_B=\vec x\_{AB}+\tfrac12\ell\_{AB}\,\vec n\_{AB},$$

where $\ell\_{AB}$ and $\vec n\_{AB}$ are the length at rest of the spring and
unit-vector that orients the spring, respectively. It is recalled (see [this
post]({filename}20201125-On_the_stiffness_matrix_of_a_linear_spring.md), with
slightly different notation) that the elastic energy of the spring is given by
the formula

$$W\_{AB}=\tfrac12k\_{AB}\bigl[\vec n\_{AB}\cdot\bigl(\vec u\_B-\vec u\_A\bigr)\bigr]^2,$$

where $k\_{AB}$ denotes the stiffness of the spring and $\vec u\_A$ and $\vec
u\_B$ are the displacements of the two end-points. We assume here that these
displacements are given by a smooth map $\vec u(\vec x)$. Then

$$\vec u\_B-\vec u\_A
=\vec u(\vec x\_{AB}+\tfrac12\ell\_{AB}\,\vec n\_{AB})
-\vec u(\vec x\_{AB}-\tfrac12\ell\_{AB}\,\vec n\_{AB}).$$

Within the framework of homogenization, we assumed that $\vec u(\vec x)$ is
“smooth”, in the sense that the typical length-scale over which this field
varies is large, compared to the typical length-scale of the microstructure. In
other words, the variations of $\vec u$ between points $A$ and $B$ are small,
and we can expand the above expression to first order in $\ell\_{AB}$

$$\vec u\_B-\vec u\_A=\ell\_{AB}\tgrad\vec u(\vec x\_{AB})\cdot\vec n\_{AB}+\mathcal O(\ell\_{AB}^2).$$

To lowest order, the elastic energy of the spring therefore reads

$$W\_{AB}=\tfrac12k\_{AB}\ell\_{AB}^2\bigl[\vec n\_{AB}\cdot\tgrad\vec u(\vec x\_{AB})\cdot\vec n\_{AB}\bigr]^2.$$

The above tensor product involves only the symmetric part of the gradient of
$\vec u$, that we will call (surprise, surprise) $\tens\varepsilon$

$$\tens\varepsilon(\vec x)=\sym\tgrad\vec u(\vec x).$$

Then

$$W\_{AB}=\tfrac12k\_{AB}\ell\_{AB}^2\bigl[\vec n\_{AB}\cdot\tens\varepsilon(\vec x\_{AB})\cdot\vec n\_{AB}\bigr]^2.$$

This expression can be specialized for all four types of springs that are
present in the mesh considered here.

### Contribution of the horizontal and vertical springs

For a horizontal spring centered at $\vec x\_{i+1/2, j}$, we have
$\ell\_{AB}=\ell\cos\theta$ and $\vec n\_{AB}=\vec e\_x$. Therefore, the elastic
energy of one horizontal spring reads

$$W\_{i+1/2, j}=\tfrac12\chi\_xk\ell^2\cos^2\theta\bigl[\varepsilon\_{xx}(\vec x\_{i+1/2, j})\bigr]^2$$

and, dividing by the area $\ell\cos\theta\times\ell\sin\theta$ of a cell, we find the elastic energy density

$$w\_x=\tfrac12k\chi\_x\operatorname{cotan}\theta\,\varepsilon\_{xx}^2.$$

For the vertical springs, we would find similarly

$$w\_y=\tfrac12k\chi\_y\tan\theta\,\varepsilon\_{yy}^2.$$

### Contribution of the diagonal springs

For the diagonal springs centered at $\vec x\_{i+1/2, j+1/2}$, we have

$$\vec n\_{AB}=\zeta\,\cos\theta\,\vec e\_x+\sin\theta\,\vec e\_y\quad\text{and}\quad\ell\_{AB}=\ell,$$

where $\zeta=+1$ (south-west to north-east spring) or $\zeta=-1$ (south-east to
north-west spring). Therefore, the energy of the diagonal spring

$$\begin{aligned}W\_{i+1/2, j+1/2}={}&\tfrac12k\ell^2\bigl[\bigl(\zeta\,\cos\theta\,\vec e\_x+\sin\theta\,\vec e\_y\bigr)\cdot\tens\varepsilon\cdot\bigl(\zeta\,\cos\theta\,\vec e\_x+\sin\theta\,\vec e\_y\bigr)\bigr]^2\\\\
={}&\tfrac12k\ell^2\bigl(\cos^2\theta\,\varepsilon\_{xx}+\sin^2\theta\,\varepsilon\_{yy}+\zeta\sin2\theta\,\varepsilon\_{xy}\bigr)^2,\end{aligned}$$

where it is understood that $\tens\varepsilon$, $\varepsilon\_{xx}$,
$\varepsilon\_{yy}$ and $\varepsilon\_{xy}$ are evaluated at $\vec x\_{i+1/2,
j+1/2}$. Using the identity $(a+b)^2+(a-b)^2=2(a^2+b^2)$, we find the total
energy of the *two* diagonal springs centered at the same point $\vec x\_{i+1/2,
j+1/2}$

$$\begin{aligned}
W\_{xy}&=k\ell^2\bigl\[\bigl(\cos^2\theta\,\varepsilon\_{xx}+\sin^2\theta\,\varepsilon\_{yy}\bigr)^2+\sin^22\theta\,\varepsilon\_{xy}^2\bigr\]\\\\
&=k\ell^2\bigl\[\cos^4\theta\,\varepsilon\_{xx}^2+\sin^4\theta\,\varepsilon\_{yy}^2+\sin^22\theta\bigl(\tfrac12\varepsilon\_{xx}\,\varepsilon\_{yy}+\varepsilon\_{xy}^2\bigr)\bigr\],
\end{aligned}
$$

from which we deduce the contribution to the elastic energy density

$$\begin{aligned}
w\_{xy}={}&k\ell^2\biggl\[\frac{\cos^3\theta}{\sin\theta}\varepsilon\_{xx}^2+\frac{\sin^3\theta}{\cos\theta}\varepsilon\_{yy}^2+\sin2\theta\bigl(\varepsilon\_{xx}\,\varepsilon\_{yy}+2\,\varepsilon\_{xy}^2\bigr)\biggr]\\\\
={}&\tfrac12k\ell^2\bigl\[\operatorname{cotan}\theta\bigl(1+\cos2\theta\bigr)\varepsilon\_{xx}^2+\tan\theta\bigl(1-\cos2\theta\bigr)\varepsilon\_{yy}^2\\\\
&+2\sin2\theta\bigl(\varepsilon\_{xx}\,\varepsilon\_{yy}+2\,\varepsilon\_{xy}^2\bigr)\bigr].
\end{aligned}$$

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- coding: utf-8 -->
<!-- End: -->
