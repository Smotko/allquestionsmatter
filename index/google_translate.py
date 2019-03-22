import json
import os
from google.oauth2 import service_account
from google.cloud import translate


def get_translate_client():
    service_account_info = json.loads(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))
    credentials = service_account.Credentials.from_service_account_info(
        service_account_info
    )
    return translate.Client(credentials=credentials)
