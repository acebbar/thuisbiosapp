from tkinter import *
import tkinter as tk

from random import randint
import datetime
import xmltodict
import urllib.request
import csv
import random
from collections import defaultdict
import pyqrcode
import os
import sys
#^import de nodige dingen
datum = datetime.date.today()
datumformat = datum.strftime('%d-%m-%Y')
#datum vastleggen
provider = ''
def bezoeker():
        with open('films {0}{1}.csv'.format(provider, datumformat), 'r') as file:
            reader = csv.reader(file, delimiter=';')
            okay=[]
            for row in reader:
                    gdlist="".join(row[0])
                    #print(gdlist)
                    gdlist2="".join(gdlist)
                    #print(gdlist2)
                    okay.append(gdlist2)
        return okay
filmlijst=bezoeker()
def aanmaken():
  with open('filmsaanbieder Marc {0}.csv'.format(datumformat), 'w', newline='') as aanbieder1:
         writer1 = csv.writer(aanbieder1, delimiter=';')
         with open('filmsaanbieder Cheraldo {0}.csv'.format(datumformat), 'w', newline='') as aanbieder2:
             writer2 = csv.writer(aanbieder2, delimiter=';')
             with open('filmsaanbieder Ali {0}.csv'.format(datumformat), 'w', newline='') as aanbieder3:
                 writer3 = csv.writer(aanbieder3, delimiter=';')
                 with open('filmsaanbieder Nahom {0}.csv'.format(datumformat), 'w', newline='') as aanbieder4:
                    writer4 = csv.writer(aanbieder4, delimiter=';')
                    with open('filmsaanbieder Roeland {0}.csv'.format(datumformat), 'w', newline='') as aanbieder5:
                         writer5 = csv.writer(aanbieder5, delimiter=';')
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self,width="30")
        self.naamvul = tk.Entry(self,width="30")
        self.resizable(width=False, height=False)
        self.iconbitmap(r"video.ico")
        naam = Label(self, text="Naam:")
        naam.grid(row=0,column=0)
        mail = Label(self, text="Email:")
        mail.grid(row=1,column=0)
        ww = Label(self, text="Wachtwoord:")
        ww.grid(row=2,column=0)
        self.entry2 = tk.Entry(self,show="*",width="30")
        self.title("Bezoeker")
        self.button = tk.Button(self, text="Aanmelden", command=self.on_button)
        self.bind('<Return>', lambda e:self.on_button())
        self.button.grid(row=5,column=1)
        self.naamvul.grid(row=0,column=1)
        self.entry.grid(row=1,column=1)
        self.entry2.grid(row=2,column=1)
        aanbd = Label(self,text="Aanbieder:")
        aanbd.grid(row=3,column=0)
        filmpje = Label(self,text="Film:")
        filmpje.grid(row=4,column=0)
        lst1 = ['Marc','Roeland','Ali','Nahom','Cheraldo']
        self.var1 = tk.StringVar(self)
        self.drop = tk.OptionMenu(self,self.var1,*lst1,command=self.func)
        self.drop.config(height=1,width=7)
        self.drop.grid(row=3,column=1)
        lst2 = filmlijst
        self.var2 = tk.StringVar(self)
        self.drop2 = tk.OptionMenu(self,self.var2,*lst2,command=self.func2)
        self.drop2.config(height=1,width=15)
        self.drop2.grid(row=4,column=1)
    def func(self,value):
        global ab
        ab=self.var1.set(" "+value)
    def func2(self,value):
        global film
        film = self.var2.set(" "+value)
    def on_button(self):
            email= self.entry.get()
            if '@' not in email or '.' not in email:
                print( 'Invalid email')
            else:
                ab=self.var1.get()
                film=self.var2.get()
                wachtwoord= self.entry2.get()
                naam = self.naamvul.get()
                code = str(randint(1000,9999))
                cd = pyqrcode.create(code)
                cd.png('jouwcode.png', scale=5)
                with open('userregistration.csv', 'a', newline='') as bezoeker:
                    writer = csv.writer(bezoeker, delimiter=';')
                    writer.writerow((naam,email,wachtwoord,code,ab,film))
#
def check():

    with open('filmsaanbieder Marc '+datumformat+'.csv'.format(datumformat), 'r') as file:
        lezer = csv.reader(file, delimiter=';')
        if os.stat('filmsaanbieder Marc '+datumformat+'.csv'.format(datumformat)).st_size == 0:
            a=''
        else:
            for rij in lezer:
                if rij:
                    global a
                    a = (rij[0])
    with open('filmsaanbieder Cheraldo '+datumformat+'.csv'.format(datumformat), 'r') as aaa:
        lezen = csv.reader(aaa, delimiter=';')
        if os.stat('filmsaanbieder Cheraldo '+datumformat+'.csv'.format(datumformat)).st_size == 0:
            b=''
        else:
            for rij in lezen:
                if rij:
                    global b
                    b = (rij[0])
    with open('filmsaanbieder Ali '+datumformat+'.csv'.format(datumformat), 'r') as bbb:
        lezeb = csv.reader(bbb, delimiter=';')
        if os.stat('filmsaanbieder Ali '+datumformat+'.csv'.format(datumformat)).st_size == 0:
            c=''
        else:
            for rij in lezeb:
                if rij:
                    global c
                    c = (rij[0])
    with open('filmsaanbieder Nahom '+datumformat+'.csv'.format(datumformat), 'r') as ccc:
        lezec = csv.reader(ccc, delimiter=';')
        if os.stat('filmsaanbieder Nahom '+datumformat+'.csv'.format(datumformat)).st_size == 0:
            d=''
        else:
            for rij in lezec:
                if rij:
                    global d
                    d = (rij[0])
    with open('filmsaanbieder Roeland '+datumformat+'.csv'.format(datumformat), 'r') as ddd:
         lezed = csv.reader(ddd, delimiter=';')
         if os.stat('filmsaanbieder Roeland '+datumformat+'.csv'.format(datumformat)).st_size == 0:
             e=''
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
                filmlijst = '\''+row[0]+'\''
                filmlijst=str(filmlijst)


#filmlijstje = check()

#bezoekers app
class aanbieder(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("")
        self.resizable(width=False, height=False)
        self.iconbitmap(r"video.ico")
        self.Naam=Label(self, text="Kies je aanbiedersaccount:")
        self.Film=Label(self, text="Kies je film die je wilt aanbieden:")
        lst1 = 'Marc','Roeland','Ali','Nahom','Cheraldo',
        self.var1 = tk.StringVar(self)
        self.drop = tk.OptionMenu(self,self.var1,*lst1,command=self.func)
        self.drop.setvar(lst1[0])
        self.drop.config(height=1,width=7)
        lst2 = filmlijst
        self.var2 = tk.StringVar(self)
        self.drop2 = tk.OptionMenu(self,self.var2,*lst2,command=self.func2)
        self.drop2.config(height=1,width=7)
        self.drop2.config(height=1,width=15)
        self.Naam.grid(row=0,column=1)
        self.drop.grid(row=1,column=1)
        self.Film.grid(row=2,column=1)
        self.drop2.grid(row=3,column=1)
        self.button = tk.Button(self, text="Send query", command=self.send)
        self.bind('<Return>', lambda e:self.send)
        self.button.grid(row=4,column=1)
    degekozen = ''
    def func(self,value):
        self.var1.set(" "+value)
        global naam
        naam = value
    def func2(self,value):
        self.var2.set(" "+value)
        global degekozen
        degekozen = value
        print(degekozen)
    #Tot aan hier werkte het script, maar vanwege tijdnood en het gewoon niet werkend krijgen van de code heeft ons groepje de applicatie gewoon niet werkend gekregen zoals we wouden
    #
    #def send(self):
    #    aanbdr = degekozen
    #    with open('films {0}.csv'.format(datumformat), 'r') as file:
    #        reader = csv.reader(file, delimiter=';')
    #        for row in reader:
    #            if aanbdr in row[0]:
    #                return rows
    #                print(rows)
    #filmkeuzes=send(0)
    #print(filmkeuzes)
    #def sendk():
    #    with open('films {0} {1}.csv'.format(aanbdr, datumformat),'a') as bestand:
    #        writer = csv.writer(bestand, delimiter=';')
    #        writer.writerow(filmkeuzes)
    #sendk
    filmlijst=bezoeker()
#aanbieders kiesscherm
class wwcheck(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(width=False, height=False)
        self.iconbitmap(r"video.ico")
        self.entry = tk.Entry(self,show='*')
        self.entry.pack()
        self.title=' '
        close_button = tk.Button(self, text="Check", command=self.close)
        close_button.pack()
        self.string = ""

    def close(self):
        global result
        self.string = self.entry.get()
        self.destroy()

    def mainloop(self):
        tk.Tk.mainloop(self)
        return self.string

app = wwcheck()
result = app.mainloop()
#wachtwoordcheck

#Root startup begin
root=Tk()
frame = Frame(root)
frame.pack()
root.geometry('{}x{}'.format(200,25))
aanbdbrtn = Button(frame, text = "Ik ben aanbieder", command=aanbieder)
if result!='5544':
    aanbdbrtn.config(state=DISABLED)
aanbdbrtn.pack(side = LEFT)

bzkrbtn = Button(frame, text = "Ik ben bezoeker", command = SampleApp)
bzkrbtn.pack(side = RIGHT)

root.resizable(width=False, height=False)
root.title("Aanmelden")
root.iconbitmap(r"video.ico")
root.mainloop()
#Root startup eind

lijst, films = urllib.request.urlretrieve('http://api.filmtotaal.nl/filmsoptv.xml?apikey=r2mnnu0mm027ijyu2lzo371e8eal1vp5&dag={0}&sorteer=0'.format(datumformat), 'films.xml')
conv = 'films.xml'
#opslaan filmsxml
def filmdata():
    with open(conv) as film:
        filestring = film.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary
database = filmdata()
data = database['filmsoptv']['film']
#xml data voorbereiden
columns = defaultdict(list)

def filminfo():
    with open('films {0}.csv'.format(datumformat), 'w', newline='') as aanbieders:
        writer = csv.writer(aanbieders, delimiter=';')

        for Film in data:
            s = float(Film['starttijd'])
            e = float(Film['eindtijd'])
            eindtijd = datetime.datetime.fromtimestamp(e)
            strttijd = datetime.datetime.fromtimestamp(s)
            Film['starttijd']=strttijd.time()
            Film['eindtijd']=eindtijd.time()
            datas = Film['titel'], Film['jaar'], Film['regisseur'], Film['tagline'], Film['imdb_rating'], Film['starttijd'], Film['eindtijd'], Film['cast'], Film['genre'], Film['synopsis'], '{0}'.format(random.randint(10000, 99999))
            writer.writerow(datas)
            global goedelijst
            goedelijst=datas[0]




#eind deel 1 Werkt
