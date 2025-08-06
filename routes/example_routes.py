"""
Módulo de rotas de exemplo para a aplicação Flask.
Este arquivo define os endpoints da API usando Flask Blueprints
para manter a organização e modularidade do código.
"""

from flask import Blueprint, jsonify, request
from services.example_service import ExampleService

# Criação do Blueprint para as rotas de exemplo
example_bp = Blueprint('example', __name__, url_prefix='/api')


@example_bp.route('/hello', methods=['GET'])
def hello():
    """
    Endpoint GET /api/hello
    Retorna uma mensagem de saudação em formato JSON
    
    Returns:
        json: Resposta com mensagem "Hello, UNINTER!" e informações adicionais
    """
    try:
        # Utiliza o serviço para obter a mensagem
        response_data = ExampleService.get_hello_message()
        
        return jsonify(response_data), 200
        
    except Exception as e:
        # Tratamento de erro genérico
        return jsonify({
            "error": "Erro interno do servidor",
            "message": str(e)
        }), 500


@example_bp.route('/info', methods=['GET'])
def app_info():
    """
    Endpoint GET /api/info
    Retorna informações sobre a aplicação
    
    Returns:
        json: Informações da aplicação
    """
    try:
        app_data = ExampleService.get_app_info()
        return jsonify(app_data), 200
        
    except Exception as e:
        return jsonify({
            "error": "Erro ao obter informações da aplicação",
            "message": str(e)
        }), 500


@example_bp.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint GET /api/health
    Endpoint de verificação de saúde da aplicação
    
    Returns:
        json: Status da aplicação
    """
    return jsonify({
        "status": "healthy",
        "message": "Aplicação funcionando corretamente"
    }), 200


# Manipulador de erro para o blueprint
@example_bp.errorhandler(404)
def not_found(error):
    """
    Manipulador de erro 404 para rotas não encontradas no blueprint
    
    Returns:
        json: Mensagem de erro 404
    """
    return jsonify({
        "error": "Endpoint não encontrado",
        "message": "A rota solicitada não existe"
    }), 404