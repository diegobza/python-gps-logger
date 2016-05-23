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
cursor = cnx.cursor()
add_leitura = ("INSERT INTO leitura "
               "(dispositivo, latitude, longitude, horario, valocidade) "
               "VALUES (%s, %s, %s, %s, %s)")

while True:
    try:
        report = session.next()
        # Wait for a 'TPV' report and display the current time
        # To see all report data, uncomment the line below
        # print report
        if report['class'] == 'TPV':
            if hasattr(report, 'lat') and hasattr(report, 'lon') and hasattr(report, 'time') and hasattr(report, 'speed'):
                dados_leitura = ('1', report.lat, report.lon, report.time, report.speed)
                cursor.execute(add_leitura, dados_leitura)
                cnx.commit()
                print report.lat
                print report.lon
                print report.time
                print report.speed
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"
