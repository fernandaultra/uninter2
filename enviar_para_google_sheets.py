import pandas as pd
import gspread
import os
import json
from google.oauth2.service_account import Credentials

# === CONFIGURAÇÕES ===
SPREADSHEET_ID = "1NPP1K8335plGHaJtSUM3ag6FZkbONEgGxISONXW3KDQ"
NOME_ABA = "Cursos Gratuitos"
ARQUIVO_EXCEL = "Cursos_Gratuitos_UNINTER_por_Curso.xlsx"

# === 1. LER O ARQUIVO EXCEL COM OS CURSOS ===
df = pd.read_excel(ARQUIVO_EXCEL)

# === 2. AUTENTICAÇÃO COM GOOGLE SHEETS USANDO VARIÁVEL DE AMBIENTE ===
GOOGLE_CREDENTIALS_JSON = os.environ["GOOGLE_CREDENTIALS_JSON"]
info = json.loads(GOOGLE_CREDENTIALS_JSON)

scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

credenciais = Credentials.from_service_account_info(info, scopes=scopes)
cliente = gspread.authorize(credenciais)

# === 3. ABRIR PLANILHA E ABA ===
planilha = cliente.open_by_key(SPREADSHEET_ID)

try:
    aba = planilha.worksheet(NOME_ABA)
except gspread.WorksheetNotFound:
    aba = planilha.add_worksheet(title=NOME_ABA, rows="100", cols="20")

# === 4. ENVIAR OS DADOS PARA A ABA ===
aba.clear()
aba.append_row(df.columns.tolist())
aba.append_rows(df.values.tolist())

print("✅ Cursos enviados com sucesso para a aba 'Cursos Gratuitos'!")
