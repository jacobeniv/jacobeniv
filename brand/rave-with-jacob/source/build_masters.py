import sys
import os
HERE = os.path.dirname(os.path.abspath(__file__))
S, B = sys.argv[1], sys.argv[2]   # S: scratch dir for concept files (needs S/logo), B: output brand dir
sys.argv = ["x", S + "/logo"]
exec(open(os.path.join(HERE, "gen_logos.py")).read())

ACID, NIGHT, WHITE = "#C6FF00", "#0B0B0F", "#FFFFFF"
sym_d = b
def sym(fill, tf=""):
    return (f'<g transform="{tf}" fill="{fill}"><path fill-rule="evenodd" d="{sym_d}"/>'
            f'<circle cx="{CX}" cy="{CY}" r="10"/></g>')
def name(fill, x, y, sc):
    return f'<g fill="{fill}">' + stacked(x, y, sc).replace('fill="#000"', "") + "</g>"
def save(fn, w, h, body, bg=None, title="Rave with Jacob logo", x0=0):
    rect = f'<rect x="{f(x0)}" width="{f(w)}" height="{f(h)}" fill="{bg}"/>' if bg else ""
    open(f"{B}/master/{fn}", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{f(x0)} 0 {f(w)} {f(h)}" role="img"><title>{title}</title>{rect}{body}</svg>\n')

# symbol, small-size cut (groove dropped, larger spindle)
save("symbol.svg", 256, 256, sym(NIGHT))
small = (f'<g fill="{NIGHT}"><path fill-rule="evenodd" d="M{SL},{TOP}H{SR}V{CY}A{RO},{RO} 0 0 1 {CX-RO},{CY}'
         f'H{CX-RI}A{RI},{RI} 0 0 0 {SL},{CY}Z"/><circle cx="{CX}" cy="{CY}" r="13"/></g>')
save("symbol-small.svg", 256, 256, small)

# horizontal lockup (viewBox starts at the J's left edge; 46-unit gap = stem width + 6)
sc = 200 / H; NX = 244; X0 = 46; Wh = NX + jw*sc + 12 - X0
save("lockup-horizontal.svg", Wh, 256, sym(NIGHT) + name(NIGHT, NX, (256 - H*sc)/2, sc), x0=X0)
save("lockup-horizontal-on-dark.svg", Wh + 36, 256, sym(ACID) + name(WHITE, NX, (256 - H*sc)/2, sc), bg=NIGHT, x0=X0-24)
save("lockup-horizontal-transparent-dark-bg.svg", Wh, 256, sym(ACID) + name(WHITE, NX, (256 - H*sc)/2, sc), x0=X0)

# stacked lockup: symbol centred above the name
sc2 = 0.62; nw = jw*sc2; Ws = max(nw, 256) + 32; Hs = 256 + 12 + H*sc2 + 16
save("lockup-stacked.svg", Ws, Hs, sym(NIGHT, f"translate({f((Ws-256)/2)},0)") + name(NIGHT, (Ws-nw)/2, 268, sc2))
save("lockup-stacked-on-dark.svg", Ws + 48, Hs + 48,
     sym(ACID, f"translate({f((Ws+48-256)/2)},24)") + name(WHITE, (Ws+48-nw)/2, 292, sc2), bg=NIGHT)

# name only
save("wordmark.svg", jw + 24, H + 24, name(NIGHT, 12, 12, 1))
print("ok", f(Wh), f(Ws), f(Hs))
save("lockup-stacked-transparent-dark-bg.svg", Ws, Hs, sym(ACID, f"translate({f((Ws-256)/2)},0)") + name(WHITE, (Ws-nw)/2, 268, sc2))
