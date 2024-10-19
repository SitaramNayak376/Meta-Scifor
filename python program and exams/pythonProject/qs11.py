import requests

response_get = requests.get('https://api.quotable.io/random')
print('status code(GET): {response_get.status_code}')
print('Response(GET):', response_get.json())

payload = {'key1':'value1','key2': 'value2'}
response_post = requests.post(' https://api.quotable.io/random',json = payload)
print('status code(post): {response_post.status_code}')
print('Response(POST):', response_post.json())
