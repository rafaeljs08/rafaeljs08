# Design brief — perfil rafaeljs08

**Objetivo:** estágio/emprego em dados e IA. Público: recrutadores e professores.
**Direção:** editorial monocromático (escolhida por Rafael).

**Conceito:** *dados brutos → decisões claras*. Uma grade de pontos que diminui até virar o retrato (o avatar ilustrado). A ideia nasce do próprio perfil: dados que viram algo legível.

## Paleta (tokens em `scripts/build.py`)

| Token | Claro | Escuro |
|---|---|---|
| Fundo | `#F4F2EE` | `#0E0E0F` |
| Texto | `#111111` | `#EDEBE6` |
| Texto secundário | `#5F5E59` | `#A09E97` |
| Linhas | `#CFCBC3` | `#2C2C2E` |
| Acento (único) | `#C2410C` | `#FF8A57` |

Texto secundário e acento têm contraste ≥ 4.5:1 sobre o fundo de cada tema.

## Tipografia
Títulos: Georgia (serifa, itálico no acento). Detalhes: monoespaçada do sistema. Sem fontes externas.

## Estrutura
Hero → resumo e links → Agora → Projetos (problema → solução → stack) → atividade → Stack → Formação → Contato.

## Decisões
- Sem emojis, badges, typing SVG, snake ou stats card de terceiros.
- Stack só com tecnologias que aparecem nos repositórios ou foram declaradas por Rafael.
- Painel de atividade gerado localmente por `scripts/build.py`; com falha da API mantém o cache (`data/activity.json`).
- Fotos reais não são publicadas; só o avatar ilustrado (`assets/avatar.png`).
- Animação (pulso dos pontos) respeita `prefers-reduced-motion`.

## Como reverter
O layout anterior está no commit `a133224` (`git checkout a133224 -- README.md`).
