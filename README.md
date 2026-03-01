# 🚀 Desafio QA Automation & Analítico - Rubeus

Este repositório contém a solução para o desafio de Analista de Qualidade Júnior da Rubeus. O projeto une **automação robusta em Python** com uma **análise consultiva de UX/UI**, focada em conversão e integridade de dados.

## 🛠️ Stack Técnica
* **Linguagem:** Python 3.13
* **Automação UI:** Playwright (Estratégia de locators resilientes e Auto-wait).
* **Testes de API:** Requests (Validação de Status Code e Latência).
* **Framework:** Pytest com relatórios dinâmicos (pytest-html).

---

## 📊 Evidência de Execução
A suíte de testes valida a integridade das URLs principais e o fluxo de comunicação com o servidor.
![Relatório de Execução](https://github.com/user-attachments/assets/44b83cb1-5aa3-4682-88f6-d4e12a5997bf)
> **Status:** 3 Passed | **Tempo Total:** 8 segundos.

---

## 🔍 Análise Crítica de Qualidade (UX/UI)

Como Analista de Qualidade, realizei uma inspeção manual detalhada em ambos os ambientes fornecidos. Abaixo, os achados divididos por impacto e localização:

### 🔴 Impacto Crítico e Funcional (/certificacao)
| Problema Identificado | Impacto no Negócio |
| :--- | :--- |
| **Erro impeditivo na Fase 2:** Notificação pouco informativa impede o avanço do cadastro. | **Abandono de Lead:** O usuário desiste da inscrição por falta de feedback claro. |
| **Falha na Máscara de Telefone:** Perda de formatação após o 11º dígito. | **Integridade de Dados:** Inserção de dados inconsistentes no banco/CRM. |
| **Lacuna de Conteúdo:** Seção "Para quem é?" sem preenchimento ou storytelling. | **Baixo Engajamento:** Perda de oportunidade de qualificar o lead. |

### 🟡 Melhorias de Usabilidade e Interface (/site)
Baseado na análise visual e de navegação do site institucional:

* **CTAs Ineficientes:** Elementos como "Inscrever-se" e "Falar com Consultor" carecem de propriedades visuais de botão (cores chamativas/sombra), não induzindo o usuário ao clique.
* **Carrossel Estático:** O banner principal não possui rolagem automática, limitando a exposição de diferentes ofertas/valores.
* **Acessibilidade e Contraste:** Ícones apagados e fontes com baixa legibilidade dificultam a navegação.
* **Canais de Contato:** A opção "Fale Conosco" está escondida; sugere-se o uso de um ícone flutuante de WhatsApp para maior visibilidade.
* **Design System:** Imagens com proporção distorcida (achatadas) e ausência de bordas arredondadas nos cards, o que confere um aspecto datado à interface.

---

## 🗄️ Validação de Backend & Banco de Dados
Para uma cobertura **End-to-End (E2E)** real, minha estratégia contempla a validação da camada de persistência (SQL):
1.  **Integridade:** Garantir que o `INSERT` no banco reflita exatamente o que foi preenchido no formulário.
2.  **Sanitização:** Validar via script se máscaras de telefone e campos sem limite de caracteres (identificados no site) são tratados antes do armazenamento.

---

## 🚀 Como rodar o projeto localmente
1.  `pip install -r requirements.txt`
2.  `playwright install chromium`
3.  `pytest --headed --html=report.html --self-contained-html`

---
**Candidato:** Bruno Albuquerque
