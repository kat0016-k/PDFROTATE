import requests
import json

instructions = {
  'actions': [
    {
      'angle_of_rotation': 90,
      'page_number': 3,
    }
  ]
}

payload = {
  'instructions': json.dumps(instructions)
}

# headers = {
#   'Authorization': 'Bearer your_api_key_here'
# }

files = {
  'document': open('kartik.pdf', 'rb')
}

response = requests.request(
  'POST',
  'http://127.0.0.1:5000/PDF',
  files=files,
  data=payload,
  stream=True
)

with open('result.pdf', 'wb') as fd:
  for chunk in response.iter_content(chunk_size=8096):
    fd.write(chunk)