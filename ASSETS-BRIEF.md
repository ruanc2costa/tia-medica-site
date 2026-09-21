# ASSETS-BRIEF — home "As duas pontas do fio"

Brief de imagens para produção no Higgsfield. O layout reutiliza primeiro o que a marca já tem; este arquivo lista só o que de fato faltava. **Única geração paga até aqui:** a ilustração do hero (peça 1), em 2026-09-20, com liberação expressa do fundador — 2 créditos. Nenhum vídeo foi gerado.

Regras que valem para qualquer peça (herdadas de `BrandBrain/docs/superpowers/specs/2026-08-20-biblioteca-social-mascote-design.md`):

- Usar exclusivamente o elemento Higgsfield `tia-medica-canonica-final-v2` (ID `e88d45d2-22c1-46b8-a3c9-cfab29cfd1a9`). Não redesenhar a personagem.
- Nenhum texto, botão, interface, marca-d'água ou número dentro da imagem. Todo texto essencial é HTML.
- Sem hospital, consultório, jaleco branco, cruz, touca, estetoscópio, equipamento médico ou procedimento clínico.
- O pin gerado por IA nunca é arte final: recompor a geometria oficial (`BrandBrain/logo/tia-pin-coracao-creme.svg`) por cima.
- Antes de gerar, estimar o custo em créditos e confirmar com o fundador.

---

## Peça 1 — Ilustração principal do hero (necessária)

**Situação em 2026-09-20: PRODUZIDA e APROVADA pelo fundador ("mascote ficou bom").** Com a liberação dele, foram geradas duas variações no Higgsfield (modelo pedido `nano_banana_pro`, executado como `nano_banana_2`; 4:5, 2k; 2 créditos no total) com o elemento `tia-medica-canonica-final-v2`. Ficou a variação 2 (job `affd78c8-5961-4a3d-bf23-c80082f0c811`): luz de janela na parede e terço esquerdo calmo. O pin oficial foi recomposto por cima do pin gerado.

- No site: `assets/personagem/tia-hero-928.webp`, `tia-hero-560.webp` e, só no celular, o recorte `tia-hero-retrato-416.webp` (rosto, ombros e pin). Cada arquivo tem ao lado um `.webp.json` com o prompt exato.
- Referência em boa resolução, variação não usada e o script do pin: `docs/redesign-2026-09/hero/`. O original em 2k continua na conta do Higgsfield.
- A imagem provisória (`tia-hero-provisoria-*`) foi removida.

O brief abaixo é o que guiou a geração e serve para refazer a peça, se o fundador pedir outra.

| Campo | Especificação |
|---|---|
| **Finalidade** | Placa do hero da home: o rosto da marca ao lado da demonstração. A Tia aparece "do outro lado da conversa" — pronta para falar, não posando. |
| **Proporção** | 4:5 retrato. Entregar em 1600 × 2000 px ou mais. O site serve versões WebP de 928 e 560 px de largura. |
| **Recorte no celular** | No celular a página usa um recorte 4:5 próprio, fechado em rosto, ombros, pin e celular (42%–98% da largura, a partir de 12,5% da altura). A personagem precisa caber inteira nessa janela. |
| **Enquadramento** | Plano médio, da cintura para cima. Tia deslocada para a direita: eixo do rosto entre **58% e 62% da largura**, olhos a ~30% da altura. Corpo em leve três-quartos, voltado para a esquerda (para onde ficam os cartões de conversa). Olhar para a câmera, sorriso discreto. Celular nas duas mãos, na altura do peito, tela não visível. |
| **Área livre** | Faixa esquerda de **32% da largura** em toda a altura, mais o canto inferior esquerdo (até 45% da largura × 40% da altura): só parede clara, cortina ou sofá desfocado — sem rosto, mãos, plantas de alto contraste ou objetos recortados. O cartão "No celular da Dona Maria" cobre essa região no desktop. Nada importante a menos de 6% das bordas (a placa tem cantos de 20 px). |
| **Ambiente** | Sala ou cozinha brasileira contemporânea, luz natural de manhã ("cozinha de casa às oito da manhã"), paleta creme, coral, terracota suave e azul-petróleo pontual; madeira clara, cerâmica, tecido. Fundo levemente desfocado. |
| **Referência necessária** | Elemento `tia-medica-canonica-final-v2`. Estilo e acabamento: `mascote-biblioteca-02-emocional/02-inicio-conversa.png` (pose e luz) e `06-confirmacao-tranquila.png` (calor da expressão). Conferência de identidade: `mascote-fundo-branco/avatar-whatsapp-busto-badge-final.png`. |
| **Pós-produção** | Recompor o pin oficial (`docs/redesign-2026-09/hero/recompor-pin.py`). Exportar `tia-hero-928.webp`, `tia-hero-560.webp` e o recorte `tia-hero-retrato-416.webp` (qualidade ~82) em `assets/personagem/`; os caminhos no `index.html` já apontam para esses nomes. |

**Prompt de produção**

> Ilustração editorial semi-realista, proporção 4:5 retrato, usando o elemento de personagem `tia-medica-canonica-final-v2`. Preservar exatamente rosto, cabelo bob escuro na altura do queixo, óculos retangulares azul-petróleo, uniforme coral de gola transpassada com filete creme e o pin de coração creme no peito esquerdo. Plano médio, da cintura para cima. A Tia está deslocada para a direita do quadro (eixo do rosto a cerca de 60% da largura), corpo em leve três-quartos voltado para a esquerda, olhando para a câmera com sorriso discreto e expressão prática, serena e acolhedora. Segura um celular com as duas mãos na altura do peito, tela não visível. Sala brasileira contemporânea iluminada pela manhã, luz natural suave entrando pela esquerda, fundo levemente desfocado em creme, terracota suave e azul-petróleo pontual, madeira clara e tecido. O terço esquerdo do quadro e o canto inferior esquerdo ficam calmos e vazios — só parede clara e cortina — reservados para uma interface que será sobreposta depois. Sem texto, sem letras, sem interface, sem marca-d'água. Sem hospital, consultório, jaleco branco, cruz, estetoscópio ou equipamento médico. Sem estética infantil, sem fotorrealismo documental.

**Critérios de aceite:** a Tia continua reconhecível (óculos, bob, uniforme, pin no lugar certo); as duas áreas livres estão realmente livres; o recorte de retrato do celular mantém rosto, ombros e pin inteiros; nada sugere ato clínico nem visita domiciliar de profissional de saúde.

---

## O que não precisa ser produzido agora

- **Avatar da conversa** — já existe e está em uso: `assets/personagem/tia-avatar-{96,192}.webp`, derivado de `mascote-fundo-branco/avatar-whatsapp-busto-badge-512.png` (busto final, pin oficial recomposto).
- **Imagem de compartilhamento (OG)** — `assets/og-tia-2026.jpg` foi mantida: ela ainda casa com o `<title>` e a `description`, que não mudaram. Se a direção for aprovada e o fundador quiser o rosto da Tia no link compartilhado, a nova OG é uma **montagem** (Peça 1 + título em HTML/Figma, 1200 × 630), sem geração paga.
- **Cena de quem cuida** ("a outra ponta do fio": a filha no trabalho olhando o celular) — enriqueceria o momento das 08:31, mas o layout **não reserva espaço** para ela e funciona sem. Só vale briefar depois da aprovação da direção.
- **Naturezas-mortas do site anterior** (`assets/ilustracoes/cozinha|familia|receita*.webp`) — continuam no repositório, sem uso nesta versão: o traço de guache delas não conversa com o acabamento da personagem, e duas mãos de ilustração na mesma página enfraquecem a marca. Decisão reversível.

---

## Inventário da personagem (o que existe hoje)

| Arquivo | O que é | Papel |
|---|---|---|
| `BrandBrain/logo/tia-canonica-oculos-base.png` | Retrato canônico, sem pin | Base da personagem |
| `BrandBrain/logo/tia-canonica-oculos-medalhao-original.png` | Mesmo retrato com medalhão redondo (coração coral em círculo branco) | Variante descartada |
| `BrandBrain/logo/tia-canonica-oculos-pin-coracao-creme.png` | Mesmo retrato com o pin de coração creme | **Retrato canônico de referência** |
| `BrandBrain/social/mascote-fundo-branco/01–06-*.png` | Seis poses em fundo branco (acolhimento, explicação, escuta, celular, celebração, confiança) | Recortes para peças; sem cenário |
| `…/avatar-whatsapp-original.png` · `…-busto-raw.png` | Bustos sem pin | Etapas intermediárias |
| `…/avatar-whatsapp-busto-badge-final.png` (+ `-512`, prévias 48 px e circular) | Busto com o pin oficial recomposto | **Avatar final** — é o que a home usa |
| `BrandBrain/social/mascote-biblioteca-01/` | 12 cenas, primeira geração | Substituída pela 02 |
| `BrandBrain/social/mascote-biblioteca-02-emocional/` (+ `-02-piloto-emocional/`) | 12 cenas com mais expressão | **Provisória** — aguarda aprovação e acabamento do pin; já não é usada no site |
| `BrandBrain/logo/tia-avatar-coral.svg`, `tia-avatar-instagram-*.png` | Avatares só com o símbolo (coração, "Tia" manuscrito) | Marca sem personagem |
| `assets/tia-mascote.webp`, `assets/tia-familia.webp` (site) | Mascote antiga: cabelo longo ondulado, estetoscópio, outro rosto | **Obsoleta** — contradiz as regras atuais; não usar |

**Referência principal para a home:** a personagem canônica com pin de coração creme — elemento `tia-medica-canonica-final-v2`, conferida contra `tia-canonica-oculos-pin-coracao-creme.png` e `avatar-whatsapp-busto-badge-final.png`.

**Dúvidas registradas (não decididas aqui):**

1. Qual é a foto de perfil em uso no WhatsApp Business: o coração coral (`logo/LEIA-ME.md`, 18/08) ou o busto da personagem (arquivos de 20/08)? A home mostra o busto no cabeçalho da conversa, como os posts 01 e 02.
2. O Pilar 3 e a Folha de Referência (18/08) ainda dizem "sem mascote, a Tia não tem rosto"; o trabalho social posterior adotou a personagem. Os dois documentos precisam de revisão para não contradizer o site.
3. A biblioteca 02-emocional está aprovada? O site já não depende dela: o hero usa a ilustração gerada em 2026-09-20, já aprovada pelo fundador.
