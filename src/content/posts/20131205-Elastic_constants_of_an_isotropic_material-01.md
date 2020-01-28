Title: Elastic constants of an isotropic material, part 1: 3D elasticity
Date: 2013-12-05
Category: Continuum Mechanics
UseKaTeX: True

Among all classes of materials, the class of linearly elastic and isotropic
materials is probably the simplest. Such materials are defined by two elastic
constants: for example, Young\'s modulus $E$ and Poisson\'s ratio
$\nu$. However, depending on the situation, this pair of constants might not be
the most appropriate (meaning that they may not lead to the most compact
expressions). Alternative sets of elastic constants are

- Lamé's constants $\lambda$ and $\mu$,
- bulk and shear moduli $\kappa$ and $\mu$,
- shear modulus and Poisson ratio $\mu$ and $\nu$.

Each pair of constants is of course strictly equivalent to any other. I tend to
work primarily with $\mu$ and $\nu$, and always find myself looking for the
expression of E, $\lambda$ and $\kappa$ as a function of $\mu$ and $\nu$. In
this series, we will derive these expressions, starting with 3D elasticity.

## Lamé's constants

The constitutive equation of a linearly elastic and isotropic material reads

<a name="eq01"></a>
$$\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij},\tag{1}$$

where $\sigma_{ij}$ (resp. $\varepsilon_{ij}$) denotes the stress (resp.
strain) tensor, while $\lambda$ (resp. $\mu$) is Lamé\'s first (resp.  second)
constant; $\mu$ is also called the *shear modulus*. Eq.  [(1)](#eq01) is
inverted so as to express the strain tensor as a function of the stress
tensor. Taking $i = j$ and summing over repeated indices, we find

$$\sigma_{ii} = (3\lambda + 2\mu)\varepsilon_{kk},$$

where it is recalled that $\delta_{ii} = 3$ (the dimension of the physical
space). Plugging into Eq. [(1)](#eq01)

$$\sigma_{ij} = \frac{\lambda}{3\lambda+2\mu}\sigma_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}$$

and finally

<a name="eq02"></a>
$$\varepsilon_{ij} = \frac{\sigma_{ij}}{2\mu} - \frac{\lambda}{2\mu(3\lambda+2\mu)}\sigma_{kk}\delta_{ij}.\tag{2}$$

## Young's modulus and Poisson ratio

We consider a uniaxial traction experiment, where the stress tensor reduces to
$\sigma\vec e_3\otimes\vec e_3$ ($\sigma$ is the imposed uniaxial
stress). Substitution in Eq. [(2)](#eq02) leads to the following expression of
the longitudinal strain

$$\varepsilon_{33} = \frac{\lambda+\mu}{\mu(3\lambda+2\mu)}\sigma.$$

By definition, Young's modulus is the longitudinal stress to longitudinal strain
ratio: $E=\sigma/\varepsilon_{33}$, so that

<a name="eq03"></a>
$$E = \frac{\mu(3\lambda+2\mu)}{\lambda+\mu}.\tag{3}$$

The expression of the transverse strains is again derived using Eq. [(2)](#eq02)

$$\varepsilon_{11} = \varepsilon_{22} = -\frac{\lambda}{2\mu(3\lambda+2\mu)}$$

and by definition, Poisson's ratio is the oposite of the transverse to
longitudinal strain ratio

<a name="eq04"></a>
$$\nu = -\frac{\varepsilon_{11}}{\varepsilon_{33}} = -\frac{\varepsilon_{22}}{\varepsilon_{33}} = \frac{\lambda}{2(\lambda+\mu)}.\tag{4}$$

Expressions [(3)](#eq03) and [(4)](#eq04) can be substituted in the constitutive
equation [(2)](#eq02), leading to

<a name="eq05"></a>
$$\varepsilon_{ij} = \frac{1+\nu}E\sigma_{ij} - \frac\nu E\sigma_{kk}\delta_{ij}.\tag{5}$$

## Bulk and shear moduli

We now consider an isotropic compression experiment, where the stress tensor
reduces to a hydrostatic pressure $\sigma_{ij}=-p\delta_{ij}$. Using
Eq. [(1)](#eq01), we find that the strain tensor is also isotropic

<a name="eq06"></a>
$$\varepsilon_{ij} = -\frac{p\delta_{ij}}{3\lambda+2\mu}.\tag{6}$$

It is recalled that $\varepsilon_\text v=\varepsilon_{kk} / 3$ denotes the
relative volume change of the material. Then, from Eq. [(6)](#eq06)

$$\varepsilon_\text v = -\frac p{\kappa_\text{3D}},$$

where $\kappa_\text{3D}$ denotes the bulk modulus, defined as follows

<a name="eq07"></a>
$$\kappa_\text{3D} = \lambda + \frac 23\mu.\tag{7}$$

As we shall see in the [next
instalment]({filename}20131229-Elastic_constants_of_an_isotropic_material-02.md)
of this series, the definition of the bulk modulus *depends on the dimension of
the physical space*, hence the \'3D\' subscript. Using $\kappa$ and $\mu$ as
elastic constants, Eq. [(1)](#eq01) reads

<a name="eq08"></a>
$$\sigma_{ij} = \kappa_\text{3D}\varepsilon_{kk}\delta_{ij}+2\mu\left(\varepsilon_{ij}-\frac{\varepsilon_{kk}}3\delta_{ij}\right)\tag{8}$$

## Shear modulus and Poisson ratio

I quite often use the shear modulus $\mu$ and Poisson ratio $\nu$ as the
constants defining the elastic material. One of the reasons for this is the fact
that the components of the fourth-rank Green operator for strains have the same
expression in 3D and 2D (plane strain) elasticity when expressed as a function
of $\mu$ and $\nu$.

In the present section, all other elastic constants are expressed as functions
of these two constants. First, from Eq. [(4)](#eq04), it is readily found that

<a name="eq09"></a>
$$\lambda = \frac{2\mu\nu}{1-2\nu}.\tag{9}$$

Then, combining Eqs. [(3)](#eq03) and [(4)](#eq04)

$$E = 2\mu(1+\nu).$$

Finally, from Eqs. [(7)](#eq07) and [(9)](#eq09)

$$\kappa_\text{3D} = \frac23\frac{1+\nu}{1-2\nu}\mu.$$

## Conclusion

In this instalment, we have defined Lamé's first and second constants, Young's
modulus, Poisson's ratio, as well as the (3D) bulk modulus.  Expressions
relating these various constants have also been derived. In the [next
instalment]({filename}20131229-Elastic_constants_of_an_isotropic_material-02.md)
of this series, we will discuss the case of 2D (plane strain elasticity).

<!-- Local Variables: -->
<!-- mode: markdown -->
<!-- fill-column: 80 -->
<!-- End: -->
