Title: On the stiffness matrix of a linear spring
Date: 2020-11-25
UseKaTeX: True

This post is not going to be the most exciting I have ever written. We will
derive the expression of the elastic energy of a linear spring as a function of
the displacement of its two end-points. I will need this expression in my series
on [“What is homogenization”]({filename}). Having derived the elastic energy, we
will be only one step away from the stiffness matrix of the spring, to be used
in a finite element setting.

## Expression of the elastic energy

![A linear spring]({static}On_the_stiffness_matrix_of_a_linear_spring/spring.png){.fig50p100}

We consider a spring located between points $A$ and $B$. Its initial length (at
rest) is $L$, and we introduce the unit vector $\vec n$ that points from $A$ to
$B$

$$\vec X\_B=\vec X\_A+L\,\vec n,$$

where $\vec X\_A$ and $\vec X\_B$ denote the radius vectors of points $A$ and $B$
in the initial (undeformed) configuration.

At equilibrium, the length of the spring is $\ell$ and its elastic energy is
$$U=\tfrac12k\bigl(\ell-L\bigr)^2,$$
where $k$ denotes the stiffness of the spring. We want to express this elastic
energy as a function of the displacements $\vec u\_A$ and $\vec u\_B$ of the
points $A$ and $B$

$$\vec x\_A=\vec X\_A+\vec u\_A\quad\text{and}\quad\vec x\_B=\vec X\_B+\vec u\_B,$$

where $\vec x\_A$ and $\vec x\_B$ now denote the radius vectors of points $A$
and $B$ in the current (deformed) configuration. We will work under the
assumption that these displacements are small and we will keep only the lowest
order term of the energy.

We have

$$\ell=\lVert\vec x\_B-\vec x\_A\rVert=\lVert\vec X\_B-\vec X\_A+\vec u\_B-\vec u\_A\rVert=L\lVert\vec n+\vec\xi\rVert,$$

where we have introduced the following dimensionless vector

$$\vec\xi=L^{-1}\bigl(\vec u\_B-\vec u\_A\bigr).$$

Then

$$\ell^2=L^2\bigl(\vec n+\vec\xi\bigr)^2=L^2\bigl(1+2\,\vec n\cdot\vec\xi+\vec\xi\cdot\vec\xi\bigr)$$

and, to first order in $\vec\xi$

$$\ell=L\bigl[1+\vec n\cdot\vec\xi+\mathcal O(\vec\xi^2)\bigr].$$

Plugging the expression of $\vec\xi$ as a function of the displacements $\vec
u\_A$ and $\vec u\_B$, we find the elongation of the spring

$$\ell-L=\vec n\cdot\bigl(\vec u\_B-\vec u\_A\bigr)+\text{h.o.t.}$$

Finally, the elastic energy of the spring is, to lowest order

$$U=\tfrac12k\bigl[\vec n\cdot\bigl(\vec u\_B-\vec u\_A\bigr)\bigr]^2,$$

which is the expression we were looking for.

## Expression of the stiffness matrix

The above expression can also be written

$$U=\tfrac12k\bigl(\vec u\_B-\vec u\_A\bigr)\cdot\bigl(\vec n\otimes\vec n\bigr)\cdot\bigl(\vec u\_B-\vec u\_A\bigr)$$

and, upon expansion

$$U=\tfrac12k\bigl[\vec u\_A\cdot\bigl(\vec n\otimes\vec n\bigr)\cdot\vec u\_A+\vec u\_B\cdot\bigl(\vec n\otimes\vec n\bigr)\cdot\vec u\_B-2\vec u\_A\cdot\bigl(\vec n\otimes\vec n\bigr)\cdot\vec u\_B\bigr].$$

This delivers the expression of the stiffness matrix of the spring. Indeed, let
$q$ be the vector of dofs of the spring. This is a column vector of size $2d$
($d$: number of spatial dimensions): $q=[\vec u\_A, \vec u\_B]^\mathsf{T}$,
where we store first the $d$ components of the displacement of point $A$, then
the $d$ components of the displacement of point $B$. The elastic energy of the
spring can now be written

$$U=\tfrac12q^\mathsf{T}\cdot K\cdot q,$$

where the stiffness matrix $K$ reads, in block form

$$K=k\begin{bmatrix}\vec n\otimes\vec n & -\vec n\otimes\vec n\\\\-\vec n\otimes\vec n & \vec n\otimes\vec n\end{bmatrix}.$$

For $d=2$, we introduce the components $u\_\star$ and $v\_\star$ of the
displacement $\vec u\_\star$

$$\vec u\_\star=u\_\star\,\vec e\_x+v\_\star\,\vec e\_y,\quad q^\mathsf{T}=\bigl[u\_A, v\_A, u\_B, v\_B\bigr]$$

and

$$K=k\begin{bmatrix}
n\_xn\_x & n\_xn\_y & -n\_xn\_x & -n\_xn\_y\\\\
n\_xn\_y & n\_yn\_y & -n\_xn\_y & -n\_yn\_y\\\\
-n\_xn\_x & -n\_xn\_y & n\_xn\_x & n\_xn\_y\\\\
-n\_xn\_y & -n\_yn\_y & n\_xn\_y & n\_yn\_y
\end{bmatrix}.$$

For $d=3$, we introduce the components $u\_\star$, $v\_\star$ and $w\_\star$ of
the displacement $\vec u\_\star$

$$\vec u\_\star=u\_\star\,\vec e\_x+v\_\star\,\vec e\_y+w\_\star\,\vec e\_z,\quad q^\mathsf{T}=\bigl[u\_A, v\_A, w\_A, u\_B, v\_B, w\_B\bigr]$$

and


$$K=k\begin{bmatrix}
 n\_xn\_x &  n\_xn\_y &  n\_xn\_z & -n\_xn\_x & -n\_xn\_y & -n\_xn\_z\\\\
 n\_yn\_x &  n\_yn\_y &  n\_yn\_z & -n\_yn\_x & -n\_yn\_y & -n\_yn\_z\\\\
 n\_zn\_x &  n\_zn\_y &  n\_zn\_z & -n\_zn\_x & -n\_zn\_y & -n\_zn\_z\\\\
-n\_xn\_x & -n\_xn\_y & -n\_xn\_z &  n\_xn\_x &  n\_xn\_y &  n\_xn\_z\\\\
-n\_yn\_x & -n\_yn\_y & -n\_yn\_z &  n\_yn\_x &  n\_yn\_y &  n\_yn\_z\\\\
-n\_zn\_x & -n\_zn\_y & -n\_zn\_z &  n\_zn\_x &  n\_zn\_y &  n\_zn\_z
\end{bmatrix}.$$


<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- coding: utf-8 -->
<!-- End: -->
