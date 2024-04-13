import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd

class GoogleSheetHelper():

    def __init__(self) -> None:
        '''
        We set 2 instant parameters during initial instance.
        1. SCOPES: The permission to handle Google sheet.
        2. credential: The credential to handle Google drive.

        Remark:
        - We can checks other scope by the link below.
        https://developers.google.com/sheets/api/scopes
        - We can read more about Google sheet API from the link below.
        https://developers.google.com/sheets/api/guides/create
        '''

        self.SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
        self.credential = None

    def get_credential(self):
        '''
        Get the credential for the specific permission to handle a Google drive.

        Remark: The credential with permission is set to the instance parameter
        credential. 
        '''
        if os.path.exists("token.json"):
            self.credential = Credentials.from_authorized_user_file("token.json", self.SCOPES)

        # If there are no (valid) credentials available, let the user log in.
        if not self.credential or not self.credential.valid:
            if self.credential and self.credential.expired and self.credential.refresh_token:
                self.credential.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "Google/credentials.json", self.SCOPES
            )
                self.credential = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(self.credential.to_json())

    def read_data_from_sheet(self, sheet_id:str, range:str):
        # Create service
        service = build(
            'sheets',
            'v4',
            credentials=self.credential,
            cache_discovery=False).spreadsheets()
        
        range = range # 'Sheet1!A:B'
        result = service.values().get(spreadsheetId=sheet_id, range=range).execute()
        data = result.get('values', [])
        df = pd.DataFrame(data[1:], columns=data[0])
        print(df.head())


    def write_data_to_sheet(self, sheet_id:str, range:str, data:pd.DataFrame):

        service = build(
            'sheets',
            'v4',
            credentials=self.credential,
            cache_discovery=False).spreadsheets()

        # [1: ] to exclude the header
        data_to_write: list = data.T.reset_index().values.T.tolist()[1:]

        service.values().clear(spreadsheetId=sheet_id,
                                            range=range).execute()
        
        service.values().update(spreadsheetId=sheet_id,
                                        range=range,
                                        valueInputOption="USER_ENTERED",
                                        body={"values": data_to_write}).execute()

'''
--- Test Area ---
'''

sheet_id = "1_vsCWU5xDsb94O5Oxx7RboYrnzfHP43iejFHoT1kp40"

id = ['6', '7', '8']
names = ['A', 'B', 'C']

df = pd.DataFrame(
    list(zip(id, names))
)


gsheet_helper = GoogleSheetHelper()
gsheet_helper.get_credential()
# gsheet_helper.read_data_from_sheet(sheet_id, "Sheet1!A:B")
gsheet_helper.write_data_to_sheet(sheet_id, "Sheet1!A5", df)
