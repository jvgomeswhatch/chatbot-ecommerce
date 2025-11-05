# 🤖 Chatbot de E-commerce com Rasa

![Rasa](https://img.shields.io/badge/Rasa-3.x-5A00E6?style=for-the-badge&logo=rasa)
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python)

Um assistente de IA de código aberto construído com o framework Rasa para simular a interação com um cliente de e-commerce. O chatbot é capaz de responder a perguntas frequentes, recomendar produtos e verificar o status de pedidos.

Este projeto foi desenvolvido como um item de portfólio para demonstrar habilidades em desenvolvimento de software, inteligência artificial e boas práticas de engenharia.

---

### 🎬 Demonstração

O GIF abaixo demonstra um fluxo de conversa onde o usuário pergunta sobre formas de pagamento, pede uma recomendação de produto e recebe uma sugestão.

<p align="center">
  <img src="assets/ChatBot1.gif" alt="Demonstração do Chatbot" width="800"/>
</p>

---

### ✨ Funcionalidades Principais

*   **🧠 Processamento de Linguagem Natural (NLU):** Entende a intenção do usuário, mesmo com variações de frases, e extrai entidades importantes (como categoria de produto e ID do pedido).
*   **🗣️ Gerenciamento de Diálogo:** Mantém o contexto da conversa usando uma combinação de Regras (para FAQs) e Histórias (para fluxos complexos).
*   **🛍️ Recomendações de Produtos:** Sugere produtos com base na categoria informada pelo usuário.
*   **📦 Consulta de Pedidos:** Verifica o status de um pedido através de um ID (lógica simulada).
*   **❓ Respostas a FAQs:** Responde instantaneamente a perguntas comuns sobre frete e formas de pagamento usando `RulePolicy`.
*   **🛠️ Ações Customizadas:** Utiliza código Python (`rasa-sdk`) para executar lógicas de negócio, como consultar um banco de dados (simulado).

---

### 🛠️ Tecnologias Utilizadas

*   **Framework de IA:** [Rasa Open Source](https://rasa.com/)
*   **Linguagem:** Python 3.8+
*   **Servidor de Ações:** Rasa SDK
*   **Gerenciamento de Dependências:** Pip & Venv

---

#### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/seu-usuario/chatbot-ecommerce.git
    cd chatbot-ecommerce
    ```

2.  **Crie e ative um ambiente virtual:**

    *Para Linux/macOS:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    *Para Windows:*
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

### ▶️ Executando a Aplicação

Para interagir com o chatbot, você precisará de **dois terminais** abertos na pasta do projeto.

1.  **Treine o modelo de IA:**
    (Este comando só precisa ser executado uma vez, ou sempre que você alterar os arquivos em `data/` ou `config.yml`)
    ```bash
    rasa train
    ```

2.  **Inicie o servidor de ações (Terminal 1):**
    Este servidor executa o código Python customizado que está em `actions/actions.py`.
    ```bash
    rasa run actions
    ```

3.  **Inicie o chatbot e converse (Terminal 2):**
    Abra um novo terminal, ative o ambiente virtual e execute o comando abaixo para conversar com seu bot.
    ```bash
    rasa shell
    ```

### 🧪 Executando os Testes

O Rasa possui um conjunto de testes integrado que valida seus dados de treinamento. Para executar os testes, rode o seguinte comando:

```bash
rasa test


📂 Estrutura do Projeto

chatbot-ecommerce/
├── actions/
│   └── actions.py         # Lógica customizada em Python
├── data/
│   ├── nlu.yml            # Dados de treinamento de NLU
│   ├── rules.yml          # Regras para conversas diretas
│   └── stories.yml        # Fluxos de conversa (histórias)
├── models/                # Modelos treinados (.tar.gz)
├── .github/               # Workflows de CI/CD
├── .gitignore             # Arquivos ignorados pelo Git
├── config.yml             # Pipeline de NLU e políticas de diálogo
├── domain.yml             # O "cérebro" do bot
├── endpoints.yml          # Configuração de endpoints
├── requirements.txt       # Dependências do projeto
└── README.md              # Esta documentação