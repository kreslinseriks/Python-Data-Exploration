import urllib.request, urllib.parse, urllib.error
import json
import ssl

# user input for latitude and longitude
latitude = input("Enter latitude: ")
longitude = input("Enter longitude: ")

# constructing the API request URL
url = 'https://nominatim.openstreetmap.org/reverse?' + urllib.parse.urlencode({
    'format': 'geojson',
    'lat': latitude,
    'lon': longitude,
    'addressdetails': 1
})

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    # sending the API request
    response = urllib.request.urlopen(url, context=ctx).read().decode()

    # loading response as JSON
    data = json.loads(response)

    # extracting the relevant information from JSON and printing the output
    if 'features' in data and len(data['features']) > 0:
        place_name = data['features'][0]['properties']['display_name']
        place_type = data['features'][0]['properties']['type']
        house_number = data['features'][0]['properties']['address'].get('house_number', '')
        street_name = data['features'][0]['properties']['address'].get('road', '')
        city = data['features'][0]['properties']['address'].get('city', '')
        postcode = data['features'][0]['properties']['address'].get('postcode', '')
        country_name = data['features'][0]['properties']['address'].get('country', '')
        country_code = data['features'][0]['properties']['address'].get('country_code', '')

        print("Place name: " + place_name)
        print("Place type: " + place_type)
        print("House number: " + house_number)
        print("Street name: " + street_name)
        print("City: " + city)
        print("Postcode: " + postcode)
        print("Country name: " + country_name)
        print("Country code: " + country_code)
    else:
        print('==== Failure To Retrieve ====')
        print(data)

except urllib.error.URLError as e:
    print('==== Failure to establish connection ====')
except (ValueError, KeyError):
    print('==== Failure To Retrieve ====')
