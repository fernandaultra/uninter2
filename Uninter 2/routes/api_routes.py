"""
Rotas da API para coleta de cursos
"""

import os
import json
from flask import Blueprint, jsonify, request
from services.google_atelie_service import GoogleAtelieService
from services.senai_service import SenaiService
from services.gov_br_service import GovBrService
from services.ciee_service import CieeService
from utils.sheets_manager import SheetsManager

api_bp = Blueprint('api', __name__)

@api_bp.route('/coletar/google-atelie', methods=['POST'])
def coletar_google_atelie():
    """Coleta cursos do Google Ateliê Digital"""
    try:
        service = GoogleAtelieService()
        cursos = service.coletar_cursos()
        
        # Salva em CSV
        service.salvar_csv(cursos)
        
        # Envia para Google Sheets
        sheets_manager = SheetsManager()
        sheets_manager.atualizar_planilha(cursos, 'Google Ateliê Digital')
        
        return jsonify({
            'success': True,
            'message': f'Coletados {len(cursos)} cursos do Google Ateliê Digital',
            'cursos': cursos
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/coletar/senai', methods=['POST'])
def coletar_senai():
    """Coleta cursos do SENAI"""
    try:
        service = SenaiService()
        cursos = service.coletar_cursos()
        
        # Salva em CSV
        service.salvar_csv(cursos)
        
        # Envia para Google Sheets
        sheets_manager = SheetsManager()
        sheets_manager.atualizar_planilha(cursos, 'SENAI')
        
        return jsonify({
            'success': True,
            'message': f'Coletados {len(cursos)} cursos do SENAI',
            'cursos': cursos
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/coletar/gov-br', methods=['POST'])
def coletar_gov_br():
    """Coleta cursos do Gov.br"""
    try:
        service = GovBrService()
        cursos = service.coletar_cursos()
        
        # Salva em CSV
        service.salvar_csv(cursos)
        
        # Envia para Google Sheets
        sheets_manager = SheetsManager()
        sheets_manager.atualizar_planilha(cursos, 'Gov.br')
        
        return jsonify({
            'success': True,
            'message': f'Coletados {len(cursos)} cursos do Gov.br',
            'cursos': cursos
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/coletar/ciee', methods=['POST'])
def coletar_ciee():
    """Coleta cursos do CIEE"""
    try:
        service = CieeService()
        cursos = service.coletar_cursos()
        
        # Salva em CSV
        service.salvar_csv(cursos)
        
        # Envia para Google Sheets
        sheets_manager = SheetsManager()
        sheets_manager.atualizar_planilha(cursos, 'CIEE')
        
        return jsonify({
            'success': True,
            'message': f'Coletados {len(cursos)} cursos do CIEE',
            'cursos': cursos
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/coletar/todos', methods=['POST'])
def coletar_todos():
    """Coleta cursos de todas as plataformas"""
    try:
        resultados = {}
        
        # Google Ateliê Digital
        try:
            service = GoogleAtelieService()
            cursos_google = service.coletar_cursos()
            service.salvar_csv(cursos_google)
            resultados['google_atelie'] = {
                'success': True,
                'quantidade': len(cursos_google)
            }
        except Exception as e:
            resultados['google_atelie'] = {
                'success': False,
                'error': str(e)
            }
        
        # SENAI
        try:
            service = SenaiService()
            cursos_senai = service.coletar_cursos()
            service.salvar_csv(cursos_senai)
            resultados['senai'] = {
                'success': True,
                'quantidade': len(cursos_senai)
            }
        except Exception as e:
            resultados['senai'] = {
                'success': False,
                'error': str(e)
            }
        
        # Gov.br
        try:
            service = GovBrService()
            cursos_gov = service.coletar_cursos()
            service.salvar_csv(cursos_gov)
            resultados['gov_br'] = {
                'success': True,
                'quantidade': len(cursos_gov)
            }
        except Exception as e:
            resultados['gov_br'] = {
                'success': False,
                'error': str(e)
            }
        
        # CIEE
        try:
            service = CieeService()
            cursos_ciee = service.coletar_cursos()
            service.salvar_csv(cursos_ciee)
            resultados['ciee'] = {
                'success': True,
                'quantidade': len(cursos_ciee)
            }
        except Exception as e:
            resultados['ciee'] = {
                'success': False,
                'error': str(e)
            }
        
        return jsonify({
            'success': True,
            'message': 'Coleta concluída para todas as plataformas',
            'resultados': resultados
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
