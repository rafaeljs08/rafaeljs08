# Contexto para sessões futuras

Notas salvas a pedido de Rafael para reaproveitar em redesigns, portfólio ou currículo. Nada aqui é sensível além do que ele autorizou publicar.

## Preferências decididas (29/10/2026)
- Objetivo do perfil: estágio/emprego em **dados e IA**.
- Visual: **editorial monocromático**, um único acento de cor.
- Imagens: só o **avatar ilustrado** (`assets/avatar.png`). **Fotos reais não vão para repositório público.**
- Autorizado a publicar: e-mail, LinkedIn, Instagram, cidade (Itajubá/MG).

## Identidade visual
- Avatar: ilustração vetorial com contorno preto, fundo cinza claro, cabelo curto, brinco de argola, camiseta preta de gola redonda, olhar para cima e para a direita.
- Fotos de referência (não salvas no repositório): selfie de frente com porta de madeira ao fundo; selfie de espelho em elevador, camiseta preta, colar e pulseira prateados.

## Repositórios e discrepâncias a revisar
- `escalacao-brasileirao` é em dupla (com Vitor Faria de Oliveira e Silva).
- READMEs de `crypto-tech`, `api-rest-spring-boot`, `analisador-vendas-marketing` e `escalacao-brasileirao` corrigidos em 04/11/2026 (branch `claude/corrige-readme` em cada um; ver PRs).
- `api-rest-spring-boot` é a API `parcelamentos` (Java 21, Spring Boot 3.5.5, Flyway, MySQL); só o CRUD de clientes existe, `Parcelamento` é esqueleto.
- `escalacao-brasileirao`: o código (`seed_brasileirao.py`) ainda cria `admin`/`admin` e redefine a senha a cada execução; o README agora avisa. Trocar o seed por variável de ambiente seria o ideal.
- `analisador-vendas-marketing`: `src/ai_report.py` termina com `print("API KEY:", os.getenv("OPENAI_API_KEY"))`, que imprime a chave da OpenAI. Remover essa linha.
- `Game_Vault`: Django em dupla (Vitor Faria de Oliveira e Silva e Rafael); README ainda aponta clone/CI para `VitorFos11/GameVault`.
- `ProLobby.com` é um **espelho automático** (workflow `mirror-upstream`, a cada 30 min) de `ljborgess/ProLobby.com`: matchmaking competitivo e identidade verificada para EA FC Pro Clubs (Next.js, NestJS, PostgreSQL, discord.js), em desenvolvimento, em equipe. Rafael disse que **contribui** no projeto. O README do projeto diz "Projeto privado. Todos os direitos reservados aos sócios", e o espelho está público: confirmar com os sócios.
- Há também um repositório `portfolio` (só um README e uma pasta `formulario`) e `proj_DJANGO` (privado).

## Currículo (recebido em 29/10/2026)
- Rafael Junqueira de Souza. Estagiário de Desenvolvimento Full Stack na Support Informática desde 03/2026 (sistemas web de gestão hospitalar e clínica; PHP, JavaScript, MySQL, APIs REST, procedures, relatórios/BI).
- Habilidades: PHP, Python, JavaScript, Java (básico); MySQL; APIs REST, HTML, CSS; LangChain, n8n, Streamlit, ChatGPT, Copilot Studio; Git, GitHub.
- Formação: Sistemas de Informação, FEPI, 2024–2027. Inglês intermediário. Cursos na Alura (RAG/LangChain, n8n, Copilot Studio, IA, Python, marketing).
- **Telefone e nomes de clientes do estágio não vão para o perfil público.**

## Pendências
- Período confirmado por Rafael em 29/10/2026: **6º**. O currículo em PDF ainda diz 5º e precisa ser atualizado por ele.
