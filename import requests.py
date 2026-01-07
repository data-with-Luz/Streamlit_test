import requests
response = requests.get("https://api.frankfurter.app/latest")
print(response.json())

params = {"from":"USD", "to":"GBP", "amount":20}
res = requests.get("https://api.frankfurter.app/latest")
print(res.json())

response = requests.get("https://api.frankfurter.app/latest")
print(response.headers['Server'])
print(response.headers['Content-Type'])
print(response.headers['Content-Encoding'])

for loc_info in aw_location_res.json():
    print('{:>8} {:10} {:16} {:16}'.format(
        loc_info['Key'],
        loc_info['EnglishName'],
        loc_info['Country'][EnglishName],
        loc_info['AdministrativeArea']['EnglishName']
    ))