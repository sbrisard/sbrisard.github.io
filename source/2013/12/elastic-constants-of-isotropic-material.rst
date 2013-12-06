*****************************************************************
Elastic constants of an isotropic material, part 1: 3D elasticity
*****************************************************************

Among all classes of materials, the class of linearly elastic and isotropic materials is probably the simplest. Such materials are defined by two elastic constants: for example, Young's modulus E and Poisson's ratio ν. However, depending on the situation, this pair of constants might not be the most appropriate (meaning that they may not lead to the most compact expressions). Alternative sets of elastic constants are

- Lamé's constants λ and μ,
- bulk and shear moduli κ and μ,
- shear modulus and Poisson ratio μ and ν.

Each pair of constants is of course strictly equivalent to any other. I tend to work primarily with μ and ν, and always find myself looking for the expression of E, λ and κ as a function of μ and ν. In this series, we will derive these expressions, starting with 3D elasticity.

Lamé's constants
================

The constitutive equation of a linearly elastic and isotropic material reads

.. math:: \sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}
   :label: 1

where :math:`\sigma_{ij}` (resp. :math:`\varepsilon_{ij}`) denotes the stress (resp. strain) tensor, while λ (resp. μ) is Lamé's first (resp. second) constant; μ is also called the *shear modulus*. Eq. :eq:`1` is inverted so as to express the strain tensor as a function of the stress tensor. Taking :math:`i = j` and summing over repeated indices, we find

.. math:: \sigma_{ii} = (3\lambda + 2\mu)\varepsilon_{kk},

where it is recalled that :math:`\delta_{ii} = 3` (the dimension of the physical space). Plugging into Eq. :eq:`1`

.. math:: \sigma_{ij} = \frac{\lambda}{3\lambda+2\mu}\sigma_{kk}\delta_{ij} + 2\mu\varepsilon_{ij}

and finally

.. math:: \varepsilon_{ij} = \frac{\sigma_{ij}}{2\mu} - \frac{\lambda}{2\mu(3\lambda+2\mu)}\sigma_{kk}\delta_{ij}.
   :label: 2

Young's modulus and Poisson ratio
=================================

We consider a uniaxial traction experiment, where the stress tensor reduces to :math:`\sigma\vec e_3\otimes\vec e_3` (:math:`\sigma` is the imposed uniaxial stress). Substitution in Eq. :eq:`2` leads to the following expression of the longitudinal strain

.. math:: \varepsilon_{33} = \frac{\lambda+\mu}{\mu(3\lambda+2\mu)}\sigma.

By definition, Young's modulus is the longitudinal stress to longitudinal strain ratio: :math:`E=\sigma/\varepsilon_{33}`, so that

.. math:: E = \frac{\mu(3\lambda+2\mu)}{\lambda+\mu}.
   :label: 3

The expression of the transverse strains is again derived using Eq. :eq:`2`

.. math:: \varepsilon_{11} = \varepsilon_{22} = -\frac{\lambda}{2\mu(3\lambda+2\mu)}

and by definition, Poisson's ratio is the oposite of the transverse to longitudinal strain ratio

.. math:: \nu = -\frac{\varepsilon_{11}}{\varepsilon_{33}} = -\frac{\varepsilon_{22}}{\varepsilon_{33}} = \frac{\lambda}{2(\lambda+\mu)}.
   :label: 4

Expressions :eq:`3` and :eq:`4` can be substituted in the constitutive equation :eq:`2`, leading to

.. math:: \varepsilon_{ij} = \frac{1+\nu}E\sigma_{ij} - \frac\nu E\sigma_{kk}\delta_{ij}.
   :label: 5

Bulk and shear moduli
=====================

We now consider an isotropic compression experiment, where the stress tensor reduces to a hydrostatic pressure :math:`\sigma_{ij}=-p\delta_{ij}`. Using Eq. :eq:`1`, we find that the strain tensor is also isotropic

.. math:: \varepsilon_{ij} = -\frac{p\delta_{ij}}{3\lambda+2\mu}.
   :label: 6

It is recalled that :math:`\varepsilon_\text v=\varepsilon_{kk} / 3` denotes the relative volume change of the material. Then, from Eq. :eq:`6`

.. math:: \varepsilon_\text v = -\frac p\kappa_\text{3D},

where :math:`\kappa_\text{3D}` denotes the bulk modulus, defined as follows

.. math:: \kappa_\text{3D} = \lambda + \frac 23\mu.
   :label: 7

As we shall see in the **next instalment** of this series, the definition of the bulk modulus depends on the dimension of the physical space, hence the '3D' subscript. Using κ and μ as elastic constants, Eq. :eq:`1` reads

.. math:: \sigma_{ij} = \kappa_\text{3D}\varepsilon_{kk}\delta_{ij}+2\mu\left(\varepsilon_{ij}-\frac{\varepsilon_{kk}}3\delta_{ij}\right)
   :label: 8

Shear modulus and Poisson ratio
===============================

I quite often use the shear modulus μ and Poisson ratio ν as the constants defining the elastic material. One of the reasons for this is the fact that the components of the fourth-rank Green operator for strains have the same expression in 3D and 2D (plane strain) elasticity when expressed as a function of μ and ν.

In the present section, all other elastic constants are expressed as functions of these two constants. First, from Eq. :eq:`4`, it is readily found that

.. math:: \lambda =  \frac{2\mu\nu}{1-2\nu}.
   :label: 9

Then, combining Eqs. :eq:`3` and :eq:`4`

.. math:: E = 2\mu(1+\nu).
   :label: 10

Finally, from Eqs. :eq:`7` and :eq:`9`

.. math:: \kappa_\text{3D} = \frac23\frac{1+\nu}{1-2\nu}\mu.
   :label: 11

Conclusion
==========
In this instalment, we have defined Lamé's first and second constants, Young's modulus, Poisson's ratio, as well as the (3D) bulk modulus. Expressions relating these various constants have also been derived. In the next instalment of this series, we will discuss the case of 2D (plane strain elasticity).
