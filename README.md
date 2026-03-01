# 🚀 Desafio QA Automation & Analítico - Rubeus

Este repositório contém a solução para o desafio de Analista de Qualidade Júnior, unindo automação robusta em Python e uma análise crítica de usabilidade e experiência do usuário (UX).

## 🛠️ Stack Técnica
* **Automação UI:** Python + Playwright (Estratégia de locators resilientes e Auto-wait).
* **Testes de API:** Requests (Validação de Status Code e Latência).
* **Framework:** Pytest com relatórios em HTML.

---

## 🔍 Análise Crítica de Qualidade (UX/UI)

Dividi minha análise técnica entre os dois ambientes fornecidos, focando em pontos que impactam diretamente a conversão do usuário.

### 1. Landing Page: /certificacao
* **Bloqueio de Fluxo (Crítico):** Identificado erro pouco informativo ao tentar avançar para a Fase 2. A falta de clareza na mensagem de erro impede a conclusão da jornada do usuário.
* **Validação de Campos:** O campo de telefone perde a formatação (máscara) após o 11º dígito, permitindo a entrada de dados inconsistentes.
* **Componentes Visuais:** Presença de imagens (consultor) com distorção de aspecto (achatada) e baixa resolução, o que transmite menor autoridade da marca.
* **Lacunas de Conteúdo:** A seção "Para quem é essa certificação?" carece de elementos interativos ou informativos (texto/storytelling) para engajar o público-alvo.

### 2. Site Institucional: /site
* **Call to Action (CTA):** Elementos importantes como "Inscrever-se" e "Falar com Consultor" não possuem destaque visual ou comportamento de botão, dificultando a conversão.
* **Usabilidade Mobile/Web:** Ícones com baixa visibilidade (apagados) e botões de contato (Fale Conosco) pouco acessíveis; sugere-se substituição por ícones flutuantes (ex: WhatsApp).
* **Design System:** Sugestão de modernização com bordas arredondadas e carrossel automático para melhorar a fluidez da leitura e o engajamento visual.

---

## 🗄️ Estratégia de Banco de Dados (Diferencial)
Como QA, minha validação E2E incluiria o uso de bibliotecas como `PyMySQL` ou `SQLAlchemy` para:
1. Validar se os dados enviados via Playwright foram persistidos sem truncamento.
2. Garantir que a máscara de telefone (corrigida) salve apenas os dígitos numéricos no banco.

---

## 🚀 Como rodar a automação
1. `pip install -r requirements.txt`
2. `playwright install chromium`
3. `pytest --headed --html=report.html --self-contained-html`
