Title: When a thin shell is not so thin, part 2: the 3D, exact solution
Date: 2015-07-01
Category: Shell theory
UseKaTex: True

In the [previous
instalment]({filename}20150608-When_a_thin_shell_is_not_so_thin-01.md) of this
series, we analysed a spherical pressure vessel by means of Koiter's linear
theory of thin shells. We found the somewhat unexpected result that the stress
couple was not null. Besides, we also found that the stress resultant was
slightly different from the well-known value $N=pR/2$. So what was wrong with
the previous analysis? To explore this question, we will make use of the exact
solution in 3D elasticity.

## The spherical pressure vessel, exact solution

Finding the stresses and displacements in a pressure vessel is a classical
exercise in 3D linear elasticity. In this post, I will spare you the details of
the derivation (which can be found in e.g. Timoshenko and Goodier, *Theory of
Elasticity*, 2nd edition, McGraw-Hill, 1951 art. 121). Instead, I will come
straight to the point, and provide you with the exact expression of the stress
tensor in spherical coordinates ($r$: distance to the center of the spherical
pressure vessel)

<a name="eq01"></a>
$$\sigma\_{rr}(r)=A-\frac{2B}{r^3},\tag{1}$$

<a name="eq02"></a>
$$\sigma\_{\theta\theta}(r)=\sigma\_{\phi\phi}(r)=A+\frac{B}{r^3},\tag{2}$$

all other components being null. The integration constants $A$ and $B$ are
defined below

$$A=-\frac{p\_\text{ext}R\_\text{ext}^3-p\_\text{int}R\_\text{int}^3}{R\_\text{ext}^3-R\_\text{int}^3},$$
$$B=-\frac12\frac{\bigl(p\_\text{ext}-p\_\text{int}\bigr)R\_\text{int}^3R\_\text{ext}^3}{R\_\text{ext}^3-R\_\text{int}^3},$$

where $R\_\text{int}=R-h/2$ and $R\_\text{ext}=R+h/2$ denote the internal and
external radii of the spherical pressure vessel ($R$: radius of midsurface, $h$:
thickness); $p\_\text{int}$ and $p\_\text{ext}$ denote the internal and external
pressures. To make a fair comparison between the shell theory and the 3D exact
solution, it is customary to share the load equally between the upper and lower
faces (see e.g. [Reissner, 1947](https://doi.org/10.1090/qam/20440)). In other
words,

$$p\_\text{int}=-p\_\text{ext}=\frac p2.$$

In the remainder of this post, $\sigma$ will denote the common value of the
in-plane stresses

<a name="eq06">
$$\sigma=\sigma\_{\theta\theta}=\sigma\_{\phi\phi}.\tag{3}$$
</a>

From Eq. [(2)](#eq02), we readily find the following expressions of the stress
resultant $N=N\_{\theta\theta}=N\_{\phi\phi}$ and stress couple
$M=M\_{\theta\theta}=M\_{\phi\phi}$

<a name="eq07"></a>
$$N=\int\_{R\_\text{int}}^{R\_\text{ext}}\sigma(r)\,\mathrm{d}r=\frac{pR}2\frac{1+\frac{5h^2}{12R^2}}{1+\frac{h^2}{12R^2}}=\frac{pR}2\Bigl(1+\frac{h^2}{3R^2}\Bigr)+\mathcal O\Bigl(\frac{h^4}{R^4}\Bigr),\tag{4}$$
<a name="eq08"></a>
$$M=-\int\_{R\_\text{int}}^{R\_\text{ext}}\bigl(r-R\bigr)\sigma(r)\,\mathrm{d}r=\frac{ph^2}{24}\frac{1-\frac{h^2}{4R^2}}{1+\frac{h^2}{12R^2}}=\frac{ph^2}{24}\Bigl(1-\frac{h^2}{3R^2}\Bigr)+\mathcal O\Bigl(\frac{h^6}{R^6}\Bigr).\tag{5}$$

Comparing with [Koiter\'s
solution]({filename}20150608-When_a_thin_shell_is_not_so_thin-01.md), it is
found that the dominant terms of the stress resultant coincide.  This is not
true of the stress couple, though. Even worse, the signs differ! While in
Koiter's solution, the stress couple is negative (as expected), integration of
the 3D solution leads to a *positive* stress couple, which is
unphysical. Something nasty is definitely taking place, here!

In the next section, I will show that Eqs. [(4)](#eq07) and [(5)](#eq08) are in
fact (poor) approximations of the true expression of the stress resultant and
couple.

## Stress resultants and stress couples: the correct definition

Stress resultants and stress couples are defined from the internal resultant
forces and moments exerted on subdomains of the shell. In this section, I will
show how such subsystems are constructed from a closed path drawn on the
midsurface.

![The shell, seen as a continuum]({static}20150701-When_a_thin_shell_is_not_so_thin-02/fig01.svg){.figure}

The story begins with a shell, seen as a continuum.

![The upper and lower faces of the shell]({static}20150701-When_a_thin_shell_is_not_so_thin-02/fig02.svg){.figure}

We will focus on the upper and lower faces of the shell, $\Sigma^+$ and
$\Sigma^-$, as well as the base surface, $\Sigma$. For homogeneous shells, the
base surface usually coincides with the midsurface (in other words, it is
equidistant to the upper and lower faces). This is not really required here, as
we are only discussing equilibrium issues.  However, for the sake of simplicity,
we will just assume that the base surface *is* the midsurface.

![A closed path on the base surface]({static}20150701-When_a_thin_shell_is_not_so_thin-02/fig03.svg){.figure}

To define a subregion of the shell, we first draw a closed path $\Gamma$ on the
base surface, and define the local basis $(\vec\tau, \vec n, \vec\nu)$ attached
to this curve: $\vec\tau$ is the unit tangent, $\vec n$ is the unit normal to
the base surface, and $\vec\nu=\vec\tau\times\vec n$ is the unit in-plane normal
to $\Gamma$.

![The normal sweeps the lateral surface of the subsystem]({static}20150701-When_a_thin_shell_is_not_so_thin-02/fig04.svg){.figure}

As the current point moves along this path, the normal to the base surface
sweeps a new surface, which will be the *lateral surface* of the subregion. It
should be noted that, by construction, the lateral surface is a ruled
surface. The outer normal to this surface is constant, equal to $\vec\nu$
along each of the generating lines.

![The lateral surface intersects the upper and lower faces]({static}20150701-When_a_thin_shell_is_not_so_thin-02/fig05.svg){.figure}

The lateral surface intersects the upper and lower faces of the shell…

![The subsystem]({static}20150701-When_a_thin_shell_is_not_so_thin-02/fig06.svg){.figure}

… thus defining the upper and lower boundaries of the subregion.  That's it! We
have defined our subsystem!

Let us now compute the resultant force $\boldsymbol{\mathcal R}$ and moment
$\boldsymbol{\mathcal M}$ exerted by the remainder of the shell on this
subregion. By definition of the Cauchy stress tensor $\tens\sigma$, we have

<a name="eq09"></a>
$$\boldsymbol{\mathcal R}=\int\_{\mathbf x\in\Sigma^\mathrm{lat}}\boldsymbol\sigma\cdot\boldsymbol\nu\,\mathrm{d}\Sigma\_{\mathbf x}^\mathrm{lat},\tag{6}$$

<a name="eq10"></a>
$$\boldsymbol{\mathcal M}=\int\_{\mathbf x\in\Sigma^\mathrm{lat}}\mathbf{x}\times\bigl(\boldsymbol\sigma\cdot\boldsymbol\nu\bigr)\mathrm{d}\Sigma\_{\mathbf x}^\mathrm{lat},\tag{7}$$

where $\mathbf x$ denotes the current point on the lateral surface. By
definition, the membrane stress resultant $\tens N$ (second order tensor), the
shear stress resultant $\vec Q$ (vector) and the stress couple $\tens M$ (second
order tensor) allow the reduction of the above surface integrals to contour
integrals

<a name="eq11"></a>
$$\boldsymbol{\mathcal R}=\int\_{\mathbf x\in\Gamma}\bigl[\mathbf N\cdot\boldsymbol\nu+\bigl(\mathbf Q\cdot\boldsymbol\nu\bigr)\mathbf n\bigr]\mathrm{d}s,\tag{8}$$

<a name="eq12"></a>
$$\boldsymbol{\mathcal M}=\int\_{\mathbf x\in\Gamma}\mathbf x\times\bigl[\mathbf N\cdot\boldsymbol\nu+\bigl(\mathbf Q\cdot\boldsymbol\nu\bigr)\mathbf n\bigr]\mathrm{d}s-\int\_{\mathbf x\in\Gamma}\mathbf n\times\bigl(\mathbf M\cdot\boldsymbol\nu\bigr)\mathrm ds.\tag{9}$$

This definition will be used in the next section to compute the stress resultant
and couple in the spherical pressure vessel.

## Stress resultant and couple in the spherical pressure vessel

![Integration on the lateral surface]({static}20150701-When_a_thin_shell_is_not_so_thin-02/fig07.svg){.figure}

In order to compute $N$ and $M$ from the stress distribution in the spherical
pressure vessel, we consider a subdomain obtained by taking the equator as
closed path $\Gamma$. Then, the lateral surface $\Sigma^\mathrm{lat}$ is an
annulus, and the outer normal $\boldsymbol\nu$ is constant, vertical. Points on
the lateral surface are specified by their radial distance $r$ and polar angle
$\phi$.

We first use Eq. [(6)](#eq09) to compute the resultant internal force
$\boldsymbol{\mathcal R}$. The surface element $\mathrm{d}\Sigma^\mathrm{lat}$
reads

$$\mathrm{d}\Sigma^\mathrm{lat}=r\,\mathrm{d}r\,\mathrm{d}\phi=\frac rR\,\mathrm{d}r\,\mathrm{d}s.$$

where it is observed that $\mathrm{d}s=R\mathrm{d}\phi$ ($s$: arc-length
measured on $\Gamma$). Furthermore, from Eq. [(3)](#eq06), we have
$\boldsymbol\sigma\cdot\boldsymbol\nu=\sigma(r)\,\boldsymbol\nu$. Eq. [(6)](#eq09)
then reads

<a name="eq14"></a>
$$\boldsymbol{\mathcal R}=\int\_\Gamma\Bigl[\int\_{R\_\mathrm{int}}^{R\_\mathrm{ext}}\sigma(r)\,\frac rR\,\mathrm{d}r\Bigr]\boldsymbol\nu\,\mathrm{d}s,\tag{10}$$

where we have used the fact that $\boldsymbol\nu$ is constant along
$\Gamma$. Turning now to Eq. [(8)](#eq11), and recalling that
$N\_{\theta\theta}=N\_{\phi\phi}=N$ and $\mathbf Q=\mathbf 0$, we find

<a name="eq15"></a>
$$\boldsymbol{\mathcal R}=\int\_{\Gamma}N\,\boldsymbol\nu\mathrm{d}s.\tag{11}$$

Upon identification of Eqs. [(10)](#eq14) and [(11)](#eq15), we finally find the
following expression of the stress resultant $N$

<a name="eq16"></a>
$$N=\int\_{R\_\mathrm{int}}^{R\_\mathrm{ext}}\sigma(r)\,{\color{red}\frac rR}\,\mathrm{d}r,\tag{12}$$

while a similar calculation delivers the stress couple $M$

<a name="eq17"></a>
$$M=\int\_{R\_\mathrm{int}}^{R\_\mathrm{ext}}-\bigl(r-R\bigr)\sigma(r)\,{\color{red}\frac rR}\,\mathrm{d}r.\tag{13}$$

Comparing Eqs. [(12)](#eq16) and [(13)](#eq17) with Eqs. [(4)](#eq07) and
[(5)](#eq08), we observe that we forgot the Jacobian $r/R$! For thin shells,
we have $r\simeq R$ and this correction is usually neglected.

In the present case, using Eq. [(2)](#eq02), we find

<a name="eq18"></a>
$$N=\frac{pR}2\bigl(1+\frac{h^2}{4R^2}\bigr),\tag{14}$$

<a name="eq19"></a>
$$M=-\frac{ph^2}{30}\,\frac{h^2}{R^2}+\mathcal O\bigl(\frac{h^6}{R^6}\bigr).\tag{15}$$

Comparing Eqs. [(14)](#eq18) and [(15)](#eq19) with Eqs. [(4)](#eq07) and
[(5)](#eq08), we see that the results are dramatically different!  Indeed, the
stress couple has a different sign, and is two order of magnitude smaller (with
respect to the thickness of the shell)! Clearly, the thin shell approximation is
questionable in the present case.

## Conclusion

In this post, we used the exact stress distribution within the spherical vessel
to compute the stress resultant and stress couple. We showed that the thin shell
approximation, which amounts to neglecting the jacobian in a surface integral,
results in poor estimates in this case. Exact integration delivers much more
convincing results. However, we still have not completely solved the
problem. Indeed, comparing Eqs. [(14)](#eq18) and [(15)](#eq19) with Eqs. (17)
and (18) in the [previous
instalment]({filename}20150608-When_a_thin_shell_is_not_so_thin-01.md) of this
series, we still observe major differences: the two values of the stress couple
have the same sign, but they differ by two orders of magnitude (with respect to
the thickness of the shell).

In the [next
instalment]({filename}20150706-When_a_thin_shell_is_not_so_thin-03.md) of this
series, we will go back to Koiter's shell model and use constitutive equations
for *thick shells* to finally resolve the apparent contradiction.

Figures in this post were generated with the nice
[PyX](http://pyx.sourceforge.net/) library.

<!-- Local Variables: -->
<!-- fill-column: 80 -->
<!-- End: -->
