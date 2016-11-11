
import csv
import pyqrcode
from random import randint
from collections import defaultdict
import datetime

datum = datetime.date.today()
datumformat = datum.strftime('%d-%m-%Y')

columns = defaultdict(list) # each value in each column is appended to a list

with open('films {}.csv'.format(datumformat),'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)

naam= input("Typ je naam in: ")
email= input("Typ je e-mail adres in: ")
code = str(randint(1000,1999))
aanbieder = {}
aanbieder['1.']="Marc"
aanbieder['2.']="Nahom"
aanbieder['3.']="Roeland"
aanbieder['4.']="Cheraldo"
aanbieder['5.']="Ali"
options=aanbieder.keys()
sorted(options)
for regel in options:
    print(regel, aanbieder[regel])
keuze = input("Maak een keuze: ")
if keuze =='1':
    ab = 'Marc'
if keuze =='2':
    ab = 'Nahom'
if keuze =='3':
    ab = 'Roeland'
if keuze =='4':
    ab = 'Cheraldo'
if keuze =='5':
    ab = 'Ali'

print(columns[0])
def lezen():
    global fk
    fk = input("Uw Film keuze: ")
    with open('films {0}.csv'.format(datumformat), 'r') as myCSVFile:
        reader = csv.reader(myCSVFile, delimiter=';')
        for row in reader:
            if fk in row[0]:
                return print(row)
lezen()
def qrcode():
    cd = pyqrcode.create(code)
    cd.png('jouwcode.png', scale=5)
    # ('C:\\Users\\xxx\\Desktop\\jouwcode.png, scale=5) ## for Windows cd.png
def write():
    with open('userregistration.csv', 'a', newline='') as bezoeker:
        writer = csv.writer(bezoeker, delimiter=';')
        writer.writerow((naam,email,fk,str(code),ab))
write()
qrcode()
