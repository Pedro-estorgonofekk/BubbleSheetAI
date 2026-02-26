
## Desafio Técnico | Microsserviço de Correção de Gabaritos (Python & Visão Computacional)

### Objetivo

Desenvolver um microsserviço em **Python** capaz de gerar folhas de respostas (gabaritos) customizadas e realizar a leitura automática dessas folhas a partir de imagens, devolvendo os dados processados em formato JSON.

### Arquitetura e Tecnologias

* **Linguagem:** Python
* **Framework Web:** Flask
* **Processamento de Imagem:** Bibliotecas como OpenCV, Pillow (PIL), ReportLab ou similares.
* **Inteligência Artificial:** É permitido o uso de modelos de IA (Gemini Vision, GPT-4o, Claude, Tesseract, EasyOCR, etc.), desde que a solução seja **leve e execute exclusivamente em CPU** (sem necessidade de GPU).

---

### Funcionalidades e Rotas

#### 1. Geração de Gabarito

**Rota:** `POST /gerar-gabarito`
Deve gerar uma imagem (PNG ou JPG) ou PDF de uma folha de respostas baseada nos parâmetros recebidos.

**Corpo da Requisição (Exemplo):**

```json
{
  "total_questoes": 20,
  "alternativas_por_questao": 5,
  "orientacao": "retrato",
  "id_prova": "A-2026"
}

```

* **Requisito:** A imagem gerada deve conter espaços claros para marcação (ex: círculos ou quadrados) e identificação da questão e das alternativas (A, B, C, D...).

#### 2. Correção de Gabarito

**Rota:** `POST /corrigir-gabarito`
Deve receber uma imagem da folha de respostas preenchida e identificar quais alternativas foram marcadas pelo usuário.

**Corpo da Requisição:** `Multipart/form-data` contendo:

* `file`: O arquivo de imagem da folha preenchida.
* `metadata`: JSON com as especificações da prova (quantidade de questões e alternativas) para orientar o algoritmo.

**Resposta Esperada (JSON):**

```json
{
  "id_prova": "A-2026",
  "respostas": {
    "question_1": "D",
    "question_2": "A",
    "question_3": "E",
    "...": "..."
  }
}

```

---

### Requisitos Técnicos

* **Processamento sem GPU:** A solução deve ser capaz de rodar em ambientes comuns de servidor (como instâncias básicas de nuvem ou máquinas locais simples).
* **Tratamento de Imagem:** O sistema deve ser resiliente a pequenas rotações ou variações de brilho na imagem enviada para correção.

---


### Entrega


1. **Estrutura:**
```text
├── app/
│   ├── main.py        → Entry point do Flask
│   ├── services/      → Lógica de geração e correção
│   └── utils/         → Helpers de imagem ( config da lib visual)
├── examples/          → Pasta com exemplos de gabaritos gerados
├── requirements.txt
└── README.md

```


3. **Documentação (README):**
* Como instalar as dependências.
* Como executar o serviço localmente.


