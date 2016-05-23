#!/usr/bin/python
# -*- coding: UTF-8 -*-

import gps
import mysql.connector

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

config = {
    'user': 'dondestou',
    'password': 'J7WAisfXoyu9nq4iYr',
    'host': 'lab.tatulab.com',
    'database': 'dondestas',
}

cnx = mysql.connector.connect(**config)

while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        # print report
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                print report.time
            if hasattr(report, 'lat'):
                print report.lat
            if hasattr(report, 'lon'):
                print report.lon
            if hasattr(report, 'speed'):
                print report.speed
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"
