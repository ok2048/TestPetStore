import json
import requests

base_url='https://petstore.swagger.io/v2'

# GET-запрос
res = requests.get(f"{base_url}/pet/findByStatus", params={'status': 'available'},
                    headers = {'accept': 'application/json'})
print(res.status_code)
print(res.json())

# POST-запрос
new_pet = {"id": 0, "name": "Basik", "photoUrls": [], "tags": [], "status": "available"}
res = requests.post(f"{base_url}/pet", headers={'content-type': 'application/json'}, data=json.dumps(new_pet))
print(res.status_code)
print(res.json())
new_pet['id'] = dict(res.json())['id']

# PUT-запрос
new_pet['photoUrls'] = ['https://budibasa.com/upload/iblock/049/y4cgn308ulbwca6g4w0ztk0gzhfd730e/igrushka_magnitnaya_basik_ABB_030_3_foto.jpg']
res = requests.put(f"{base_url}/pet", headers={'content-type': 'application/json'}, data=json.dumps(new_pet))
print(res.status_code)
print(res.json())

# DELETE-запрос
res = requests.delete(f"{base_url}/pet/{new_pet['id']}")
print(res.status_code)
print(res.json())