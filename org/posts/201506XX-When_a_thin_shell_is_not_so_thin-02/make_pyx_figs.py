import numpy as np
import pyx

from scipy.optimize import brentq

def wedge(x, y, out=None):
    x, y = np.broadcast_arrays(x, y)
    if out is None:
        out = np.empty_like(x)
    out[0] = x[1]*y[2]-x[2]*y[1]
    out[1] = x[2]*y[0]-x[0]*y[2]
    out[2] = x[0]*y[1]-x[1]*y[0]
    return out


class Curve:
    def __init__(self, point, t_range, dim=3, eps=1E-8):
        self.point = point
        self.t_range = t_range
        self.dim = dim
        self.eps=eps

    def tangent(self, t):
        p1 = self.point(t-0.5*self.eps)
        p2 = self.point(t+0.5*self.eps)
        return (p2-p1)/self.eps

    def normal(self, t):
        t1 = self.tangent(t-0.5*self.eps)
        t2 = self.tangent(t+0.5*self.eps)
        n = (t2-t1)/self.eps
        norm = np.sqrt(np.sum(n**2, axis=0))
        return n/norm[..., None]


class Surface:
    def __init__(self, point, u_range, v_range, dim=3, eps=1E-8):
        self.point = point
        self.u_range = u_range
        self.v_range = v_range
        self.dim = dim
        self.eps=eps

    def tangent_u(self, u, v):
        p1 = self.point(u-0.5*self.eps, v)
        p2 = self.point(u+0.5*self.eps, v)
        return (p2-p1)/self.eps

    def tangent_v(self, u, v):
        p1 = self.point(u, v-0.5*self.eps)
        p2 = self.point(u, v+0.5*self.eps)
        return (p2-p1)/self.eps

    def normal(self, u, v):
        n = wedge(self.tangent_u(u, v), self.tangent_v(u, v))
        norm = np.sqrt(np.sum(n**2, axis=0))
        return n/norm[None, ...]

    def iso_u(self, u):
        # TODO: check that u is a scalar
        def f(t, out=None):
            return self.point(u, t, out)
        return Curve(f, self.v_range, self.dim, self.eps)

    def iso_v(self, v):
        # TODO: check that v is a scalar
        def f(t, out=None):
            return self.point(t, v, out)
        return Curve(f, self.u_range, self.dim, self.eps)

def boundary(surf, u, v, out=None):
    u = np.asarray(u)
    v = np.asarray(v)
    nu = u.shape[0]
    nv = v.shape[0]
    if out is None:
        out = np.empty((surf.dim, 2*(nu+nv)), dtype=np.float64)
    boundary1 = surf.point(u, surf.v_range[0], out[:, 0:nu])
    boundary2 = surf.point(surf.u_range[1], v, out[:, nu:nu+nv])
    boundary3 = surf.point(u[::-1], surf.v_range[1], out[:, nu+nv:2*nu+nv])
    boundary4 = surf.point(surf.u_range[0], v[::-1], out[:, 2*nu+nv:])
    return out


def parallel(surf, z):
    def f(u, v, out=None):
        u, v = np.broadcast_arrays(u, v)
        if out is None:
            out = np.empty((surf.dim,)+u.shape, dtype=np.float64)
        p = surf.point(u, v)
        n = surf.normal(u, v)
        return np.add(p, z*n, out)
    return Surface(f, surf.u_range, surf.v_range, surf.dim, surf.eps)


def lateral_surface(surf, curve, z_range):
    def f(t, z, out=None):
        t, z  = np.broadcast_arrays(t, z)
        if out is None:
            out = np.empty(t.shape+(surf.dim,), dtype=np.float64)
        uv = curve.point(t)
        u = uv[0]
        v = uv[1]
        p = surf.point(u, v)
        n = surf.normal(u, v)
        return np.add(p, z[None, ...]*n, out)
    return Surface(f, curve.t_range, z_range, surf.dim, surf.eps)


def multiline(x, y, closed=False):
    x, y = np.broadcast_arrays(x, y)
    n = x.shape[0]
    items = [pyx.path.moveto(x[0], y[0])]
    for i in range(1, n):
        items.append(pyx.path.lineto(x[i], y[i]))
    if closed:
        items.append(pyx.path.closepath())
    return pyx.path.path(*items)


def create_surfaces(h):
    def base(u, v, out=None):
        u, v = np.broadcast_arrays(u, v)
        if out is None:
            out = np.empty((3,)+u.shape)
        out[0] = 4*u
        out[1] = 4*v
        out[2] = -0.9*(u**2-v**2)
        return out
    u_range = (-1.0, 1.0)
    v_range = (-1.0, 1.0)
    base = Surface(base, u_range, v_range)
    return base, parallel(base, 0.5*h), parallel(base, -0.5*h)


def create_inner_boundary():
    def boundary(t, out=None):
        t = np.asarray(t)
        if out is None:
            out = np.empty((2,)+t.shape, dtype=np.float64)
        out[0] = 0.5*np.cos(t)
        out[1] = 0.5*np.sin(t)
        return out
    return Curve(boundary, (0, 2*np.pi), dim=2)


def inner_boundaries(base, boundary, h):
    t = np.linspace(*boundary.t_range, num=40)
    uv = boundary.point(t[::-1])
    n = base.normal(*uv)
    p = base.point(*uv)
    return p, p+0.5*h*n, p-0.5*h*n


def visible_boundaries(base, boundary, h, proj):
    def f(t):
        uv = boundary.point(t)
        uv_prime = boundary.tangent(t)
        a_u = base.tangent_u(*uv)
        a_v = base.tangent_v(*uv)
        v1 = uv_prime[0]*a_u+uv_prime[1]*a_v
        v1 = proj(*v1)
        v2 = base.normal(*uv)
        v2 = proj(*v2)
        return v1[0]*v2[1]-v1[1]*v2[0]

    t1 = brentq(f, -1.0, 0.0)
    t2 = brentq(f, 1.5, 2.5)

    t = np.linspace(t1, t2, num=20)
    uv = inner_boundary.point(t)
    p = base.point(*uv)
    n = base.normal(*uv)
    return p, p+0.5*h*n, p-0.5*h*n


def id_u(v, u_range):
    def f(t, out=None):
        t = np.asarray(t)
        if out is None:
            out = np.empty((2,)+t.shape)
        out[0] = t
        out[1] = v
        return out
    return Curve(f, u_range, dim=2)


def id_v(u, v_range):
    def f(t, out=None):
        t = np.asarray(t)
        if out is None:
            out = np.empty((2,)+t.shape)
        out[0] = u
        out[1] = t
        return out
    return Curve(f, v_range, dim=2)


if __name__ == '__main__':
    # Using package txfonts leads to LaTeX messages that pyx cannot parse.
    pyx.text.set(pyx.text.LatexRunner,
                 docopt='12pt',
                 errordetail=pyx.text.errordetail.full,
                 texmessages_preamble=[pyx.text.texmessage.ignore],
                 texmessages_run=[pyx.text.texmessage.ignore])
    pyx.text.preamble(r'\usepackage{amsmath, bm, txfonts}')

    proj = pyx.graph.graphxyz.parallel(45, 30).point

    h = 1.5

    boundary_thickness = pyx.style.linewidth.THick
    isoline_thickness = pyx.style.linewidth.normal
    normal_thickness = pyx.style.linewidth.Thick

    boundary_color = pyx.color.cmyk.PineGreen
    base_color = pyx.color.cmyk.Blue
    normal_color = pyx.color.cmyk.Orange

    inner_transparency = pyx.color.transparency(0.5)
    outer_transparency = pyx.color.transparency(0.85)

    base, upper, lower = create_surfaces(h)
    inner_boundary = create_inner_boundary()
    z_range = (-h/2, h/2)

    u_fine = np.linspace(*base.u_range, num=20)
    v_fine = np.linspace(*base.v_range, num=20)
    u_coarse = np.linspace(*base.u_range, num=9)
    v_coarse = np.linspace(*base.v_range, num=9)

    upper_outer_boundary = boundary(upper, u_fine, v_fine)
    base_outer_boundary = boundary(base, u_fine, v_fine)
    lower_outer_boundary = boundary(lower, u_fine, v_fine)

    out = inner_boundaries(base, inner_boundary, h)
    base_inner_boundary = out[0]
    upper_inner_boundary = out[1]
    lower_inner_boundary = out[2]

    out = visible_boundaries(base, inner_boundary, h, proj)
    base_inner_visible_boundary = out[0]
    upper_inner_visible_boundary = out[1]
    lower_inner_visible_boundary = out[2]

    num_normals = 20

    # ------------------------------------------------------------------------
    #                                 Figure 1
    # ------------------------------------------------------------------------
    c1 = pyx.canvas.canvas()

    # Outer boundaries
    attrs = [pyx.deco.stroked([boundary_thickness, boundary_color])]
    c1.stroke(multiline(*proj(*upper_outer_boundary)), attrs)
    curve2 = id_v(base.u_range[1], base.v_range)
    lat2 = lateral_surface(base, curve2, z_range)
    c1.stroke(multiline(*proj(*boundary(lat2, v_fine, z_range))), attrs)
    curve3 = id_u(base.v_range[1], base.u_range)
    lat3 = lateral_surface(base, curve3, z_range)
    c1.stroke(multiline(*proj(*boundary(lat3, u_fine, z_range))), attrs)

    # Iso-lines
    attrs = [isoline_thickness, boundary_color]
    xyz = np.empty((3, v_fine.shape[0]+1), dtype=np.float64)
    for u in u_coarse:
        upper.point(u, v_fine, xyz[:, :-1])
        lower.point(u, lower.v_range[1], xyz[:, -1])
        c1.stroke(multiline(*proj(*xyz)), attrs)
    xyz = np.empty((3, u_fine.shape[0]+1), dtype=np.float64)
    for v in v_coarse:
        upper.point(u_fine, v, xyz[:, 0:-1])
        lower.point(lower.u_range[1], v, xyz[:, -1])
        c1.stroke(multiline(*proj(*xyz)), attrs)

    # Trace of base surface
    attrs = [isoline_thickness, base_color]
    c1.stroke(multiline(*proj(*base.point(*curve2.point(v_fine)))), attrs)
    c1.stroke(multiline(*proj(*base.point(*curve3.point(u_fine)))), attrs)

    c1.writeSVGfile('fig01')

    # ------------------------------------------------------------------------
    #                                 Figure 2
    # ------------------------------------------------------------------------
    c2 = pyx.canvas.canvas()

    attrs = [pyx.deco.filled([base_color, outer_transparency])]
    c2.draw(multiline(*proj(*base_outer_boundary), closed=True), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    c2.draw(multiline(*proj(*upper_outer_boundary), closed=True), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    c2.draw(multiline(*proj(*lower_outer_boundary), closed=True), attrs)

    text_scaling = pyx.trafo.scale(1.4)
    text_attrs = [pyx.text.halign.boxleft, pyx.text.valign.middle,
                  pyx.color.rgb.black, pyx.color.transparency(0.)]

    u, v = -0.57, 0.57

    x, y = proj(*base.point(u, v))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma$', text_attrs)
    c2.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    x, y = proj(*upper.point(u, v))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma^+$', text_attrs)
    c2.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    x, y = proj(*lower.point(u, v))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma^-$', text_attrs)
    c2.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    c2.writeSVGfile('fig02')

    # ------------------------------------------------------------------------
    #                                 Figures 3 & 4
    # ------------------------------------------------------------------------
    c4 = pyx.canvas.canvas()
    c3 = pyx.canvas.canvas()

    attrs = [pyx.deco.filled([base_color, outer_transparency])]
    xyz = np.hstack((base_outer_boundary, base_inner_boundary))
    c4.draw(multiline(*proj(*xyz), closed=True), attrs)
    c3.draw(multiline(*proj(*xyz), closed=True), attrs)

    attrs = [pyx.deco.stroked([base_color, boundary_thickness]),
             pyx.deco.filled([base_color, inner_transparency])]
    c4.draw(multiline(*proj(*base_inner_boundary)), attrs)
    c3.draw(multiline(*proj(*base_inner_boundary)), attrs)

    arrow_attrs = [pyx.deco.filled([normal_color,
                                    pyx.color.transparency(0.0)])]
    attrs = [pyx.deco.stroked([normal_thickness, normal_color]),
             pyx.deco.earrow(arrow_attrs, size=0.25)]
    t = np.linspace(*inner_boundary.t_range, num=num_normals, endpoint=False)
    uv = inner_boundary.point(t)
    xyz1 = base.point(*uv)
    n = base.normal(*uv)
    x1, y1 = proj(*xyz1)
    xyz2 = xyz1+n
    x2, y2 = proj(*xyz2)
    for i in range(len(t)):
        c4.stroke(pyx.path.line(x1[i], y1[i], x2[i], y2[i]), attrs)

    x, y = proj(*base.point(-0.57, 0.57))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma$', text_attrs)
    c4.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])
    c3.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    x, y = proj(*base.point(*inner_boundary.point(3.95)))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Gamma$', [pyx.text.halign.boxleft,
                                pyx.text.valign.bottom,
                                pyx.color.rgb.black,
                                pyx.color.transparency(0.)])
    c4.insert(cc, [text_scaling, pyx.trafo.translate(x, y+.1)])
    c3.insert(cc, [text_scaling, pyx.trafo.translate(x, y+.1)])

    # Local basis
    t = 0.4
    uv, uv_prime = inner_boundary.point(t), inner_boundary.tangent(t)
    xyz0, n = base.point(*uv), base.normal(*uv)
    tau = uv_prime[0]*base.tangent_u(*uv)+uv_prime[1]*base.tangent_v(*uv)
    tau /= np.sqrt(np.sum(tau**2, axis=0))
    nu = wedge(tau, n)

    x0, y0 = proj(*xyz0)
    x1, y1 = proj(*(xyz0+tau))
    x2, y2 = proj(*(xyz0+n))
    x3, y3 = proj(*(xyz0+nu))
    c3.stroke(pyx.path.line(x0, y0, x1, y1), attrs)
    c3.stroke(pyx.path.line(x0, y0, x2, y2), attrs)
    c3.stroke(pyx.path.line(x0, y0, x3, y3), attrs)

    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\bm{\tau}$', [pyx.text.halign.boxleft,
                                   pyx.text.valign.middle,
                                   normal_color,
                                   pyx.color.transparency(0.)])
    c3.insert(cc, [text_scaling, pyx.trafo.translate(x1, y1)])
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\bm{\mathrm{n}}$', [pyx.text.halign.boxcenter,
                                         pyx.text.valign.bottom,
                                         normal_color,
                                         pyx.color.transparency(0.)])
    c3.insert(cc, [text_scaling, pyx.trafo.translate(x2, y2)])
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\bm{\nu}$', [pyx.text.halign.boxleft,
                                  pyx.text.valign.top,
                                  normal_color,
                                  pyx.color.transparency(0.)])
    c3.insert(cc, [text_scaling, pyx.trafo.translate(x3, y3)])

    c3.writeSVGfile('fig03')
    c4.writeSVGfile('fig04')

    # ------------------------------------------------------------------------
    #                                 Figure 5
    # ------------------------------------------------------------------------
    c5 = pyx.canvas.canvas()

    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    xyz = np.hstack((lower_outer_boundary, lower_inner_boundary))
    c5.draw(multiline(*proj(*xyz)), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    xyz = np.hstack((upper_outer_boundary, upper_inner_boundary))
    c5.draw(multiline(*proj(*xyz)), attrs)

    attrs = [pyx.deco.stroked([boundary_color, boundary_thickness]),
             pyx.deco.filled([boundary_color, inner_transparency])]
    c5.draw(multiline(*proj(*upper_inner_boundary)), attrs)
    c5.draw(multiline(*proj(*lower_inner_boundary)), attrs)

    attrs = [pyx.deco.stroked([normal_thickness, normal_color])]
    t = np.linspace(*inner_boundary.t_range, num=num_normals, endpoint=False)
    uv = inner_boundary.point(t)
    xyz = base.point(*uv)
    n = base.normal(*uv)
    xyz1 = xyz-0.5*h*n
    x1, y1 = proj(*xyz1)
    xyz2 = xyz+0.5*h*n
    x2, y2 = proj(*xyz2)
    for i in range(len(t)):
        c5.stroke(pyx.path.line(x1[i], y1[i], x2[i], y2[i]), attrs)

    u, v = -0.57, 0.57

    x, y = proj(*upper.point(u, v))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma^+$', text_attrs)
    c5.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    x, y = proj(*lower.point(u, v))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma^-$', text_attrs)
    c5.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    c5.writeSVGfile('fig05')

    # ------------------------------------------------------------------------
    #                                 Figure 6
    # ------------------------------------------------------------------------

    c6 = pyx.canvas.canvas()

    attrs = [pyx.deco.stroked([boundary_color, boundary_thickness])]
    c6.draw(multiline(*proj(*upper_inner_boundary), closed=True), attrs)
    c6.draw(multiline(*proj(*lower_inner_visible_boundary)), attrs)
    x_up, y_up = proj(*upper_inner_visible_boundary)
    x_lo, y_lo = proj(*lower_inner_visible_boundary)
    c6.draw(pyx.path.line(x_up[0], y_up[0], x_lo[0], y_lo[0]), attrs)
    c6.draw(pyx.path.line(x_up[-1], y_up[-1], x_lo[-1], y_lo[-1]), attrs)

    attrs = [pyx.deco.stroked([base_color, isoline_thickness])]
    c6.draw(multiline(*proj(*base_inner_visible_boundary)), attrs)

    t = np.linspace(*inner_boundary.t_range, num=200)
    uv = inner_boundary.point(t)
    u_min = np.min(uv[0])
    u_max = np.max(uv[0])
    v_min = np.min(uv[1])
    v_max = np.max(uv[1])

    # Iso-lines
    attrs = [isoline_thickness, boundary_color]
    xyz = np.empty((3, v_fine.shape[0]+1), dtype=np.float64)
    for u in u_coarse:
        if u >= u_min and u <= u_max:
            def f(t):
                uv = inner_boundary.point(t)
                return uv[0]-u
            t1 = brentq(f, np.pi, 2*np.pi)
            t2 = brentq(f, 0, np.pi)
            uv = inner_boundary.point([t1, t2])
            vv = np.linspace(uv[1, 0], uv[1, 1], num=v_fine.shape[0])
            upper.point(u, vv, xyz[:, :-1])
            lower.point(u, vv[-1], xyz[:, -1])
            c6.stroke(multiline(*proj(*xyz)), attrs)

    xyz = np.empty((3, u_fine.shape[0]+1), dtype=np.float64)
    for v in v_coarse:
        if v >= v_min and v <= v_max:
            def f(t):
                uv = inner_boundary.point(t)
                return uv[1]-v
            t1 = brentq(f, 0.5*np.pi, 1.5*np.pi)
            t2 = brentq(f, -0.5*np.pi, 0.5*np.pi)
            uv = inner_boundary.point([t1, t2])
            uu = np.linspace(uv[0, 0], uv[0, 1], num=u_fine.shape[0])
            upper.point(uu, v, xyz[:, :-1])
            lower.point(uu[-1], v, xyz[:, -1])
            c6.stroke(multiline(*proj(*xyz)), attrs)

    # Outer normal
    t = 0.4
    uv, uv_prime = inner_boundary.point(t), inner_boundary.tangent(t)
    xyz0, n = base.point(*uv), base.normal(*uv)
    xyz4 = xyz0+0.25*h*n
    tau = uv_prime[0]*base.tangent_u(*uv)+uv_prime[1]*base.tangent_v(*uv)
    tau /= np.sqrt(np.sum(tau**2, axis=0))
    nu = wedge(tau, n)

    x4, y4 = proj(*xyz4)
    x3, y3 = proj(*(xyz4+nu))
    attrs = [pyx.deco.stroked([normal_thickness, normal_color]),
             pyx.deco.earrow(arrow_attrs, size=0.25)]
    c6.stroke(pyx.path.line(x4, y4, x3, y3), attrs)
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\bm{\nu}$', [pyx.text.halign.boxcenter,
                                  pyx.text.valign.top,
                                  normal_color,
                                  pyx.color.transparency(0.)])
    c6.insert(cc, [text_scaling, pyx.trafo.translate(x3, y3)])

    c6.writeSVGfile('fig06')

    # ------------------------------------------------------------------------
    #                                 Figure 100
    # ------------------------------------------------------------------------
    c100 = pyx.canvas.canvas()

    attrs = [pyx.deco.filled([base_color, outer_transparency])]
    xyz = np.hstack((base_outer_boundary, base_inner_boundary))
    c100.draw(multiline(*proj(*xyz)), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    xyz = np.hstack((lower_outer_boundary, lower_inner_boundary))
    c100.draw(multiline(*proj(*xyz)), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    xyz = np.hstack((upper_outer_boundary, upper_inner_boundary))
    c100.draw(multiline(*proj(*xyz)), attrs)

    attrs = [pyx.deco.filled([base_color, inner_transparency])]
    c100.draw(multiline(*proj(*base_inner_boundary), closed=True), attrs)
    attrs = [pyx.deco.filled([boundary_color, inner_transparency])]
    c100.draw(multiline(*proj(*upper_inner_boundary), closed=True), attrs)
    attrs = [pyx.deco.filled([boundary_color, inner_transparency])]
    c100.draw(multiline(*proj(*lower_inner_boundary), closed=True), attrs)

    #c100.writeSVGfile('fig100')

    # ------------------------------------------------------------------------
    #                                 Figure 7
    # ------------------------------------------------------------------------
    h = 1.0
    R = 3.0
    R_int = R-0.5*h
    R_ext = R+0.5*h

    c7 = pyx.canvas.canvas()

    t = np.linspace(0, 2*np.pi, num=100, endpoint=False)

    attrs = [pyx.deco.stroked([boundary_thickness, boundary_color]),
             pyx.deco.filled([boundary_color, outer_transparency])]

    phi = -0.25*np.pi
    theta = np.linspace(-0.5*np.pi, 0.5*np.pi, num=100)
    x = R_ext*np.sin(theta)*np.cos(phi)
    y = R_ext*np.sin(theta)*np.sin(phi)
    z = -R_ext*np.cos(theta)
    x, y = proj(x, y, z)
    c7.draw(multiline(x, y, closed=False), attrs)

    t = np.linspace(0.75*np.pi, 1.75*np.pi, num=100)
    x, y = proj(R_ext*np.cos(t), R_ext*np.sin(t), 0)
    c7.draw(multiline(x, y), attrs)

    t = np.linspace(0, 2*np.pi, num=100)
    x, y = proj(R_int*np.cos(t), R_int*np.sin(t), 0)
    c7.draw(multiline(x, y, closed=True), attrs)
    x, y = proj(R_ext*np.cos(t), R_ext*np.sin(t), 0)
    c7.draw(multiline(x, y, closed=True), attrs)
    x, y = proj(R*np.cos(t), R*np.sin(t), 0)
    attrs = [pyx.deco.stroked([boundary_thickness, base_color,
                               pyx.color.transparency(0.)])]
    c7.draw(multiline(x, y, closed=True), attrs)

    r = 1.5*R
    t1 = 0.0
    x1, y1 = proj(r*np.cos(t1), r*np.sin(t1), 0)

    t2 = np.pi/3
    x2, y2 = proj(r*np.cos(t2), r*np.sin(t2), 0)
    x3, y3 = proj(R*np.cos(t2), R*np.sin(t2), 0)

    arrow_attrs = [pyx.deco.filled([normal_color,
                                    pyx.color.transparency(0.0)])]
    attrs = [pyx.deco.stroked([normal_thickness, normal_color]),
             pyx.deco.earrow(arrow_attrs, size=0.25)]
    c7.draw(pyx.path.line(x3, y3, x3, y3+1), attrs)

    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\boldsymbol\nu$', [pyx.text.halign.boxcenter,
                                        pyx.text.valign.bottom,
                                        normal_color,
                                        pyx.color.transparency(0.)])
    c7.insert(cc, [text_scaling, pyx.trafo.translate(x3, y3+1)])

    attrs = [pyx.deco.stroked([isoline_thickness,
                               pyx.color.rgb.black,
                               pyx.color.transparency(0.)])]
    c7.draw(pyx.path.line(0, 0, x1, y1), attrs)
    c7.draw(pyx.path.line(0, 0, x2, y2), attrs)

    text_attrs = [pyx.text.halign.boxcenter, pyx.text.valign.top,
                  pyx.color.rgb.black, pyx.color.transparency(0.)]
    arrow_attrs = [pyx.deco.filled([pyx.color.rgb.black,
                                    pyx.color.transparency(0.0)])]
    attrs = [pyx.deco.stroked([isoline_thickness, pyx.color.rgb.black]),
             pyx.deco.earrow(arrow_attrs, size=0.25)]
    t = np.linspace(t1, t2, num=20)
    r = 1.4*R
    c7.draw(multiline(*proj(r*np.cos(t), r*np.sin(t), 0)), attrs)
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\phi$', text_attrs)
    t = 0.5*(t1+t2)
    c7.insert(cc, [text_scaling, pyx.trafo.translate(*proj(r*np.cos(t),
                                                           r*np.sin(t), 0))])

    text_attrs = [pyx.text.halign.boxleft, pyx.text.valign.middle,
                  pyx.color.rgb.black, pyx.color.transparency(0.)]
    t = 2*np.pi/3
    x, y = proj(R_ext*np.cos(t), R_ext*np.sin(t), 0)
    c7.draw(pyx.path.line(0, 0, x, y), attrs)
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$R_\mathrm{ext}$', text_attrs)
    c7.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    t = 5*np.pi/6
    x, y = proj(R_int*np.cos(t), R_int*np.sin(t), 0)
    c7.draw(pyx.path.line(0, 0, x, y), attrs)
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$R_\mathrm{int}$', text_attrs)
    c7.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    text_attrs = [pyx.text.halign.boxleft, pyx.text.valign.middle,
                  pyx.color.rgb.black, pyx.color.transparency(0.)]
    t = 7*np.pi/6
    x4, y4 = proj(R*np.cos(t), R*np.sin(t), 0)
    x1, y1 = x4+1.5, y4+1.2
    x3, y3 = x4-0.3, y4+1.0
    x2, y2 = x1, y1
    c7.draw(pyx.path.curve(x1, y1, x2, y2, x3, y3, x4, y4), attrs)
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Gamma$', text_attrs)
    c7.insert(cc, [text_scaling, pyx.trafo.translate(x1, y1)])

    text_attrs = [pyx.text.halign.boxright, pyx.text.valign.middle,
                  pyx.color.rgb.black, pyx.color.transparency(0.)]
    t = 4*np.pi/3
    r = R+.25*h
    x4, y4 = proj(r*np.cos(t), r*np.sin(t), 0)
    x1, y1 = x4-1., y4+1.5
    x3, y3 = x4+0.3, y4+1.0
    x2, y2 = x1, y1
    c7.draw(pyx.path.curve(x1, y1, x2, y2, x3, y3, x4, y4), attrs)
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma^\mathrm{lat}$', text_attrs)
    c7.insert(cc, [text_scaling, pyx.trafo.translate(x1, y1)])

    c7.writeSVGfile('fig07')
