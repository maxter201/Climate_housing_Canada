import folium

# Create map object
m = folium.Map(location = [38.790496838 , -96.735330392], zoom_start = 5)

# Global tooltip
tooltip = "Click For More Info"




# Create markers
folium.Marker([40.6943, -73.9249],
        popup = '\tNew York\t 1981- 2010 \t RCP 4.5 Average: 24.1</strong>',
        tooltip = tooltip).add_to(m)
folium.Marker([34.1139, -118.4068],
        popup = '\tLos Angeles\t 1981- 2010 \t RCP 4.5 Average: 45.8</strong>',
        tooltip = tooltip).add_to(m)
folium.Marker([41.8373, -87.6862],
        popup = '\tChicago\t 1981- 2010 \t RCP 4.5 Average: 29.0</strong>',
        tooltip = tooltip).add_to(m)
folium.Marker([32.7936, -96.7662],
        popup = '\tDallas\t 1981- 2010 \t RCP 4.5 Average: 47.9</strong>',
        tooltip = tooltip).add_to(m)
folium.Marker([40.0077, -75.1339],
        popup = '\tPhiladelphia\t 1981- 2010 \t RCP 4.5 Average: 29.1</strong>',
        tooltip = tooltip).add_to(m)
folium.Marker([29.7863, -95.3889],
        popup = '\tHouston\t 1981- 2010 \t RCP 4.5 Average: 47.9</strong>',
        tooltip = tooltip).add_to(m)
folium.Marker([38.9047, -77.0163],
        popup = '\tWashington D.C\t 1981- 2010 \t RCP 4.5 Average: 35.5</strong>',
        tooltip = tooltip).add_to(m)
folium.Marker([25.7839, -80.2102],
        popup = '\tMiami\t 1981- 2010 \t RCP 4.5 Average: 59.2</strong>',
        tooltip = tooltip).add_to(m)
folium.Marker([33.7627, -84.4224],
        popup = '\tAtlanta\t 1981- 2010 \t RCP 4.5 Average: 47.3</strong>',
        tooltip = tooltip).add_to(m)
folium.Marker([42.3188, -71.0846],
        popup = '\tBoston\t 1981- 2010 \t RCP 4.5 Average: 28.1</strong>',
        tooltip = tooltip).add_to(m)

# Generate map

m.save('map3.html')