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
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {h}" width="{W}" height="{h}" role="img" aria-label="Rafael Junqueira — dados brutos, decisões claras">
<style>
.k{{font:600 12px {MONO};letter-spacing:.14em;fill:{t['muted']}}}
.h{{font:400 52px/1 {SERIF};fill:{t['ink']};letter-spacing:-.02em}}
.a{{font-style:italic;fill:{t['accent']}}}
.d{{fill:{t['dot']};opacity:.85;animation:p 3.6s ease-in-out infinite}}
@keyframes p{{0%,100%{{opacity:.25}}50%{{opacity:.9}}}}
@media (prefers-reduced-motion:reduce){{.d{{animation:none;opacity:.7}}}}
</style>
<rect width="{W}" height="{h}" rx="20" fill="{t['bg']}"/>
<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="19.5" fill="none" stroke="{t['rule']}"/>
<text class="k" x="36" y="52">RAFAEL JUNQUEIRA · SISTEMAS DE INFORMAÇÃO</text>
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
    print("ok")


if __name__ == "__main__":
    main()
