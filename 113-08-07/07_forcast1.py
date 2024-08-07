import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-A0003-063'
P = {}
P['Authorization'] = 'CWA-30230C2F-8E63-4819-9379-15DA1D70F0E7'
r = requests.get(URL,params=P)
t = r.json()

n = len(t['records']['locations'][0]['location'][0]['weatherElement'])
for i in range(n):
    print(i, t['records']['locations'][0]['location'][0]['weatherElement'][i]['description'])
