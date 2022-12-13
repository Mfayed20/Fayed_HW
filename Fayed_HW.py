import json
import urllib3

url = urllib3.PoolManager()
gURL = url.request('GET', 'https://reqres.in/api/unknown/2')  # good url
# gURL = url.request('GET', 'https://reqres.in/api/users/23') # error url for testing

print('\nGet request:')
print('Status code:', gURL.status)
if gURL.status != 200:
    print('There is no response from the server')
else:
    if type(gURL.data) == str:  # check if the data is string
        print('\nIt is a string')
    else:
        print('\nThe data is not a string')

    data = json.loads(gURL.data.decode('utf-8'))  # change to be json format
    print("\nData:", data)
    print("\nSelected data:")
    print('Id:', data['data']['id'])
    print('Name:', data['data']['name'])
    print('Text:', data['support']['text'])

print('\nPost request:')
rURL = url.request('POST', 'https://reqres.in/api/users', body=json.dumps(
    {'Name': 'Fayed', 'UNI': 'Alfaisal'}), headers={'Content-Type': 'application/json'})
print('Status code:', rURL.status)
print(rURL.data, '\n')
