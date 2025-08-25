"""
Gerenciador para integração com Google Sheets
"""

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

class SheetsManager:
    """Gerenciador para integração com Google Sheets"""
    
    def __init__(self):
        self.credentials_path = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
        self.spreadsheet_id = os.environ.get('SPREADSHEET_ID')
        self.client = None
        self.spreadsheet = None
        
        if self.credentials_path and self.spreadsheet_id:
            self._conectar()
    
    def _conectar(self):
        """Conecta ao Google Sheets"""
        try:
            # Define o escopo
            scope = [
                'https://spreadsheets.google.com/feeds',
                'https://www.googleapis.com/auth/drive'
            ]
            
            # Carrega as credenciais
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                self.credentials_path, scope
            )
            
            # Conecta ao Google Sheets
            self.client = gspread.authorize(credentials)
            self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
            
            print("Conectado ao Google Sheets com sucesso")
            
        except Exception as e:
            print(f"Erro ao conectar ao Google Sheets: {e}")
            self.client = None
            self.spreadsheet = None
    
    def atualizar_planilha(self, cursos, plataforma):
        """Atualiza a planilha com os cursos coletados"""
        if not self.spreadsheet:
            print("Não foi possível conectar ao Google Sheets")
            return False
        
        try:
            # Tenta encontrar a aba da plataforma
            try:
                worksheet = self.spreadsheet.worksheet(plataforma)
            except:
                # Se não existir, cria uma nova aba
                worksheet = self.spreadsheet.add_worksheet(
                    title=plataforma,
                    rows=1000,
                    cols=10
                )
            
            # Prepara os dados para inserção
            dados = []
            for curso in cursos:
                linha = [
                    curso.get('nome_curso', ''),
                    curso.get('area_conhecimento', ''),
                    curso.get('requisitos', ''),
                    curso.get('link_inscricao', ''),
                    curso.get('plataforma_origem', ''),
                    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                ]
                dados.append(linha)
            
            if dados:
                # Limpa a aba (exceto cabeçalho)
                try:
                    worksheet.clear()
                    # Adiciona cabeçalho
                    cabecalho = [
                        'Nome do Curso',
                        'Área de Conhecimento',
                        'Requisitos',
                        'Link de Inscrição',
                        'Plataforma de Origem',
                        'Data de Coleta'
                    ]
                    worksheet.append_row(cabecalho)
                except:
                    pass
                
                # Adiciona os dados
                for linha in dados:
                    worksheet.append_row(linha)
                
                print(f"Planilha atualizada com {len(dados)} cursos da {plataforma}")
                return True
            
        except Exception as e:
            print(f"Erro ao atualizar planilha: {e}")
            return False
    
    def obter_cursos_existentes(self, plataforma):
        """Obtém cursos já existentes na planilha"""
        if not self.spreadsheet:
            return []
        
        try:
            worksheet = self.spreadsheet.worksheet(plataforma)
            dados = worksheet.get_all_records()
            
            cursos_existentes = []
            for linha in dados:
                curso = {
                    'nome_curso': linha.get('Nome do Curso', ''),
                    'area_conhecimento': linha.get('Área de Conhecimento', ''),
                    'requisitos': linha.get('Requisitos', ''),
                    'link_inscricao': linha.get('Link de Inscrição', ''),
                    'plataforma_origem': linha.get('Plataforma de Origem', '')
                }
                cursos_existentes.append(curso)
            
            return cursos_existentes
            
        except Exception as e:
            print(f"Erro ao obter cursos existentes: {e}")
            return []
