import json
import requests
from google.oauth2 import service_account
from google.auth.transport.requests import Request

# Load the service account key
key_path = './service_account.json'
credentials = service_account.Credentials.from_service_account_file(
	key_path,
	scopes=['https://www.googleapis.com/auth/indexing'],
)

# Refresh the credentials if necessary
if not credentials.valid or credentials.expired:
	credentials.refresh(Request())

# Read the batch of URLs from a file
with open('urls.txt', 'r') as file:
	batch = file.read().splitlines()

# Prepare the batch request
boundary = 'batch_foobarbaz'  # Define a boundary string
body = ''
for line in batch:
	body += '--' + boundary + '\n'
	body += 'Content-Type: application/http\n'
	body += '\n'
	body += 'POST /v3/urlNotifications:publish HTTP/1.1\n'
	body += 'Content-Type: application/json; charset=utf-8\n'
	body += '\n'
	body += json.dumps({'url': line, 'type': 'URL_UPDATED'}) + '\n'

body += '--' + boundary + '--'

# Configure the request
headers = {
	'Authorization': f'Bearer {credentials.token}',
	'Content-Type': 'multipart/mixed; boundary=' + boundary
}
response = requests.post('https://indexing.googleapis.com/batch', headers=headers, data=body)

# Print the response
print(response.text)
