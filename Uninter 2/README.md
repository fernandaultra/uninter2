# 🎓 Coletor de Cursos Gratuitos

Sistema automatizado para coleta de cursos gratuitos de diversas plataformas educacionais, estruturado para fins educacionais.

## 🎯 Objetivo

Automatizar a coleta de cursos gratuitos em plataformas como:
- **Google Ateliê Digital** - https://learndigital.withgoogle.com/ateliedigital/courses
- **SENAI** - https://www.portaldaindustria.com.br/senai/cursos/?estado=RJ
- **Gov.br** - https://www.escolavirtual.gov.br/
- **CIEE** - https://portal.ciee.org.br/cursos

## 🏗️ Estrutura do Projeto

```
uninter1/
├── app.py                 # Aplicação principal Flask
├── requirements.txt       # Dependências Python
├── Procfile              # Configuração para deploy no Render
├── env.example           # Exemplo de variáveis de ambiente
├── README.md             # Este arquivo
├── routes/               # Rotas da API
│   ├── __init__.py
│   └── api_routes.py
├── services/             # Lógica de scraping por plataforma
│   ├── __init__.py
│   ├── base_service.py
│   ├── google_atelie_service.py
│   ├── senai_service.py
│   ├── gov_br_service.py
│   └── ciee_service.py
├── utils/                # Funções auxiliares
│   ├── __init__.py
│   └── sheets_manager.py
└── data/                 # Arquivos CSV gerados (criado automaticamente)
```

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **Flask** - Framework web
- **Selenium** - Para sites dinâmicos (Google Ateliê Digital)
- **BeautifulSoup4** - Para sites estáticos
- **Pandas** - Manipulação de dados
- **gspread** - Integração com Google Sheets
- **python-dotenv** - Variáveis de ambiente

## 📋 Pré-requisitos

1. **Python 3.11** instalado
2. **Chrome/Chromium** (para Selenium)
3. **Conta Google** com Google Sheets
4. **Credenciais do Google Sheets API**

## ⚙️ Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/fernandaultra/uninter1.git
cd uninter1
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente

Copie o arquivo `env.example` para `.env`:

```bash
cp env.example .env
```

Edite o arquivo `.env` com suas configurações:

```env
# Google Sheets Configuration
GOOGLE_SHEETS_CREDENTIALS=path/to/credentials.json
SPREADSHEET_ID=1NPP1K8335plGHaJtSUM3ag6FZkbONEgGxISONXW3KDQ

# Flask Configuration
FLASK_ENV=development
FLASK_DEBUG=True

# Selenium Configuration
SELENIUM_HEADLESS=True
SELENIUM_TIMEOUT=30
```

### 4. Configure o Google Sheets

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Crie um novo projeto
3. Ative a Google Sheets API
4. Crie uma conta de serviço
5. Baixe o arquivo JSON de credenciais
6. Coloque o arquivo no projeto e atualize o caminho no `.env`

## 🎯 Como Usar

### Executando Localmente

```bash
python app.py
```

A aplicação estará disponível em: `http://localhost:5000`

### Endpoints da API

#### 1. Coletar cursos do Google Ateliê Digital
```bash
curl -X POST http://localhost:5000/api/coletar/google-atelie
```

#### 2. Coletar cursos do SENAI
```bash
curl -X POST http://localhost:5000/api/coletar/senai
```

#### 3. Coletar cursos do Gov.br
```bash
curl -X POST http://localhost:5000/api/coletar/gov-br
```

#### 4. Coletar cursos do CIEE
```bash
curl -X POST http://localhost:5000/api/coletar/ciee
```

#### 5. Coletar cursos de todas as plataformas
```bash
curl -X POST http://localhost:5000/api/coletar/todos
```

#### 6. Health Check
```bash
curl http://localhost:5000/health
```

## 📊 Estrutura dos Dados

Os cursos coletados seguem a estrutura:

| Campo | Descrição |
|-------|-----------|
| `nome_curso` | Nome do curso |
| `area_conhecimento` | Área de conhecimento (extraída automaticamente) |
| `requisitos` | Requisitos para o curso |
| `link_inscricao` | Link para inscrição |
| `plataforma_origem` | Plataforma de origem |

## 📁 Armazenamento

### Arquivos CSV
- Os dados são salvos automaticamente em arquivos CSV na pasta `data/`
- Nomenclatura: `{plataforma}_{timestamp}.csv`

### Google Sheets
- Os dados são enviados automaticamente para a planilha do Google Sheets
- Cada plataforma tem sua própria aba
- Planilha: https://docs.google.com/spreadsheets/d/1NPP1K8335plGHaJtSUM3ag6FZkbONEgGxISONXW3KDQ

## 🚀 Deploy no Render

### 1. Conecte o repositório ao Render

1. Acesse [Render](https://render.com/)
2. Conecte sua conta GitHub
3. Selecione o repositório `uninter1`

### 2. Configure o serviço

- **Tipo**: Web Service
- **Runtime**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

### 3. Configure as variáveis de ambiente

No painel do Render, adicione as variáveis:
- `GOOGLE_SHEETS_CREDENTIALS`
- `SPREADSHEET_ID`
- `FLASK_ENV=production`

### 4. Deploy

O serviço estará disponível em: https://uninter1.onrender.com

## 🔧 Desenvolvimento

### Estrutura de Serviços

Cada plataforma tem seu próprio serviço que herda de `BaseService`:

```python
class MinhaPlataformaService(BaseService):
    def __init__(self):
        super().__init__()
        self.url = "https://minha-plataforma.com"
        self.plataforma = "Minha Plataforma"
    
    def coletar_cursos(self):
        # Implementação específica da plataforma
        pass
```

### Adicionando Nova Plataforma

1. Crie um novo arquivo em `services/`
2. Herde de `BaseService`
3. Implemente o método `coletar_cursos()`
4. Adicione a rota em `routes/api_routes.py`

## 🐛 Troubleshooting

### Problemas com Selenium

- Certifique-se de que o Chrome/Chromium está instalado
- Para Linux: `sudo apt-get install chromium-browser`
- Para Windows: Baixe o ChromeDriver manualmente

### Problemas com Google Sheets

- Verifique se as credenciais estão corretas
- Certifique-se de que a API está ativada
- Verifique se a planilha existe e é acessível

### Problemas de Coleta

- Alguns sites podem ter proteções anti-bot
- Verifique se os seletores CSS ainda são válidos
- Considere adicionar delays entre requisições

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Suporte

Para suporte, abra uma issue no GitHub ou entre em contato através do email.

---

**Desenvolvido com ❤️ para facilitar o acesso à educação gratuita**
