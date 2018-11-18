from getPop import getPopulation 
import pygal


def getPopGrowth():
    data = getPopulation()
    pop_growth = {}
    years = set()
    start, end = 1950, 1975
    countries = ['Ukraine', 'Uganda', 'Belgium', 'Italy']
    for countryDict in data:
        country, pop, year = countryDict['Country Name'], countryDict['Value'], countryDict['Year']
        if year in range(start, end+1) and country in countries:
            years.add(year)
            try:
                pop_growth[country].append(pop)
            except KeyError:
                pop_growth[country] = []
                pop_growth[country].append(pop)
    dictPop = {}
    dictPop['years_range'] = years
    dictPop['pop'] = pop_growth
    # return {
    #     'years_range': years,
    #     'pop': pop_growth
    # }
    return dictPop

def drawChart():
    chartData = getPopGrowth()
    line_chart = pygal.Bar()
    line_chart.title = 'Population growth'
    line_chart.x_labels = chartData['year_range']
    for country, years in chartData['pop'].items():
        line_chart.add(country, years)
    line_chart.render_to_file('countriesGrowth.svg')
        




drawChart()