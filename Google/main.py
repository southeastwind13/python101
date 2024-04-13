from google_auth_helper import GoogldAuthHelper

client_secret_path = "Google/client_secret_529489852448-6bq97e7cfuel5c8jgf782189j6leob2f.apps.googleusercontent.com.json"
creds = GoogldAuthHelper.get_authentication(client_secret_path)


print("hello")