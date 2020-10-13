from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
CFNAME = "projects/larc-ocio-datasci-cf8a8915/locations/us-central1/functions/function-1"

if __name__ == "__main__":
    print("accessing cloud function")
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
