#!/usr/bin/env python3
"""Gera os SVGs do perfil (hero + painel de atividade), claro e escuro.

Só biblioteca padrão. A data do último push de cada repositório vem da API do
GitHub; se a API falhar, usa o cache em data/activity.json e segue em frente.

Uso:  python scripts/build.py [--offline]
"""
import base64
import datetime as dt
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
W = 830  # largura útil do README no GitHub

THEMES = {
    "light": dict(bg="#F4F2EE", ink="#111111", muted="#5F5E59", rule="#CFCBC3",
                  accent="#C2410C", panel="#E9E6DF", dot="#111111"),
    "dark": dict(bg="#0E0E0F", ink="#EDEBE6", muted="#A09E97", rule="#2C2C2E",
                 accent="#FF8A57", panel="#1A1A1C", dot="#EDEBE6"),
}
SERIF = "Georgia, 'Times New Roman', serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


PHRASES = ["Olá, me chamo Rafael Junqueira",
           "Estudante de Sistemas de Informação",
           "Dev full stack · Dados · IA aplicada"]
CW, DUR = 13.2, 15  # largura do caractere (px) e duração do ciclo (s)


def typing(t):
    """Letreiro: cada frase é digitada, fica parada e é apagada. Só transform/opacity."""
    css, body = [], []
    slot = 100 / len(PHRASES)
    for k, ph in enumerate(PHRASES):
        n, full = len(ph), len(ph) * CW
        s = k * slot
        e1, e2, e3 = s + 10.7, s + 28, s + 32
        css.append(
            f"@keyframes g{k}{{0%,{max(s - .01, 0):.2f}%{{opacity:{1 if k == 0 else 0}}}"
            f"{s:.2f}%,{e3:.2f}%{{opacity:1}}{e3 + .01:.2f}%,100%{{opacity:0}}}}"
            f"@keyframes m{k}{{{s:.2f}%{{transform:translateX(0);animation-timing-function:steps({n})}}"
            f"{e1:.2f}%{{transform:translateX({full:.1f}px)}}"
            f"{e2:.2f}%{{transform:translateX({full:.1f}px);animation-timing-function:steps({n})}}"
            f"{e3:.2f}%,100%{{transform:translateX(0)}}}}"
            f".g{k}{{animation:g{k} {DUR}s linear infinite;opacity:0}}"
            f".m{k}{{animation:m{k} {DUR}s linear infinite}}")
        body.append(
            f'<g class="g{k}"><text class="t" x="36" y="52" textLength="{full:.1f}" lengthAdjust="spacing">{esc(ph)}</text>'
            f'<g class="m{k}"><rect x="36" y="28" width="{full + 24:.1f}" height="32" fill="{t["bg"]}"/>'
            f'<rect class="cr" x="36" y="32" width="2.5" height="24" fill="{t["accent"]}"/></g></g>')
    css.append(".cr{animation:b 1s steps(1) infinite}@keyframes b{50%{opacity:0}}")
    css.append("@media (prefers-reduced-motion:reduce){.g0{animation:none;opacity:1}"
               ".g1,.g2{display:none}.m0{animation:none;transform:translateX(%.1fpx)}.cr{display:none}}"
               % (len(PHRASES[0]) * CW))
    return "".join(css), "".join(body)


def hero(t):
    avatar = base64.b64encode((ASSETS / "avatar.png").read_bytes()).decode()
    h, size, ax, ay = 300, 196, 596, 52
    dots = []
    cols, rows, step = 9, 12, 18
    for c in range(cols):
        for r in range(rows):
            # raio diminui em direção ao retrato: dado bruto -> imagem
            rad = 5.2 * (1 - c / cols) ** 1.3
            if rad < 0.7:
                continue
            x = 424 + c * step
            y = 66 + r * step
            dots.append(
                f'<circle class="d" style="animation-delay:{c * 0.12:.2f}s" '
                f'cx="{x}" cy="{y}" r="{rad:.2f}"/>')
    tcss, tbody = typing(t)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="Olá, me chamo Rafael Junqueira. Dados brutos, decisões claras.">
<style>
.k{{font:600 12px {MONO};letter-spacing:.14em;fill:{t['muted']}}}
.h{{font:400 52px/1 {SERIF};fill:{t['ink']};letter-spacing:-.02em}}
.a{{font-style:italic;fill:{t['accent']}}}
.t{{font:500 22px {MONO};fill:{t['ink']}}}
{tcss}
.d{{fill:{t['dot']};opacity:.85;animation:p 3.6s ease-in-out infinite}}
@keyframes p{{0%,100%{{opacity:.25}}50%{{opacity:.9}}}}
@media (prefers-reduced-motion:reduce){{.d{{animation:none;opacity:.7}}}}
</style>
<rect width="{W}" height="{h}" rx="20" fill="{t['bg']}"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="19.5" fill="none" stroke="{t['rule']}"/>
{tbody}
<text class="h" x="36" y="132">Dados brutos,</text>
<text class="h a" x="36" y="192">decisões claras.</text>
<rect x="36" y="228" width="44" height="3" fill="{t['accent']}"/>
<text class="k" x="36" y="262">PYTHON · DADOS · IA APLICADA</text>
{''.join(dots)}
<defs><clipPath id="c"><rect x="{ax}" y="{ay}" width="{size}" height="{size}" rx="18"/></clipPath></defs>
<rect x="{ax - 8}" y="{ay - 8}" width="{size + 16}" height="{size + 16}" rx="24" fill="{t['panel']}"/>
<image href="data:image/png;base64,{avatar}" x="{ax}" y="{ay}" width="{size}" height="{size}" clip-path="url(#c)" preserveAspectRatio="xMidYMid slice"/>
<text class="k" x="{W - 36}" y="{h - 22}" text-anchor="end">ITAJUBÁ · MG</text>
</svg>
"""


STACK = [("Python", "python-original"), ("PHP", "php-original"),
         ("JavaScript", "javascript-original"), ("Java", "java-original"),
         ("MySQL", "mysql-original"), ("Django", "django-plain"),
         ("Pandas", "pandas-original"), ("Streamlit", "streamlit-original"),
         ("n8n", "n8n-original"), ("Git", "git-original"), ("GitHub", "github-original")]


def stack():
    """Faixa de ícones (devicon, MIT) embutidos: sem depender de CDN. Tema único, tiles claros."""
    import re
    tw, th, n = 64, 92, len(STACK)
    gap = (W - n * tw) / (n - 1)
    out = []
    for i, (label, fn) in enumerate(STACK):
        x = i * (tw + gap)
        svg = (ASSETS / "stack" / f"{fn}.svg").read_text(encoding="utf-8")
        svg = re.sub(r"^<\?xml[^>]*\?>\s*", "", svg)
        inner = re.sub(r"<svg[^>]*>", "", svg, count=1).replace("</svg>", "")
        out.append(
            f'<g transform="translate({x:.1f} 0)"><rect width="{tw}" height="{th}" rx="14" fill="#ECE9E2" stroke="#CFCBC3"/>'
            f'<svg x="12" y="12" width="40" height="40" viewBox="0 0 128 128">{inner}</svg>'
            f'<text x="{tw / 2}" y="76" text-anchor="middle" font-family="{MONO}" font-size="10.5" font-weight="600" fill="#111111">{label}</text></g>')
    names = ", ".join(l for l, _ in STACK)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {th}" width="{W}" height="{th}" role="img" '
            f'aria-label="Stack: {names}">{"".join(out)}</svg>\n')


def rel(days):
    if days <= 0:
        return "hoje"
    if days < 30:
        return f"há {days} d"
    if days < 365:
        return f"há {days // 30} {'mês' if days < 60 else 'meses'}"
    n = days // 365
    return f"há {n} {'ano' if n == 1 else 'anos'}"


def status(t, rows, today):
    rh, top = 46, 78
    h = top + rh * len(rows) + 22
    out = []
    for i, (label, stack, days) in enumerate(rows):
        y = top + i * rh
        fill = max(0.06, 1 - days / 365)
        out.append(f"""<text class="n" x="36" y="{y}">{esc(label)}</text>
<text class="s" x="36" y="{y + 18}">{esc(stack)}</text>
<rect x="400" y="{y - 10}" width="280" height="6" rx="3" fill="{t['rule']}"/>
<rect x="400" y="{y - 10}" width="{280 * fill:.0f}" height="6" rx="3" fill="{t['accent']}"/>
<text class="s" x="{W - 36}" y="{y}" text-anchor="end">{rel(days)}</text>""")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="Atividade recente nos repositórios, atualizada em {today:%d/%m/%Y}">
<style>
.k{{font:600 12px {MONO};letter-spacing:.14em;fill:{t['muted']}}}
.n{{font:600 17px {MONO};fill:{t['ink']}}}
.s{{font:400 14px {MONO};fill:{t['muted']}}}
</style>
<rect width="{W}" height="{h}" rx="20" fill="{t['bg']}"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="19.5" fill="none" stroke="{t['rule']}"/>
<text class="k" x="36" y="40">ATIVIDADE RECENTE</text>
<text class="k" x="{W - 36}" y="40" text-anchor="end">ATUALIZADO EM {today:%d/%m/%Y}</text>
<line x1="36" y1="54" x2="{W - 36}" y2="54" stroke="{t['rule']}"/>
{''.join(out)}
</svg>
"""


def fetch_pushed(owner, repo):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "perfil-build"})
    tok = os.environ.get("GITHUB_TOKEN")
    if tok:
        req.add_header("Authorization", f"Bearer {tok}")
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.load(r)["pushed_at"][:10]


def main():
    offline = "--offline" in sys.argv
    cfg = json.loads((ROOT / "data/projects.json").read_text())
    cache_path = ROOT / "data/activity.json"
    cache = json.loads(cache_path.read_text())
    today = dt.date.today()
    for p in cfg["projects"]:
        if offline:
            break
        try:
            cache[p["repo"]] = fetch_pushed(cfg["owner"], p["repo"])
        except Exception as e:  # falha segura: mantém o último valor conhecido
            print(f"aviso: {p['repo']}: {e}; usando cache", file=sys.stderr)
    rows = []
    for p in cfg["projects"]:
        d = dt.date.fromisoformat(cache[p["repo"]])
        rows.append((p["label"], p["stack"], (today - d).days))
    rows.sort(key=lambda r: r[2])
    cache_path.write_text(json.dumps(cache, indent=2, ensure_ascii=False) + "\n")
    for name, t in THEMES.items():
        (ASSETS / f"hero-{name}.svg").write_text(hero(t), encoding="utf-8")
        (ASSETS / f"status-{name}.svg").write_text(status(t, rows, today), encoding="utf-8")
    (ASSETS / "stack.svg").write_text(stack(), encoding="utf-8")
    print("ok")


if __name__ == "__main__":
    main()
