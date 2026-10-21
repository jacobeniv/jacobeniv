import math, sys, os
out = sys.argv[1]
f = lambda v: f"{v:.2f}".rstrip("0").rstrip(".")

def svg(w, h, d, extra=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(w)} {f(h)}" width="{f(w)}" height="{f(h)}">'
            f'<path fill="#000" fill-rule="evenodd" d="{d}"/>{extra}</svg>\n')

# ---- shared J symbol geometry (256 canvas) ----
CX, CY, RO, RI, TOP = 128, 153, 70, 30, 33
SL, SR = CX + RI, CX + RO          # stem x range 158..198

def hx(r, dy):
    return math.sqrt(max(r*r - dy*dy, 0))

# A: Strobe J — J sliced into five equal bands by strobe gaps
def strobe():
    d = []
    for y0, y1 in [(33, 63), (75, 105), (117, 147)]:
        d.append(f"M{SL},{y0}H{SR}V{y1}H{SL}Z")
    # band 4: two pieces across the hook, y 159..181 (dy 6..28 < RI)
    y0, y1 = 159, 181
    a0, a1 = y0 - CY, y1 - CY
    for s in (1, -1):
        xo0, xo1, xi0, xi1 = CX+s*hx(RO,a0), CX+s*hx(RO,a1), CX+s*hx(RI,a0), CX+s*hx(RI,a1)
        sw_o = 1 if s == 1 else 0
        d.append(f"M{f(xi0)},{y0}L{f(xo0)},{y0}A{RO},{RO} 0 0 {sw_o} {f(xo1)},{y1}"
                 f"L{f(xi1)},{y1}A{RI},{RI} 0 0 {1-sw_o} {f(xi0)},{y0}Z")
    # band 5: bottom cap, y 193..223
    y0 = 193
    xo = hx(RO, y0 - CY)
    d.append(f"M{f(CX-xo)},{y0}H{f(CX+xo)}A{RO},{RO} 0 0 1 {f(CX-xo)},{y0}Z")
    return "".join(d)

# B: Vinyl J — the hook is half a record: one groove + spindle hole
def vinyl():
    gi, go = 45, 55
    a0 = math.radians(28)       # groove starts below the stem so the J stays one piece
    d = (f"M{SL},{TOP}H{SR}V{CY}A{RO},{RO} 0 0 1 {CX-RO},{CY}H{CX-RI}"
         f"A{RI},{RI} 0 0 0 {SL},{CY}Z")
    p = lambda r: (CX + r*math.cos(a0), CY + r*math.sin(a0))
    (x1, y1), (x2, y2) = p(go), p(gi)
    d += (f"M{f(x1)},{f(y1)}A{go},{go} 0 0 1 {CX-go},{CY}H{CX-gi}"
          f"A{gi},{gi} 0 0 0 {f(x2)},{f(y2)}Z")
    return d, f'<circle cx="{CX}" cy="{CY}" r="10" fill="#000"/>'

# ---- wordmark JΛCOB, cap 128, stroke 20 ----
T = 20
def letter_J(x):
    r_o, r_i = 36, 16
    cx, cy = x + r_o, 128 - r_o
    return (f"M{cx+r_i},0H{cx+r_o}V{cy}A{r_o},{r_o} 0 0 1 {cx-r_o},{cy}H{cx-r_i}"
            f"A{r_i},{r_i} 0 0 0 {cx+r_i},{cy}Z"), 2*r_o
def letter_A(x):
    W, th = 88, 22
    yi = 128 - (132/(W/2))*(W/2 - th)
    return (f"M{x},128L{x+W/2},-4L{x+W},128H{x+W-th}L{x+W/2},{f(yi)}L{x+th},128Z"), W
def ring(cx, cy, ro, ri):
    return (f"M{cx+ro},{cy}A{ro},{ro} 0 1 1 {cx-ro},{cy}A{ro},{ro} 0 1 1 {cx+ro},{cy}Z"
            f"M{cx+ri},{cy}A{ri},{ri} 0 1 0 {cx-ri},{cy}A{ri},{ri} 0 1 0 {cx+ri},{cy}Z")
def letter_C(x):
    ro, ri, ang = 66, 46, math.radians(42)
    cx, cy = x + ro, 64
    p = lambda r, s: (cx + r*math.cos(ang), cy + s*r*math.sin(ang))
    (ax, ay), (bx, by) = p(ro, -1), p(ro, 1)
    (cx2, cy2), (dx, dy) = p(ri, 1), p(ri, -1)
    return (f"M{f(ax)},{f(ay)}A{ro},{ro} 0 1 0 {f(bx)},{f(by)}L{f(cx2)},{f(cy2)}"
            f"A{ri},{ri} 0 1 1 {f(dx)},{f(dy)}Z"), ro + ro*math.cos(ang)
def letter_O(x):
    ro, ri, rd = 66, 46, 14
    cx, cy = x + ro, 64
    dot = (f"M{cx+rd},{cy}A{rd},{rd} 0 1 1 {cx-rd},{cy}A{rd},{rd} 0 1 1 {cx+rd},{cy}Z")
    return ring(cx, cy, ro, ri) + dot, 2*ro
def letter_B(x):
    L, R = x + 36, 37
    xm = L + math.sqrt(R*R - 27*27)
    return (f"M{x},0H{L}A{R},{R} 0 0 1 {f(xm)},64A{R},{R} 0 0 1 {L},128H{x}Z"
            f"M{x+T},{T}H{L}A17,17 0 0 1 {L},54H{x+T}Z"
            f"M{x+T},74H{L}A17,17 0 0 1 {L},108H{x+T}Z"), 73

def wordmark(x0=0, y0=0):
    gaps = [18, 10, 12, 12]   # optical spacing: rounds sit closer
    x, parts = 0, []
    for i, fn in enumerate([letter_J, letter_A, letter_C, letter_O, letter_B]):
        d, w = fn(x)
        parts.append(d)
        x += w + (gaps[i] if i < 4 else 0)
    return "".join(parts), x

def shift(d, dx, dy):
    return f'<g transform="translate({f(dx)},{f(dy)})"><path fill="#000" fill-rule="evenodd" d="{d}"/></g>'

wm, wmw = wordmark()
open(f"{out}/c-wordmark.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-8 -40 {f(wmw+16)} 208">{shift(wm,0,0)}</svg>\n')
# C symbol: the speaker-O alone, scaled to 256
o, _ = letter_O(0)
open(f"{out}/c-symbol.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"><g transform="translate(28,32) scale(1.5)">'
    f'<path fill="#000" fill-rule="evenodd" d="{o}"/></g></svg>\n')

a = strobe()
b, bdot = vinyl()
open(f"{out}/a-symbol.svg", "w").write(svg(256, 256, a))
open(f"{out}/b-symbol.svg", "w").write(svg(256, 256, b, bdot))

def lockup(name, d, extra=""):
    sc = 0.75
    W = 256 + 24 + wmw*sc + 16
    body = (f'<path fill="#000" fill-rule="evenodd" d="{d}"/>{extra}'
            f'<g transform="translate(280,{f(128-64*sc)}) scale({sc})"><path fill="#000" fill-rule="evenodd" d="{wm}"/></g>')
    open(f"{out}/{name}", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(W)} 256">{body}</svg>\n')
lockup("a-lockup.svg", a)
lockup("b-lockup.svg", b, bdot)
print("wordmark width", wmw)

# ================= "RAVE WITH JACOB" lockups =================
def L_R(x):
    L = x + 36
    bowl = (f"M{x},0H{L}A37,37 0 0 1 {L},74H{x+T}V128H{x}Z"
            f"M{x+T},{T}H{L}A17,17 0 0 1 {L},54H{x+T}Z")
    leg = f"M{x+28},60H{x+52}L{x+75},128H{x+51}Z"
    return [bowl, leg], 75
def V_shape(x, W=88, th=22):
    yi = 132 - (132/(W/2))*(W/2 - th)
    return f"M{x},0H{x+th}L{f(x+W/2)},{f(yi)}L{x+W-th},0H{x+W}L{f(x+W/2)},132Z"
def L_V(x): return [V_shape(x)], 88
def L_E(x): return [f"M{x},0H{x+64}V20H{x+T}V54H{x+56}V74H{x+T}V108H{x+64}V128H{x}Z"], 64
def L_W(x): return [V_shape(x, 80), V_shape(x+58, 80)], 138
def L_I(x): return [f"M{x},0H{x+T}V128H{x}Z"], T
def L_T(x): return [f"M{x},0H{x+80}V20H{x+50}V128H{x+30}V20H{x}Z"], 80
def L_H(x): return [f"M{x},0H{x+T}V54H{x+64}V0H{x+84}V128H{x+64}V74H{x+T}V128H{x}Z"], 84
def wrap(fn):
    def g(x):
        d, w = fn(x); return ([d] if isinstance(d, str) else d), w
    return g
GLYPH = {"R": L_R, "A": wrap(letter_A), "V": L_V, "E": L_E, "W": L_W, "I": L_I, "T": L_T,
         "H": L_H, "J": wrap(letter_J), "C": wrap(letter_C), "O": wrap(letter_O), "B": wrap(letter_B)}

def text(word, track=14, space=56):
    x, ds = 0, []
    for ch in word:
        if ch == " ":
            x += space; continue
        d, w = GLYPH[ch](x)
        ds += d
        x += w + track
    return ds, x - track

def paths(ds, tf=""):
    inner = "".join(f'<path fill-rule="evenodd" d="{d}"/>' for d in ds)
    return f'<g fill="#000" transform="{tf}">{inner}</g>'

# stacked name: small "RAVE WITH" over big "JACOB", both the same width
top, tw = text("RAVE WITH", track=30, space=70)
jac, jw = text("JACOB", track=14)
jac, jw = wm_parts = (None, None)
jd, jw = [], 0
x = 0
for i, ch in enumerate("JACOB"):
    d, w = GLYPH[ch](x); jd += d; x += w + ([18, 10, 12, 12, 0][i])
jw = x
ts = jw / tw                       # scale top line to match JACOB width
th_ = 128 * ts
GAP = 26
H = th_ + GAP + 128
def stacked(tf_x=0, tf_y=0, sc=1.0):
    return (paths(top, f"translate({f(tf_x)},{f(tf_y)}) scale({f(sc*ts)})")
            + paths(jd, f"translate({f(tf_x)},{f(tf_y + (th_+GAP)*sc)}) scale({f(sc)})"))

open(f"{out}/name-stacked.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-12 -12 {f(jw+24)} {f(H+24)}">{stacked()}</svg>\n')

def lockup2(name, sym):
    sc = 200 / H                    # stacked name fills ~200 of the 256 height
    W = 256 + 28 + jw*sc + 12
    body = sym + stacked(284, (256 - H*sc)/2, sc)
    open(f"{out}/{name}", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {f(W)} 256">{body}</svg>\n')
lockup2("a-lockup2.svg", f'<path fill="#000" fill-rule="evenodd" d="{a}"/>')
lockup2("b-lockup2.svg", f'<path fill="#000" fill-rule="evenodd" d="{b}"/>{bdot}')
