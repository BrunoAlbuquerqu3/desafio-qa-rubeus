import pytest
from playwright.sync_api import Page, expect
import requests

# 1. TESTE DE API (Seu diferencial de Requests)
def test_api_status_check():
    url = "https://qualidade.apprbs.com.br/certificacao"
    response = requests.get(url, timeout=5)
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0

# 2. TESTE DE UI (Playwright com Seletores Genéricos)
def test_form_certificacao_elements(page: Page):
    page.goto("https://qualidade.apprbs.com.br/certificacao")
    page.wait_for_load_state("networkidle")

    # Em vez de 'Nome', vamos buscar por qualquer input que pareça um nome
    # Isso torna seu teste mais resiliente (estratégia de QA Sênior)
    nome_input = page.locator("input[type='text'], input[name*='nome']").first
    email_input = page.locator("input[type='email'], input[name*='email']").first
    
    # Validações
    expect(nome_input).to_be_visible(timeout=10000)
    expect(email_input).to_be_visible(timeout=10000)
    
    # Preenchimento de teste
    nome_input.fill("Bruno QA Test")
    email_input.fill("bruno@exemplo.com")
    print("\n[SUCESSO] Campos identificados e preenchidos.")

def test_site_main_title(page: Page):
    page.goto("https://qualidade.apprbs.com.br/site")
    assert page.title() != ""