Title: On the double dot product
Date: 2014-02-19 Wed
Category: Tensor algebra
UseKaTeX: True

The double dot product of two tensors is the contraction of these tensors with
respect to the last two indices of the first one, and the first two indices of
the second one. Whether or not this contraction is performed on the *closest*
indices is a matter of convention. In this post, I will show that this choice
has some important implications.

Let $\tens a$ and $\tens b$ be two second-rank tensors. The following two
alternative definitions might be adopted for the double dot product $\tens
a\dbldot\tens b$

<a name="def01"></a>
**Definition 1:** $\tens a\dbldot\tens b=a\_{ij}b\_{ji}$ (contraction on the closest indices),

<a name="def02"></a>
**Definition 2:** $\tens a\dbldot\tens b=a\_{ij}b\_{ij}$.

In continuum mechanics, most second-rank tensors (strain, stress) are symmetric,
so that both definitions coincide. In the general case of asymmetric tensors
however, it is important to check which convention is adopted by the author. In
the present post, we examine both definitions in turn, and how they affect the
expression of the transpose of fourth-rank tensors, the definition of which is
first recalled.

## Transpose of a fourth-rank tensor

Let $\tens A$ be a fourth-rank tensor. Then the linear mapping $\tens
x\mapsto\tens A\dbldot\tens x$ ($\tens x$: second-rank tensor) is an
endomorphism over the space of second-rank tensors. As such, it is possible to
define its transpose $\tens A^{\mathsf T}$, provided that the space of second-rank
tensors is equipped with a scalar product $\langle\cdot,\cdot\rangle$. Then, by
definition

<a name="eq01"></a>
$$\langle\tens A^{\mathsf T}\dbldot\tens x,\tens y\rangle=\langle\tens x, \tens A\dbldot\tens y\rangle.\tag{1}$$

How is the scalar product of two second-rank tensors defined? The most obvious
choice is

<a name="eq02"></a>
$$\langle\tens x,\tens y\rangle=x\_{ij}y\_{ij},\tag{2}$$

so that the scalar product of two second-rank tensors is closely related to
either definition of their double dot product. In the next sections, it is shown
that each definition of the double dot product induces a different definition of
the transpose.

## Definition 1

In this section, the [first definition](#def01) of the double dot product is
examined

<a name="eq03"></a>
$$\tens x\dbldot\tens y=x\_{ij}y\_{ji},\tag{3}$$

where $\tens x$ and $\tens y$ are second-rank tensors. Then $\langle\tens
x,\tens y\rangle=\tens x^{\mathsf T}\dbldot\tens y$. Let $\tens A$ be a
fourth-rank tensor. Eqs. [(1)](#eq01) and [(2)](#eq02) are used in conjunction
with Eq. [(3)](#eq03) to find the components of $\tens A^{\mathsf T}$

$$\langle\tens x, \tens A\dbldot\tens y\rangle=\tens x^{\mathsf T}\dbldot\bigl(\tens A\dbldot\tens y\bigr)=\bigl(\tens x^{\mathsf T}\bigr)\_{ji}\bigl(\tens A\dbldot\tens y\bigr)\_{ij}=x\_{ij}A\_{ijkl}y\_{lk}.$$

Introducing the fourth-rank tensor $\tens A'$ defined component-wise by
$A\_{ijkl}'=A\_{lkji}$, the above identity reads

$$\langle\tens x, \tens A\dbldot\tens y\rangle=y\_{lk}A\_{lkji}'x\_{ij}=\bigl(\tens y^{\mathsf T}\bigr)\_{kl}\bigl(\tens A'\dbldot\tens x\bigr)\_{lk}=\tens y^{\mathsf T}\dbldot\bigl(\tens A'\dbldot\tens x\bigr)=\langle\tens A'\dbldot\tens x,\tens y\rangle,$$

which proves that $\tens A'$ is the transpose of $\tens A$. In other words, if
[definition 1](def:1) is adopted for the double dot product, then the components
of the transpose of any fourth-rank tensor $\tens A$ read

<a name="eq04"></a>
$$\bigl(\tens A^{\mathsf T}\bigr)\_{ijkl}=A\_{lkji}.\tag{4}$$

## Definition 2

We now examine the [second definition](#def02) of the double dot product

<a name="eq05"></a>
$$\tens x\dbldot\tens y=x\_{ij}y\_{ij},\tag{5}$$

where $\tens x$ and $\tens y$ are second-rank tensors. Then $\langle\tens
x,\tens y\rangle=\tens x\dbldot\tens y$. Let $\tens A$ be a fourth-rank
tensor. Eqs. [(1)](#eq01) and [(2)](#eq02) are again used in conjunction with
Eq. [(5)](#eq05) to find the components of $\tens A^{\mathsf T}$

$$\langle\tens x, \tens A\dbldot\tens y\rangle=\tens x\dbldot\bigl(\tens A\dbldot\tens y\bigr)=x\_{ij}\bigl(\tens A\dbldot\tens y\bigr)\_{ij}=x\_{ij}A\_{ijkl}y\_{kl}.$$

Introducing the fourth-rank tensor $\tens A''$ defined component-wise by
$A\_{ijkl}''=A\_{klij}$, the above identity reads

$$\langle\tens x, \tens A\dbldot\tens y\rangle=y\_{kl}A\_{klij}''x\_{ij}=y\_{kl}\bigl(\tens A''\dbldot\tens x\bigr)\_{kl}=\tens y\dbldot\bigl(\tens A''\dbldot\tens x\bigr)=\langle\tens A''\dbldot\tens x,\tens y\rangle,$$

which proves that $\tens A''$ is the transpose of $\tens A$. In other words, if
[definition 2](#def02) is adopted for the double dot product, then the
components of the transpose of a fourth-rank tensor $\tens A$ read

<a name="eq06"></a>
$$\bigl(\tens A^{\mathsf T}\bigr)\_{ijkl}=A\_{klij}.\tag{6}$$

## Which definition to adopt?

… is a pure matter of taste. For aesthetic reasons, I tend to prefer
Eq. [(6)](#eq06) over Eq. [(4)](#eq04). Besides, [definition 2](#def02) of the
double dot product directly defines a scalar product over the space of
second-rank tensors. Therefore, [definition 2](#def02) \[see Eq. [(5)](#eq05)\]
*will be adopted in this blog*. In other words, given two tensors $\tens T$ and
$\tens U$ of arbitrary rank (≥ 2), the product $\tens T\dbldot\tens U$ is
defined as follows

<a name="eq07"></a>
$$\tens T\dbldot\tens U=T\_{\ldots ij}U\_{ij\ldots}.\tag{7}$$

With this definition of the double dot product, the components of the transpose
of a fourth-rank tensor $\tens A$ are found from Eq. [(6)](#eq06). Furthermore,
Eq. [(7)](#eq07) can readily be specialized to the case of a tensor $\tens T$ of
arbitrary rank and a decomposed, second-rank tensor $\vec u\otimes\vec v$ ($\vec
u$, $\vec v$: vectors)

$$\tens T\dbldot\bigl(\vec u\otimes\vec v\bigr)=\bigl(\tens T\cdot\vec v\bigr)\cdot\vec u$$

and

$$\bigl(\vec u\otimes\vec v\bigr)\dbldot\tens T=\vec v\cdot\bigl(\vec u\cdot\tens T\bigr).$$

Finally, for a second-rank tensor $\tens a$ and a decomposed, second-rank tensor
$\vec u\otimes\vec v$ ($\vec u$, $\vec v$: vectors)

$$\tens a\dbldot\bigl(\vec u\otimes\vec v\bigr)=\bigl(\vec u\otimes\vec v\bigr)\dbldot\tens a=\vec u\cdot\tens a\cdot\vec v.$$

To conclude, two definitions of the double dot product are possible, and one
should always check which is adopted. It should be kept in mind that, while
arbitrary, this choice has many consequences, including on the definition of the
transpose of fourth-rank tensors.

<!-- Local Variables: -->
<!-- mode: markdown -->
<!-- fill-column: 80 -->
<!-- End: -->
