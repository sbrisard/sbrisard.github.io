Title: Elastic constants of an isotropic material, part 2: plane strain elasticity
Date: 2013-12-29
Category: Continuum mechanics
UseKaTeX: True

In the [previous
instalment]({filename}20131205-Elastic_constants_of_an_isotropic_material-01.md)
of this series, I introduced the constitutive law of an isotropically elastic
material, and the related material constants, within the framework of 3D
elasticity. I will now address the case of plane strain elasticity.

Problems of plane strain elasticity are defined as problems where the following
components of the strain tensor are null

<a name="eq1"></a>
$$\varepsilon_{31} = \varepsilon_{23} = \varepsilon_{33} = 0.\tag{1}$$

This is typically true of problems for which the geometry *and the loading* are
invariant along the third direction $\vec e_3$. In what follows, it will be
covenient to adopt the following classical notation

- latin indices (e.g. $i, j, k$) can take values in $\{1, 2, 3\}$,
- greek indices (e.g. $\alpha, \beta, \gamma$) can take values in $\{1,
  2\}$.

In both cases, Einstein's convention applies; in other words,
$\varepsilon_{kk}$ stands for

$$\sum_{k=1}^3\varepsilon_{kk},$$

while $\varepsilon_{\gamma\gamma}$ stands for

$$\sum_{\gamma=1}^2\varepsilon_{\gamma\gamma}.$$

As in the previous instalment, the constitutive laws in isotropic, plane strain
elasticity will be derived using various sets of material constants, starting
with the bulk modulus $E$ and the Poisso ratio $\nu$.

## Young's modulus and Poisson ratio

We first recall the consitutive law in isotropic, 3D elasticity

<a name="eq2"></a>
$$\varepsilon_{ij}=\frac{1+\nu}E\sigma_{ij}-\frac\nu E\sigma_{kk}\delta_{ij}.\tag{2}$$

Combination of Eqs. [(1)](#eq1) and [(2)](#eq2) for $(i, j)=(3, 1)$ and $(i,
j)=(2, 3)$, first leads to $\sigma_{31}=\sigma_{23}=0$. Then, for $(i, j) = (3,
3)$, $\sigma_{33}=\nu\sigma_{\gamma\gamma}$. The 3D trace of $\tens{\sigma}$ can
therefore be expressed as a function of its 2D trace

$$\sigma_{kk}=\left(1+\nu\right)\sigma_{\gamma\gamma}.$$

Substituting in Eq. [(2)](#eq2)

$$\varepsilon_{\alpha\beta}=\frac{1+\nu}E\left(\sigma_{\alpha\beta}-\nu\sigma_{\gamma\gamma}\delta_{\alpha\beta}\right),$$

which is the plane strain constitutive low we were looking for.

## Shear modulus and Poisson ratio

Recalling (see [previous
instalment]({filename}20131205-Elastic_constants_of_an_isotropic_material-01.md))
that $E=2\mu\left(1+\nu\right)$, Eq. [(2)](#eq2) can also be cast as follows

<a name="eq3"></a>
$$\varepsilon_{\alpha\beta}=\frac1{2\mu}\left(\sigma_{\alpha\beta}-\nu\sigma_{\gamma\gamma}\delta_{\alpha\beta}\right).\tag{3}$$

## Bulk and shear moduli

For (2D) isotropic stresses, $\sigma_{\alpha\beta}=-p\delta_{\alpha\beta}$,
Eq. [(3)](#eq3) reads

$$\varepsilon_{\alpha\beta}=-\frac{1-2\nu}{2\mu}p\delta_{\alpha\beta},$$

and the relative surface change $\varepsilon_\text s$, defined as
$\varepsilon_\text s=\varepsilon_{\gamma\gamma}$, reads

$$\varepsilon_\text s=-\frac p{\kappa_\text{2D}},$$

with

$$\kappa_\text{2D}=\frac\mu{1-2\nu}.$$

$\kappa_\text{2D}$ thus defined is the 2D (plane strain) bulk modulus of the
material. Attention should be paid to the fact that, unlike the shear modulus,
the bulk modulus of a material *depends on the dimension of the physical
space*. More generally, the (2D) trace of the strain tensor is related to the
average stress

<a name="eq4"></a>
$$\varepsilon_{\gamma\gamma}=\frac{1-2\nu}{2\mu}\sigma_{\gamma\gamma}.\tag{4}$$

Combining Eqs. [(3)](#eq3) and [(4)](#eq4)

$$\sigma_{\alpha\beta}=2\mu\varepsilon_{\alpha\beta}+\frac{2\mu\nu}{1-2\nu}\varepsilon_{\gamma\gamma}\delta_{\alpha\beta}=\frac{\mu}{1-2\nu}\varepsilon_{\gamma\gamma}\delta_{\alpha\beta}+2\mu\left(\varepsilon_{\alpha\beta}-\frac{\varepsilon_{\gamma\gamma}}2\delta_{\alpha\beta}\right),$$

and the stress-strain relationship finally reads

$$\sigma_{\alpha\beta}=\kappa_\text{2D}\varepsilon_{\gamma\gamma}\delta_{\alpha\beta}+2\mu\left(\varepsilon_{\alpha\beta}-\frac{\varepsilon_{\gamma\gamma}}2\delta_{\alpha\beta}\right).$$

## Conclusion

In this instalment, we have seen how the plane strain asumption affects the
constitutive law of isotropic, linear and elastic materials. In particular, the
bulk modulus which is the ratio of the average stress to the relative surface
change appears to be dimension dependent. In the [next
instalment]({filename}20140112-Elastic_constants_of_an_isotropic_material-03.md),
we will reconcile the 3D and 2D points of view.

<!-- Local Variables: -->
<!-- mode: markdown -->
<!-- fill-column: 80 -->
<!-- End: -->
