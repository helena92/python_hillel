from pygal.maps.world import World
from getCountryCodes import getCountryCode
from getPop import getPopulation 

def drawMap():
    mapData = {}
    year = 1978
    data = getPopulation()
    for countryData in data:
        code = getCountryCode(countryData['Country Name'])
        if code:
            if year == countryData['Year']:
                mapData[code] = countryData['Value']
     
    worldmap_chart = World()
    worldmap_chart.add(year, mapData)
    worldmap_chart.render_to_file('countriesMap.svg')


drawMap()