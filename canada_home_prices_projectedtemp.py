import random as ran
import folium

m = folium.Map(location = [52.87678524411274, -90.39048415746682], zoom_start = 4)
tooltip = "Click for More Info"

start_lat = 60.0000
start_long = -140.00000
add_degrees = 2

description_text = "has a projected change in mean number of +30C days by:{} Click this link for more information:\
                    https://climateatlas.ca/map/canada/plus30_2030_85#z=4&lat=62.55&lng=-113.99&grid=1166"
# YAKUTAT, yakclimate = (start_lat, start_long), 0.7
# TATSHENSHINI_RIVER, tatclimate = (start_lat, -138.0), 0.5
# SKAGWAY, skagclimate = (start_lat, -136.0), 0.4
# ATLIN, atlinclimate = (start_lat, -134.0), 0.8
grid_names = ["YAKUTAT","TATSHENSHINI_RIVER","SKAGWAY", "ATLIN"]
grid_names_climate = {"YAKUTAT" : 0.7, "TATSHENSHINI_RIVER" : 0.5, "SKAGWAY" : 0.4, "ATLIN" : 0.8}
grid_coordinates = {1 : [start_lat, start_long], 2 : [start_lat, -138.0], 3 : [start_lat, -136.0], 4 : [start_lat, -134.0]}


def long_add(start_long, start_lat):
    if start_lat == 60.0:
        for i in range(40):
            start_long += add_degrees
            return start_long


# print(long_add(start_long, start_lat))
def description(phrase):
    for stat_num in range(10):
        temp = str(grid_names[stat_num])
        if phrase == "statement{}".format(stat_num):
            statement = ("{} has aa projected change in mean number of +30C days by:{} Click this link for more "
                          "information: https://climateatlas.ca/map/canada/plus30_2030_85#z=4&lat=62.55&lng=-113.99&grid=1166"
                            .format(grid_names[stat_num],grid_names_climate[temp]))
            return statement

        elif phrase == "statement2":
            statement2 = ("{} has a projected change in mean number of +30C days by:{} Click this link for "
                          "more information: https://climateatlas.ca/map/canada/plus30_2030_85#z=4&lat=62.55&lng=-113.99&grid=1166" \
                             .format(grid_names[stat_num],grid_names_climate[temp]))
            return(statement2) 
        elif phrase == "statement3":
            statement2 = ("{} has a projected change in mean number of +30C days by:{} Click this link for "
                          "more information: https://climateatlas.ca/map/canada/plus30_2030_85#z=4&lat=62.55&lng=-113.99&grid=1166" \
                             .format(grid_names[stat_num],grid_names_climate[temp]))
            return(statement2)


for i in range(3):
    first_lat = ran.randint(59,60)
    last_lat = ran.uniform(0, 1)
    lat = first_lat + last_lat

    first_long = ran.randint(135, 140)
    last_long = ran.uniform(0, 1)
    long = first_long + (last_long)
    long = long * -1
    print(lat, (long))

    if lat < grid_coordinates[1][0] and lat >= 59 and long >= grid_coordinates[1][1] and long < grid_coordinates[2][1]:
        print(description("statement{}".format(i)))
        folium.Marker([lat, long],
                      popup="House {} {}".format(i, print(description("statement1")),
                      tooltip=tooltip)).add_to(m)
    elif lat < grid_coordinates[1][0] and lat >= 59 and long >= grid_coordinates[2][1] and long < grid_coordinates[3][1]:
        print(description("statement{}".format(i)))
        folium.Marker([lat, long],
                      popup="House {} {}".format(i, description("statement2")),
                      tooltip=tooltip).add_to(m)
    elif lat < grid_coordinates[1][0] and lat >= 59 and long >= grid_coordinates[3][1] and long < grid_coordinates[4][1]:
        print(description("statement{}".format(i)))
        folium.Marker([lat, long],
                      popup="House {} {}".format(i, description("statement3")),
                      tooltip=tooltip).add_to(m)


# print("House {} {}".format(i,description("statement2")))

m.save("canada_home_prices_projecttemp.html")