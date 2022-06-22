import requests
from bs4 import BeautifulSoup

#                             USAGE
#a = GetCar("aa0999bc")
#print(a.getInfo())

class GetCar():
    URL = 'https://baza-gai.com.ua/nomer/'
    HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0', 'accept': '*/*'}
    number = ""

    def __init__(self,number):
        self.number = number
    
    def getInfo(self):
        return self.__parse(self.URL+"/"+self.number)

    def __get_html(self,url, params=None):
        r = requests.get(url, headers=self.HEADERS, params=params)
        return r


    def __get_content(self,html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            items = soup.find('div', class_="plate-model-card").find_all('ul')
            car = []
            for item in items:
                regstr = item.find_all('li')
                reg = regstr[1].find('span').find('span').get_text()
                typecar = regstr[2].find('span').find('span').get_text()
                caryear = soup.find('div',class_="plate-model-card__content-bottom").find('div').find('div').get_text()
                model = soup.find('h4',class_="plate-model-card__content-title").get_text().replace(" ","").replace("\n"," ")
                adress = regstr[4].find('span').find('span').get_text().replace(" ","").replace(",",", ").replace("\n","")
                ugon = soup.find('div', class_="mt-2 mt-md-0").get_text()
                car.append({
                    'registr': reg,
                    'typecar':typecar,
                    'caryear':caryear,
                    'model':model,
                    'adress':adress,
                    'ugon':ugon,
                })
        except:
            return "Error"
        return car


    def __parse(self,URL: str = None):
        html = self.__get_html(URL)
        if html.status_code == 200:
            car = self.__get_content(html.text)
            if car != "Error":
                info = ""
                info += "Дата регистрации: "+car[0]["registr"]+"\n"
                info += "Приметы: "+car[0]["typecar"]+"\n"
                info += "Год выпуска: "+car[0]["caryear"]+"\n"
                info += "Модель:"+car[0]["model"]+"\n"
                info += "Адрес: "+car[0]["adress"]+"\n"
                info += "Угон: "+car[0]["ugon"]
                return info
            else:
                return "Error"
        else:
            return 'Error'