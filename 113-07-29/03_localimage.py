import requests

URL = 'https://notify-api.line.me/api/notify/'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer ncgcrKBszCeRdtl4CCm8smbdclaiHHR7XDVjhdGDVWB'
P['message'] = '本機圖片'
F['imageFile'] = open('header.jpg', 'rb')
requests.post(URL, headers=H, params=P, files=F)