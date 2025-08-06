"""
Módulo para carregar variáveis de ambiente usando python-dotenv.
Este módulo centraliza a configuração de variáveis de ambiente da aplicação.
"""

import os
from dotenv import load_dotenv


def load_environment_variables():
    """
    Carrega as variáveis de ambiente do arquivo .env
    
    Returns:
        bool: True se o arquivo .env foi encontrado e carregado, False caso contrário
    """
    # Carrega o arquivo .env se existir
    env_loaded = load_dotenv()
    
    if env_loaded:
        print("Variáveis de ambiente carregadas com sucesso!")
    else:
        print("Arquivo .env não encontrado. Usando variáveis de ambiente do sistema.")
    
    return env_loaded


def get_secret_key():
    """
    Obtém a SECRET_KEY das variáveis de ambiente
    
    Returns:
        str: A chave secreta ou uma chave padrão se não estiver definida
    """
    secret_key = os.getenv('SECRET_KEY', 'chave-padrao-desenvolvimento')
    
    if secret_key == 'chave-padrao-desenvolvimento':
        print("AVISO: Usando chave secreta padrão. Configure SECRET_KEY no arquivo .env para produção!")
    
    return secret_key


def get_env_variable(variable_name, default_value=None):
    """
    Função utilitária para obter qualquer variável de ambiente
    
    Args:
        variable_name (str): Nome da variável de ambiente
        default_value (str, optional): Valor padrão se a variável não existir
    
    Returns:
        str: Valor da variável de ambiente ou valor padrão
    """
    return os.getenv(variable_name, default_value)