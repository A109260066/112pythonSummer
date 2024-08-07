import requests

URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-A0003-063'
P = {}
P['Authorization'] = 'CWA-30230C2F-8E63-4819-9379-15DA1D70F0E7'
r = requests.get(URL,params=P)
t = r.json()

n = len(t['records']['locations'][0]['location'])
for i in range(n):
    print(t['records']['locations'][0]['location'][i]['locationName'], 
          t['records']['locations'][0]['location'][i]['weatherElement'][1]['time'][1]['elementValue'][0]['value'])