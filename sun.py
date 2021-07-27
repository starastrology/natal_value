# http://www.skyscript.co.uk/dig2.html
# https://www.astro.com/astrowiki/en/Detriment

from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib.chart import Chart
from flatlib import const
from math import floor

year=input('year:')
month=input('month:')
day=input('day:')

def get_estimated_value(year, month, day):
    planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn"]
    exalted = {planets[0]: 4, planets[1]: 5, planets[2]: 9, planets[3]: 3, planets[4]: 1, planets[5]: 7, planets[6]: 10}
    ruling = {planets[0]: [8], planets[1]: [7], planets[2]: [6, 9], planets[3]: [5, 10], planets[4]: [4, 11], planets[5]: [12, 3], planets[6]: [1, 2]}
    planet_values = [70, 10, 0, 0, 0, 10, 10]

    dob = str(year) + "/" + str(month) + "/" + str(day)
    date = Datetime(dob, '12:00', '+00:00')
    pos = GeoPos('0n0', '0w0')
    chart = Chart(date, pos)

    sun = floor((chart.getObject(const.SUN).lon / 30 + 4) % 12)
    moon = floor((chart.getObject(const.MOON).lon / 30 + 4) % 12)
    mercury = floor((chart.getObject(const.MERCURY).lon / 30 + 4) % 12)
    venus = floor((chart.getObject(const.VENUS).lon / 30 + 4) % 12)
    mars = floor((chart.getObject(const.MARS).lon / 30 + 4) % 12)
    jupiter = floor((chart.getObject(const.JUPITER).lon / 30 + 4) % 12)
    saturn = floor((chart.getObject(const.SATURN).lon / 30 + 4) % 12)
    if sun==0:
        sun = 12
    if moon==0:
        moon=12
    if mercury==0:
        mercury=12
    if venus==0:
        venus=12
    if mars==0:
        mars=12
    if jupiter==0:
        jupiter=12
    if saturn==0:
        saturn=12

    sun_degrees = chart.get(const.SUN).lon % 30.0
    moon_degrees = chart.get(const.MOON).lon % 30.0
    mercury_degrees = chart.get(const.MERCURY).lon % 30.0
    venus_degrees = chart.get(const.VENUS).lon % 30.0
    mars_degrees = chart.get(const.MARS).lon % 30.0
    jupiter_degrees = chart.get(const.JUPITER).lon % 30.0
    saturn_degrees = chart.get(const.SATURN).lon % 30.0

    test_data = [sun, moon, mercury, venus, mars, jupiter, saturn]
    test_data_degrees = [sun_degrees, moon_degrees, mercury_degrees, venus_degrees, mars_degrees, jupiter_degrees, saturn_degrees]
    print(test_data)
    print(test_data_degrees)

    # Find estimated value from exalted/falls and ruling/detriments
    exalted_values = list(exalted.values())
    ruling_values = list(ruling.values())
    estimated_value = 0
    for i in range(0, len(test_data)):
        if test_data[i] == exalted_values[i]:
            estimated_value += 1 * planet_values[i]
        elif test_data[i] == (exalted_values[i] + 6) % 12:
            estimated_value -= 1 * planet_values[i]
    
        for k in ruling_values[i]:
            if test_data[i] == k:
                estimated_value += 1 * planet_values[i]
                break
            elif test_data[i] == (k + 6) % 12:
                estimated_value -= 1 * planet_values[i]
                break

    # Get estimated value for terms of the planets
    test_data_degrees = [15, 14, 29, 26, 7, 6, 16]
    terms = {4: {planets[5]: 6, planets[3]: 14, planets[2]: 21, planets[4]: 26, planets[6]: 30},
         5: {planets[3]: 8, planets[2]: 15, planets[5]: 22, planets[6]: 26, planets[4]: 30},
         6: {planets[2]: 7, planets[5]: 14, planets[3]: 21, planets[6]: 25, planets[4]: 30},
         7: {planets[4]: 6, planets[5]: 13, planets[2]: 20, planets[3]: 27, planets[6]: 30},
         8: {planets[6]: 6, planets[2]: 13, planets[3]: 20, planets[5]: 25, planets[4]: 30},
         9: {planets[2]: 7, planets[3]: 13, planets[5]: 18, planets[6]: 24, planets[4]: 30},
         10: {planets[6]: 6, planets[3]: 11, planets[5]: 19, planets[2]: 24, planets[4]: 30},
         11: {planets[4]: 6, planets[5]: 14, planets[3]: 21, planets[2]: 27, planets[6]: 30},
         12: {planets[5]: 8, planets[3]: 14, planets[2]: 19, planets[6]: 25, planets[4]: 30},
         1: {planets[3]: 6, planets[2]: 12, planets[5]: 19, planets[4]: 25, planets[6]: 30},
         2: {planets[6]: 6, planets[2]: 12, planets[3]: 20, planets[5]: 25, planets[4]: 30},
         3: {planets[3]: 8, planets[5]: 14, planets[2]: 20, planets[4]: 26, planets[6]: 30},
        }
    for i in range(0, len(test_data)):
        terms_values = list(terms.get(test_data[i]).values())
        j = 4
        while j > -1:
            if test_data_degrees[i] < terms_values[j]:  
                j -= 1
            else:
                break
        if list(terms.get(test_data[i]))[j+1] == planets[i]:
            estimated_value += 2 * planet_values[i]
       
    # Get estimated value for faces of the planets       
    faces = {4: {planets[4]: 10, planets[0]: 20, planets[3]: 30},
         5: {planets[2]: 10, planets[1]: 20, planets[6]: 30},
         6: {planets[5]: 10, planets[4]: 20, planets[0]: 30},
         7: {planets[3]: 10, planets[2]: 20, planets[1]: 30},
         8: {planets[6]: 10, planets[5]: 20, planets[4]: 30},
         9: {planets[0]: 10, planets[3]: 20, planets[2]: 30},
         10: {planets[1]: 10, planets[6]: 20, planets[5]: 30},
         11: {planets[4]: 10, planets[0]: 20, planets[3]: 30},
         12: {planets[2]: 10, planets[1]: 20, planets[6]: 30},
         1: {planets[5]: 10, planets[4]: 20, planets[0]: 30},
         2: {planets[3]: 10, planets[2]: 20, planets[1]: 30},
         3: {planets[6]: 10, planets[5]: 20, planets[4]: 30},
        }
    for i in range(0, len(test_data)):
        faces_values = list(faces.get(test_data[i]).values())
        j = 2
        while j > -1:
            if test_data_degrees[i] < faces_values[j]:  
                j -= 1
            else:
                break
        if list(faces.get(test_data[i]))[j+1] == planets[i]:
            estimated_value += 1 * planet_values[i]
     
    # Add triplicity to estimated value     
    for i in range(0, len(test_data)):
        if test_data[i] % 4 == 0 and (planets[i] == "Sun" or planets[i] == "Jupiter"):
            estimated_value += 1 * planet_values[i]
        elif test_data[i] % 4 == 1 and (planets[i] == "Venus" or planets[i] == "Moon"):
            estimated_value += 1 * planet_values[i]
        elif test_data[i] % 4 == 2 and (planets[i] == "Saturn" or planets[i] == "Mercury"):
            estimated_value += 1 * planet_values[i]
        elif test_data[i] % 4 == 3 and planets[i] == "Mars":
            estimated_value += 2 * planet_values[i]

    percent_value = (estimated_value + 200) / 567 * 100

    return [test_data[0], test_data[1], test_data[5], test_data[6], round(percent_value, 1)]

ev = get_estimated_value(year, month, day)
get_estimated_value("19"+str(ev[2])+str(ev[3]), ev[0], ev[1])
