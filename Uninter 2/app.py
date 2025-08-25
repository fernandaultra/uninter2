"""
Aplicação principal para coleta automatizada de cursos gratuitos
"""

import os
from flask import Flask, jsonify, request
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

def create_app():
    """Cria e configura a aplicação Flask"""
    app = Flask(__name__)
    
    # Configurações
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['GOOGLE_SHEETS_CREDENTIALS'] = os.environ.get('GOOGLE_SHEETS_CREDENTIALS')
    app.config['SPREADSHEET_ID'] = os.environ.get('SPREADSHEET_ID')
    
    # Registra blueprints
    from routes.api_routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    
    @app.route('/')
    def index():
        """Rota principal"""
        return jsonify({
            'message': 'API de Coleta de Cursos Gratuitos',
            'version': '1.0.0',
            'endpoints': {
                'coletar_google_atelie': '/api/coletar/google-atelie',
                'coletar_senai': '/api/coletar/senai',
                'coletar_gov_br': '/api/coletar/gov-br',
                'coletar_ciee': '/api/coletar/ciee',
                'coletar_todos': '/api/coletar/todos'
            }
        })
    
    @app.route('/health')
    def health():
        """Rota de health check"""
        return jsonify({'status': 'healthy'})
    
    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.environ.get('FLASK_DEBUG', 'False').lower() == 'true')
