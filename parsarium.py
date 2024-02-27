import requests
from bs4 import BeautifulSoup
import tkinter
import time
class Window:
    def __init__(self, links):
        self.root = tkinter.Tk()
        self.root.geometry("800x600")
        self.root.title("star")
        self.label = tkinter.Label(self.root, wraplength=740)
        self.label.pack()
        self.placeCity(links)

        self.btn = tkinter.Button(self.root, text="Ввод", command=lambda:self.add(links))
        self.btn.pack()
        self.entry = tkinter.Entry(self.root, width= 60)
        self.entry.pack()

        self.lable = tkinter.Label(self.root, wraplength=740)
        self.lable.pack()

    def add(self, lincs):
        text = self.entry.get()
        if text not in list(lincs.keys()):
            return
        self.ParCit(lincs[text])
    def ParCit(self, linc):
        print(linc)
        weat = Weather(linc)
        pars2 = weat.soup.find("div", {"id":"archiveString"})
        pars3 = pars2.find("span", {"class":"t_0"}).text
        if pars2 is None:
            pars4=pars2.find("div", {"class":"ArchiveInfo"})
            pars3 = pars2.find("span", {"class": "t_0"}).text

        pars4 = pars2.find("a", {"class": "ArchiveStrLink"}).text
        self.lable.configure(text=pars3)
        print(pars4)
    time.sleep(3)
    def placeCity(self, links):
        text =""
        for city in links:
            text += city +", "
        self.label.configure(text=text)


class Weather:
    def __init__(self, linc):
        self.link = linc
        request = requests.get(self.link).text
        self.soup = BeautifulSoup(request, "html.parser")
    def city(self):
        data = self.soup.find_all("a")
        lincs = {}
        skip = ("Посмотреть", " 21 сент. 2023", "О сайте", "Мобильная версия", "Главная", "Новости",
                "Частые вопросы (FAQ)", "Контакты", "Россия", "Литва",
                "Беларусь", "Украина", "Все страны", "См. на карте", "Чукотка", "Коми")
        for city in data:
            text = city.__str__()

            firstA = text.find("/")
            citylink = text[firstA:]
            lastA = citylink.find('">')
            citylink = citylink[:lastA]
            name = city.get_text()
            print(citylink)
            if name not in skip:
                lincs[name] = "https://rp5.ru/" + citylink  # собираем полную ссылку


        return lincs
star = Weather("https://rp5.ru/Погода_в_России")
data = star.city()
for city, linc in data.items():

    print(city, linc)
a = Window(data)
a.root.mainloop()