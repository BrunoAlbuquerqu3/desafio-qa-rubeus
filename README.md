# 🚀 Desafio QA Automation - Rubeus

Repositório dedicado à automação de testes para o processo seletivo de **Analista de Qualidade Júnior**.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.13
* **Framework de Teste:** Pytest
* **Automação Web:** Playwright (Moderno, rápido e resiliente)
* **Testes de API:** Requests
* **Relatórios:** Pytest-HTML

## 🧪 Escopo dos Testes
1. **Automação de UI:** Validação de carregamento e preenchimento de campos essenciais (Nome/E-mail) nas páginas de Certificação e Site Institucional.
2. **Teste de API:** Validação de Status Code (200 OK) e análise de performance (Latência < 2s).
3. **Cross-browser:** Execução em Chromium para garantir compatibilidade.

## 🗄️ Visão de Banco de Dados (Diferencial Técnico)
Em um cenário real de produção, a automação não terminaria no clique do botão. Para garantir a integridade total (End-to-End), eu implementaria uma camada de validação de dados:
* **Fluxo:** Após o `page.click()`, o script realizaria uma conexão com o banco (MySQL/PostgreSQL).
* **Validação:** Execução de um `SELECT * FROM leads WHERE email = 'teste@exemplo.com'` para confirmar se o dado preenchido na UI foi persistido corretamente no Back-end sem corrupção de caracteres ou perda de informação.

## 🚀 Como rodar o projeto
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`.
3. Ative o venv: `.\venv\Scripts\activate`.
4. Instale as dependências: `pip install -r requirements.txt`.
5. Instale o navegador: `playwright install chromium`.
6. Execute: `pytest --headed --html=report.html --self-contained-html`.