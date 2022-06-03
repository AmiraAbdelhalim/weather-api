import requests


class Weather:
    """
    https://api.weatherapi.com/v1/current.json?key=1d00fc04790449d1b4c132801220306&q=Alexandria&aqi=no
    https://api.weatherapi.com/v1/forecast.json?key=1d00fc04790449d1b4c132801220306&q=Alexandria&days=4&aqi=no&alerts=no

    """
    def __init__(self):
        self.__api_key = '1d00fc04790449d1b4c132801220306'
        self.current_url = 'https://api.weatherapi.com/v1/current.json'
        self.forecast_url = 'https://api.weatherapi.com/v1/forecast.json'

    def get_current_temperature(self, city):
        full_api_url = f'{self.current_url}?key={self.__api_key}&q={city}&aqi=no'
        response = requests.get(full_api_url)
        if response.status_code == 200:
            response_temp = response.json().get('current')
            return response_temp.get('temp_c')
        else:
            print(f'error with response code = {response.status_code}')
            return None

    def get_temperature_after(self, city, days, hour=None):
        if hour:
            full_api_url = f'{self.forecast_url}?key={self.__api_key}&q={city}&days={days}&hour={hour}&aqi=no&alerts=no'
        else:
            full_api_url = f'{self.forecast_url}?key={self.__api_key}&q={city}&days={days}&aqi=no&alerts=no'
        response = requests.get(full_api_url)
        if response.status_code == 200:
            forecast = response.json().get('forecast')
            return forecast.get('forecastday')
        else:
            print(f'error with response code = {response.status_code}')
            return None

    def get_lat_and_long(self, city):
        full_api_url = f'{self.current_url}?key={self.__api_key}&q={city}&aqi=no'
        response = requests.get(full_api_url)
        if response.status_code == 200:
            response_location = response.json().get('location')
            location = {
                'lat': response_location.get('lat'),
                'long': response_location.get('lon'),
            }
            return location
        else:
            print(f'error with response code = {response.status_code}')
            return None

