#!/bin/sh
import datetime
import xmltodict
import urllib.request
import csv


#tijdformat voor API link
datum = datetime.date.today()
datumformat = datum.strftime('%d-%m-%Y')
lijst, films = urllib.request.urlretrieve('http://api.filmtotaal.nl/filmsoptv.xml?apikey=r2mnnu0mm027ijyu2lzo371e8eal1vp5&dag={0}&sorteer=0'.format(datumformat), 'films.xml')
conv = 'films.xml'

def filmdata():
    with open(conv, 'r', encoding='iso-8859-1') as film:
        filestring = film.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary
database = filmdata()
data = database['filmsoptv']['film']


def filminfo():
    with open('films {0}.csv'.format(datumformat), 'w', encoding='iso-8859-1') as aanbieders:
        writer = csv.writer(aanbieders, delimiter=';')
        writer.writerow(('Film', 'Jaar', 'Regisseur', 'Tagline', 'IMDB', 'Begintijd', 'Eindtijd', 'Cast', 'Genre', 'Samenvatting', 'Aanbieder', 'Code', 'Bezoeker'))
        for Film in data:
            datas = Film['titel'], Film['jaar'], Film['regisseur'], Film['tagline'], Film['imdb_rating'], Film['starttijd'], Film['eindtijd'], Film['cast'], Film['genre'], Film['synopsis'],'','', ''
            writer.writerow(datas)
filmdata()
filminfo()
