# Design brief — perfil rafaeljs08

**Objetivo:** estágio/emprego em dados e IA. Público: recrutadores e professores.
**Direção:** editorial monocromático (escolhida por Rafael), com acento que alterna entre azul e verde (também escolha dele).

**Conceito:** *dados brutos → decisões claras*. Uma grade de pontos que diminui até virar o retrato (o avatar ilustrado). A ideia nasce do próprio perfil: dados que viram algo legível.

## Paleta (tokens em `scripts/build.py`)

| Token | Claro | Escuro |
|---|---|---|
| Fundo | `#F4F2EE` | `#0E0E0F` |
| Texto | `#111111` | `#EDEBE6` |
| Texto secundário | `#5F5E59` | `#A09E97` |
| Linhas | `#CFCBC3` | `#2C2C2E` |
| Acento: azul | `#1D4ED8` | `#60A5FA` |
| Acento: verde | `#047857` | `#34D399` |

Texto secundário e os dois tons do acento têm contraste ≥ 4.5:1 sobre o fundo de cada tema.

**Acento animado, com economia:** o único destaque alterna entre o azul e o verde em ciclo lento de 12 s (`.ac`, em `scripts/build.py`). Filosofia em `docs/DESIGN_PHILOSOPHY.md` ("Sinal Único") e prancha de referência em `docs/prancha-sinal-unico.png`: um acento só vale enquanto é escasso. Onde ele aparece:

- "decisões claras." (hero) e "com aplicação prática." (Sobre), as duas frases-assinatura;
- cursor e régua curta do hero;
- ícone dos botões de contato;
- traço curto sob cada título de seção;
- barras dos projetos atualizados há até 45 dias (as demais ficam cinza).

Todo o resto (textos, bordas, grade de pontos, moldura do avatar, tiles da stack) fica em tinta e cinza. Com movimento reduzido o acento fica fixo no azul.

**Títulos das seções:** imagens geradas por `scripts/build.py` (`assets/h-*.svg`) dentro de um `<h2>` com `alt`. **Cache:** o build grava em cada imagem do README um `?v=<hash>`, para o GitHub redesenhar quando o arquivo muda.

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
