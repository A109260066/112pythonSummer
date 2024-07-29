import requests

URL = 'https://notify-api.line.me/api/notify/'
H, P = {}, {}
H['Authorization'] = 'Bearer ncgcrKBszCeRdtl4CCm8smbdclaiHHR7XDVjhdGDVWB'
P['message'] = '黃金獵犬'
requests.post(URL, headers=H, params=P)
