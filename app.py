"""
Ponto de entrada principal da aplicação Flask.
Este arquivo configura e inicializa a aplicação Flask com todas as rotas
e configurações necessárias.
"""

from flask import Flask, jsonify
from utils.env_loader import load_environment_variables, get_secret_key
from routes.example_routes import example_bp


def create_app():
    """
    Factory function para criar e configurar a aplicação Flask
    
    Returns:
        Flask: Instância configurada da aplicação Flask
    """
    # Carrega as variáveis de ambiente
    load_environment_variables()
    
    # Cria a instância do Flask
    app = Flask(__name__)
    
    # Configurações da aplicação
    app.config['SECRET_KEY'] = get_secret_key()
    app.config['JSON_SORT_KEYS'] = False  # Mantém a ordem das chaves no JSON
    
    # Registra os blueprints (rotas)
    app.register_blueprint(example_bp)
    
    # Rota raiz da aplicação
    @app.route('/')
    def index():
        """
        Rota raiz que fornece informações básicas sobre a API
        
        Returns:
            json: Informações de boas-vindas e endpoints disponíveis
        """
        return jsonify({
            "message": "Bem-vindo à API Flask!",
            "description": "Projeto Flask simples com estrutura organizada",
            "endpoints": {
                "GET /": "Esta página de boas-vindas",
                "GET /api/hello": "Mensagem de saudação",
                "GET /api/info": "Informações da aplicação",
                "GET /api/health": "Verificação de saúde da aplicação"
            },
            "status": "online"
        })
    
    # Manipulador de erro global para 404
    @app.errorhandler(404)
    def page_not_found(error):
        """
        Manipulador global de erro 404
        
        Returns:
            json: Mensagem de erro 404
        """
        return jsonify({
            "error": "Página não encontrada",
            "message": "O endpoint solicitado não existe",
            "status_code": 404
        }), 404
    
    # Manipulador de erro global para 500
    @app.errorhandler(500)
    def internal_server_error(error):
        """
        Manipulador global de erro 500
        
        Returns:
            json: Mensagem de erro interno do servidor
        """
        return jsonify({
            "error": "Erro interno do servidor",
            "message": "Ocorreu um erro inesperado",
            "status_code": 500
        }), 500
    
    return app


if __name__ == '__main__':
    # Cria a aplicação
    app = create_app()
    
    # Configurações para execução
    debug_mode = True  # Defina como False em produção
    host = '0.0.0.0'   # Permite acesso externo (necessário para Render)
    port = 5000        # Porta padrão do Flask
    
    print(f"Iniciando aplicação Flask...")
    print(f"Modo debug: {debug_mode}")
    print(f"Host: {host}")
    print(f"Porta: {port}")
    print(f"Acesse: http://localhost:{port}")
    
    # Inicia a aplicação
    app.run(
        host=host,
        port=port,
        debug=debug_mode
    )