from gps import *
from time import *
import time
import threading
import pandas as pd
from datetime import datetime, timezone


class Location():
    def __init__(self, polling_rate, distance_unit, average_interval, timezone, location_type='GPS', GPS_Time=True):
        self.location_type = location_type
        self.polling_rate = polling_rate
        self.distance_unit = distance_unit
        self.average_interval = average_interval
        if self.polling_rate != (10 or 5 or 1):
            raise ('Polling rate not supported 1,5 & 10hz supported')
        if self.polling_rate == 10:
            # TODO average data for realtime output
            print('test')
        if self.polling_rate == 5:
            # TODO average data for realtime output
            print('test')
        if self.polling_rate == 1:
            # TODO average data for realtime output
            print('test')
        if self.gps_time == True:
            def getTime(timezone, rolling_df):
                if timezone in range(-12.14):
                    ts = max(rolling_df['time'])
                    # assumes UTC Input
                    ts = datetime.fromtimestamp(ts)
                    return ts.replace(tzinfo=timezone.utc).astimezone(tz=timezone)
                else:
                    raise('Invalid timezone offset enter int value -12 through 14 Example PST would be -8')

    def rolling_one_minute(self):
        df = pd.DataFrame()
        gpsp = GpsPoller()
        try:
            gpsp.start()
            while True:
                data_entry = {"altitude": gpsd.fix.altitude, "latitude": gpsd.fix.latitude,
                              "longitude": gpsd.fix.longitude,
                              "speed": gpsd.fix.speed, "climb": gpsd.fix.climb, "time": gpsd.fix.time,
                              "status": gpsd.fix.status, "mode": gpsd.fix.mode}
                df = df.append(data_entry, ignore_index=True)
                if self.polling_rate == 10:
                    df = df.rolling(600)
                if self.polling_rate == 5:
                    df = df.rolling(300)
                if self.polling_rate == 1:
                    df = df.rolling(60)
        except:
            print('gps service unavailable')


class GpsPoller(threading.Thread):
    gpsd = None  # seting the global variable


def __init__(self):
    threading.Thread.__init__(self)
    global gpsd  # bring it in scope
    gpsd = gps(mode=WATCH_ENABLE)  # starting the stream of info
    self.current_value = None
    self.running = True  # setting the thread running to true


def run(self):
    global gpsd
    while gpsp.running:
        gpsd.next()  # this will continue to loop and grab EACH set of gpsd info to clear the buffer
