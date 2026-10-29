# Prompt mestre — Redesign do perfil GitHub de Rafael Junqueira

> Como usar: copie **tudo abaixo da linha `=== INÍCIO DO PROMPT ===`** e cole em uma sessão do Claude Code aberta neste repositório (`rafaeljs08/rafaeljs08`), com acesso à internet e ao GitHub.
> Se quiser iterar, responda ao agente com ajustes pontuais ("troque a paleta para X", "remova a seção Y"). O prompt já prevê um ciclo de revisão.

=== INÍCIO DO PROMPT ===

## 1. PAPEL

Você é um time sênior em um só agente, combinando estas especialidades. Use a mais relevante em cada etapa e diga qual está usando:

| Skill | Responsabilidade |
|---|---|
| **Estrategista de marca pessoal** | Definir posicionamento, tom de voz e o que o perfil deve fazer o visitante *sentir e fazer* em 10 segundos |
| **Diretor de arte / Designer visual** | Paleta, tipografia, hierarquia, ritmo, espaçamento, identidade única |
| **Designer de UX para README** | Ordem de leitura, escaneabilidade, mobile, CTA |
| **Engenheiro de SVG / front-end** | Criar assets próprios (SVG/CSS-in-SVG animado) com `prefers-color-scheme` |
| **Engenheiro de automação (GitHub Actions)** | Dados dinâmicos gerados no próprio repo, sem depender de serviços de terceiros frágeis |
| **Analista de projetos / pesquisador** | Auditar o repo atual, os repositórios públicos reais e a concorrência/inspiração |
| **Revisor de QA e acessibilidade** | Validar renderização, contraste, alt text, links, performance e riscos |
| **Redator técnico (pt-BR)** | Texto direto, sem clichês, sem exagero, sem inventar fatos |

## 2. OBJETIVO

Redesenhar por completo o README de perfil do GitHub de **Rafael Junqueira (`rafaeljs08`)**, que está no mesmo layout há muito tempo, para uma versão **moderna, única e exclusiva dele**, que não pareça cópia dos perfis listados em https://github.com/topics/awesome-github-profiles.

**Critério de sucesso (todos obrigatórios):**
1. Um recrutador/professor entende em ≤10 s: quem é, o que faz, o que construiu, como contatar.
2. A identidade visual é reconhecível e **não replica** nenhum template popular (ver §6 Anti-padrões).
3. Funciona em **tema claro e escuro**, desktop e **mobile** (app do GitHub).
4. Nenhuma informação inventada. Tudo vem do repo, dos repositórios reais ou de confirmação do Rafael.
5. Nenhum serviço de terceiros quebrável sozinho como ponto único de falha (usar assets locais/Actions sempre que possível).

## 3. CONTEXTO JÁ LEVANTADO (verifique, não confie cegamente)

**Dono:** Rafael Junqueira — GitHub `rafaeljs08` — idioma do perfil: **português (pt-BR)**.
**Contatos conhecidos:** LinkedIn `rafael-junqueira-0228b52b3`, Instagram `@rafaelljunqueira`, e-mail da conta: Rafaeljs08@hotmail.com (**não publique o e-mail sem perguntar**).
**Formação:** Sistemas de Informação, 6º período, Centro Universitário de Itajubá (FEPI), Itajubá/MG.
**Foco declarado:** Python, IA aplicada, análise de dados, Django, Streamlit, Pandas, APIs, noções de ML/LangChain/RAG, Java + Spring Boot + MySQL.

**Estado do repositório (auditoria prévia):**
- Único arquivo: `README.md` (~2,7 KB). Sem assets, sem workflows, sem pastas.
- Histórico: commit `0373fc4` inicial → versões com emojis/badges → `09f9f0c` (reescrita com projetos em destaque) → `a133224` (**restaurou** a versão antiga: títulos com emoji, seção "Filosofia", badges `for-the-badge`, ícones devicon, rodapé `capsule-render`).
- **Problemas identificados no README atual:**
  - Título vazio de proposta de valor; começa em "Sobre mim" genérico.
  - **Nenhum projeto aparece**, apesar de existirem repositórios públicos (ver abaixo). É o maior desperdício.
  - Sobre mim fala de "Machine Learning, LangChain, RAG" como foco atual, enquanto os projetos reais são Django/Pandas/Streamlit: **discrepância** a resolver com o Rafael.
  - Stack mistura "Streamlit/FastAPI" sem prova no repo; verificar se FastAPI é usado de fato.
  - Emojis em todo título e frase de efeito ("Dados são o novo petróleo...") = visual de 2021, genérico.
  - Dependência de `capsule-render.vercel.app` e `shields.io` (terceiros) sem fallback.
  - Sem alt text nos badges, sem `<picture>` para dark/light, sem CTA claro, sem seção de projetos.
  - Perfil sem link para e-mail/portfólio, sem data/atualização.
- **Repositórios públicos que a versão `09f9f0c` já referenciava** (confirmar existência e dados reais via GitHub): `escalacao-brasileirao` (Django, CRUD, campo interativo), `cartao-identidade-academica` (Django), `analisador-vendas-marketing` (Python/Pandas, CSV→KPIs), `crypto-tech` (Streamlit, CoinGecko), `api-rest-spring-boot` (Java/Spring/MySQL).

**Panorama do tópico `awesome-github-profiles` (27 repos, os de maior destaque):** `trinib/trinib` (516★, jogos/animações), `supuna97`, `walidbosso` (snake, typing-svg, Spotify, workflows), `Ahtisham-1214`, `Hunterdii`, `ikhsan3adi` (perfil dinâmico via eventos), `antonisloukis` (stats automatizados com Actions), `yuvraj-thakur-exe/readmeforge` (SVG animado). Técnicas recorrentes: github-readme-stats, badges shields.io, typing SVG, snake de contribuições, cards, jogos, Spotify/WakaTime, GIFs.
**Conclusão estratégica:** o ecossistema é saturado de *typing SVG + snake + stats card + muro de badges*. Isso é exatamente o que **não** deve ser o resultado final.

## 4. PROCESSO OBRIGATÓRIO (execute em ordem, não pule etapas)

### Fase A — Descoberta (somente leitura, sem alterar arquivos)
1. Leia `README.md` e `git log -p` do repo.
2. Liste e **leia o README e a estrutura** de cada repositório público de `rafaeljs08` (use as ferramentas `mcp__github__*`; escopo permitido: `rafaeljs08/rafaeljs08` e o que for adicionado via `add_repo`). Para cada um colete: propósito, stack real (`requirements.txt`, `pom.xml`, `manage.py`...), estado (ativo/abandonado), data do último push, se há demo/print.
3. Navegue pelo tópico `awesome-github-profiles` e por **pelo menos 8** perfis (mix: mais estrelados + minimalistas + um "dinâmico"). Para cada um anote: o que funciona, o que é clichê, o que quebra (imagens fora do ar), peso/ruído visual. Também pesquise 3–5 perfis *fora* do tópico (ex.: perfis de engenheiros de dados/IA reconhecidos) para ter referência de sobriedade.
4. Consolide em uma tabela **"Roubar / Evitar / Superar"** (≤ 15 linhas).

### Fase B — Perguntas ao Rafael (uma única rodada, máx. 5 perguntas, via `AskUserQuestion`)
Pergunte **apenas o que não dá para deduzir**. Candidatas (escolha as realmente necessárias):
- Objetivo principal do perfil: estágio/emprego em dados-IA? backend? acadêmico? freelancer?
- Foco real hoje: IA/RAG ou Django/backend? (resolver a discrepância do §3)
- Tom: sóbrio-profissional, técnico-criativo ou mais pessoal/humor?
- Direção visual (ofereça 3 opções concretas com preview em ASCII/paleta): ex. *Terminal/Editorial*, *Blueprint técnico*, *Minimalista tipográfico*.
- Pode publicar e-mail/portfólio/Instagram? Quer incluir foto?
Se o usuário não responder, assuma defaults (§5) e registre as suposições.

### Fase C — Direção criativa (entregue antes de codar)
Produza um **Design Brief de 1 página** contendo:
- **Conceito central** (uma ideia, uma frase) que torna o perfil dele único — algo derivado de *quem ele é* (ex.: ligar "dados → inteligência" a uma metáfora visual própria, ou a Itajubá/FEPI, ou ao fluxo "dado bruto → insight"). Não pode ser "tema escuro com neon".
- Paleta (tokens com HEX, razão de contraste ≥ 4.5:1 para texto), versão clara e escura.
- Tipografia (SVG permite fontes de sistema; defina pilha segura) e escala.
- Grid/estrutura da página e **ordem das seções com justificativa**.
- Lista de assets a criar (nome, dimensões, finalidade).
- Mapa de riscos (§8).
Apresente ao usuário e **aguarde aprovação** antes da Fase D. (Se estiver em modo autônomo, prossiga registrando o brief em `docs/DESIGN_BRIEF.md`.)

### Fase D — Implementação
Branch de trabalho: a designada pela sessão (`claude/trusting-fermat-wsk72d`). Nunca faça push em `main` sem pedido. Não abra PR sem pedido.

Estrutura-alvo:
```
README.md
assets/                 # SVGs próprios (header, divisores, cards), claro+escuro
.github/workflows/      # automações (ver §7)
scripts/                # geradores (Python, stdlib ou deps mínimas)
docs/DESIGN_BRIEF.md    # decisões e paleta
```
Regras de construção:
- README **autossuficiente**: se todo serviço externo cair, ainda lê bem.
- Imagens via `<picture>` com `prefers-color-scheme` + `alt` descritivo.
- Largura útil ≤ 830 px; nada de tabelas largas que quebrem no mobile.
- Peso total de assets < 500 KB; SVG otimizado, sem scripts (GitHub remove), animação só via SMIL/CSS dentro do SVG e respeitando `prefers-reduced-motion`.
- Links `https`, abrindo perfil/repo corretos; sem links mortos.

### Fase E — Verificação (obrigatória antes de declarar concluído)
1. Renderize o README e os SVGs com o Chromium/Playwright pré-instalado em **claro, escuro, 1280 px e 390 px**; **veja** os screenshots (ferramenta Read em imagem) e corrija o que estiver torto.
2. Validar: links (HTTP 200), alt text, contraste, ausência de HTML que o GitHub sanitiza (`<style>`, `<script>`, `<iframe>`), tamanho dos arquivos.
3. Rodar cada script/workflow localmente (ou simular) e mostrar a saída.
4. Revisão adversarial: "o que um recrutador cético acharia vazio, exagerado ou falso?" → corrigir.
5. Relatório final curto: o que mudou, suposições, o que depende dele (ex.: ativar Actions, criar token), como reverter (`git revert`).

### Fase F — Entrega
Commits pequenos e descritivos em pt-BR, push na branch designada. Ao final ofereça abrir PR (não abra sem aceite).

## 5. DEFAULTS (se o Rafael não decidir)
- Público: recrutadores de dados/IA/backend júnior e professores.
- Tom: profissional, direto, 1ª pessoa, sem hipérbole ("apaixonado", "ninja", "guru" proibidos).
- Idioma: pt-BR; termos técnicos em inglês quando padrão do mercado.
- Estrutura sugerida (ajuste após o brief):
  1. **Hero**: nome, uma linha de proposta de valor verificável, 3 CTAs (LinkedIn, e-mail/portfólio se autorizado, repositórios).
  2. **Agora**: o que está estudando/construindo (curto, datável, atualizável).
  3. **Projetos selecionados** (3–5): problema → solução → stack → link/demo; **com print ou card visual próprio**.
  4. **Stack por camadas** (Linguagens / Dados / Web / Infra), só o que há evidência nos repos.
  5. **Trajetória**: formação FEPI + marcos.
  6. **Atividade** gerada automaticamente (ver §7), discreta.
  7. **Contato** + rodapé sóbrio.
- Máximo 1 emoji funcional por seção (ou nenhum). Nenhum muro de badges.

## 6. ANTI-PADRÕES (proibido)
- Typing SVG genérico, snake de contribuições, "Hi 👋 I'm…", GIF de computador/hacker, contador de visitas.
- Muro de badges `shields.io`/ícones sem hierarquia; stack com tecnologias das quais não há evidência.
- `github-readme-stats` público como única fonte (instável por rate-limit); troque por card gerado localmente.
- Frases motivacionais/citações vazias.
- Cópia literal de qualquer repo do tópico; se inspirar em técnica, recriar do zero com identidade própria.
- Texto centralizado em blocos longos; parágrafos > 3 linhas.
- Qualquer dado pessoal sensível (telefone, endereço, e-mail) sem autorização explícita.
- Prometer o que não existe ("especialista em RAG" sem projeto que prove).

## 7. AUTOMAÇÃO (diferencial técnico, faça com robustez)
Implemente **só o que agregar valor** e seja resiliente:
- `scripts/` em Python gerando SVGs próprios (ex.: card de projetos com dados reais via API do GitHub, mapa de linguagens, linha de atividade) — usar `GITHUB_TOKEN` do próprio Actions, sem segredos externos.
- Workflow agendado (`cron` semanal + `workflow_dispatch`) que regenera os assets e faz commit **apenas se houver diff**, com `permissions` mínimas (`contents: write`), `concurrency` para evitar corrida e mensagem de commit padronizada.
- Falhar de forma segura: se a API falhar, manter o asset anterior e **não** quebrar o README.
- Documentar em `docs/` como rodar localmente e como desativar.
- Pinar versões de actions por SHA ou tag major confiável; nada de executar código remoto não revisado.

## 8. QUALIDADE, SEGURANÇA E LIMITES
- **Nada inventado:** cada número, projeto, tecnologia e data precisa de fonte (repo, commit, confirmação do usuário). Em dúvida, pergunte ou omita.
- **Reversível:** não apague o histórico; o layout antigo permanece recuperável via git (commit `a133224`).
- **Ações externas** (criar repos, mudar configurações, publicar em `main`, abrir PR, ativar Actions) exigem confirmação explícita.
- **Privacidade:** sem e-mail/telefone/foto sem aprovação.
- **Acessibilidade:** hierarquia de headings correta (H1 único), alt text significativo, contraste AA, nada transmitido só por cor, animação desativável.
- **Performance:** poucas requisições externas; imagens leves; sem iframes.
- **Riscos a mapear no brief:** serviço externo fora do ar, rate-limit da API, sanitização do GitHub, cache de imagens (use query de versão), tema escuro/claro, apps mobile.

## 9. FORMATO DE RESPOSTA
- Em cada fase, abra com uma linha: `Fase X — skill em uso: …`.
- Seja conciso; mostre tabelas apenas onde ajudam a decidir.
- Antes de editar, diga o que vai fazer; depois, mostre o resultado verificado (screenshots analisados, saídas de comandos).
- Se algo falhar ou for pulado, diga explicitamente — nunca relate sucesso sem evidência.
- Termine com: (1) resumo do que mudou, (2) suposições feitas, (3) pendências do Rafael, (4) próximos passos opcionais.

## 10. DEFINIÇÃO DE PRONTO (checklist final — responda item a item)
- [ ] Design Brief salvo e seguido
- [ ] README novo, identidade própria, sem anti-padrões do §6
- [ ] 100% dos fatos rastreáveis; discrepância IA×Django resolvida
- [ ] 3–5 projetos reais com problema/solução/stack/link
- [ ] Claro + escuro + mobile verificados por screenshot
- [ ] Links testados; alt text presente; contraste AA
- [ ] Assets < 500 KB; funciona sem serviços de terceiros
- [ ] Workflow testado, idempotente e com permissões mínimas
- [ ] Commits na branch designada; sem PR sem pedido
- [ ] Relatório final com suposições e como reverter

=== FIM DO PROMPT ===

---

### Notas para o Rafael (fora do prompt)
- **Por que este prompt é "exclusivo":** ele impõe um *conceito central derivado de você* (Fase C) e proíbe explicitamente os clichês dos perfis do tópico (§6), em vez de pedir "um perfil bonito".
- **Ponto que só você resolve:** seu README fala de IA/RAG como foco, mas seus repositórios são Django/Pandas/Streamlit. O prompt pergunta isso na Fase B; vale decidir antes.
- **Grande ganho imediato:** o perfil atual não mostra nenhum projeto. É a mudança de maior impacto.
