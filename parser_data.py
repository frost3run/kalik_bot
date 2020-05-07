import requests
from bs4 import BeautifulSoup

def get_data_from_vlru():
    r = requests.get('https://www.newsvl.ru/covid19/')
    html = r.text
    data = ''
    vlru_data = {}

    soup = BeautifulSoup(html, "lxml")
    vlru_title = soup.find_all('h2', class_='wdg-covid19__title')
    vlru_data_title = soup.find_all(class_='wdg-covid19__item-title')
    vlru_data_count = soup.find_all(class_='wdg-covid19__item-counter')
    for i in range(len(vlru_title)):
        vlru_title = vlru_title[i].text
    data += 'VL.RU: ' + vlru_title + ':\n\n'
    for i in range(len(vlru_data_title)):
        vlru_data.update({vlru_data_title[i].text: vlru_data_count[i].text})
        data += vlru_data_title[i].text + ': ' + vlru_data_count[i].text + '\n'
    return data


def get_data_from_stopcovid():
    stopcovid_data = {}
    data = ''
    r = requests.get('https://xn--80aesfpebagmfblc0a.xn--p1ai/')
    html = r.text

    soup = BeautifulSoup(html, 'lxml')
    stopcovid_title = soup.find_all('div', class_='cv-banner__description')
    stopcovid_data_title = soup.find_all(class_='cv-countdown__item-label')
    stopcovid_data_count = soup.find_all(class_='cv-countdown__item-value')
    for i in range(len(stopcovid_title)):
        stopcovid_title = stopcovid_title[i].text
    data += 'Стопкоронавирус.рф: ' + stopcovid_title + ':\n\n'

    for i in range(len(stopcovid_data_title)):
        s = str(stopcovid_data_title[i].text)
        tmp = ' '.join(s.split())
        stopcovid_data.update({tmp: stopcovid_data_count[i].text})
        data += tmp + ': ' + stopcovid_data_count[i].text + '\n'
    return data

def check_update():
    pass