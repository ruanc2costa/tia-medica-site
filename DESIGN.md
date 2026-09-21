---
# PROPOSTA EXPERIMENTAL — sujeita à aprovação do fundador · 2026-09-20 · branch exp/home-redesign · NÃO publicada · não substitui nada até ser aprovada
name: "Tia Médica — home experimental “As duas pontas do fio”"
description: "Proposta experimental (2026-09-20, branch exp/home-redesign, não publicada): a home como um fio com duas pontas — o celular de quem toma o remédio e o celular de quem cuida."
colors:
  paper: "oklch(97.6% 0.008 80)"
  paper-2: "oklch(95.3% 0.012 80)"
  surface: "oklch(99.4% 0.005 80)"
  rule: "oklch(92.5% 0.018 80)"
  rule-2: "oklch(88% 0.02 80)"
  ink: "oklch(36.5% 0.045 218)"
  ink-deep: "oklch(30% 0.045 218)"
  ink-2: "oklch(48% 0.04 212)"
  accent: "oklch(68% 0.16 38)"
  accent-ink: "oklch(58.5% 0.15 36)"
  call: "oklch(53% 0.15 36)"
  call-deep: "oklch(47% 0.14 36)"
  accent-soft: "oklch(93% 0.03 40)"
  focus: "oklch(53% 0.15 36)"
  teal: "oklch(55% 0.095 180)"
  teal-ink: "oklch(48% 0.085 182)"
  teal-layer: "oklch(88.5% 0.04 188)"
  teal-thread: "oklch(80% 0.055 190)"
  lilac-ink: "oklch(48% 0.2 292)"
  lilac-soft: "oklch(94% 0.03 300)"
  lilac-layer: "oklch(87.5% 0.06 298)"
  wpp-bg: "oklch(92% 0.012 80)"
  wpp-bubble: "oklch(95% 0.06 130)"
  wpp-tick: "oklch(50% 0.13 235)"
typography:
  display:
    fontFamily: "Fraunces, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(2.125rem, 2.6vw + 1.3rem, 3.5rem)"
    fontWeight: 600
    lineHeight: 1.06
    letterSpacing: "-0.02em"
  headline:
    fontFamily: "Fraunces, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(2rem, 2.4vw + 1.2rem, 3rem)"
    fontWeight: 540
    lineHeight: 1.1
    letterSpacing: "-0.012em"
  title:
    fontFamily: "Fraunces, Iowan Old Style, Georgia, serif"
    fontSize: "1.75rem"
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: "-0.012em"
  title-lg:
    fontFamily: "Fraunces, Iowan Old Style, Georgia, serif"
    fontSize: "clamp(1.75rem, 1.6vw + 1.2rem, 2.5rem)"
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: "-0.012em"
  pull:
    fontFamily: "Fraunces, Iowan Old Style, Georgia, serif"
    fontSize: "1.4375rem"
    fontWeight: 500
    lineHeight: 1.3
  body:
    fontFamily: "Nunito, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 600
    lineHeight: 1.6
  lede:
    fontFamily: "Nunito, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 600
    lineHeight: 1.55
  fine:
    fontFamily: "Nunito, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "0.9375rem"
    fontWeight: 600
    lineHeight: 1.5
  label:
    fontFamily: "Nunito, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "1rem"
    fontWeight: 800
    lineHeight: 1.1
  price:
    fontFamily: "Nunito, Segoe UI, system-ui, -apple-system, sans-serif"
    fontSize: "1.75rem"
    fontWeight: 800
    lineHeight: 1.15
    fontFeature: "tabular-nums lining-nums"
  time:
    fontFamily: "JetBrains Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: "1.0625rem"
    fontWeight: 700
    letterSpacing: "-0.01em"
    fontFeature: "tabular-nums"
rounded:
  icon: "16px"
  card: "20px"
  pill: "999px"
spacing:
  2xs: "0.25rem"
  xs: "0.5rem"
  sm: "0.75rem"
  md: "1rem"
  lg: "1.5rem"
  xl: "2.5rem"
  2xl: "4rem"
  section: "clamp(4rem, 7vw, 7rem)"
  page-gutter: "clamp(1.125rem, 4vw, 3rem)"
  layer: "10px"
components:
  button-primary:
    backgroundColor: "{colors.call}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.7em 1.5em"
    height: "52px"
  button-primary-hover:
    backgroundColor: "{colors.call-deep}"
  button-primary-lg:
    backgroundColor: "{colors.call}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "0.75em 1.7em 0.75em 1.35em"
    height: "60px"
  button-primary-nav:
    backgroundColor: "{colors.call}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "0.5em 1.15em 0.5em 0.95em"
    height: "46px"
  chip:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.6em 1.3em"
    height: "48px"
  chip-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
  link:
    textColor: "{colors.ink}"
    padding: "0.5em 0 0.3em"
  link-hover:
    textColor: "{colors.call}"
  status-live:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    padding: "0.1em 0.8em"
  status-pilot:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.call-deep}"
    rounded: "{rounded.pill}"
    padding: "0.1em 0.8em"
  status-plan:
    backgroundColor: "transparent"
    textColor: "{colors.ink-2}"
    rounded: "{rounded.pill}"
    padding: "0.1em 0.8em"
  reply:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: "0.45em 1.1em"
    height: "44px"
  reply-hover:
    backgroundColor: "{colors.teal-ink}"
    textColor: "{colors.paper}"
  chat-card:
    backgroundColor: "{colors.wpp-bg}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
  chat-message:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "14px"
    padding: "0.5em 0.8em 0.35em"
  chat-message-sent:
    backgroundColor: "{colors.wpp-bubble}"
    textColor: "{colors.ink}"
  hour-pill:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.time}"
    rounded: "{rounded.pill}"
    padding: "0.3em 0.9em 0.3em 0.75em"
  hour-pill-caregiver:
    backgroundColor: "{colors.lilac-soft}"
    textColor: "{colors.ink}"
  sheet:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.card}"
    padding: "clamp(1.25rem, 3vw, 2.25rem)"
  aside-note:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.icon}"
    padding: "1rem 1.5rem"
---

# Design System: Tia Médica — home experimental “As duas pontas do fio”

> **PROPOSTA EXPERIMENTAL — sujeita à aprovação do fundador.**
> Data: **2026-09-20**. Vive só na branch **`exp/home-redesign`**. **Não está publicada nem implantada.** **Não substitui nada** — nem o site em produção, nem os documentos da marca — até ser aprovada. Direção: **“As duas pontas do fio”**.
>
> Este documento foi escrito **depois** da construção, a partir do que está em `index.html`, `assets/tia.css` (bloco `:root`) e `assets/tia.js`. Onde o plano e o código divergem, vale o código, e a divergência está anotada. Os tokens do cabeçalho YAML são normativos e estão em OKLCH, o formato em que foram entregues; a prosa não repete os valores.
>
> O documento separa três camadas: **A — o que a marca já tinha decidido** e esta versão só preserva; **B — o que esta versão propõe de novo**, com o motivo de cada mudança; **C — conflitos e pendências**, registrados e não resolvidos. As três estão na seção “Camadas de decisão”, depois das seções canônicas.

## Overview

**Creative North Star: "As duas pontas do fio"**

A home é um fio com duas pontas: a cozinha dela às oito da manhã e o celular de quem cuida. Tudo o que a página demonstra é uma confirmação viajando de uma ponta à outra — o lembrete chega, ela responde “já tomei”, fica registrado, e quem cuida fica sabendo. O produto é a conversa, então a conversa é a demonstração: não há moldura de celular, não há captura de tela, há cartões de conversa de verdade, em HTML, ligados por um fio trançado.

O tom é o da marca — acolhedora, precisa, honesta — levado para uma página sóbria: papel creme, tinta azul-petróleo, uma afirmação em Fraunces itálico por seção, e o coral guardado para o que chama. A densidade é de carta, não de painel: uma coluna de leitura, bastante respiro, e as partes “de contrato” (limites, ofertas, dúvidas) sem decoração nenhuma, porque o fundador pediu menos ornamento. O fio aparece onde há demonstração e some onde há contrato.

A página recusa o arranjo padrão da categoria — título centralizado, três cartões de recurso, cartões de preço — e recusa também a versão anterior do site, sem rosto e de natureza-morta. Nada de adesão virando gráfico, nada de alarme, nada de promessa maior que o produto.

**Key Characteristics:**
- Papel creme com faixas wash alternadas; nunca branco puro como fundo de página.
- Um só fio trançado (coral + tinta + teal claro) como espinha da demonstração; ausente em limites, ofertas e dúvidas.
- Cartões de conversa com uma segunda folha deslocada — teal na ponta dela, lilás na ponta de quem cuida.
- Coral em três degraus: grafismo, palavra grande, chamada. O degrau certo depende do tamanho do texto.
- Horas em mono presas ao fio; preço nunca em mono.
- Status dito com pílulas: hoje a página usa **Em piloto** e **Em breve**; **Disponível** (tinta cheia) fica reservada para quando uma oferta paga entrar no ar.
- Completa sem JavaScript e parada, inteira, com movimento reduzido.

## Colors

Uma paleta de papel e tinta com um único chamado quente; teal e lilás não são acentos livres, são significados.

### Primary
- **Coral de Chamada** (`call`): a ação primária (todas as pílulas “Falar com a Tia”), o coral em texto pequeno, os marcadores de estrela, os ícones de nota, o sinal do acordeão e o anel de foco (`focus` aponta para o mesmo valor). Mede 5,3:1 sobre o papel.
- **Coral de Chamada Profundo** (`call-deep`): hover da ação primária, texto da pílula “Em piloto” e a frase de apoio sobre a faixa coral-leite (5,9:1 sobre `accent-soft`).
- **Coral da Marca** (`accent`): só grafismo — um dos três fios da trança, o pulso que percorre o fio, o sublinhado de 2px dos links, o coração do compromisso. Mede 2,9:1 sobre o papel: nunca é cor de texto.
- **Coral de Palavra** (`accent-ink`): a palavra em destaque dentro do H1 (“ela tomou”). 4,2:1 — só em corpo grande de display.
- **Coral Leite** (`accent-soft`): faixa do compromisso, fundo da pílula “Em piloto”, bloco de aviso de urgência, cor de seleção de texto.

### Secondary
- **Teal do Registro** (`teal`, `teal-ink`): o que ficou confirmado e registrado — o contorno das respostas rápidas (“Já tomei”), o check da lista “A Tia faz”. `teal-ink` é o degrau para ícone e preenchimento em hover (6,1:1 sobre a superfície).
- **Teal de Folha** (`teal-layer`): a segunda folha atrás do cartão de conversa dela.
- **Teal de Fio** (`teal-thread`): o terceiro fio da trança. Só existe dentro do fio.

### Tertiary
- **Lilás de Quem Cuida** (`lilac-ink`, `lilac-soft`, `lilac-layer`): exclusivamente a ponta do cuidador — o rótulo “No seu celular”, a segunda folha do cartão dele, a pílula de hora das 08:31, os três passos do combinado, o halo da mensagem que pousa. `lilac-ink` mede 6,7:1 no papel e 6,0:1 sobre `lilac-soft`.

### Neutral
- **Papel Creme** (`paper`): fundo da página, texto sobre tinta e sobre coral de chamada.
- **Papel Wash** (`paper-2`): faixas alternadas (tese, limites, fechamento) e fundo da placa da personagem.
- **Superfície** (`surface`): o que sobe — cabeçalho e balões da conversa, a folha de limites, anéis de avatar.
- **Linha** (`rule`) e **Linha Forte** (`rule-2`): divisores de 1px, contorno interno das pílulas de hora e da pílula “Em breve”.
- **Tinta Azul-Petróleo** (`ink`): todo título e texto principal (9,8:1), o traço escuro da trança, o preenchimento de “Disponível”, o contorno do chip. **Tinta Profunda** (`ink-deep`) só no título do compromisso e na seleção.
- **Tinta 2** (`ink-2`): texto de apoio, ledes, legendas, ícone de recusa. 6,0:1 no papel, 5,6:1 no wash, 5,1:1 no fundo da conversa.
- **WhatsApp literal** (`wpp-bg`, `wpp-bubble`, `wpp-tick`): fundo greige do corpo da conversa, balão verde-claro de quem envia, tique azul de lido. Só dentro do cartão de conversa.

### Named Rules
**A Regra dos Três Corais.** O coral da marca não é cor de texto: mede 2,9:1 no creme e falha até como texto grande. Grafismo usa `accent`; palavra de display usa `accent-ink`; ação e qualquer coral pequeno usam `call`. Escolhe-se o degrau pelo tamanho, nunca pelo gosto.

**A Regra da Cor com Dono.** Teal quer dizer “registrado”. Lilás quer dizer “quem cuida”. Nenhum dos dois decora. Se a peça não fala de confirmação, não tem teal; se não fala do cuidador, não tem lilás.

**A Regra do Verde Emprestado.** O verde e o azul do WhatsApp só existem dentro de um cartão de conversa, como representação literal da interface. Fora dele, não são cores do sistema.

**A Regra Sem Vermelho.** Não existe vermelho, nem para urgência. Urgência é dita com palavra (UPA, SAMU 192) sobre coral-leite e tinta.

## Typography

**Display Font:** Fraunces itálico, eixo óptico automático (com Iowan Old Style, Georgia)
**Body Font:** Nunito (com Segoe UI, system-ui)
**Label/Mono Font:** JetBrains Mono — só para hora

**Character:** Uma serifa itálica de letreiro, leve e conversada, sobre uma sans redonda e firme. A itálica afirma; a Nunito explica; a mono marca a hora e mais nada.

### Hierarchy
- **Display** (600, `clamp(2.125rem → 3.5rem)`, 1.06, -0.02em): o H1 do hero e o título do compromisso. Medida curta, 13–17ch.
- **Headline** (540, `clamp(2rem → 3rem)`, 1.1): um H2 por seção — uma afirmação inteira, com ponto final. 17–24ch.
- **Title** (600, 1.75rem; variante grande `clamp(1.75rem → 2.5rem)`): H3 dos momentos do dia, nomes das ofertas, pergunta do acordeão (1.4375rem).
- **Pull** (500, 1.4375rem–2.5rem, 1.15–1.3): frases de corte — “Cuidar sem vigiar.”, “É nesse intervalo que a Tia trabalha.”, a assinatura do rodapé. O peso mais leve do sistema.
- **Body** (600, 1.125rem / 18px, 1.6): texto corrido, 52–62ch. **Lede** (600, 1.25rem, 1.55, até 54ch) abre seção.
- **Label** (800, 1rem, 1.1): botões, chips, respostas rápidas, links de navegação (1.0625rem). Textos de apoio descem a 1rem e 0.9375rem; pílulas de status e rótulos de hora usam 0.875rem em 800.
- **Price** (Nunito 800, algarismos tabulares e alinhados, 1.75rem–2.5rem): todo valor em reais.
- **Time** (JetBrains Mono 700, tabular, -0.01em, 0.9375–1.0625rem): a hora nas pílulas presas ao fio; peso 500 no carimbo de hora dentro do balão.

### Named Rules
**A Regra da Hora em Mono.** JetBrains Mono escreve hora e o número do passo no combinado — nada mais. Preço em mono é proibido: o zero cortado faz “R$ 0” ler como “R$ Ø”.

**A Regra do Itálico Leve.** Fraunces sempre itálico, sempre com eixo óptico automático, nunca acima de 600. H1 e H3 em 600, H2 em 540, frase de corte em 500. Se o título parece impresso em negrito, está errado.

**A Regra dos Dezoito.** O corpo é 18px com peso 600. O público inclui quem tem 55–85 anos; texto de leitura não desce disso.

## Layout

Uma coluna central de 72rem com calha fluida (`page-gutter`), seções separadas por `section` e alternando papel e wash. Não há grade de cartões em lugar nenhum: as seções se organizam em pares assimétricos de colunas (5/7, 6/6, 4/8, 8/4, 7/5) que colapsam para uma coluna abaixo de 60rem. Os espaçamentos internos seguem a escala `2xs`–`2xl`; a distância entre momentos do dia é `2xl` (4.5rem no desktop).

**Hero.** A partir de 72rem: texto em 5/12, palco em 7/12 (até 40rem). O palco é uma grade de 12 colunas em que a placa da personagem (4:5) ocupa as colunas 6–12 e os dois cartões de conversa se sobrepõem à borda esquerda dela, empilhados em diagonal e ligados por uma travessia do fio com a hora montada. Abaixo de 72rem vira uma coluna; abaixo de 40rem a ordem é: título, lede, ação, status, **conversa, e só então o retrato** — pequeno (6.5rem), ao lado do aparte “Cuida do seu pai…”, como quem assina. A ação primária ocupa a largura inteira.

**Um dia com a Tia.** Lista ordenada com o fio vertical de 28px. No celular o fio corre à esquerda e as pílulas de hora sentam sobre ele; a partir de 60rem o fio vai para o centro, a hora vira um bloco de 9rem no eixo e texto e conversa alternam de lado a cada momento. Dois nós de tinta fecham as pontas.

**Ofertas.** Livro-razão: uma régua de tinta de 2px em cima, linhas de 1px entre ofertas, e no desktop quatro colunas — status, nome e preço, descrição, ação. A primeira oferta (a gratuita) tem nome e preço um degrau acima.

**Navegação e dock.** Barra fixa de 72px (64px abaixo de 60rem) com papel a 94% e desfoque; a borda inferior só aparece depois de rolar. Abaixo de 60rem os links viram painel sob a barra e, depois do hero, uma dock inferior traz a ação — enquanto ela está visível, a ação da barra some (uma ação por tela). O rodapé reserva 4rem extras para a dock.

Pontos de quebra observados: 26rem, 40rem, 48rem, 60rem, 72rem.

## Elevation & Depth

Híbrido contido. A profundidade principal é tonal — creme respira, superfície eleva, wash separa — e há três sombras, todas feitas de tinta diluída. A única profundidade “dura” é a segunda folha dos cartões de conversa, que é papel colorido, não sombra.

### Shadow Vocabulary
- **Sussurro** (`box-shadow: 0 1px 2px oklch(36.5% 0.045 218 / 0.07)`): balões, rótulo do celular, avatar pousado, placa no celular, botão pressionado.
- **Suave** (`box-shadow: 0 10px 30px oklch(36.5% 0.045 218 / 0.06)`): ação primária em repouso, placa da personagem, folha de limites, avatar do fechamento.
- **Média** (`box-shadow: 0 16px 34px oklch(36.5% 0.045 218 / 0.1)`): cartão de conversa, hover da ação primária, painel do menu no celular.
- **Segunda folha** (`box-shadow: 10px 10px 0 <teal-layer | lilac-layer>`, somada à Média): deslocamento fixo de `layer`, sem desfoque, para baixo e para a direita.

### Named Rules
**A Regra da Sombra de Tinta.** Toda sombra é a tinta azul-petróleo diluída (6–10%). Preto puro não existe — nem em texto, nem em sombra.

**A Regra da Segunda Folha.** A folha deslocada pertence só ao cartão de conversa. Não vai em botão, em cartão de oferta, em imagem, em folha de limites. Teal na ponta dela, lilás na ponta de quem cuida, sempre 10px.

## Shapes

Três raios e nenhum canto vivo: `pill` para tudo o que se toca ou rotula (ações, chips, respostas, status, pílulas de hora, passos do combinado); `card` para o que contém (cartão de conversa, placa, folha de limites); `icon` para blocos pequenos (aviso de urgência, bloco de hora no desktop). Os balões usam 14px com um canto de 4px do lado de quem fala — forma literal do WhatsApp, só dentro da conversa. Avatares são círculos com anel de superfície (3–4px).

Contornos são internos (`inset 0 0 0 1.5px` para rótulos, `2px` para chip e resposta), nunca `border` que altere a caixa. Divisores são linhas de 1px; a única linha grossa é a régua de 2px que abre o livro-razão.

O fio trançado é a geometria recorrente: três traços de 3,5px (coral, tinta, teal claro) num módulo de 28 × 64, com um trecho de tinta repetido por cima para o fio passar “por baixo e por cima”. É desenhado uma vez (padrão SVG no HTML, vertical e horizontal) e como arte autoral em `assets/fio/` (travessia larga e estreita do hero, coração do compromisso).

Ícones são um conjunto próprio de traço único em `assets/icones/` (check, checks, recusa, seta, seta-baixo, cadeado, telefone, estrela), aplicados como máscara CSS e pintados pela cor do contexto. Emoji só dentro das mensagens da conversa.

### Named Rules
**A Regra de Onde o Fio Vive.** O fio aparece em cinco lugares: a travessia entre os dois celulares, a linha “consulta — consulta” da tese, a linha do tempo do dia, o coração do compromisso e a chegada até a Tia no fechamento. Limites, ofertas, dúvidas, clínicas e rodapé ficam sem fio, de propósito.

## Components

### Buttons
Pílulas firmes e quentes; afundam 1px ao toque.
- **Shape:** pílula (999px).
- **Primary:** fundo `call`, texto `paper`, Nunito 800, altura mínima 52px (60px na versão grande do hero e do fechamento, 46px na barra e na dock), sombra Suave; ícone de balão em traço de 1,8.
- **Hover / Focus:** fundo `call-deep` e sombra Média em 220ms com ease-out exponencial; ativo desce 1px e cai para Sussurro; foco com anel de 3px `focus`, afastado 3px.
- **Chip (secundário):** transparente, contorno interno de 2px em tinta, 48px; hover inverte para tinta cheia. Usado para ações por e-mail (lista de espera, aviso, parceria).
- **Link sublinhado (terciário):** Nunito 800 em tinta com sublinhado de 2px em `accent`; hover leva texto e linha a `call`; seta do conjunto próprio desliza 3px.

### Chips
- **Pílula de status:** 0.875rem, 800, altura mínima 1.9em. **Disponível** = tinta cheia com texto papel. **Em piloto** = coral-leite com texto `call-deep`. **Em breve** = transparente, texto `ink-2`, contorno interno de 1,5px. É o mesmo vocabulário no hero, na legenda e no livro-razão; quanto menos existe, menos tinta recebe.
- **Pílula de hora:** papel com contorno interno de 1,5px, hora em mono + rótulo em Nunito 800 (“todo dia”, “primeiro dia”); sentada sobre o fio. Na ponta de quem cuida, fundo `lilac-soft` e contorno `lilac-layer`. No desktop vira bloco de raio 16px, centralizado no eixo.
- **Resposta rápida:** superfície com contorno interno de 2px teal, 44px; hover preenche com `teal-ink`; desabilitada a 50% enquanto a Tia “digita”.
- **Passo do combinado:** pílula `lilac-soft` com o número em mono lilás.

### Cards / Containers
- **Cartão de conversa:** raio 20px, corpo em `wpp-bg`, cabeçalho em superfície com avatar de 40px, nome e estado; balões de superfície (recebidos) e `wpp-bubble` (enviados) com carimbo de hora em mono e tique. Sombra Média + segunda folha. Sem moldura de aparelho. Rótulo acima (“No celular da Dona Maria” / “No seu celular”, este em lilás).
- **Cartão com avatar pousado:** nos momentos do dia o cabeçalho sai e o avatar de 48px, em anel de superfície de 3px, pousa 24px acima da borda superior esquerda do cartão. Largura máxima 26rem.
- **Placa da personagem:** 4:5, raio 20px, sombra Suave, recorte ancorado no alto para preservar o rosto.
- **Folha de limites:** uma só superfície de raio 20px com duas listas lado a lado (5/7): “A Tia faz” com check teal e “A Tia recusa” com o sinal de recusa em `ink-2`. A lista de recusas é visivelmente mais longa — é o argumento da seção, e a proporção deve ser mantida.
- **Livro-razão de ofertas:** linhas, não cartões (ver Layout). Preço em `price`; o que o preço não cobre vem junto, em texto pequeno.
- **Bloco de aviso:** coral-leite, raio 16px, tinta — para a linha de urgência.

### Navigation
Lockup à esquerda, três links em Nunito 800 (1.0625rem) com sublinhado de 2px em `accent` no hover, pílula de ação à direita. No celular: botão circular de 46px com três traços que viram X, painel de links em 1.25rem com divisores, fecha com Esc e ao escolher. Link “Pular para o conteúdo” em pílula de tinta, visível ao receber foco. Rodapé em forma de carta: assinatura em Pull, P.S. com a linha de limite, links em 800.

### Acordeão de dúvidas
Pergunta em Fraunces itálico 600 (1.4375rem), alvo de 56px, sinal de mais/menos desenhado com dois traços `call` de 2,5px; a resposta abre por `grid-template-rows` em 420ms. Sem JavaScript, todas as respostas ficam abertas e o sinal some.

### A travessia (componente-assinatura)
Dois cartões de conversa em diagonal, ligados por um trecho em S do fio trançado com a pílula “08:04 chega a quem cuida” montada no meio. Tocar “Já tomei” no celular dela: a mensagem sobe 8px (420ms, ease-out exponencial), a Tia responde, **um único ponto coral percorre o fio** em 1100ms (`offset-path`, só onde há suporte) e a confirmação pousa no celular de quem cuida com um halo lilás que se dissolve. “Ainda não” mostra antes o novo lembrete gentil e o celular de quem cuida responde com uma frase quieta, sem alarme. Na seção do dia, o fio vertical se desenrola com a rolagem onde existe `animation-timeline` e o visitante não pediu movimento reduzido. O estado inicial em HTML já mostra a história completa nos dois celulares.

## Do's and Don'ts

### Do:
- **Do** escolher o coral pelo tamanho do texto: `accent` para grafismo, `accent-ink` para palavra de display, `call` para ação e texto pequeno.
- **Do** manter o corpo em 18px / Nunito 600 e todo alvo de toque com 44px ou mais (ações 46–60px, chip 48px, resposta 44px, pergunta 56px).
- **Do** usar Fraunces sempre itálico, eixo óptico automático, pesos 500–600, com uma afirmação inteira por seção.
- **Do** prender toda hora ao fio numa pílula, em JetBrains Mono tabular; escrever preço em Nunito 800 com algarismos tabulares.
- **Do** dar a todo cartão de conversa a segunda folha de 10px — teal na ponta dela, lilás na ponta de quem cuida — e rotular as conversas como exemplo com nomes fictícios.
- **Do** dizer o status com as pílulas (Em piloto, Em breve — e Disponível quando existir) e mostrar ofertas em linhas com coluna de status.
- **Do** entregar o conteúdo completo em HTML: conversas escritas, respostas abertas sem JS, nada essencial revelado só por animação.
- **Do** fazer toda sombra com a tinta diluída e todo ícone com o conjunto próprio de traço único, aplicado como máscara.

### Don't:
- **Don't** usar o coral da marca (`accent`) como cor de texto ou de botão — 2,9:1 no creme.
- **Don't** usar vermelho, preto puro, sombra preta ou branco puro como fundo de página.
- **Don't** usar teal fora de confirmação/registro, lilás fora da ponta de quem cuida, nem verde de WhatsApp fora do cartão de conversa.
- **Don't** pôr o fio em limites, ofertas, dúvidas, clínicas ou rodapé; ele é a espinha da demonstração, não um enfeite de seção.
- **Don't** pôr preço em mono, nem mono em qualquer coisa que não seja hora.
- **Don't** usar emoji ou glifo como ícone de interface; emoji só dentro das mensagens.
- **Don't** transformar ofertas em cartões de preço ou bento, nem adesão em nota, gráfico, anel ou medalha.
- **Don't** colocar a segunda folha em botões, imagens ou outros cartões.
- **Don't** devolver a faixa promocional do topo nem o seletor de perfil; uma ação por tela.
- **Don't** mostrar a personagem em cena clínica, infantilizada ou comunicando cobrança.

## Camadas de decisão

### A — Herdado da marca e preservado (não decidido por esta versão)

Fontes: `BrandBrain/pilares/Pilar-3-Identidade-Visual.md`, `BrandBrain/Folha-de-Referencia-de-Marca.md`, `BrandBrain/social` (posts aprovados 01 e 02).

- Fundo de papel creme (`#FAF7F2` na folha de referência) com faixas wash; nunca branco puro.
- Tinta azul-petróleo para todo título e texto; nunca preto.
- Coral como a cor de chamada; teal = confirmação/registro; lilás só na ponta de quem cuida.
- Fraunces itálico no display, Nunito no corpo (a marca prevê 600–900), JetBrains Mono só para hora.
- Raios 16 / 20 / 999.
- Sombra sempre tingida de tinta, nunca preta.
- Nenhum vermelho, em lugar nenhum.
- Verde do WhatsApp só em representação literal da conversa.
- A estrela ★ como marcador de categoria e o travessão como pontuação da marca.
- A personagem canônica (elemento Higgsfield `tia-medica-canonica-final-v2`): bob escuro na altura do queixo, óculos retangulares teal, uniforme coral transpassado com filete creme, pin de coração creme.

Como a herança chegou ao código: os valores da marca foram transcritos para OKLCH e alguns não batem exatamente com os hex da folha de referência (ver C, item 5).

### B — Proposto por esta versão, com o motivo

1. **O fio trançado (coral + tinta + teal claro) como espinha.** Motivo: a página precisava mostrar uma confirmação *viajando* entre duas pessoas, e a marca não tinha um elemento de ligação. O fio nasce das cores já existentes e da linha vertical com nós que os posts já usam. Aparece na travessia do hero, na tese, no dia, no coração e no fechamento; fica de fora de limites, ofertas e dúvidas porque o fundador pediu menos decoração.
2. **Hero “duas pontas” e a interação-assinatura.** Motivo: provar o produto em vez de descrevê-lo — o visitante responde no lugar dela e vê a confirmação chegar ao “seu” celular.
3. **Cartões de conversa com a segunda folha deslocada** (teal; lilás no cuidador). Motivo: trazer para o site o objeto mais reconhecível dos posts 01/02, em vez de moldura de celular.
4. **Avatar pousado na borda do cartão.** Motivo: mesmo gesto dos posts; assina a conversa sem repetir um cabeçalho inteiro em cada exemplo.
5. **Pílulas de hora em mono presas ao fio.** Motivo: a hora é o que organiza o dia; presa ao fio, vira linha do tempo sem virar gráfico.
6. **Ação primária passou de tinta para coral profundo (`call`).** Motivo: a marca define o coral como a cor de chamada, mas o coral da marca mede ~2,8–2,9:1 no creme e falha até como texto grande. Resultado: coral da marca só em grafismo, `accent-ink` para palavra de display, `call` (5,3:1) para ação e coral pequeno.
7. **`ink-2` escurecida para 6,0:1.** Motivo: sustentar AA com folga em texto de apoio também sobre o wash e sobre o fundo da conversa.
8. **Corpo em 18px.** Motivo: público de 55–85 anos lê a página.
9. **Pesos de display mais leves** (H1/H3 600, H2 540, corte 500, eixo óptico automático em vez de `opsz 144` forçado). Motivo: casar com o letreiro dos posts aprovados.
10. **Preço fora do mono.** Motivo: o zero cortado do JetBrains Mono fazia “R$ 0” ler “R$ Ø”.
11. **Vocabulário de status + livro-razão no lugar de cartões bento.** Motivo: a página precisa separar o que existe, o que está em piloto e o que é plano. Disponível = tinta cheia, Em piloto = coral-leite, Em breve = contorno.
12. **Folha de limites em duas listas, recusas mais longas.** Motivo: a tese da marca (“a lista do que ela recusa é maior”) passa a ser visível na forma.
13. **Conjunto próprio de ícones de traço único**, no lugar de glifo/emoji fora dos balões. Motivo: ícone de interface precisa pegar a cor do sistema e ter o mesmo desenho em todo aparelho; emoji fica onde é literal, dentro da mensagem.
14. **Faixa promocional do topo e seletor de perfil removidos.** Motivo: a página passou a ter um visitante principal (quem cuida) e uma ação; os outros perfis são atendidos por uma frase — “Cuida do seu pai, de outra pessoa — ou de você? Funciona do mesmo jeito.”
15. **Dock mantida no celular; ação da barra oculta enquanto a dock está visível.** Motivo: uma ação por tela.
16. **Ordem do hero no celular: conversa antes do retrato; o retrato assina o aparte.** Motivo: em 390 × 844 o que precisa estar acima da dobra é o lembrete das 08:00, não o rosto.

### C — Conflitos e pendências (registrados, não resolvidos)

1. **“Sem mascote” × personagem.** O Pilar 3 e a Folha de Referência (2026-08-18) ainda dizem “sem mascote, a Tia não tem rosto”; o trabalho social aprovado depois (2026-08-20/25) e o fundador adotaram a personagem. Os dois documentos precisam de revisão.
2. **Imagem do hero — produzida e aprovada pelo fundador em 2026-09-20.** Gerada no Higgsfield com o elemento canônico, no enquadramento do `ASSETS-BRIEF.md` (peça 1), com o pin oficial recomposto; no celular entra um recorte próprio de retrato. A imagem provisória da biblioteca 02-emocional foi removida.
3. **“Leitura de receita por foto” — resolvido em 2026-09-20.** Aparecia como início gratuito da rotina e também como item do Plano Tia Cuidado. O fundador decidiu: é da rotina gratuita; o item saiu da lista do Plano, que ficou com três (até 2 pessoas, relatório mensal em PDF, consultas incluídas).
4. **Ilustrações de guache do site anterior** (`assets/ilustracoes/`) continuam no repositório, sem uso: a mão delas não casa com o acabamento da personagem. Reversível.
5. **Desvios entre a marca e o código, não corrigidos aqui:** a estrela ★ é pintada em `call` (a folha de referência prevê amarelo `#F4C430`, que não existe nos tokens); `teal` e `lilac-ink` foram entregues mais escuros que os hex da marca, para servir de contorno e de texto; a tinta em OKLCH resulta um pouco mais escura que `#264653`; a Tinta 3 da marca não foi levada para o site; Nunito 900 é carregada e não é usada (o código usa 600, 700 e 800).
6. **Tudo o que é pago fica “Em breve” — decisão do fundador em 2026-09-20.** Consulta, análise de pele e Plano aparecem com a pílula “Em breve” (a consulta deixou de ser “Disponível”; o botão virou “Quero ser avisado”). O médico respondendo na conversa passou para o futuro no momento das 19:12, na folha de limites e nas dúvidas; o princípio “a decisão clínica é de um médico” continua no presente. A pílula “Disponível” continua no sistema, sem uso hoje.
7. **Preços das ofertas pagas fora da página — decisão do fundador em 2026-09-20.** Os valores ainda não estão definidos; a linha de preço da consulta e da análise de pele diz “Preço em breve” (Nunito 800, tinta secundária). O único preço publicado é o “R$ 0 · para sempre” da rotina.
8. Pendência de produto herdada do brief: qual é a foto de perfil em uso no WhatsApp Business?

## Acessibilidade e movimento (como implementado)

- **Contraste AA medido sobre o texto renderizado**, não sobre o token isolado: tinta 9,8:1; `ink-2` 6,0 / 5,6 / 5,1 (papel / wash / conversa); `call` 5,3; papel sobre `call` 5,3; `call-deep` sobre coral-leite 5,9; `lilac-ink` 6,7 e 6,0; `teal-ink` 6,1. `accent-ink` (4,2) só em display; `accent` (2,9) nunca em texto.
- **Alvos de toque ≥ 44px no celular**: ações 46–60px, chip 48px, resposta 44px, menu 46px, pergunta 56px, links de navegação e rodapé com preenchimento vertical.
- **Foco visível**: anel de 3px em `focus`, afastado 3px, em todo link e botão. **Link de pular** para `#conteudo`.
- **Completa sem JavaScript**: as duas conversas do hero estão escritas no HTML; as respostas das dúvidas ficam abertas; a linha “Responda no lugar dela” nasce oculta (`hidden`) e só o script a revela.
- **`prefers-reduced-motion: reduce`** zera animações e transições na página inteira, desliga a rolagem suave, e o script troca as esperas por zero — o estado final aparece de imediato.
- **Revelação do fio por rolagem** só dentro de `@supports (animation-timeline: view())` **e** `prefers-reduced-motion: no-preference`.
- **Pulso no fio** por `offset-path`, dentro de `@supports` — melhoria progressiva; sem suporte, a confirmação simplesmente chega.
- Regiões vivas (`aria-live="polite"`) nos dois corpos de conversa; fio, tiques e travessia com `aria-hidden`.

### O fio que desce trançando (acrescentado em 2026-09-20, a pedido do fundador)

Na linha do tempo “Um dia com a Tia”, com JavaScript e movimento liberado, o fio acompanha a rolagem: a trama é revelada até cerca de 62% da altura da janela, gira enquanto desce (a fase da trança anda à metade da velocidade da ponta) e os três fios seguem soltos logo abaixo, entrando na trança; perto do fim a ponta se recolhe. Uma linha-guia de 2px mostra o caminho ainda não tecido. Cada pílula de hora ganha contorno em tinta (lilás na ponta de quem cuida) quando o fio chega nela. Sem JavaScript ou com `prefers-reduced-motion`, o fio fica inteiro e parado, com o ponto final — nada de conteúdo depende do movimento. Substitui a revelação só-CSS por `animation-timeline`, que não rodava em Safari nem Firefox.

## Restrições técnicas

- HTML, CSS e JS estáticos, sem dependências nem etapa de build.
- CSP com `script-src 'self'` e `script-src-attr 'none'`: nenhum JavaScript inline, nenhum `onclick`. `form-action 'none'` e nenhum `<form>` na página.
- Âncoras preservadas: `#como-funciona`, `#precos`, `#duvidas`, `#clinicas`. Título, descrição, OG e JSON-LD preservados.
- Fontes via Google Fonts (Fraunces itálico 500–700 com eixo óptico, Nunito 600–900, JetBrains Mono 500/700).
- Documentos de trabalho fora da publicação por `.vercelignore`: `PRODUCT.md`, `DESIGN.md`, `ASSETS-BRIEF.md`, `.impeccable`, `docs`, `tests` e os sidecars `assets/personagem/*.json`.
- Todo raster da personagem carrega um sidecar de procedência (`*.webp.json`).
