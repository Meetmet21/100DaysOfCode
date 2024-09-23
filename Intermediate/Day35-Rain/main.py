import requests
from twilio.rest import Client
import os

class RainMessage:
    def __init__(self):
        # API OpenWeather
        self.END_POINT = "api.openweathermap.org/data/2.5/forecast"
        self.LAT = os.environ["LAT"]
        self.LNG = os.environ["LNG"]
        self.APPID = os.environ["APPID_OPENWEATHER"]
        self.paramters = {
            "lat": self.LAT,
            "lon": self.LNG,
            "appid": self.APPID,
            "units": "metric",
            "cnt": 4
            }
        # API Twilio
        self.account_id = os.environ["ID_TWILIO"]
        self.auth_token = os.environ["AUTH_TWILIO"]
        self.client = Client(username=self.account_id, password=self.auth_token)
        self.tw_number = ""
        self.to_number = ""

        # Cheks if it rains roday
        self.rain_today()

    def send_request(self) -> dict:
        """
        Send request to OPen Weather for meteo forecast for next 12 hours for 5 days.
        :return: Dict with 5 days weather prediction each 6 hours of a day.
        """
        response = requests.get(url=self.END_POINT, params=self.paramters)
        response.raise_for_status()
        weather = response.json()["list"]

        return weather

    def rain_today(self) -> bool:
        """
        Checks if it rains today.
        :return:  Boolean
        """
        weather = self.send_request()
        # Look for day 1
        for timestamp in weather[0]["weather"]:
            if int(timestamp["id"]) < 700:
                return True

        return False

    def semd_sms(self) -> None:
        """
        Semds a SMS to number if it rains today.
        :return: None
        """
        if self.rain_today():
            message = self.client.messages.create(body="It will rain today!",
                                                  from_=self.tw_number,
                                                  to=self.to_number)

if __name__ == '__main__':
    RainMessage()