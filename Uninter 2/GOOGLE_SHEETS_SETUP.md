# 🔐 Configuração do Google Sheets

Este documento explica como configurar as credenciais do Google Sheets para o projeto.

## 📋 Pré-requisitos

1. Conta Google
2. Acesso ao Google Cloud Console
3. Projeto no Google Cloud

## 🚀 Passo a Passo

### 1. Criar Projeto no Google Cloud

1. Acesse [Google Cloud Console](https://console.cloud.google.com/)
2. Clique em "Selecionar projeto" > "Novo projeto"
3. Digite um nome para o projeto (ex: "uninter1-cursos")
4. Clique em "Criar"

### 2. Ativar Google Sheets API

1. No menu lateral, vá em "APIs e serviços" > "Biblioteca"
2. Procure por "Google Sheets API"
3. Clique na API e depois em "Ativar"

### 4. Criar Conta de Serviço

1. No menu lateral, vá em "APIs e serviços" > "Credenciais"
2. Clique em "Criar credenciais" > "Conta de serviço"
3. Preencha:
   - **Nome da conta de serviço**: `uninter1-sheets`
   - **Descrição**: `Conta de serviço para coleta de cursos`
4. Clique em "Criar e continuar"
5. Em "Conceder acesso a esta conta de serviço", selecione:
   - **Função**: Editor
6. Clique em "Concluído"

### 5. Gerar Chave JSON

1. Na lista de contas de serviço, clique na que você criou
2. Vá na aba "Chaves"
3. Clique em "Adicionar chave" > "Criar nova chave"
4. Selecione "JSON"
5. Clique em "Criar"
6. O arquivo será baixado automaticamente

### 6. Configurar no Projeto

1. Renomeie o arquivo baixado para `credentials.json`
2. Coloque o arquivo na raiz do projeto
3. Adicione o arquivo ao `.gitignore` (já está configurado)

### 7. Configurar Variáveis de Ambiente

No arquivo `.env`:

```env
GOOGLE_SHEETS_CREDENTIALS=credentials.json
SPREADSHEET_ID=1NPP1K8335plGHaJtSUM3ag6FZkbONEgGxISONXW3KDQ
```

### 8. Compartilhar Planilha

1. Abra a planilha: https://docs.google.com/spreadsheets/d/1NPP1K8335plGHaJtSUM3ag6FZkbONEgGxISONXW3KDQ
2. Clique em "Compartilhar"
3. Adicione o email da conta de serviço (ex: `uninter1-sheets@your-project-id.iam.gserviceaccount.com`)
4. Dê permissão de "Editor"
5. Clique em "Enviar"

## 🔍 Verificação

Para verificar se tudo está funcionando:

1. Execute o projeto: `python app.py`
2. Faça uma requisição para coletar cursos:
   ```bash
   curl -X POST http://localhost:5000/api/coletar/google-atelie
   ```
3. Verifique se os dados aparecem na planilha

## 🐛 Troubleshooting

### Erro: "Invalid credentials"

- Verifique se o arquivo `credentials.json` está no local correto
- Verifique se o email da conta de serviço tem acesso à planilha

### Erro: "API not enabled"

- Certifique-se de que a Google Sheets API está ativada no projeto

### Erro: "Permission denied"

- Verifique se a conta de serviço tem permissão de "Editor" na planilha

## 📝 Exemplo de Arquivo credentials.json

```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n",
  "client_email": "your-service-account@your-project-id.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your-service-account%40your-project-id.iam.gserviceaccount.com"
}
```

## 🔒 Segurança

⚠️ **IMPORTANTE**: Nunca commite o arquivo `credentials.json` no Git!

- O arquivo já está no `.gitignore`
- Mantenha as credenciais seguras
- Use variáveis de ambiente em produção
