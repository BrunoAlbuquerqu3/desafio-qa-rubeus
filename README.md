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

Como Analista de Qualidade, realizei uma inspeção manual minuciosa focada na jornada do usuário. Abaixo, os principais achados divididos por impacto:

### 🔴 Impacto Crítico (Bloqueadores)
| Local | Problema | Impacto no Negócio |
| :--- | :--- | :--- |
| `/certificacao` | Erro não informativo ao tentar avançar para Fase 2. | **Abandono de Lead:** O usuário não consegue finalizar a inscrição. |
| `/certificacao` | Falha na máscara de Telefone (> 11 dígitos). | **Integridade de Dados:** Inserção de dados "sujos" no banco/CRM. |

### 🟡 Impacto de Usabilidade e Interface (UX/UI)
* **Hierarquia Visual (Site):** Elementos como "Inscrever-se" e "Falar com Consultor" carecem de propriedades de botão (CTA), reduzindo o incentivo ao clique.
* **Acessibilidade:** Ícones com baixo contraste e fontes que poderiam ser otimizadas para melhor legibilidade.
* **Design System:** Imagens com proporção distorcida (aspect-ratio) na página de certificação, afetando a credibilidade visual da marca.
* **Engajamento:** Falha na automação do carrossel no site principal; sugere-se transição automática para exposição de novos conteúdos.

---

## 🗄️ Validação de Backend & Banco de Dados
Para uma cobertura **End-to-End (E2E)** real, minha estratégia contempla a validação da camada de persistência (SQL):
1.  **Integridade:** Garantir que o `INSERT` no banco reflita exatamente o que foi preenchido no formulário.
2.  **Sanitização:** Validar via script (PyMySQL/SQLAlchemy) se caracteres especiais ou máscaras de telefone estão sendo tratadas corretamente antes do armazenamento.

---

## 🚀 Como rodar o projeto localmente
1.  Clone o repositório.
2.  Instale as dependências: `pip install -r requirements.txt`
3.  Instale os binários do navegador: `playwright install chromium`
4.  Execute os testes e gere o relatório:
```bash
pytest --headed --html=report.html --self-contained-html
