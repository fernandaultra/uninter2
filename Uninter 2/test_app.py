"""
Arquivo de teste para verificar se a aplicação está funcionando
"""

import sys
import os

# Adiciona o diretório atual ao path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Testa se todas as importações estão funcionando"""
    try:
        print("Testando importações...")
        
        # Testa importações básicas
        from flask import Flask
        print("✓ Flask importado com sucesso")
        
        from dotenv import load_dotenv
        print("✓ python-dotenv importado com sucesso")
        
        # Testa importações dos serviços
        from services.base_service import BaseService
        print("✓ BaseService importado com sucesso")
        
        from services.google_atelie_service import GoogleAtelieService
        print("✓ GoogleAtelieService importado com sucesso")
        
        from services.senai_service import SenaiService
        print("✓ SenaiService importado com sucesso")
        
        from services.gov_br_service import GovBrService
        print("✓ GovBrService importado com sucesso")
        
        from services.ciee_service import CieeService
        print("✓ CieeService importado com sucesso")
        
        # Testa importações das rotas
        from routes.api_routes import api_bp
        print("✓ api_bp importado com sucesso")
        
        # Testa importações dos utilitários
        from utils.sheets_manager import SheetsManager
        print("✓ SheetsManager importado com sucesso")
        
        print("\n🎉 Todas as importações estão funcionando!")
        return True
        
    except ImportError as e:
        print(f"❌ Erro na importação: {e}")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

def test_app_creation():
    """Testa se a aplicação Flask pode ser criada"""
    try:
        print("\nTestando criação da aplicação...")
        
        from app import create_app
        app = create_app()
        
        print("✓ Aplicação Flask criada com sucesso")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao criar aplicação: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Iniciando testes...\n")
    
    # Testa importações
    imports_ok = test_imports()
    
    # Testa criação da aplicação
    app_ok = test_app_creation()
    
    if imports_ok and app_ok:
        print("\n✅ Todos os testes passaram! A aplicação está pronta para uso.")
    else:
        print("\n❌ Alguns testes falharam. Verifique os erros acima.")
        sys.exit(1)
