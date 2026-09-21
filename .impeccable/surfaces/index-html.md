---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

# Home — tiamedica.com (`index.html`)

Escopo: home pública, página única. Modo: **Persuade**. Status: aprovada pelo fundador e publicada em 2026-09-20 (PR #6, merge `b42b8d6`). Build: code-led. A geração de imagem só foi liberada pelo fundador depois da revisão de acabamento, para a ilustração do hero.

## Quem, o quê, para quê

- Visitante: filha, filho ou cuidador familiar (35–60), no celular, vindo do Instagram ou de indicação. A pessoa cuidada também lê.
- Deve entender: a Tia lembra os remédios pelo WhatsApp, a pessoa responde "já tomei", fica registrado, e quem cuida fica sabendo — sem aplicativo novo e sem fiscalizar.
- Deve acreditar: é honesto. Rotina gratuita (em piloto), o que é pago vem depois e está dito como "em breve", decisão clínica é de médico, limites ditos sem rodeio.
- Deve fazer: tocar em "Falar com a Tia no WhatsApp" para participar do piloto. Clínicas: e-mail.
- Prova disponível: a própria conversa (exemplos com nomes fictícios, rotulados), as decisões caras da marca (lembrete nunca bloqueado por pagamento), a tabela do que a Tia faz e do que é do médico. Nada de depoimento, número ou certificação.
- Intocável: preços e condições comerciais, páginas legais, URLs e âncoras (`#como-funciona`, `#precos`, `#duvidas`, `#clinicas`), title/description/OG/JSON-LD, CSP sem JS inline, zero `<form>`.
- O que faria um resultado polido parecer errado: cara de landing de IA; personagem infantilizada ou em pose clínica; adesão virando gráfico; alarme; promessa maior que o produto.

## Direction contract

THESIS: a home é um fio com duas pontas — a cozinha dela às 8h e o seu celular — e mostra a confirmação viajando de uma à outra. Recusa o arranjo padrão da categoria: título centralizado, três cartões de recurso e cartões de preço; recusa também a versão sem rosto, de natureza-morta, do site atual.

OWN-WORLD: papel creme com faixas wash; tinta azul-petróleo; coral como a única cor de chamada; teal para confirmação e registro (o check do que a Tia faz, a resposta "já tomei"); lilás só na ponta de quem cuida; status "Disponível" em tinta cheia (reservado; hoje só há "Em piloto" e "Em breve"). O fio trançado (coral + tinta + teal claro) é a espinha da demonstração — liga os dois celulares no hero, vira a linha do tempo do dia — e volta em dois lugares: forma o coração do compromisso e chega até a Tia no fechamento. Limites, ofertas e dúvidas ficam sem fio, de propósito: o fundador pediu menos decoração. Conversas em cartões de raio 20px, sombra petróleo diluída e segunda folha deslocada em teal claro (lilás na ponta do cuidador), como nos posts 01/02; o corpo da conversa usa o fundo literal do WhatsApp (greige) com balões brancos — representação literal da interface, permitida pelo Pilar 3; avatar da Tia num anel branco pousado na borda do cartão; horas em JetBrains Mono presas ao fio (mono só para hora — preço é Nunito 800 com algarismos tabulares); títulos em Fraunces itálico: h1 e h3 em 600, h2 em 540, frases de corte em 500; corpo Nunito 600–800; pílulas 999px; ícones próprios de traço único (check, recusa, seta, cadeado, telefone, estrela) usados como máscara — emoji só dentro das mensagens da conversa.

STORY: entende que a mãe recebe o lembrete, responde, e ela fica sabendo; acredita porque a página diz o que a Tia não faz e separa o que existe, o que está em piloto e o que é planejado; age pelo WhatsApp.

FIRST VIEWPORT (1440×900): nav de 72px — lockup à esquerda, três links, pílula de ação à direita. Coluna esquerda (5/12): H1 "Você não precisa ligar todo dia pra perguntar se ela tomou." em Fraunces itálico 600, ~3.4rem, até 4 linhas; lede de 3–4 linhas na coluna inteira; ação primária coral de 60px de altura em ~y=560; status como pílula "Em piloto" seguida de uma frase (a pílula é o mesmo vocabulário de status do livro-razão). Coluna direita (7/12): palco com a placa da Tia (4:5, ~400px, à direita) e, sobrepostos à sua borda esquerda, dois cartões de conversa empilhados em diagonal — "No celular da Dona Maria" com o lembrete das 08:00 e as respostas rápidas; abaixo e deslocado, "No seu celular", onde a confirmação chega — ligados por uma travessia do fio trançado (~350px de fio, em S, saindo de baixo do primeiro cartão e entrando por trás do segundo) com a hora em mono montada nela. No celular (390×844) a conversa vem antes do retrato: rótulo, cabeçalho e o lembrete das 08:00 ficam acima da dobra; status e aparte descem para depois do palco.

SIGNATURE INTERACTION: tocar "Já tomei" no celular dela faz um pulso descer pelo fio e a confirmação pousar no "seu" celular; "Ainda não" mostra antes o novo lembrete gentil. Gramática de movimento: mensagens sobem 8px com ease-out exponencial; um único ponto percorre o fio; na linha do tempo o fio desce com a rolagem, trançando — a trama gira, os três fios seguem soltos na ponta e cada hora acende quando o fio chega (pedido do fundador em 2026-09-20). Tudo está completo e visível sem JS e com movimento reduzido.

FORM: "As duas pontas do fio" — posição 1 da minha lista ordenada; seleção fixada pelo brief do fundador (duas direções, escolha justificada por público e objetivo), que prevalece sobre o sorteio. O sorteio (seed 80cc72c4) distribuiu 4/6/5 com "Carta aberta" à frente; ela foi apresentada como direção B. Elevações herdadas — de "Carta aberta": uma afirmação em Fraunces por seção, sobriedade conduzida por texto, o compromisso gratuito como momento tipográfico; de "Ficha honesta": ofertas como livro-razão com coluna de status, não como cartões; do desafiante "daylight section": horas tabulares presas a uma seção contínua e um estado parado completo para movimento reduzido.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Decidido pelo fundador

- 2026-09-20: leitura de receita por foto é da rotina gratuita; o item saiu da lista do Plano Tia Cuidado.
- 2026-09-20: tudo o que é pago fica "Em breve" (consulta, análise de pele, Plano). O médico respondendo na conversa aparece no futuro; só a rotina gratuita, em piloto, abre o WhatsApp.

- 2026-09-20: os valores das ofertas pagas ainda não estão definidos — a página diz "Preço em breve"; o único preço publicado é o R$ 0 da rotina.

- 2026-09-20: ilustração do hero (Higgsfield, elemento canônico, pin oficial recomposto) aprovada pelo fundador.

## Em aberto

- Foto de perfil em uso no WhatsApp Business: coração coral ou busto da personagem?
