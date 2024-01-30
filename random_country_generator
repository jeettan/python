import requests
import pycountry
import random
import time

#Define a function lat_lon, gives a random lat or longtitude

def lat_lon():
    lat = random.uniform(-90, 90)
    lon = random.uniform(-180, 180) 
    return lat,lon

start = time.time()

result1 = ""
country_list = []

while result1 == "":    

    result = None

    print("Generating random country based on lan/lon")

    while result is None:

        lat,lon = lat_lon()
        weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=7054f476149777bca5772b889f95c0c4")
        print(".")
    #uses weather api to insert lat lon
        try:
            city = weather_data.json()['sys']['country']
            output = pycountry.countries.get(alpha_2=city)
            result = output.name
        except:
            pass
#If there's an error parsing the weather api, it will try again UNTIL it successfully passes. And when the result field is filled, then the program ends. Printing out the country based on using pycountry
#and weather api.

    print(result)
    country_list.append(result)
    result1 = input("Press enter to continue, type in any letter to end program.\n")

print("Countries generated:", country_list)
string = "You have generated {} countries".format(len(country_list))
print(string)

end = time.time()
print("Time elapsed:", end - start,"seconds")
