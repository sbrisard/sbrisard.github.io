Title: Elastic constants of an isotropic material, part 3: putting it all together
Date: 2014-01-12
Category: Continuum mechanics
UseKaTeX: True

In the previous instalments of this series (see [Part
1]({filename}20131205-Elastic_constants_of_an_isotropic_material-01.md) and
[Part 2]({filename}20131229-Elastic_constants_of_an_isotropic_material-02.md)),
I have shown that regardless of the dimensionality (3D or plane strain
elasticity), the constitutive law of an isotropically elastic material reads

<a name="eq01"></a>
$$\sigma_{ij}=\kappa\varepsilon_{kk}\delta_{ij}+2\mu\left(\varepsilon_{ij}-\frac{\varepsilon_{kk}}d\delta_{ij}\right),\tag{1}$$

where $d$ is the dimension of the physical space ($d=3$ for 3D elasticity, $d=2$
for plane strain elasticity), $\mu$ is the shear modulus, and $\kappa$ is the
bulk modulus, whose expression depends on $d$

<a name="eq02"></a>
$$\kappa=\frac23\frac{1+\nu}{1-2\nu}\mu\qquad(d=3),\tag{2}$$

<a name="eq03"></a>
$$\kappa=\frac\mu{1-2\nu}\qquad(d=2).\tag{3}$$

In this instalment, I am going to introduce some classical isotropic,
fourth-rank tensors which will prove extremely useful and will allow us to cast
Eq. [(1)](#eq01) in an intrinsic (component-free) form. It should be noted that
the following developments are restricted to fourth-rank tensors $\tens T$ with
both *minor symmetries*

$$T_{ijkl}=T_{jikl}=T_{ijlk},$$

and *major symmetry*

$$T_{ijkl}=T_{klij}.$$

## Spherical and deviatoric projection tensors

In the present section, I am going to introduce the fourth-rank identity,
spherical and deviatoric projection tensors.

### Fourth-rank identity tensor

The fourth-rank identity tensor $\tens{I}$ maps any second-rank, symmetric
tensor $\tens u$ onto itself

$$\tens I\dbldot\tens u=\tens u.$$

It is straightforward to work out the components of $\tens I$ (accounting for
minor symmetries)

$$I_{ijkl}=\frac12\left(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}\right).$$

### Fourth-rank spherical projection tensor

The fourth-rank spherical projection tensor $\tens J$ extracts the spherical
part of any symmetric, second-rank tensor $\tens u$

$$\tens J\dbldot\tens u=\frac1d\tr(\tens u)\tens\delta,$$

where $\tens\delta$ is the second-rank identity tensor (with components
$\delta_{ij}$). In particular, $\tens J\dbldot\tens\delta=\tens\delta$. In
intrinsic form, $\tens J$ reads

$$\tens J=\frac1d\tens\delta\otimes\tens\delta,$$

where $\otimes$ denotes the [tensor
product](http://en.wikipedia.org/wiki/Tensor_product). The components of
$\tens J$ are

$$J_{ijkl} = \frac1d\delta_{ij}\delta_{kl}.$$

### Fourth-rank deviatoric projection tensor

The fourth-rank deviatoric projection tensor $\tens K$ extracts the deviatoric
part of any symmetric, second-rank tensor $\tens u$

$$\tens K\dbldot\tens u=\tens u-\frac1d\tr(\tens u)\tens{\delta}=\tens u-\tens J\dbldot\tens u,$$

from which it results that

$$\tens K=\tens I-\tens J.$$

## Stiffness tensor

Going back the constitutive law of the linearly elastic, isotropic material
given by Eq. [(1)](#eq01), it is found that

$$\tens\sigma=d\kappa\tens J\dbldot\tens\varepsilon+2\mu\tens K\dbldot\tens\varepsilon=\tens C\dbldot\tens\varepsilon,$$

where $\tens C$ is the fourth-rank stiffness tensor of the material

$$\tens C=d\kappa\tens J+2\mu\tens K.$$

In isotropic elasticity, the stiffness tensor is a linear combination of the two
tensors $\tens J$ and $\tens K$. This is in fact a general result, which is
heavily used in materials science: any *isotropic* fourth-rank tensor with minor
and major symmetries is a linear combination of $\tens J$ and $\tens K$. In
other words, $\tens J$ and $\tens K$ form a *basis* of the space of fourth-rank
isotropic tensors with minor and major symmetries. Why this is useful will
become obvious in the next section, where I will show that algebra in this basis
is dead simple.

## Algebra of the $\tens{J}$ and $\tens{K}$ tensors

It can readily be verified that

$$\tens J\dbldot\tens J=\tens J,\quad\tens K\dbldot\tens K=\tens K\quad\text{and}\quad\tens K\dbldot\tens J=\tens J\dbldot\tens K=\tens0.$$

Therefore, multiplication of two isotropic tensors
$\tens T_i=a_i\tens{J}+b_i\tens{K}$ ($i=1,2$) is trivial

$$\tens T_1\dbldot\tens T_2=a_1a_2\tens J+b_1b_2\tens K.$$

Also, inversion of an isotropic tensor $\tens T=a\tens{J}+b\tens{K}$ is
straightforward

$$\tens T^{-1}=\frac1a\tens J+\frac1b\tens K.$$

All these expressions will prove extremely useful in due time.

## Conclusion

This is the end of this series on the elastic constants of isotropic
materials. I have shown that (regardless of the dimension $d$ of the physical
space), such materials are characterized by two constants. The shear modulus
$\mu$, the Poisson ratio $\nu$ and Young's modulus $E$ do not depend on $d$,
while the plane strains expression of the bulk modulus $\kappa$ differs from its
3D expression (see Eqs. [(2)](#eq02) and [(3)](#eq03)).

This series was also a good opportunity to introduce the tensors $\tens J$ and
$\tens K$, which form a basis for the isotropic, fourth-rank tensors. Using this
basis is very convenient, as algebra within this basis is extremely simple.

<!-- Local Variables: -->
<!-- mode: markdown -->
<!-- fill-column: 80 -->
<!-- End: -->
