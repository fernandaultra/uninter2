"""
Módulo de serviços para lógica de negócio da aplicação.
Este arquivo contém as funções que implementam a lógica de negócio,
separando-a das rotas para manter o código organizado.
"""

from datetime import datetime


class ExampleService:
    """
    Classe de serviço com métodos para lógica de negócio relacionada aos exemplos.
    """
    
    @staticmethod
    def get_hello_message():
        """
        Gera a mensagem de saudação para o endpoint /api/hello
        
        Returns:
            dict: Dicionário com a mensagem de saudação e timestamp
        """
        return {
            "message": "Hello, UNINTER!",
            "timestamp": datetime.now().isoformat(),
            "status": "success"
        }
    
    @staticmethod
    def get_app_info():
        """
        Retorna informações básicas sobre a aplicação
        
        Returns:
            dict: Informações da aplicação
        """
        return {
            "app_name": "Flask API Example",
            "version": "1.0.0",
            "description": "Projeto Flask simples com estrutura organizada",
            "framework": "Flask",
            "language": "Python"
        }
    
    @staticmethod
    def validate_request_data(data):
        """
        Método exemplo para validação de dados de requisição
        
        Args:
            data (dict): Dados da requisição para validar
            
        Returns:
            tuple: (is_valid, error_message)
        """
        if not data:
            return False, "Dados não fornecidos"
        
        # Exemplo de validação simples
        if not isinstance(data, dict):
            return False, "Dados devem estar em formato JSON"
        
        return True, None