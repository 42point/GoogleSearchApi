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
items = []
for line in batch:
	item = {
		'Content-Type': 'application/http',
		'Content-ID': '',
		'body': 'POST /v3/urlNotifications:publish HTTP/1.1\n'
				'Content-Type: application/json\n\n' +
				json.dumps({
					'url': line,
					'type': 'URL_UPDATED'
				})
	}
	items.append(item)

# Configure the request
headers = {
	'Authorization': f'Bearer {credentials.token}',
	'Content-Type': 'multipart/mixed'
}
data = {'multipart': items}
response = requests.post('https://indexing.googleapis.com/batch', headers=headers, json=data)

# Print the response
print(response.text)
