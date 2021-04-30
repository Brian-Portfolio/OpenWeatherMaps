#. Write a function that will take the latitudeand longitudeas inputs and return a 7-day weather forecast for a specified city.
#For this exercise, you will leverage the OpenWeatherMap API to source the weather information.
#More specifically, the function should use the input coordinates to fetch real-time weather data from OpenWeatherMap’s
#public API, parse through the returned object, and print specified forecast information for each of the 7 days in an easy-toread format.
#For each day, please include the current time(listed as dt), temperature, weather(listed as main, ex: cloudy,sunny, rainy), humidity, and wind speed. 

import requests 
import json
import time 

#Function Geocoding allows to get location info, such as: name, country, state
def getGecoding(lat, lon, APPID):
    #initialize dictionary
    dict_geocoding = {}

    limit = 2
    URLGeocoding = "http://api.openweathermap.org/geo/1.0/reverse?lat=%s&lon=%s&limit=%s&appid=%s" %(lat, lon, limit, APPID)

    #Get request to obtain HTTP data/ JSON loads converts JSON data into a dictionary
    response = requests.get(URLGeocoding)
    data = json.loads(response.text)

    #dictionary put into a list to convert from list to JSON array
    dict_geocoding['Current Location'] = []

    #Console log output
    print("This is Current Location")
    print("Name : ", data[0]['name'])
    print("Country : ", data[0]['country'])
    print("State : ", data[0]['state'])

    dict_geocoding['Current Location'].append({"Name : " : data[0]['name'],
                                                "Country : " : data[0]['country'],
                                                "State : " : data[0]['state']})

    #Write to JSON file/JSON dump converts Python objects into appropriate JSON objects
    with open('Location.json', 'w') as outfile:
        json.dump(dict_geocoding, outfile, indent=2)

def getAirPollution(lat, lon, APPID):
    
    #initialize dictionary
    dict_pollution = {}
    
    URLPollution = "http://api.openweathermap.org/data/2.5/air_pollution?lat=%s&lon=%s&APPID=%s" %(lat, lon, APPID)

    #Get request to obtain HTTP data/ JSON loads converts JSON data into a dictionary
    response = requests.get(URLPollution)
    data = json.loads(response.text)

    #dictionary put into a list to convert from list to JSON array
    dict_pollution['Current AirPollution Status'] = []

    print("This is Current Air pollution status")
    date = data['list'][0]['dt']
    AQI = data['list'][0]['main']['aqi']
    if AQI == 1:
        value = "Good"
    elif AQI == 2:
        value = "Fair"
    elif AQI == 3:
        value = "Moderate"
    elif AQI == 4:
        value = "Poor"
    elif AQI == 5:
        value = "Very Poor"    
    
    #Console log output
    print("Current Time : ", time.strftime("%D %H:%M", time.localtime(int(date)))) # Conversion of time
    print("Air Quality Index : ", value)
    print("Concentration of Carbon Monoxide : ", data['list'][0]['components']['co'], "micrograms/m^3")
    print("Concentration of Nitrogen Monoxide : ", data['list'][0]['components']['no'], "micrograms/m^3")
    print("Concentration of Nitrogen Dioxide : ", data['list'][0]['components']['no2'], "micrograms/m^3")
    print("Concentration of Ozone : ", data['list'][0]['components']['o3'], "micrograms/m^3")
    print("Concentration of Sulphur Dioxide : ", data['list'][0]['components']['so2'], "micrograms/m^3")
    print("Concentration of Fine particles matter : ", data['list'][0]['components']['pm2_5'], "micrograms/m^3")
    print("Concentration of Coarse particulate matter : ", data['list'][0]['components']['pm10'], "micrograms/m^3")
    print("Concentration of Ammonia : ", data['list'][0]['components']['nh3'], "micrograms/m^3")

    dict_pollution['Current AirPollution Status'].append({"Current Time : ": time.strftime("%D %H:%M", time.localtime(int(date))),
                                            "Air Quality Index : ": value,
                                            "Concentration of Carbon Monoxide : ": str(data['list'][0]['components']['co'])+ "micrograms/m^3",
                                            "Concentration of Nitrogen Monoxide : ": str(data['list'][0]['components']['no'])+ "micrograms/m^3",
                                            "Concentration of Nitrogen Dioxide : ": str(data['list'][0]['components']['no2'])+ "micrograms/m^3",
                                            "Concentration of Ozone : ": str(data['list'][0]['components']['o3'])+ "micrograms/m^3",
                                            "Concentration of Sulphur Dioxide : ": str(data['list'][0]['components']['so2'])+ "micrograms/m^3",
                                            "Concentration of Fine particles matter : ": str(data['list'][0]['components']['pm2_5'])+ "micrograms/m^3",
                                            "Concentration of Coarse particulate matter : ": str(data['list'][0]['components']['pm10'])+ "micrograms/m^3",
                                            "Concentration of Ammonia : ": str(data['list'][0]['components']['nh3'])+ "micrograms/m^3"})
    
     #Write to JSON file/JSON dump converts Python objects into appropriate JSON objects
    with open('PollutionStatus.json', 'w') as outfile:
        json.dump(dict_pollution, outfile, indent=2)

def get_Weather(lat, lon, APPID):
    
    #initialize dictionary
    dict_json = {}

    #APPID = "1835c387deb010b8c5f3b587b1a4222c"

    URLWeather = "http://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&APPID=%s&units=imperial&exclude=current,minutely,hourly" %(lat, lon, APPID)
    
    #Get request to obtain HTTP data/ JSON loads converts JSON data into a dictionary
    response = requests.get(URLWeather)
    data = json.loads(response.text)
    
    #dictionary put into a list to convert from list to JSON array
    dict_json['Weather Forecast'] = []


    print("This is the 7 day weather forecast for the timezone : ", data['timezone'])
    for i in range(0,7):
        date = data['daily'][i]['dt']
        print('--------------------------------')
        print("Current Time : ", time.strftime("%D %H:%M", time.localtime(int(date)))) # Conversion of time
        print("Temperature : ", data['daily'][i]['temp']['day'])
        print("Weather : ", data['daily'][i]['weather'][0]['main'])
        print("Humidity : ", data['daily'][i]['humidity'])
        print("Wind Speed : ", data['daily'][i]['wind_speed'])
        
        dict_json['Weather Forecast'].append({'Current Time : ': time.strftime("%D %H:%M", time.localtime(int(date))), 
                                            'Temperature : ': data['daily'][i]['temp']['day'], 
                                            'Weather : ': data['daily'][i]['weather'][0]['main'], 
                                            'Humidity : ': data['daily'][i]['humidity'],
                                            'Wind Speed : ': data['daily'][i]['wind_speed'] })

    #Write to JSON file/JSON dump converts Python objects into appropriate JSON objects
    with open('WeatherForecast.json', 'w') as outfile:
        json.dump(dict_json, outfile, indent=2)

def main():
    
    APIKey = input("Please enter your API Key : ")

    while(True):
        lat = float(input("Please enter a latitude value in the range -90 to 90 : "))
        if lat >= -90 and lat <= 90:
            break
        else:
            print("Invalid Entry, please try again.")

    while(True):    
        lon = float(input("Please enter a longitude value in the range from -180 to 180 : "))
        if lon >= -180 and lon <=180:
            break
        else:
            print("Invalid Entry, please try again.")

    get_Weather(lat, lon, APIKey)
    getAirPollution(lat, lon, APIKey)
    getGecoding(lat, lon, APIKey)

if __name__ == "__main__":
    main()