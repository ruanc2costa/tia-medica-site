# Product

<!-- impeccable:product-schema 1 -->

> Registro de produto para o site público. Fontes: `BrandBrain/` (pilares 1–4, folha de referência, specs dos posts 01/02), o site atual e a confirmação do fundador em 2026-09-20. O código e o `BrandBrain` prevalecem sobre este resumo; quando o produto andar, atualize aqui.

## Platform

web

## Users

**Visitante principal da home (confirmado em 2026-09-20):** filha, filho ou cuidador familiar, 35–60 anos, que trabalha, mora em outra casa e acompanha à distância alguém que toma remédio contínuo. Sabe os remédios de cor e não sabe o que acontece entre as ligações. Quer saber se tomou — e, por baixo, quer saber se está tudo bem. Costuma chegar pelo Instagram ou por indicação, no celular.

**Segundo público, sempre presente:** a própria pessoa que toma remédio todo dia (55–85 anos), que usa WhatsApp e quase nenhum outro aplicativo. Ela lê o site também — nada dito a quem cuida pode humilhar quem é cuidado.

**Terceiro público, secundário na home:** clínicas e profissionais de saúde interessados em coortes acompanhadas. Falam por e-mail, não pelo WhatsApp.

## Product Purpose

A Tia Médica organiza a rotina de cuidado com a saúde no intervalo entre as consultas, numa conversa de WhatsApp: lembra remédios, hábitos e consultas, registra as confirmações e, com o combinado dos dois lados, mantém quem cuida informado. Quando a decisão é clínica, ela é de um médico com CRM ativo, que responde na própria conversa.

Sucesso, para a home: o visitante entende em segundos o que é, confia no limite do produto e começa uma conversa no WhatsApp para participar do piloto.

## Positioning

A Tia cuida do intervalo; o médico cuida do resto. Ela ganha a confiança pelo que se recusa a fazer: não diagnostica, não prescreve, não transforma adesão em nota. Vai até onde a pessoa já está (WhatsApp, sem aplicativo novo) e nunca coloca lembrete de medicamento atrás de pagamento — sempre vai existir uma Tia gratuita.

## Operating Context

- A experiência acontece inteira no WhatsApp: texto ou áudio, sem download, sem cadastro, sem senha.
- A Tia é uma assistente virtual com inteligência artificial conversacional (divulgado na Política de Privacidade). A personagem ilustrada é o rosto da marca, não uma profissional que visita a casa nem que pratica ato clínico.
- Vínculo de cuidador é combinado dos dois lados: a pessoa convida, quem cuida aceita, e ela pode desligar quando quiser.
- Pagamento só por link oficial do Mercado Pago (PIX ou cartão). A Tia nunca pede número de cartão, código ou senha na conversa.
- Consulta na modalidade assíncrona (Resolução CFM nº 2.314/2022), resposta em até 24–48h. Não atende urgência: UPA, hospital ou SAMU 192.

## Capabilities and Constraints

Status das ofertas (decisão do fundador em 2026-09-20: **tudo o que é pago fica "em breve"**; só a rotina gratuita funciona hoje, em piloto):

| Oferta | Preço | Status |
|---|---|---|
| Rotina: lembretes de remédio, hábitos e consultas, com confirmações registradas e aviso a quem cuida | gratuita | **Em piloto** pelo WhatsApp, aberto a pessoas de todo o Brasil |
| Consulta com médico parceiro | **a definir** — o site diz "Preço em breve" | **Em breve** — quando chegar: cobrada por consulta, resposta em até 24–48h; sem resposta no prazo, crédito devolvido |
| Análise de pele com médico | **a definir** — o site diz "Preço em breve" | **Em breve** — cobrada por avaliação; não garante laudo ou atestado |
| Plano Tia Cuidado | não anunciado | **Em breve** — lista de espera por e-mail. Itens anunciados: até 2 pessoas, relatório mensal em PDF, consultas com médico incluídas |

Decisão do fundador (2026-09-20): **a leitura de receita por foto faz parte da rotina gratuita** e não é item do Plano Tia Cuidado; o item "Leitura de receitas e exames por foto" saiu da lista do Plano.

Decisão do fundador (2026-09-20): **os valores das ofertas pagas ainda não estão definidos** — R$ 49,90 e R$ 69,90 saíram da página e não podem voltar sem decisão dele. O único preço publicado é o R$ 0 da rotina.

Consequência para o texto do site: o médico respondendo na conversa aparece sempre no futuro ("em breve, um médico parceiro vai responder…"); o princípio "a decisão clínica é de um médico" continua no presente. Hoje não há nada a pagar.

Capacidades que o site pode mostrar: lembrete na hora combinada; confirmação por texto ou áudio; novo lembrete gentil depois de um "ainda não"; leitura de receita por foto com confirmação antes de cadastrar; aviso a quem cuida; organização da queixa e encaminhamento a médico parceiro.

Limites que o site precisa manter:

- Nenhum ato privativo de médico: sem diagnóstico, prescrição, posologia, interpretação de exame ou prognóstico.
- Nunca prometer infalibilidade ("nunca mais esqueça" é proibido). A Tia não detecta queda.
- Adesão nunca aparece como score, nota, ranking, meta, gráfico ou anel de progresso.
- Nunca afirmar ação sem prova: anotei ≠ agendei; entregue ≠ avisado.
- Todo preço aparece com o que ele não cobre (prazo de 24–48h, não é urgência).
- Onde houver sintoma, consulta ou urgência: UPA, hospital ou SAMU 192.
- Preços e condições comerciais não mudam sem decisão explícita do fundador.

Restrições técnicas do site: HTML/CSS/JS estático servido pela Vercel a partir da raiz do repositório; CSP com `script-src 'self'` (zero JavaScript inline, zero `onclick`); sem `<form>`; rotas `/privacidade` e `/excluir-conta` por rewrite; URLs, páginas legais e metadados existentes são preservados.

Em aberto (não decidir sem o fundador): qual é a foto de perfil em uso no WhatsApp Business (coração coral ou busto da personagem).

## Brand Commitments

- Nome, logotipo (coração coral com o "Tia" manuscrito), lockups e paleta oficiais — nunca ajustados a olho.
- Três palavras: **acolhedora · precisa · honesta.** Acolhedora, não fofa. Precisa, não fria. Honesta, mesmo quando custa a venda.
- Preferência do fundador para o site (2026-09-20): cuidado próximo, clareza, personalidade e sobriedade, sem infantilizar.
- A personagem canônica da Tia (elemento Higgsfield `tia-medica-canonica-final-v2`): mulher brasileira de 38–45 anos, bob escuro na altura do queixo, óculos retangulares azul-petróleo, uniforme coral de gola transpassada com filete creme, pin de coração creme no peito esquerdo. Nunca redesenhada do zero; nunca em cena clínica; nunca comunicando erro ou cobrança. O pin gerado por IA não é arte final — a geometria oficial é recomposta por cima.
- Voz da Casa no site: terceira pessoa, frase de uma respiração, travessão como pontuação, prova antes de adjetivo, sem parênteses de gênero, sem "vovó" nem diminutivo automático, no máximo um ponto de exclamação por peça. Régua: se a frase caberia no site de um concorrente, reescreve.
- Não existe vermelho na marca, nem preto puro. Verde do WhatsApp só em representação literal da interface.
- Toda peça que fale de saúde fecha com a linha de limite: "A Tia organiza, lembra e registra. Não diagnostica, prescreve nem substitui profissionais de saúde. Em emergência: SAMU 192."

Conflito documentado: o Pilar 3 e a Folha de Referência (18/08/2026) dizem "sem mascote, a Tia não tem rosto"; o trabalho posterior em `BrandBrain/social` (20–25/08/2026) criou e usou a personagem canônica nos posts 01 e 02. O fundador confirmou a personagem como identidade a preservar. Os dois documentos antigos precisam de revisão.

## Evidence on Hand

- Conversas de exemplo já escritas na voz da Tia (site atual e posts), sempre com nomes fictícios e rótulo de exemplo.
- Peças aprovadas: carrosséis `BrandBrain/social/post-01-o-que-e-a-tia` e `post-02-tia-gratuita`; avatar final `mascote-fundo-branco/avatar-whatsapp-busto-badge-final.png`.
- Biblioteca da personagem `mascote-biblioteca-02-emocional` (12 cenas): **provisória** — aguarda aprovação visual e acabamento do pin; o site não a usa.
- Ilustração do hero gerada em 2026-09-20 (Higgsfield, elemento canônico, pin oficial recomposto): `assets/personagem/tia-hero-*.webp` — aprovada pelo fundador em 2026-09-20.
- Provas publicáveis por decisão, não por número: o lembrete que não para quando o pagamento para; a Tia gratuita permanente; a frase literal que a engenharia protege.
- **Não existe e não pode ser inventado:** depoimento, número de usuários, resultado clínico, certificação, percentual de adesão.

## Product Principles

1. A conversa é a demonstração — mostrar a Tia trabalhando vale mais que descrevê-la.
2. Dizer o que ela não faz, no corpo do texto e com o destino: a decisão clínica é de um médico.
3. Cuidado básico não é moeda de troca — o gratuito nunca aparece como isca.
4. Cuidar sem vigiar — nada no site transforma a pessoa cuidada em objeto de monitoramento.
5. Na dúvida entre parecer mais capaz e ser mais honesta, honesta.

## Accessibility & Inclusion

Público inclui pessoas de 55–85 anos: corpo de texto de 17–18px no mínimo, contraste AA, alvos de toque de 44px ou mais, nunca texto essencial sobre foto, nada essencial revelado só por animação, respeito a `prefers-reduced-motion`, navegação completa por teclado com foco visível. Parênteses de gênero são proibidos também por acessibilidade (leitor de tela).
