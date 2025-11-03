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

### 📂 Estrutura do Projeto

O projeto segue a estrutura padrão do Rasa, promovendo a manutenibilidade e escalabilidade.