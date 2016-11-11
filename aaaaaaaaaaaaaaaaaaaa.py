import csv
import datetime
import os
datum = datetime.date.today()
datumformat = datum.strftime('%d-%m-%Y')
def check():
        with open('filmsaanbieder Marc {0}.csv'.format(datumformat, 'r')) as file:
            lezer = csv.reader(file, delimiter=';')
            if os.stat('filmsaanbieder Marc {0}.csv'.format(datumformat)).st_size == 0:
                return
            else:
                for rij in lezer:
                    if rij:
                        global a
                        a = (rij[0])
        with open('filmsaanbieder Cheraldo {0}.csv'.format(datumformat, 'r')) as aaa:
            lezen = csv.reader(aaa, delimiter=';')
            if os.stat('filmsaanbieder Cheraldo {0}.csv'.format(datumformat)).st_size == 0:
                return
            else:
                for rij in lezen:
                    if rij:
                        global b
                        b = (rij[0])
        with open('filmsaanbieder Ali {0}.csv'.format(datumformat, 'r')) as bbb:
            lezeb = csv.reader(bbb, delimiter=';')
            if os.stat('filmsaanbieder Ali {0}.csv'.format(datumformat)).st_size == 0:
                return
            else:
                for rij in lezeb:
                    if rij:
                        global c
                        c = (rij[0])
        with open('filmsaanbieder Nahom {0}.csv'.format(datumformat, 'r')) as ccc:
            lezec = csv.reader(ccc, delimiter=';')
            if os.stat('filmsaanbieder Nahom {0}.csv'.format(datumformat)).st_size == 0:
                return
            else:
                for rij in lezec:
                    if rij:
                        global d
                        d = (rij[0])
        with open('filmsaanbieder Roeland {0}.csv'.format(datumformat, 'r')) as ddd:
             lezed = csv.reader(ddd, delimiter=';')
             if os.stat('filmsaanbieder Roeland {0}.csv'.format(datumformat)).st_size == 0:
                 return
             else:
                for rij in lezed:
                    if rij:
                        global e
                        e = (rij[0])
        with open('films {0}.csv'.format(datumformat), 'r') as bestand:
            reader = csv.reader(bestand, delimiter=';')
            for row in reader:
                if row[0] not in a and row[0] not in b and row[0] not in c and row[0] not in d and row[0] not in e:
                    global filmlijst
                    filmlijst = row[0]
                    print(row[0])
                    global filmgoedelijst
                    print (filmlijst)
                    filmgoedelijst ='\''+filmlijst+'\','
                    print(filmgoedelijst)
check()
