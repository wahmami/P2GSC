from googleapiclient.discovery import build
from google.oauth2 import service_account
import streamlit as st
import pandas as pd


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_FILE = 'sarout.py'

creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_FILE, scopes=SCOPES)

# The ID of a sample spreadsheet.
SPREADSHEET_ID = "1Jikc_g2dxe3qOYcS1HqnpfW1P7cInADKvoQolZunXwE"

service = build("sheets", "v4", credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()

result = (
    sheet.values()
    .get(spreadsheetId=SPREADSHEET_ID, range="2425!A1:Z1000")     #Sheet!Range(A1:X9)
    .execute()
)
values = result.get("values", [])

st.header("Ecole Nour Alfitra", divider="rainbow")
st.subheader("Liste des élèves")

options = st.multiselect(
    "Classes: ", ["PS", "MS", "GS", "CP", "CE1", "CE2", "CM1", "CM2", "CE6"],
    ["CP", "CE1", "CE2", "CM1", "CM2", "CE6"],
)

df= pd.DataFrame(values)
df.columns = df.iloc[0]
df = df[1:]
st.dataframe(df[df['Niveau'].isin(options)])
