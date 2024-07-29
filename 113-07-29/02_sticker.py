import requests

URL = 'https://notify-api.line.me/api/notify/'
H, P = {}, {}
H['Authorization'] = 'Bearer ncgcrKBszCeRdtl4CCm8smbdclaiHHR7XDVjhdGDVWB'
P['message'] = '貼圖測試'
P['stickerPackageID'] = 6325
P['stickerID'] = 10979907
requests.post(URL, headers=H, params=P)

