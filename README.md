# Flask API Project

Projeto Flask simples com estrutura organizada e boas práticas de desenvolvimento.

## 📁 Estrutura do Projeto

```
projeto/
├── app.py                 # Ponto de entrada da aplicação
├── routes/
│   └── example_routes.py  # Definição das rotas da API
├── services/
│   └── example_service.py # Lógica de negócio
├── utils/
│   └── env_loader.py      # Carregamento de variáveis de ambiente
├── .env.example           # Exemplo de variáveis de ambiente
├── requirements.txt       # Dependências do projeto
├── Procfile              # Configuração para deploy no Render
└── README.md             # Este arquivo
```

## 🚀 Como Executar

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente

Copie o arquivo `env.example` para `.env` e configure as variáveis:

```bash
cp env.example .env
```

Edite o arquivo `.env` com suas configurações:

```env
SECRET_KEY=sua_chave_secreta_aqui
```

### 3. Executar a Aplicação

```bash
python app.py
```

A aplicação estará disponível em: `http://localhost:5000`

## 📋 Endpoints Disponíveis

### Rota Raiz
- **GET** `/` - Página de boas-vindas com informações da API

### API Endpoints
- **GET** `/api/hello` - Retorna mensagem "Hello, UNINTER!"
- **GET** `/api/info` - Informações sobre a aplicação
- **GET** `/api/health` - Verificação de saúde da aplicação

### Exemplo de Resposta `/api/hello`:

```json
{
  "message": "Hello, UNINTER!",
  "timestamp": "2024-01-20T10:30:00.123456",
  "status": "success"
}
```

## 🛠️ Tecnologias Utilizadas

- **Flask** 2.3.3 - Framework web
- **python-dotenv** 1.0.0 - Carregamento de variáveis de ambiente

## 📦 Deploy no Render

O projeto está configurado para deploy no Render usando o arquivo `Procfile`. 

1. Conecte seu repositório no Render
2. Configure as variáveis de ambiente na dashboard do Render
3. O deploy será automático usando o comando: `web: python app.py`

## 🏗️ Arquitetura

O projeto segue uma arquitetura modular:

- **`app.py`**: Configuração principal e inicialização da aplicação
- **`routes/`**: Definição de endpoints usando Flask Blueprints
- **`services/`**: Lógica de negócio separada das rotas
- **`utils/`**: Funções utilitárias (carregamento de ambiente, etc.)

## 📝 Boas Práticas Implementadas

- ✅ Separação de responsabilidades
- ✅ Uso de Flask Blueprints
- ✅ Tratamento de erros
- ✅ Carregamento seguro de variáveis de ambiente
- ✅ Estrutura de pastas organizada
- ✅ Código comentado e documentado
- ✅ Factory pattern para criação da aplicação

## 🔧 Desenvolvimento

Para adicionar novos endpoints:

1. Crie a lógica no arquivo apropriado em `services/`
2. Adicione a rota em `routes/` ou crie um novo arquivo de rotas
3. Registre o blueprint em `app.py`

Exemplo de nova rota:

```python
# Em routes/example_routes.py
@example_bp.route('/new-endpoint', methods=['GET'])
def new_endpoint():
    return jsonify({"message": "Novo endpoint!"})
```