#imports the necessary stuff
import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk,Image

#gets the weather info from the url
url="https://weather.com/en-IN/weather/today/l/3eb968d7a06604b522f130b07342afa0c5728ddfc8a4ed54787b8676df413142"
# for the screen
master=Tk()
master.title("prajwal pokhrel's weather app")
master.config(bg="light blue")

#the image
img=Image.open("cloudy.jpg")
img=img.resize((150,150))
img=ImageTk.PhotoImage(img)

locationclass='_1Ayv3'
temperatureclass='_3KcTQ'
weatherpredictionclass='_2xXSr'
futurepredictionclass='RBVJT'
timeclass="_1SWy5"


#get weather function
def getweather():
	page=requests.get(url)
	soup=BeautifulSoup(page.content,"html.parser")
	location=soup.find('h1',class_=locationclass).text
	temperature=soup.find('span',class_=temperatureclass).text
	weatherprediction=soup.find('div',class_=weatherpredictionclass).text
	futureprediction=soup.find('div',class_=futurepredictionclass).text
	time=soup.find('div',class_=timeclass).text
	locationlabel.config(text=location)
	temperaturelabel.config(text=temperature)
	weatherpredictionlabel.config(text=weatherprediction)
	futurepredictionlabel.config(text=futureprediction)
	timelabel.config(text=time)
	#updates the weather after every 1 minute 
	temperaturelabel.after(60000,getweather)
	locationlabel.after(60000,getweather)
	weatherpredictionlabel.after(60000,getweather)
	futurepredictionlabel.after(60000,getweather)
	timelabel.after(60000,getweather)
	master.update()
#labels of screen
locationlabel=Label(master,font=("calibri bold",20),bg="light blue")
locationlabel.grid(row=0,sticky="N",padx=100)
temperaturelabel=Label(master,font=("calibri bold",70),bg="light blue")
temperaturelabel.grid(row=1,sticky="W",padx=40)
Label(master,image=img,bg="light blue").grid(row=1,sticky="E")
weatherpredictionlabel=Label(master,font=("calibri bold",15),bg="light blue")
weatherpredictionlabel.grid(row=2,sticky="W",padx=40)
futurepredictionlabel=Label(master,font=("calibri bold",20),bg="light blue")
futurepredictionlabel.grid(row=4,sticky="S",padx=100)
timelabel=Label(master,font=("calibri bold",20),bg="light blue")
timelabel.grid(row=1,sticky="W",padx=200)
#runs the mainloop
getweather()
master.mainloop()

