import requests
from datetime import datetime

class IssOverHead:
    def __init__(self):
        # My latitude and longitude
        self.latitude = 46.21916
        self.longitude = 6.13808
        self.parameters = {
            "lat": self.latitude,
            "lng": self.longitude,
            "formatted": 0,
        }
        # End point ISS
        self.end_point_iss = "http://api.open-notify.org/iss-now.json"
        # End point sunrise sunset
        self.end_point_ss = "https://api.sunrise-sunset.org/json"

    def sun_status(self):
        """
        Send an API resuqest to get the sunrise and sunset time in current region.

        :return: A dictionnary containing the sunset and the sunrise hour.
        """

        response = requests.get(url=self.end_point_ss, params=self.parameters)
        response.raise_for_status()

        return response.json()["results"]

    def where_is_iss(self):
        """
        Send a request to ISS API for latitude and longidute.

        :return: dictionary containing latitude and langitude
        """

        # Get data
        response = requests.get(url=self.end_point_iss)
        # Raise HTTP status related errors
        response.raise_for_status()

        return response.json()["iss_position"]

    def iss_is_near(self):
        """
        Checks whether iss is close to current position and visible by night.
        :return: Boolean
        """

        iss_pos = self.where_is_iss()
        # Sunset in hour
        sunset_hour = self.sun_status()["sunset"].split("T")[1].split(":")[0]
        # Current time
        now = datetime.now()
        # Nearness threshold
        thr = 5

        if (self.latitude + thr >= float(iss_pos["latitude"]) <= self.latitude - thr
                or self.longitude + thr >= float(iss_pos["longitude"]) <= self.longitude - thr
                and int(sunset_hour) <= int(now.hour)):

            # ISS is above head and can be seen
            return True

if __name__ == '__main__':
    session = IssOverHead()
    if session.iss_is_near():
        print("You can see ISS right above you head!")
    else:
        print("No ISS to see right now.")