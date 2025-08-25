"""
Serviço para coleta de cursos do Google Ateliê Digital
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from .base_service import BaseService

class GoogleAtelieService(BaseService):
    """Serviço para coleta de cursos do Google Ateliê Digital"""
    
    def __init__(self):
        super().__init__()
        self.url = "https://learndigital.withgoogle.com/ateliedigital/courses"
        self.plataforma = "Google Ateliê Digital"
    
    def coletar_cursos(self):
        """Coleta cursos do Google Ateliê Digital"""
        print(f"Iniciando coleta de cursos do {self.plataforma}...")
        
        # Configuração do Chrome
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        driver = None
        try:
            # Inicializa o driver
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Acessa a página
            driver.get(self.url)
            print("Página carregada, aguardando elementos...")
            
            # Aguarda carregamento dos cursos
            wait = WebDriverWait(driver, 30)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='course-card']")))
            
            # Aguarda um pouco mais para garantir carregamento completo
            time.sleep(5)
            
            # Coleta os cursos
            cursos = []
            elementos_cursos = driver.find_elements(By.CSS_SELECTOR, "[data-testid='course-card']")
            
            print(f"Encontrados {len(elementos_cursos)} cursos")
            
            for elemento in elementos_cursos:
                try:
                    # Extrai informações do curso
                    titulo = self._extrair_titulo(elemento)
                    descricao = self._extrair_descricao(elemento)
                    link = self._extrair_link(elemento)
                    requisitos = self._extrair_requisitos(elemento)
                    
                    if titulo:
                        curso = {
                            'nome_curso': self.limpar_texto(titulo),
                            'area_conhecimento': self.extrair_area_conhecimento(titulo, descricao),
                            'requisitos': self.limpar_texto(requisitos) if requisitos else "Não especificado",
                            'link_inscricao': link if link else self.url,
                            'plataforma_origem': self.plataforma
                        }
                        cursos.append(curso)
                        
                except Exception as e:
                    print(f"Erro ao processar curso: {e}")
                    continue
            
            print(f"Coletados {len(cursos)} cursos do {self.plataforma}")
            return cursos
            
        except Exception as e:
            print(f"Erro na coleta do {self.plataforma}: {e}")
            return []
        
        finally:
            if driver:
                driver.quit()
    
    def _extrair_titulo(self, elemento):
        """Extrai o título do curso"""
        try:
            # Tenta diferentes seletores para o título
            seletores = [
                "h3",
                "[data-testid='course-title']",
                ".course-title",
                "h2",
                "h1"
            ]
            
            for seletor in seletores:
                titulo_element = elemento.find_element(By.CSS_SELECTOR, seletor)
                if titulo_element:
                    return titulo_element.text
            
            return None
        except:
            return None
    
    def _extrair_descricao(self, elemento):
        """Extrai a descrição do curso"""
        try:
            # Tenta diferentes seletores para a descrição
            seletores = [
                "[data-testid='course-description']",
                ".course-description",
                "p",
                ".description"
            ]
            
            for seletor in seletores:
                desc_element = elemento.find_element(By.CSS_SELECTOR, seletor)
                if desc_element:
                    return desc_element.text
            
            return ""
        except:
            return ""
    
    def _extrair_link(self, elemento):
        """Extrai o link do curso"""
        try:
            # Procura por links
            link_element = elemento.find_element(By.CSS_SELECTOR, "a")
            return link_element.get_attribute("href")
        except:
            return None
    
    def _extrair_requisitos(self, elemento):
        """Extrai os requisitos do curso"""
        try:
            # Tenta encontrar requisitos
            seletores = [
                "[data-testid='course-requirements']",
                ".requirements",
                ".prerequisites"
            ]
            
            for seletor in seletores:
                req_element = elemento.find_element(By.CSS_SELECTOR, seletor)
                if req_element:
                    return req_element.text
            
            return "Não especificado"
        except:
            return "Não especificado"
