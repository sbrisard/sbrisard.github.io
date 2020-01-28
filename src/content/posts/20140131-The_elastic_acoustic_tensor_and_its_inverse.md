Title: The elastic acoustic tensor and its inverse
Date: 2014-01-31
Category: Continuum Mechanics
UseKaTeX: True

In this post, I will introduce the acoustic tensor of linearly elastic
materials. Closed-form expressions of the inverse of this tensor can be derived
in the case of *isotropic* materials. This will later come in handy to derive
closed-form expressions of the periodic Green operator for strains.

We consider a linearly elastic material with stiffness $\tens C$. For any
wave-vector $\vec k$, the elastic acoustic tensor $\tens A(\vec k)$ is defined
as follows

<a name="eq01"></a>
$$\tens A(\vec k)=\vec k\cdot\tens C\cdot\vec k=k^2\vec n\cdot\tens C\cdot\vec n,\tag{1}$$

where $k$ is the amplitude of the wave-vector $\vec k$, $k=\sqrt{\vec k\cdot\vec
k}$, and $\vec n$ is its direction ($\vec k=k\vec n$). The acoustic tensor is
used to assess material stability (Bigoni and Zaccaria, *European Journal of
Mechanics- A/Solids* **13(5)**, pp. 621–638, 1994) and study the propagation of
waves ([Gentile and Straughan,
2013](https://doi.org/10.1016/j.ijengsci.2013.07.006)). As far as we are
concerned, the derivation of the periodic Green operator for strains will
require the expressions of the inverse of the acoustic tensor. This is the topic
of the present post, which is restricted to isotropic materials: the stiffness
tensor $\tens C$ of isotropic materials is therefore a linear combination of the
[isotropic projection
tensors]({filename}20140112-Elastic_constants_of_an_isotropic_material-03.md)
$\tens J$, and $\tens K$

<a name="eq02"></a>
$$\tens C=d\kappa\tens J+2\mu\tens K.\tag{2}$$

To compute the elastic acoustic tensor, we therefore need to find the
expressions of $\vec n\cdot\tens J\cdot\vec n$ and $\vec n\cdot\tens K\cdot\vec
n$, for any unit vector $\vec n$. We start with the computation of $\vec
n\cdot\tens I\cdot\vec n$, where $\tens I$ denotes the fourth-rank identity
tensor. We have

$$\bigl(\vec n\cdot\tens I\cdot\vec n\bigr)\_{jk}=n\_iI\_{ijkl}n\_l=n\_in\_l\frac12\bigl(\delta\_{il}\delta\_{jk}+\delta\_{jl}\delta\_{ik}\bigr)=\frac12\bigl(n\_in\_i\delta\_{jk}+n\_jn\_k\bigr).$$

Since $\vec n$ is a unit vector, we have $n_in_i=1$, and

$$\vec n\cdot\tens I\cdot\vec n=\frac12\bigl(\tens\delta+\vec n\otimes\vec n\bigr),$$

where $\tens\delta$ denotes the second-rank identity tensor. It will be
convenient to introduce the projectors $\tens p$ and $\tens q$, defined as
follows

$$\tens p=\vec n\otimes\vec n\quad\text{and}\quad\tens q=\tens\delta-\tens p,$$

or, using indices

$$p_{ij}=n_in_j\quad\text{and}\quad q_{ij}=\delta_{ij}-n_in_j.$$

It can readily be verified that

<a name="eq03"></a>
$$\tens p\cdot\tens p=\tens p,\quad\tens q\cdot\tens q=\tens q\quad\text{and}\quad\tens p\cdot\tens q=\tens q\cdot\tens p=\tens0,\tag{3}$$

and

<a name="eq04"></a>
$$\vec n\cdot\tens I\cdot\vec n=\tens p+\frac12\tens q.\tag{4}$$

Similarly

<a name="eq05"></a>
$$\vec n\cdot\tens J\cdot\vec n=\frac1d\vec n\cdot\bigl(\tens\delta\otimes\tens\delta\bigr)\cdot\vec n=\frac1d\vec n\otimes\vec n=\frac1d\tens p.\tag{5}$$

Finally, combining identity $\tens K=\tens I-\tens J$ with Eqs. [(4)](#eq04) and
[(5)](#eq05)

<a name="eq06"></a>
$$\vec n\cdot\tens K\cdot\vec n=\frac{d-1}d\tens p+\frac12\tens q.\tag{6}$$

The acoustic tensor of an elastic, linear, isotropic material is obtained from
Eqs. [(1)](#eq01), [(2)](#eq02), [(5)](#eq05) and [(6)](#eq06)

$$\tens A(\vec n)=\Bigl(\kappa+2\mu\frac{d-1}d\Bigr)\tens p+\mu\tens q.$$

From [this
post]({filename}20140112-Elastic_constants_of_an_isotropic_material-03.md), it can
readily be verified that

$$\kappa+2\mu\frac{d-1}d=2\mu\frac{1-\nu}{1-2\nu},$$

this identity being true in both 3D and plane strain elasticity. The acoustic
tensor therefore reads

$$\tens A(\vec k)=k^2\mu\Bigl[\frac{2\bigl(1-\nu\bigr)}{1-2\nu}\tens p+\tens q\Bigr].$$

Finally, using the properties of the projectors $\tens p$ and $\tens q$ \[see
Eq. [(3)](#eq03)\], the *inverse* of the acoustic tensor can be derived

$$\tens A^{-1}(\vec k)=\frac1{k^2\mu}\Bigl[\frac{1-2\nu}{2\bigl(1-\nu\bigr)}\tens p+\tens q\Bigr].$$

<!-- Local Variables: -->
<!-- mode: markdown -->
<!-- fill-column: 80 -->
<!-- End: -->
