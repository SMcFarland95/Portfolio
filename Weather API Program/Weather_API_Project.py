# Welcome to my Weather API Project
# Author: Shannon McFarland
# 8/13/22

# weather_output prints out weather data requested from OpenWeatherMap API.
def weather_output(weather_json_response, degree_symbol):
    print("Description: ", weather_json_response['weather'][0]['description']
          .title())
    print("Current Temperature: ", weather_json_response['main']['temp'],
          degree_symbol)
    print("Feels like: ", weather_json_response['main']['feels_like'],
          degree_symbol)
    print("High Temp: ", weather_json_response['main']['temp_max'],
          degree_symbol)
    print("Low Temp: ", weather_json_response['main']['temp_min'],
          degree_symbol)
    print("Humidity: ", weather_json_response['main']['humidity'], "%")
    print("Pressure: ", weather_json_response['main']['pressure'], "hPa")


def main():
    import requests  # Imports Request library
    print("Welcome to US Weather! "
          "\N{smiling face with sunglasses}")  # Sunglasses smiley emoji
    user_answer = input("Would you like to lookup the current weather by zip"
                        " code or city? \nPlease enter 1 for zip code, 2 for"
                        " city, or 3 to exit: ")
    # While loop continues to prompt user until user enters "3".
    while user_answer == "1" or "2" or "3":
        if user_answer == "1":  # Weather lookup by zip code
            zip_code = input("Please enter zip code: ")
            # Inputted zip code added to API request urL.
            geo_api = "http://api.openweathermap.org/geo/1.0/zip?zip=" +\
                      zip_code + ",US&appid=c6476cc0097416d9cdda3a9a8fc32b1f"
            # Requests response from Geocoding API.
            # The requested API generates coordinates from inputted zip code.
            try:
                geo_response = requests.get(geo_api)
            except ConnectionError:
                print("Program is having trouble connecting to the API.")
            # Returns JSON response object from Geocoding API.
            geo_json_response = geo_response.json()
            # Latitude and longitude coordinates are parsed from JSON data.
            # Coordinates are converted to string values.
            try:
                latitude = str(geo_json_response["lat"])
                longitude = str(geo_json_response["lon"])
            except KeyError:
                print("I'm sorry. Zip code is not recognized.")
                break
            temp_units = input("Would you like to view you temperature values"
                               " in Celsius, Fahrenheit, or Kelvin? Please"
                               " enter 1 for Celsius, 2 for Fahrenheit, or 3 "
                               "for Kelvin:  ")
            # Latitude and longitude added to OpenWeatherMap API request urL.
            while temp_units == "1" or "2" or "3":
                if temp_units == "1":  # Celsius temperature output
                    weather_api = "https://api.openweathermap.org/data/2.5/" \
                                  "weather?lat=" + latitude + "&lon=" + \
                                  longitude + "&appid=c6476cc0097416d9cdda3" \
                                              "a9a8fc32b1f&units=metric"
                    degree_symbol = "\u00B0C"
                    break
                elif temp_units == "2":  # Fahrenheit temperature output
                    weather_api = "https://api.openweathermap.org/data/2.5/" \
                                          "weather?lat=" + latitude + \
                                  "&lon=" + longitude + "&appid=c6476cc00974" \
                                  "16d9cdda3a9a8fc32b1f&units=imperial"
                    degree_symbol = "\u00B0F"
                    break
                elif temp_units == "3":  # Kelvin temperature output
                    weather_api = "https://api.openweathermap.org/data/2.5/" \
                                          "weather?lat=" + latitude + "&lon="\
                                  + longitude + "&appid=c6476cc0097416d9" \
                                  "cdda3a9a8fc32b1f"
                    degree_symbol = "K"
                    break
                else:
                    print("Not a valid response, please try again.")
                    temp_units = input("Would you like to view you "
                                       "temperature values in Celsius, "
                                       "Fahrenheit, or Kelvin? Please enter 1"
                                       " for Celsius, 2 for Fahrenheit, or 3 "
                                       "for Kelvin: ")
            # Requests response from OpenWeatherMap API.
            # The requested API generates weather data from coordinates
            weather_response = requests.get(weather_api)
            # Returns JSON response object from OpenWeatherMap API.
            weather_json_response = weather_response.json()
            print("________________________________________")
            print("Weather Conditions for", zip_code)
            weather_output(weather_json_response, degree_symbol)
            user_answer = input("\nWould you like to lookup the more weather"
                                " data by zip code or city? \nPlease enter 1 "
                                "for zip code, 2 for city, or 3 to exit: ")
        elif user_answer == "2":  # Weather lookup by city, state
            city_name = input("Please enter city name: ")
            state_name = input("Please enter the state abbreviation: ")
            # Inputted zip code added to API request urL.
            geo_api = "http://api.openweathermap.org/geo/1.0/direct?q="\
                      + city_name + "," + state_name +\
                      ",US&appid=c6476cc0097416d9cdda3a9a8fc32b1f"
            # Requests response from Geocoding API
            # The requested API generates coordinates from city, state.
            try:
                geo_response = requests.get(geo_api)
            except ConnectionError:
                print("Program is having trouble connecting to the API.")
            # Returns JSON response object from Geocoding API.
            geo_json_response = geo_response.json()
            # Latitude and longitude coordinates are parsed from JSON data.
            # Coordinates are converted to string values.
            try:
                latitude = str(geo_json_response[0]["lat"])
                longitude = str(geo_json_response[0]["lon"])
            except IndexError:
                print("I'm sorry. Inputted location values are not "
                      "recognized.")
                break
            temp_units = input("Would you like to view you temperature values"
                               " in Celsius, Fahrenheit, or Kelvin? Please "
                               "enter 1 for Celsius, 2 for Fahrenheit, or 3 "
                               "for Kelvin: ")
            # Latitude and longitude added to OpenWeatherMap API request urL.
            while temp_units == "1" or "2" or "3":
                if temp_units == "1":  # Celsius temperature output
                    weather_api = "https://api.openweathermap.org/data/2.5/" \
                                  "weather?lat=" + latitude + "&lon=" +\
                                  longitude + "&appid=c6476cc0097416d9cdda3" \
                                              "a9a8fc32b1f&units=metric"
                    degree_symbol = "\u00B0C"
                    break
                elif temp_units == "2":  # Fahrenheit temperature output
                    weather_api = "https://api.openweathermap.org/data/2.5/" \
                                          "weather?lat=" + latitude + "&lon="\
                                  + longitude + "&appid=c6476cc0097416d9cdd" \
                                                "a3a9a8fc32b1f&units=imperial"
                    degree_symbol = "\u00B0F"
                    break
                elif temp_units == "3":  # Kelvin temperature output
                    weather_api = "https://api.openweathermap.org/data/2.5/" \
                                          "weather?lat=" + latitude + "&lon="\
                                  + longitude + "&appid=c6476cc0097416d9cdd" \
                                                "a3a9a8fc32b1f"
                    degree_symbol = "K"
                    break
                else:
                    print("Not a valid response, please try again.")
                    temp_units = input("Would you like to view you "
                                       "temperature values in Celsius, "
                                       "Fahrenheit, or Kelvin? Please enter 1"
                                       " for Celsius, 2 for Fahrenheit, or 3 "
                                       "for Kelvin:  ")
            # Requests response from OpenWeatherMap API.
            # The requested API generates weather data from coordinates
            weather_response = requests.get(weather_api)
            # Returns JSON response object from OpenWeatherMap API.
            weather_json_response = weather_response.json()
            print("________________________________________")
            print("Weather Conditions for", city_name.title(), ",",
                  state_name.upper())
            weather_output(weather_json_response, degree_symbol)
            user_answer = input("\nWould you like to lookup more weather data"
                                " by zip code or city? \nPlease enter 1 for "
                                "zip code, 2 for city, or 3 to exit: ")
        elif user_answer == "3":  # Exits program
            print("Thank you for joining US Weather. Have a nice day!"
                  " \U0001F601")  # Smiley face emoji
            exit()  # Breaks while loop.
        else:   # If user does not enter valid value, user can to try again.
            print("\nNot a valid response, please try again.")
            user_answer = input("Would you like to lookup the current weather"
                                " by zip code or city? \nPlease enter 1 for "
                                "zip code, 2 for city, or 3 to exit: ")


if __name__ == '__main__':
    main()
