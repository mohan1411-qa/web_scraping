import requests
from bs4 import BeautifulSoup


class ClimateInfo:

    def get_major_cities_climate_info(self):
        file = open("F:\\Projects\\Web_Scrapping_Workspace\\WebScrapping\\data.csv", 'w')
        file.write('S No.' + ',' + 'City Name' + ',' + 'Weather' + ',' + 'Wind' + '\n')
        data = requests.get("https://mausam.imd.gov.in/")
        soup = BeautifulSoup(data.content, 'html.parser')
        cities_info = soup.find('div', {'class':'capitals clearfix'})
        weather_info = cities_info.findAll('div', {'class':'capital'})
        count = 0
        for i in weather_info:
            print("Climate of {} is {}".format(i.h3.text, i.span.text))
            file.write(str(count) + str(',') + i.h3.text + str(',') + i.span.text +
                       str(',') + i.find('p', {'class': 'wind'}).text + '\n')


obj = ClimateInfo()
obj.get_major_cities_climate_info()
