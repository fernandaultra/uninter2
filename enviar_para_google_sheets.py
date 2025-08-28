import os
import json
import gspread
import pandas as pd
from google.oauth2.service_account import Credentials

SPREADSHEET_ID = "1NPP1K8335plGHaJtSUM3ag6FZkbONEgGxISONXW3KDQ"
NOME_ABA = "Cursos Gratuitos"
ARQUIVO_EXCEL = "Cursos_Gratuitos_UNINTER_por_Curso.xlsx"

def main():
    if not os.path.exists(ARQUIVO_EXCEL):
        raise FileNotFoundError(f"Arquivo não encontrado: {ARQUIVO_EXCEL}")

    creds_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
    if not creds_json:
        raise RuntimeError("Secret GOOGLE_CREDENTIALS_JSON não foi definido no ambiente.")

    info = json.loads(creds_json)
    scopes = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    credentials = Credentials.from_service_account_info(info, scopes=scopes)
    client = gspread.authorize(credentials)

    df = pd.read_excel(ARQUIVO_EXCEL)

    sheet = client.open_by_key(SPREADSHEET_ID)
    try:
        ws = sheet.worksheet(NOME_ABA)
    except gspread.WorksheetNotFound:
        ws = sheet.add_worksheet(title=NOME_ABA, rows="100", cols="20")

    ws.clear()
    ws.append_row(df.columns.tolist())
    if not df.empty:
        ws.append_rows(df.values.tolist())

    print("✅ Cursos enviados com sucesso para a aba 'Cursos Gratuitos'!")

if __name__ == "__main__":
    main()
