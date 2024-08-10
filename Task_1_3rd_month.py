import requests
import folium

# Function to get geolocation data using IP address
def get_geolocation(ip_address=""):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to create a map and display the geolocation
def create_map(location_data):
    # Extracting latitude and longitude from the location data
    loc = location_data['loc'].split(',')
    latitude = float(loc[0])
    longitude = float(loc[1])
    
    # Create a map centered around the latitude and longitude
    geo_map = folium.Map(location=[latitude, longitude], zoom_start=10)
    
    # Add a marker to the location
    folium.Marker([latitude, longitude], popup=f"{location_data['city']}, {location_data['country']}").add_to(geo_map)
    
    # Save the map as an HTML file
    geo_map.save("geolocation_map.html")
    print("Map has been saved as 'geolocation_map.html'.")

# Fetch the geolocation data
location_data = get_geolocation()

# Check if the data was fetched successfully
if location_data:
    create_map(location_data)
else:
    print("Failed to retrieve geolocation data.")


