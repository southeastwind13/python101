import os.path
import base64
import mimetypes

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage

class GoogleMailHelper():

    def __init__(self) -> None:
        '''
        We set 2 instant parameters during initial instance.
        1. SCOPES: The permission to handle Google drive.
        2. credential: The credential to handle Google drive.

        Remark:
        - We can checks more functionality in the link below.
        https://developers.google.com/gmail/api/quickstart/python
        - We can checks other scope by the link below.
        https://developers.google.com/drive/api/guides/api-specific-auth
        '''

        self.SCOPES = ["https://mail.google.com/"]
        self.credential = None

    def get_credential(self):
            '''
            Get the credential for the specific permission to handle a Google mail.

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

    def get_labels(self):
         '''
         Get all labels in the specific email.

         :return: The list of labels. 
         '''
         service = build("gmail", "v1", credentials=self.credential)

         results = service.users().labels().list(userId="me").execute()
         labels = results.get("labels", [])

         if not labels:
            print("No labels found.")
            return
         else:
             return [label["name"] for label in labels]
         
        #  print("Labels:")
        #  for label in labels:
        #     print(label["name"])

    def create_draft_email(self, to_email:str, from_email:str, subject:str, content:str):
        service = build("gmail", "v1", credentials=self.credential)

        message = EmailMessage()

        message.set_content(content)
        message["To"] = to_email
        message["From"] = from_email
        message["Subject"] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"message": {"raw": encoded_message}}
        # pylint: disable=E1101
        draft = (
            service.users()
            .drafts()
            .create(userId="me", body=create_message)
            .execute()
        )

        print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')


    def send_email(self, to_email:str, from_email:str, subject:str, content:str, attachments:list):

        service = build("gmail", "v1", credentials=self.credential)

        message = EmailMessage()

        message.set_content(content)
        message["To"] = to_email
        message["From"] = from_email
        message["Subject"] = subject

        if attachments:
            for attachment in attachments:

                # attachment
                attachment_filename = attachment
                filename = GoogleMailHelper._get_file_name_from_path(attachment_filename)

                # guessing the MIME type
                type_subtype, _ = mimetypes.guess_type(attachment_filename)
                maintype, subtype = type_subtype.split("/")

                with open(attachment_filename, 'rb') as content_file:
                    type_subtype, _ = mimetypes.guess_type(attachment_filename)
                    maintype, subtype = type_subtype.split("/")

                    content = content_file.read()
                    message.add_attachment(content, maintype=maintype, subtype=subtype , filename=f"{filename}.{subtype}")

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )

        print(f'Message Id: {send_message["id"]}')

    def read_message(self, email_from:str='', after_time:str='', is_download_attachment=False):
        service = build("gmail", "v1", credentials=self.credential)

        # Prepare query message
        query_message = 'is:unread'

        if email_from != '':
            query_message += f' from:{email_from}'
        
        if after_time != '':
            query_message += f' after:{after_time}'

        results = service.users().messages().list(
            userId='me', 
            # labelIds=[''], 
            q=query_message 
            ).execute()
        
        messages = results.get('messages',[])

        for idx, message in enumerate(messages):
            if idx == 0:
                msg = service.users().messages().get(userId='me', id=message['id']).execute()
                email_data = msg['payload']['headers']

                for values in email_data:
                    name = values['name']
                    if name == 'From':
                        from_name = values['value'] 
                    if name == 'Subject':
                        subject = values['value']
                    if name == 'Date':
                        date = values['value']

                if 'parts' in msg['payload']:
                    complete = False
                    parts = msg['payload']['parts']

                    # Get data content from the content-type text
                    while not complete:

                        headers = parts[0]['headers']
                   
                        for value in headers:
                            name = value['name']
                            if name == 'Content-Type':
                                content_type = value['value']
                                if 'text' in content_type:
                                    complete = True
                                    data = parts[0]['body']['data']
                                else:
                                    parts = parts[0]['parts']


                else:
                    data = data = msg['payload']['body']['data']

                
                byte_code = base64.urlsafe_b64decode(data)
                text = byte_code.decode("utf-8")

                is_download_attachment = True

                
                                      
            

                if is_download_attachment:

                    number_of_files = len(msg['payload']['parts']) - 1

                    for idx in range(number_of_files):
                                          
                        attchment_id = msg['payload']['parts'][idx + 1]['body']['attachmentId']
                        file_name = msg['payload']['parts'][idx + 1]['filename']
                    
                    
                        # print(len(msg['payload']['parts']))
                    
                        attachment = service.users().messages().attachments().get(
                            userId="me", messageId=message['id'], id=attchment_id
                        ).execute()
                        file_data = base64.urlsafe_b64decode(attachment['data'].encode('UTF-8'))

                
                        if file_data:
                            #do some staff, e.g.
                            path = f'Google/download/{file_name}'
                            print(path)
                            with open(path, 'wb') as f:
                                f.write(file_data)

                return {
                    'from': from_name,
                    'subject': subject,
                    'date': date,
                    'content': text
                }

    def _get_file_name_from_path(file_path:str):
        '''
        Private function for get filename without extension from the filepath.

        :param str file_path: The path of the file.
        :return: The file name without extension.

        e.g. 
        input /google/test/picture.png
        return picture
        '''
        if '/' in file_path:
            split_file_path = file_path.split('/')
            if '.' in split_file_path[-1]:
                split_file_name = split_file_path[-1].split('.')
                return(split_file_name[-2])
            else:
                return(split_file_path[-1])
        elif '.' in file_path:
            split_file_name = file_path.split('.')
            return(split_file_name[-2])
        else:
            return(file_path)


attachments = ['Google/test_upload_file.csv', 'Google/test.png']


gmail_helper = GoogleMailHelper()
gmail_helper.get_credential()
# email_from="Baanpermsook@gmail.com", after_time="1713027600"
data = gmail_helper.read_message(email_from="Baanpermsook@gmail.com")

# labels = gmail_helper.get_labels()
# gmail_helper.send_email(
#     to_email="baanpermsook@gmail.com",
#     from_email="w.wattcharapong@gmail.com",
#     subject="Test send email",
#     content="My test automate send email",
#     attachments=attachments
# )



# msg = [{'partId': '0', 'mimeType': 'multipart/alternative', 'filename': '', 'headers': [{'name': 'Content-Type', 'value': 'multipart/alternative; boundary="00000000000039435c06160f121d"'}], 'body': {'size': 0}, 'parts': [{'partId': '0.0', 'mimeType': 'text/plain', 'filename': '', 'headers': [{'name': 'Content-Type', 'value': 'text/plain; charset="UTF-8"'}, {'name': 'Content-Transfer-Encoding', 'value': 'base64'}], 'body': {'size': 653, 'data': 'dGVzdENvbnRlbnQNCi0tIA0KDQoqLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0qDQoq4Lia4LmJ4Liy4LiZ4LmA4Lie4Li04LmI4Lih4Liq4Li44LiCIOC4q-C5ieC4reC4h-C4nuC4seC4geC4o-C4suC4ouC4p-C4seC4mSDguYDguKHguLfguK3guIfguJfguK3guIcqDQoNCjQ5LzIzIOC4i-C4reC4ouC4leC4tOC4p-C4suC4meC4meC4l-C5jCAtIOC4m-C4suC4geC5gOC4geC4o-C5h-C4lCAzNCAo4LiL4Lit4Lii4LiH4Lia4Lib4Lij4Liw4Lih4Liy4LiTIDM0KQ0KDQrguYDguKHguLfguK3guIfguJfguK3guIcg4Lib4Liy4LiB4LmA4LiB4Lij4LmH4LiUIOC4meC4meC4l-C4muC4uOC4o-C4tSAxMTEyMCDguJvguKPguLDguYDguJfguKjguYTguJfguKINCg0KVGVsLiAwOTQtOTYyLTU5NTUsIDA5OS0xNTktOTIyMg0KDQpXZWJzaXRlIDogaHR0cDovL3d3dy5iYWFucGVybXNvb2suY29tDQo='}}, {'partId': '0.1', 'mimeType': 'text/html', 'filename': '', 'headers': [{'name': 'Content-Type', 'value': 'text/html; charset="UTF-8"'}, {'name': 'Content-Transfer-Encoding', 'value': 'base64'}], 'body': {'size': 1141, 'data': 'PGRpdiBkaXI9Imx0ciI-PGJyIGNsZWFyPSJhbGwiPjxkaXY-dGVzdENvbnRlbnQ8L2Rpdj48c3BhbiBjbGFzcz0iZ21haWxfc2lnbmF0dXJlX3ByZWZpeCI-LS0gPC9zcGFuPjxicj48ZGl2IGRpcj0ibHRyIiBjbGFzcz0iZ21haWxfc2lnbmF0dXJlIiBkYXRhLXNtYXJ0bWFpbD0iZ21haWxfc2lnbmF0dXJlIj48ZGl2IGRpcj0ibHRyIj48ZGl2PjxkaXYgZGlyPSJsdHIiPjxkaXYgZGlyPSJsdHIiPjxwPjxiPjxzcGFuIHN0eWxlPSJmb250LXNpemU6My4wcHQ7Zm9udC1mYW1pbHk6JnF1b3Q7Q2VudHVyeSBHb3RoaWMmcXVvdDssc2Fucy1zZXJpZjtjb2xvcjojN2Y3ZjdmIj4tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTwvc3Bhbj48L2I-PC9wPg0KDQo8Zm9udCBjb2xvcj0iIzQ0NDQ0NCI-PGI-PGZvbnQgc2l6ZT0iNCI-4Lia4LmJ4Liy4LiZ4LmA4Lie4Li04LmI4Lih4Liq4Li44LiCIOC4q-C5ieC4reC4h-C4nuC4seC4geC4o-C4suC4ouC4p-C4seC4mSDguYDguKHguLfguK3guIfguJfguK3guIc8L2ZvbnQ-PC9iPjxicj48YnI-NDkvMjMg4LiL4Lit4Lii4LiV4Li04Lin4Liy4LiZ4LiZ4LiX4LmMIC0g4Lib4Liy4LiB4LmA4LiB4Lij4LmH4LiUIDM0ICjguIvguK3guKLguIfguJrguJvguKPguLDguKHguLLguJMgMzQpIDxicj48YnI-4LmA4Lih4Li34Lit4LiH4LiX4Lit4LiHIOC4m-C4suC4geC5gOC4geC4o-C5h-C4lCDguJnguJnguJfguJrguLjguKPguLUgMTExMjAg4Lib4Lij4Liw4LmA4LiX4Lio4LmE4LiX4LiiPGJyPjxicj5UZWwuIDA5NC05NjItNTk1NSwgMDk5LTE1OS05MjIyPGJyPjxicj5XZWJzaXRlIDogPGEgaHJlZj0iaHR0cDovL3d3dy5iYWFucGVybXNvb2suY29tIiB0YXJnZXQ9Il9ibGFuayI-aHR0cDovL3d3dy5iYWFucGVybXNvb2suY29tPC9hPjwvZm9udD48L2Rpdj48L2Rpdj48L2Rpdj48L2Rpdj48L2Rpdj48L2Rpdj4NCg=='}}]}, {'partId': '1', 'mimeType': 'image/png', 'filename': 'Screen Shot 2567-04-14 at 16.16.27.png', 'headers': [{'name': 'Content-Type', 'value': 'image/png; name="Screen Shot 2567-04-14 at 16.16.27.png"'}, {'name': 'Content-Disposition', 'value': 'attachment; filename="Screen Shot 2567-04-14 at 16.16.27.png"'}, {'name': 'Content-Transfer-Encoding', 'value': 'base64'}, {'name': 'Content-ID', 'value': '<f_luzlsc4o0>'}, {'name': 'X-Attachment-Id', 'value': 'f_luzlsc4o0'}], 'body': {'attachmentId': 'ANGjdJ_vEJi30Ubr-0UqzjAFjIxFj5L6bPVjhPFCp2qNyHBhcdiFp15-RanAuWloc-6sapXB852yy7JCyVFBhxI1uqte4MpKsBFfrQHrgx0JChBDJ26hvw13WuDTe3eJM8MmmD6OSV67NS9osby4T2w-k538KoZoUIfYL__r1EhcntBSZkr034llUe5Do9no_myVooLXj-_nNANauWOil8SkBOmPJeoGR3xPxZwbdxtjDTml9YUuaSj-MVWRkk0o8LbXTCLG9IRBRmygxvbCQ7krnKz8CmIgOI5D-KSNdj34nzoWs0X1BSRHrjIcHL3L9MCqqaenq6Lxj-yCjUQtbrB-DHLTGQFPgjekKcgK-mQl2tcTEFEFoMmGnFaCyabmW5NorR4ohsmWJvjxdpOp', 'size': 565359}}]
# print(msg[0]['parts'][0]['body']['data'])
# print(msg[1])
# data = msg['payload']['parts'][0]['body']['data']