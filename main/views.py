from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
# Create your views here.

def scrapping(link):

    DATA = {}

    x = requests.get(link)

    soup = BeautifulSoup(x.text,'html.parser')

    RANGE,COUNT = 7,0
    number = None 

    NAME = {
        1:"name",
        2:"Market",
        3:"Price",
        4:"Volume",
        5:"Circulating",
        6:"Change",
    }

    for tr in soup.find_all('tr'):
        for td in tr.find_all('td'):
            if td.string != None:
                if COUNT == 0:
                    COUNT += 1
                    number = td.string
                    DATA[td.string] = {}
                else:
                    DATA[number][NAME[COUNT]] = td.string
                    COUNT += 1 
                
                if COUNT == RANGE:
                    COUNT = 0

    return DATA

def index(request):
    link = "https://coin360.com/coin"
    data = scrapping(link)
    return render(request,'main/index.html',{'data':data})