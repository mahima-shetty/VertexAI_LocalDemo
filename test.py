import os
from google.auth import default
from dotenv import load_dotenv


load_dotenv()  # 👈 THIS is required to load .env values
creds, project = default()
print("Detected Project:", project)
print("Cred Path:", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

# import os
# print(os.path.exists("C:/Users/msshe/AppData/Roaming/gcloud/application_default_credentials.json"))
