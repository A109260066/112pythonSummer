import requests

# Define the URL and headers
URL = 'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-A0003-063'
headers = {
    'Authorization': 'CWA-30230C2F-8E63-4819-9379-15DA1D70F0E7'
}

# Send the request
response = requests.get(URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Safely access the required data
    try:
        locations = data['records']['locations'][0]['location'][0]['weatherElement']
        for i, element in enumerate(locations):
            print(i, element['description'])
    except KeyError as e:
        print(f"KeyError: {e} - The JSON structure may have changed.")
else:
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")
