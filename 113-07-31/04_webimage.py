import requests

IMG = 'https://img.4gamers.com.tw/puku-clone-version/ddfdbfd0792f5858f3d766100be2f50675194b5d.webp'
URL = 'https://notify-api.line.me/api/notify/'
H, P, F = {}, {}, {}
H['Authorization'] = 'Bearer ncgcrKBszCeRdtl4CCm8smbdclaiHHR7XDVjhdGDVWB'
P['message'] = '網路圖片'
F['imageFile'] = requests.get(IMG).content
response = requests.post(URL, headers=H, params=P, files=F)

print(response.status_code)
print(response.text)