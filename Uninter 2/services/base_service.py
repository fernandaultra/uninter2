"""
Classe base para serviços de coleta de cursos
"""

import os
import pandas as pd
from datetime import datetime
from abc import ABC, abstractmethod

class BaseService(ABC):
    """Classe base para serviços de coleta de cursos"""
    
    def __init__(self):
        self.plataforma = self.__class__.__name__.replace('Service', '')
        self.data_dir = 'data'
        self._criar_diretorio_dados()
    
    def _criar_diretorio_dados(self):
        """Cria o diretório de dados se não existir"""
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
    
    @abstractmethod
    def coletar_cursos(self):
        """Método abstrato para coleta de cursos"""
        pass
    
    def salvar_csv(self, cursos):
        """Salva os cursos coletados em arquivo CSV"""
        if not cursos:
            print(f"Nenhum curso coletado para {self.plataforma}")
            return
        
        # Cria DataFrame
        df = pd.DataFrame(cursos)
        
        # Nome do arquivo com timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{self.data_dir}/{self.plataforma.lower()}_{timestamp}.csv"
        
        # Salva arquivo
        df.to_csv(filename, index=False, encoding='utf-8')
        print(f"Arquivo salvo: {filename}")
        
        return filename
    
    def limpar_texto(self, texto):
        """Limpa e normaliza texto"""
        if not texto:
            return ""
        
        # Remove espaços extras e quebras de linha
        texto = ' '.join(texto.split())
        return texto.strip()
    
    def extrair_area_conhecimento(self, titulo, descricao=""):
        """Extrai área de conhecimento baseada no título e descrição"""
        areas = {
            'tecnologia': ['programação', 'python', 'java', 'web', 'desenvolvimento', 'ti', 'tecnologia'],
            'marketing': ['marketing', 'digital', 'publicidade', 'vendas'],
            'administração': ['administração', 'gestão', 'empreendedorismo', 'negócios'],
            'design': ['design', 'criatividade', 'arte', 'visual'],
            'saúde': ['saúde', 'medicina', 'enfermagem', 'fisioterapia'],
            'educação': ['educação', 'pedagogia', 'ensino'],
            'finanças': ['finanças', 'contabilidade', 'economia'],
            'recursos_humanos': ['rh', 'recursos humanos', 'gestão de pessoas']
        }
        
        texto_completo = f"{titulo} {descricao}".lower()
        
        for area, palavras_chave in areas.items():
            for palavra in palavras_chave:
                if palavra in texto_completo:
                    return area.replace('_', ' ').title()
        
        return "Geral"
