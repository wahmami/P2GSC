from googleapiclient.discovery import build
from google.oauth2 import service_account


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = 'sarout.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of a sample spreadsheet.
SPREADSHEET_ID = "1Jikc_g2dxe3qOYcS1HqnpfW1P7cInADKvoQolZunXwE"

service = build("sheets", "v4", credentials=creds)

request_body = {
    'requests': [
        {
            'addSheet': {
                'properties': {
                    'title':'2526',         #SHEET TITLE
                    'gridProperties': {
                        'rowCount': 20,
                        'columnCount':10
                    },
                }
            }
        }
    ]
}

service.spreadsheets().batchUpdate(
    spreadsheetId = SPREADSHEET_ID,
    body = request_body
).execute()
