from oauth2client.service_account import ServiceAccountCredentials
import httplib2

class GoogleSearchIndexingAPI:
    def __init__(self, json_key_file):
        self.scopes = ["https://www.googleapis.com/auth/indexing"]
        self.post_endpoint = "https://indexing.googleapis.com/v3/urlNotifications:publish"
        self.get_endpoint = "https://indexing.googleapis.com/v3/urlNotifications/metadata"
        self.json_key_file = json_key_file
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(self.json_key_file, scopes=self.scopes)
        self.http = self.credentials.authorize(httplib2.Http())

        # service_account_file.json is the private key that you created for your service account.
        # JSON_KEY_FILE = "wcserviceacct-395120-bc4ff100af94.json"

    def submit_new_page(self, page_url):
        content = f"""{{
            "url": "{page_url}",
            "type": "URL_UPDATED"
        }}"""
        
        print('Submitting:', content)
        
        try:
            response, content = self.http.request(self.post_endpoint, method="POST", body=content, headers={"Content-Type": "application/json"})
            print("POST response:", response)
            return response
        except Exception as e:
            print("An error occurred during submission:", e)
            return None

    def validate_page_submission(self, page_url):
        try:
            response, content = self.http.request(f"{self.get_endpoint}?url={page_url}", method="GET")
            print("GET (validate) response:", content)
            return content
        except Exception as e:
            print("An error occurred during validation:", e)
            return None

# Usage Example
# Create an instance of the GoogleSearchIndexingAPI class with the path to your JSON key file.

# indexing_api = GoogleSearchIndexingAPI("wcserviceacct-395120-bc4ff100af94.json")
# response = indexing_api.submit_new_page("https://example.com/new-page")
# Uncomment the line below to validate the submission
# validation_response = indexing_api.validate_page_submission("https://example.com/new-page")
