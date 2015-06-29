import numpy as np
import pyx

from scipy.optimize import brentq

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
        t_u = self.tangent_u(u, v)
        t_v = self.tangent_v(u, v)
        n = np.empty_like(t_u)
        n[0] = t_u[1]*t_v[2]-t_u[2]*t_v[1]
        n[1] = t_u[2]*t_v[0]-t_u[0]*t_v[2]
        n[2] = t_u[0]*t_v[1]-t_u[1]*t_v[0]
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
    c = pyx.canvas.canvas()

    # Outer boundaries
    attrs = [pyx.deco.stroked([boundary_thickness, boundary_color])]
    c.stroke(multiline(*proj(*upper_outer_boundary)), attrs)
    curve2 = id_v(base.u_range[1], base.v_range)
    lat2 = lateral_surface(base, curve2, z_range)
    c.stroke(multiline(*proj(*boundary(lat2, v_fine, z_range))), attrs)
    curve3 = id_u(base.v_range[1], base.u_range)
    lat3 = lateral_surface(base, curve3, z_range)
    c.stroke(multiline(*proj(*boundary(lat3, u_fine, z_range))), attrs)

    # Iso-lines
    attrs = [isoline_thickness, boundary_color]
    xyz = np.empty((3, v_fine.shape[0]+1), dtype=np.float64)
    for u in u_coarse:
        upper.point(u, v_fine, xyz[:, :-1])
        lower.point(u, lower.v_range[1], xyz[:, -1])
        c.stroke(multiline(*proj(*xyz)), attrs)
    xyz = np.empty((3, u_fine.shape[0]+1), dtype=np.float64)
    for v in v_coarse:
        upper.point(u_fine, v, xyz[:, 0:-1])
        lower.point(lower.u_range[1], v, xyz[:, -1])
        c.stroke(multiline(*proj(*xyz)), attrs)

    # Trace of base surface
    attrs = [isoline_thickness, base_color]
    c.stroke(multiline(*proj(*base.point(*curve2.point(v_fine)))), attrs)
    c.stroke(multiline(*proj(*base.point(*curve3.point(u_fine)))), attrs)

    c.writeSVGfile('fig01')

    # ------------------------------------------------------------------------
    #                                 Figure 2
    # ------------------------------------------------------------------------
    c = pyx.canvas.canvas()

    attrs = [pyx.deco.filled([base_color, outer_transparency])]
    c.draw(multiline(*proj(*base_outer_boundary), closed=True), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    c.draw(multiline(*proj(*upper_outer_boundary), closed=True), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    c.draw(multiline(*proj(*lower_outer_boundary), closed=True), attrs)

    text_scaling = pyx.trafo.scale(1.4)
    text_attrs = [pyx.text.halign.boxleft, pyx.text.valign.middle,
                  pyx.color.rgb.black, pyx.color.transparency(0.)]

    u, v = -0.57, 0.57

    x, y = proj(*base.point(u, v))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma$', text_attrs)
    c.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    x, y = proj(*upper.point(u, v))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma^+$', text_attrs)
    c.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    x, y = proj(*lower.point(u, v))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma^-$', text_attrs)
    c.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    c.writeSVGfile('fig02')

    # ------------------------------------------------------------------------
    #                                 Figure 3
    # ------------------------------------------------------------------------
    c = pyx.canvas.canvas()

    attrs = [pyx.deco.filled([base_color, outer_transparency])]
    xyz = np.hstack((base_outer_boundary, base_inner_boundary))
    c.draw(multiline(*proj(*xyz), closed=True), attrs)

    attrs = [pyx.deco.stroked([base_color, boundary_thickness]),
             pyx.deco.filled([base_color, inner_transparency])]
    c.draw(multiline(*proj(*base_inner_boundary)), attrs)

    arrow_attrs = [pyx.deco.filled([normal_color, pyx.color.transparency(0.0)])]
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
        c.stroke(pyx.path.line(x1[i], y1[i], x2[i], y2[i]), attrs)

    cc = pyx.canvas.canvas()
    cc.text(0, +0.1, r'$\bm{\mathrm{n}}$', [pyx.text.halign.boxcenter,
                                            pyx.text.valign.bottom,
                                            normal_color,
                                            pyx.color.transparency(0.)])
    c.insert(cc, [text_scaling, pyx.trafo.translate(x2[-5], y2[-5])])

    x, y = proj(*base.point(-0.57, 0.57))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Sigma$', text_attrs)
    c.insert(cc, [text_scaling, pyx.trafo.translate(x, y)])

    x, y = proj(*base.point(*inner_boundary.point(0.25*np.pi)))
    cc = pyx.canvas.canvas()
    cc.text(0, 0, r'$\Gamma$', [pyx.text.halign.boxleft, pyx.text.valign.top,
                                pyx.color.rgb.black, pyx.color.transparency(0.)])
    c.insert(cc, [text_scaling, pyx.trafo.translate(x, y-0.1)])

    c.writeSVGfile('fig03')

    # ------------------------------------------------------------------------
    #                                 Figure 4
    # ------------------------------------------------------------------------
    c = pyx.canvas.canvas()

    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    xyz = np.hstack((lower_outer_boundary, lower_inner_boundary))
    c.draw(multiline(*proj(*xyz)), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    xyz = np.hstack((upper_outer_boundary, upper_inner_boundary))
    c.draw(multiline(*proj(*xyz)), attrs)

    attrs = [pyx.deco.stroked([boundary_color, boundary_thickness]),
             pyx.deco.filled([boundary_color, inner_transparency])]
    c.draw(multiline(*proj(*upper_inner_boundary)), attrs)
    c.draw(multiline(*proj(*lower_inner_boundary)), attrs)

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
        c.stroke(pyx.path.line(x1[i], y1[i], x2[i], y2[i]), attrs)

    c.writeSVGfile('fig04')

    # ------------------------------------------------------------------------
    #                                 Figure 5
    # ------------------------------------------------------------------------

    c = pyx.canvas.canvas()

    attrs = [pyx.deco.stroked([boundary_color, boundary_thickness])]
    c.draw(multiline(*proj(*upper_inner_boundary), closed=True), attrs)
    c.draw(multiline(*proj(*lower_inner_visible_boundary)), attrs)
    x_up, y_up = proj(*upper_inner_visible_boundary)
    x_lo, y_lo = proj(*lower_inner_visible_boundary)
    c.draw(pyx.path.line(x_up[0], y_up[0], x_lo[0], y_lo[0]), attrs)
    c.draw(pyx.path.line(x_up[-1], y_up[-1], x_lo[-1], y_lo[-1]), attrs)

    attrs = [pyx.deco.stroked([base_color, isoline_thickness])]
    c.draw(multiline(*proj(*base_inner_visible_boundary)), attrs)

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
            c.stroke(multiline(*proj(*xyz)), attrs)

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
            c.stroke(multiline(*proj(*xyz)), attrs)

    c.writeSVGfile('fig05')


    # ------------------------------------------------------------------------
    #                                 Figure 100
    # ------------------------------------------------------------------------
    c = pyx.canvas.canvas()

    attrs = [pyx.deco.filled([base_color, outer_transparency])]
    xyz = np.hstack((base_outer_boundary, base_inner_boundary))
    c.draw(multiline(*proj(*xyz)), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    xyz = np.hstack((lower_outer_boundary, lower_inner_boundary))
    c.draw(multiline(*proj(*xyz)), attrs)
    attrs = [pyx.deco.filled([boundary_color, outer_transparency])]
    xyz = np.hstack((upper_outer_boundary, upper_inner_boundary))
    c.draw(multiline(*proj(*xyz)), attrs)

    attrs = [pyx.deco.filled([base_color, inner_transparency])]
    c.draw(multiline(*proj(*base_inner_boundary), closed=True), attrs)
    attrs = [pyx.deco.filled([boundary_color, inner_transparency])]
    c.draw(multiline(*proj(*upper_inner_boundary), closed=True), attrs)
    attrs = [pyx.deco.filled([boundary_color, inner_transparency])]
    c.draw(multiline(*proj(*lower_inner_boundary), closed=True), attrs)

    c.writeSVGfile('fig100')
