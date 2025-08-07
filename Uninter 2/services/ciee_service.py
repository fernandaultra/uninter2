"""
Serviço para coleta de cursos do CIEE
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from .base_service import BaseService

class CieeService(BaseService):
    """Serviço para coleta de cursos do CIEE"""
    
    def __init__(self):
        super().__init__()
        self.url = "https://portal.ciee.org.br/cursos"
        self.plataforma = "CIEE"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def coletar_cursos(self):
        """Coleta cursos do CIEE"""
        print(f"Iniciando coleta de cursos do {self.plataforma}...")
        
        try:
            # Faz a requisição para a página
            response = self.session.get(self.url, timeout=30)
            response.raise_for_status()
            
            # Parse do HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Coleta os cursos
            cursos = []
            
            # Procura por elementos que possam conter cursos
            elementos_cursos = self._encontrar_elementos_cursos(soup)
            
            print(f"Encontrados {len(elementos_cursos)} cursos")
            
            for elemento in elementos_cursos:
                try:
                    curso = self._extrair_curso(elemento)
                    if curso:
                        cursos.append(curso)
                except Exception as e:
                    print(f"Erro ao processar curso: {e}")
                    continue
            
            print(f"Coletados {len(cursos)} cursos do {self.plataforma}")
            return cursos
            
        except Exception as e:
            print(f"Erro na coleta do {self.plataforma}: {e}")
            return []
    
    def _encontrar_elementos_cursos(self, soup):
        """Encontra elementos que contêm informações de cursos"""
        elementos = []
        
        # Tenta diferentes seletores para encontrar cursos
        seletores = [
            '.course-item',
            '.curso-item',
            '.card',
            '.course-card',
            'article',
            '.item',
            '[class*="curso"]',
            '[class*="course"]',
            '.ciee-course',
            '.ciee-item'
        ]
        
        for seletor in seletores:
            elementos_encontrados = soup.select(seletor)
            if elementos_encontrados:
                elementos.extend(elementos_encontrados)
                break
        
        # Se não encontrou com seletores específicos, procura por divs com texto
        if not elementos:
            divs = soup.find_all('div', class_=True)
            for div in divs:
                if any(palavra in div.get('class', []) for palavra in ['curso', 'course', 'card', 'item', 'ciee']):
                    elementos.append(div)
        
        return elementos
    
    def _extrair_curso(self, elemento):
        """Extrai informações de um curso específico"""
        try:
            # Extrai título
            titulo = self._extrair_titulo(elemento)
            if not titulo:
                return None
            
            # Extrai outras informações
            descricao = self._extrair_descricao(elemento)
            link = self._extrair_link(elemento)
            requisitos = self._extrair_requisitos(elemento)
            
            curso = {
                'nome_curso': self.limpar_texto(titulo),
                'area_conhecimento': self.extrair_area_conhecimento(titulo, descricao),
                'requisitos': self.limpar_texto(requisitos) if requisitos else "Não especificado",
                'link_inscricao': link if link else self.url,
                'plataforma_origem': self.plataforma
            }
            
            return curso
            
        except Exception as e:
            print(f"Erro ao extrair curso: {e}")
            return None
    
    def _extrair_titulo(self, elemento):
        """Extrai o título do curso"""
        # Tenta diferentes seletores para o título
        seletores = [
            'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
            '.title', '.titulo', '.course-title',
            '[class*="title"]', '[class*="titulo"]'
        ]
        
        for seletor in seletores:
            titulo_element = elemento.select_one(seletor)
            if titulo_element and titulo_element.get_text().strip():
                return titulo_element.get_text().strip()
        
        # Se não encontrou, procura por texto em links
        links = elemento.find_all('a')
        for link in links:
            texto = link.get_text().strip()
            if texto and len(texto) > 5:
                return texto
        
        return None
    
    def _extrair_descricao(self, elemento):
        """Extrai a descrição do curso"""
        # Tenta diferentes seletores para a descrição
        seletores = [
            '.description', '.descricao', '.course-description',
            'p', '.summary', '.resumo'
        ]
        
        for seletor in seletores:
            desc_element = elemento.select_one(seletor)
            if desc_element:
                texto = desc_element.get_text().strip()
                if texto and len(texto) > 10:
                    return texto
        
        return ""
    
    def _extrair_link(self, elemento):
        """Extrai o link do curso"""
        # Procura por links
        links = elemento.find_all('a', href=True)
        for link in links:
            href = link.get('href')
            if href and not href.startswith('#'):
                # Converte para URL absoluta se necessário
                if href.startswith('/'):
                    return urljoin(self.url, href)
                elif href.startswith('http'):
                    return href
                else:
                    return urljoin(self.url, href)
        
        return None
    
    def _extrair_requisitos(self, elemento):
        """Extrai os requisitos do curso"""
        # Procura por elementos que possam conter requisitos
        seletores = [
            '.requirements', '.requisitos', '.prerequisites',
            '[class*="requisito"]', '[class*="requirement"]'
        ]
        
        for seletor in seletores:
            req_element = elemento.select_one(seletor)
            if req_element:
                return req_element.get_text().strip()
        
        return "Não especificado"
