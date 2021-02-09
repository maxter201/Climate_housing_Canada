import random as ran
import folium


m = folium.Map(location = [52.87678524411274, -90.39048415746682], zoom_start = 4)
tooltip = "Click for More Info"
url = {"YAKUTAT" : "https://climateatlas.ca/map/canada/plus30_2030_85#z=4&lat=62.55&lng=-113.99&grid=1166",
        "TATSHENSHINI_RIVER" : "https://climateatlas.ca/map/canada/plus30_2030_85#z=4&lat=62.55&lng=-113.99&grid=1166",
        "SKAGWAY" :  "https://climateatlas.ca/map/canada/plus30_2030_85#z=4&lat=62.55&lng=-113.99&grid=1166",
        "ATLIN" : "https://climateatlas.ca/map/canada/plus30_2030_85#z=6&lat=59.83&lng=-130.94&grid=1100",
       "JENNINGS RIVER" : "https://climateatlas.ca/map/canada/plus30_2030_85#z=4&lat=62.55&lng=-113.99&grid=1101"

}

start_lat = 60.0000
end_lat = 58.0
start_long = -140.00000
add_degrees = 2

description_text = "{} has a projected change in mean number of +30C days by:{} Click this link for more \
                        information: {}"


grid_names = ["YAKUTAT","TATSHENSHINI_RIVER","SKAGWAY", "ATLIN","JENNINGS RIVER", "MCDAME", "RABBIT RIVER",
              "TOAD RIVER", "MAXHAMISH LAKE", "PETITOT RIVER", "STEEN RIVER", "WHITESAND RIVER", "PEACE POINT",
              "FITZGERALD", "TAZIN LAKE", "FOND-DU-LAC", "STONY RAPIDS", "PHELPS LAKE", "KASMERE LAKE",
              "MUNROE LAKE", "NEJANILINI LAKE"]
grid_names_climate = {"YAKUTAT" : 0.7, "TATSHENSHINI_RIVER" : 0.5, "SKAGWAY" : 0.4, "ATLIN" : 0.8,
                      "JENNINGS RIVER" : 0.6, "MCDAME" : 1.5, "RABBIT RIVER" : 2.1, "TOAD RIVER" : 2.4,
                      "MAXHAMISH LAKE" : 4.0, "PETITOT RIVER" : 3.1, "STEEN RIVER" : 3.7, "WHITESAND RIVER" : 2.1,
                      "PEACE POINT" : 4.5, "FITZGERALD" : 4.0, "TAZIN LAKE" : 2.8, "FOND-DU-LAC" : 2.6,
                      "STONY RAPIDS" : 2.1, "PHELPS LAKE": 1.2, "KASMERE LAKE" : 1.0, "MUNROE LAKE" : 0.8,
                      "NEJANILINI LAKE" : 0.6, "CARIBOU RIVER" : 0.7}
grid_coordinates = {0 : [start_lat, start_long], 1 : [start_lat, -138.0], 2 : [start_lat, -136.0],
                    3 : [start_lat, -134.0], 4 : [start_lat, -132.0], 5 : [start_lat, -130.0],
                    6 : [start_lat, -128.0],  7 : [start_lat, -126.0], 8 : [start_lat, -124.0],
                    9 : [start_lat, -122.0], 10 : [start_lat, -120.0], 11 : [start_lat, -118.0],
                    12 : [start_lat, -116.0], 13 : [start_lat, -114.0], 14 : [start_lat, -112.0],
                    15 : [start_lat, -110.0], 16 : [start_lat, -108.0], 17 : [start_lat, -106.0],
                    18 : [start_lat, -104.0], 19 : [start_lat, -102.0], 20 : [start_lat, -100.0]}



def long_add(start_long, start_lat):
    if start_lat == 60.0:
        for i in range(40):
            start_long += add_degrees
            return start_long


# print(long_add(start_long, start_lat))
def description(phrase):
    if phrase == "statement1":
        statement = description_text.format(grid_names[0],grid_names_climate[grid_names[0]], url[grid_names[0]])
        return statement

    elif phrase == "statement2":
        statement = description_text.format(grid_names[1],grid_names_climate[grid_names[1]], url[grid_names[1]])
        return statement

    elif phrase == "statement3":
        statement = description_text.format(grid_names[2],grid_names_climate[grid_names[2]], url[grid_names[2]])
        return statement

    elif phrase == "statement4":
        statement = description_text.format(grid_names[3],grid_names_climate[grid_names[3]], url[grid_names[3]])
        return statement
    elif phrase == "statement5":
        statement = description_text.format(grid_names[4], grid_names_climate[grid_names[4]], url[grid_names[4]])
        return statement



for i in range(50):
    first_lat = ran.randint(59,60)
    last_lat = ran.uniform(0, 1)
    lat = first_lat + last_lat

    first_long = ran.randint(130, 140)
    last_long = ran.uniform(0, 1)
    long = first_long + (last_long)
    long = long * -1
    print(lat, (long))

    if lat < grid_coordinates[0][0] and lat >= end_lat and long >= grid_coordinates[0][1] and long < grid_coordinates[1][1]:
        print(description("statement{}".format(i)))
        folium.Marker([lat, long],
                      popup="House {} {}".format(i, description("statement1")),
                      tooltip=tooltip).add_to(m)


    if lat < grid_coordinates[1][0] and lat >= end_lat and long >= grid_coordinates[1][1] and long < grid_coordinates[2][1]:
        print(description("statement{}".format(i)))
        folium.Marker([lat, long],
                      popup="House {} {}".format(i, description("statement2")),
                      tooltip=tooltip).add_to(m)
    if lat < grid_coordinates[2][0] and lat >= end_lat and long >= grid_coordinates[2][1] and long < grid_coordinates[3][1]:
        print(description("statement{}".format(i)))
        folium.Marker([lat, long],
                      popup="House {} {}".format(i, description("statement3")),
                      tooltip=tooltip).add_to(m)

    if lat < grid_coordinates[3][0] and lat >= end_lat and long >= grid_coordinates[3][1] and long < grid_coordinates[4][1]:
        print(description("statement{}".format(i)))
        folium.Marker([lat, long],
                      popup="House {} {}".format(i, description("statement4")),
                      tooltip=tooltip).add_to(m)

    if lat < grid_coordinates[4][0] and lat >= end_lat and long >= grid_coordinates[4][1] and long < grid_coordinates[5][1]:
        print(description("statement{}".format(i)))
        folium.Marker([lat, long],
                      popup="House {} {}".format(i, description("statement5")),
                      tooltip=tooltip).add_to(m)


# print("House {} {}".format(i,description("statement2")))

m.save("canada_home_prices_projecttemp.html")

# "ATLIN", "JENNINGS RIVER", "MCDAME", "RABBIT RIVER",
# "TOAD RIVER", "MAXHAMISH LAKE", "PETITOT RIVER", "STEEN RIVER", "WHITESAND RIVER", "PEACE POINT",
# "FITZGERALD", "TAZIN LAKE", "FOND-DU-LAC", "STONY RAPIDS", "PHELPS LAKE", "KASMERE LAKE",
# # "MUNROE LAKE", "NEJANILINI LAKE"