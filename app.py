"""
Ponto de entrada principal da aplicação Flask.
Este arquivo configura e inicializa a aplicação Flask com todas as rotas
e configurações necessárias.
"""
import os
from flask import Flask, jsonify
from utils.env_loader import load_environment_variables, get_secret_key
from routes.example_routes import example_bp


def create_app() -> Flask:
    """
    Factory function para criar e configurar a aplicação Flask.
    """
    # Carrega as variáveis de ambiente
    load_environment_variables()

    # Cria a instância do Flask
    app = Flask(__name__)

    # Configurações da aplicação
    app.config["SECRET_KEY"] = get_secret_key()  # get_secret_key() deve prover um fallback seguro
    app.config["JSON_SORT_KEYS"] = False  # Mantém a ordem das chaves no JSON

    # Registra os blueprints (rotas)
    # Se o seu blueprint já vem com prefixo "/api", mantenha como está:
    app.register_blueprint(example_bp)

    # Rota raiz da aplicação
    @app.route("/")
    def index():
        return jsonify({
            "message": "Bem-vindo à API Flask!",
            "description": "Projeto Flask simples com estrutura organizada",
            "endpoints": {
                "GET /": "Esta página de boas-vindas",
                "GET /api/hello": "Mensagem de saudação",
                "GET /api/info": "Informações da aplicação",
                "GET /api/health": "Verificação de saúde da aplicação",
                "GET /health": "Health check para o Render"
            },
            "status": "online"
        })

    # Health check para o Render
    @app.route("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    # Manipuladores globais
    @app.errorhandler(404)
    def page_not_found(error):
        return jsonify({
            "error": "Página não encontrada",
            "message": "O endpoint solicitado não existe",
            "status_code": 404
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "error": "Erro interno do servidor",
            "message": "Ocorreu um erro inesperado",
            "status_code": 500
        }), 500

    return app


# >>> Exporte o app em nível de módulo para o Gunicorn <<<
app = create_app()

if __name__ == "__main__":
    # Execução local (dev server). No Render use Gunicorn (ver Start Command).
    port = int(os.getenv("PORT", 5000))  # Render define PORT em runtime
    host = os.getenv("HOST", "0.0.0.0")
    debug_mode = os.getenv("FLASK_DEBUG", "1") == "1"

    print("Iniciando aplicação Flask...")
    print(f"Modo debug: {debug_mode}")
    print(f"Host: {host}")
    print(f"Porta: {port}")
    print(f"Acesse: http://localhost:{port}")

    app.run(host=host, port=port, debug=debug_mode)
