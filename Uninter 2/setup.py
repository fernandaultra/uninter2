#!/usr/bin/env python3
"""
Script de setup para o projeto de coleta de cursos gratuitos
"""

import os
import sys
import subprocess
import shutil

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 ou superior é necessário")
        return False
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detectado")
    return True

def install_requirements():
    """Instala as dependências do projeto"""
    try:
        print("📦 Instalando dependências...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependências instaladas com sucesso")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def create_env_file():
    """Cria o arquivo .env se não existir"""
    if not os.path.exists('.env'):
        print("📝 Criando arquivo .env...")
        shutil.copy('env.example', '.env')
        print("✓ Arquivo .env criado")
        print("⚠️  Lembre-se de configurar as variáveis de ambiente no arquivo .env")
    else:
        print("✓ Arquivo .env já existe")

def create_data_directory():
    """Cria o diretório de dados se não existir"""
    if not os.path.exists('data'):
        print("📁 Criando diretório data...")
        os.makedirs('data')
        print("✓ Diretório data criado")
    else:
        print("✓ Diretório data já existe")

def run_tests():
    """Executa os testes básicos"""
    try:
        print("🧪 Executando testes...")
        subprocess.check_call([sys.executable, "test_app.py"])
        return True
    except subprocess.CalledProcessError:
        print("⚠️  Alguns testes falharam, mas isso pode ser normal na primeira execução")
        return False

def main():
    """Função principal do setup"""
    print("🚀 Configurando projeto de coleta de cursos gratuitos...\n")
    
    # Verifica versão do Python
    if not check_python_version():
        sys.exit(1)
    
    # Instala dependências
    if not install_requirements():
        sys.exit(1)
    
    # Cria arquivo .env
    create_env_file()
    
    # Cria diretório de dados
    create_data_directory()
    
    # Executa testes
    run_tests()
    
    print("\n🎉 Setup concluído!")
    print("\n📋 Próximos passos:")
    print("1. Configure as variáveis de ambiente no arquivo .env")
    print("2. Configure as credenciais do Google Sheets")
    print("3. Execute 'python app.py' para iniciar a aplicação")
    print("4. Acesse http://localhost:5000 para ver a API")
    
    print("\n📚 Documentação:")
    print("- Leia o README.md para instruções detalhadas")
    print("- Configure o Google Sheets conforme documentado")

if __name__ == "__main__":
    main()
