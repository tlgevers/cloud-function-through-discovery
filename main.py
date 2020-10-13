from google.oauth2 import service_account
import os

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
PROJECT_NAME = os.getenv("PROJECT_NAME")
LOCATION = os.getenv("LOCATION")


if __name__ == "__main__":
    print("accessing cloud function")
    CFNAME = f"projects/{PROJECT_NAME}/locations/{LOCATION}/functions/function-1"
    import googleapiclient.discovery
    SERVICE_ACCOUNT_FILE = 'service-account.json'

    credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    try:
        cfs = googleapiclient.discovery.build('cloudfunctions', 'v1', credentials=credentials)
        print(cfs)
        body = {'data': '{ "message": "Yellow"}'}
        res = cfs.projects().locations().functions().call(name=CFNAME, body=body).execute()
        print(res)
    except Exception as e:
        print(e)
