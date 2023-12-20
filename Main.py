# import imghdr
from ast import If
from asyncio.windows_events import NULL
from email.mime import image
from tkinter import Frame
from cv2 import *
import numpy as np
from PIL import Image,ImageOps,ImageDraw,ImageFont
from asyncore import write
from cgitb import text
import cv2
from numpy import size
# import brightness as b
from skin import crop
from brightness import bright
import reg
import pyttsx3 as p
import time 
import turtle
# turtle.setup(10,330)
# board=turtle.Turtle()
# # def draw():
    

engine=p.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

cap = cv2.VideoCapture(0)         #Runtime cam start

# ret, frame = cap.read()
while(True):
    ret, frame = cap.read()
    cv2.imshow("frame",frame)
    if cv2.waitKey(1) & 0xFF==ord('y'):
        cv2.imwrite('./test.jpg',frame)
        break

cap.release()
cv2.destroyAllWindows()           #runtime cam ends

#n = input("Enter File Name : ")
# crop.main()

img = Image.open("test.jpg")
# img1=cv2.imread('test.jpg')
im = ImageOps.grayscale(img)
# im.save("test.jpg")
# img = Image.open("test.jpg")
def output_image() :
    im.show()

pixels = im.load()
height, width=im.size
print(height,width)
print(im.load()[35,45])
k=0
avg=0
for x in range (height):
        for y in range (width):
            r = pixels[x,y]
            avg=avg+r
area=height*width
avg=avg/area
lim=avg+((255-avg)*10/100)
# lim=avg
for x in range (height):
    for y in range (width):
        r= pixels[x,y]
        if(r>=lim):
            k=k+1


# for oily

with open('oily.txt') as f:
    # content = f.readlines()
    l = []
    for i in f:
        l.append(i.strip('\n'))
# l.sort()
# print(l)
# size = len(l)
# print(size)
# index = int(((size+1)/2)-1)
# print(l[index])
# level = int(sum(l)/size)

# print(level)

# print("\n")

# # for dry 

with open('dry.txt') as f:
    # content = f.readlines()
    l1 = []
    for j in f:
        l1.append(j.strip('\n'))
# l1.sort()
# print(l1)q
# size1 = len(l1)
# print(size)
# index1 = int(((size1+1)/2)-1)
# print(index)

#level1 = int(sum(l1)/size1)

# print(level1)
moist=reg.slope *k + reg.intercept
ko=""
rate=0
rt=[]
dif=float(l[0])-float(l1[0])
sig_lev_1 = float(l[0])-(dif/2)
# print("The dif is",dif)
sig_lev_2 = float(l[0])-(dif/2) - (dif*38/100)
per = (k-sig_lev_1) / (dif*50/100) *100
rating_lim=int(k/sig_lev_1*10)
if(rating_lim>10):
    rating_lim=10
while(rate<rating_lim):
    rt.append("*")
    rate+=1
if(k>=sig_lev_1):
#     if(k<float(l[0])):
    name="Oily Skin "
elif(k<=sig_lev_2):
    name="Dry Skin"
elif(k>sig_lev_2 and k<sig_lev_1):
    name="Mixed"

ko="".join(rt)

moist=round(moist,2)

I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('FreeMono.ttf', 25)
I1.text((20, 350),"#" +name+"\n#Rating : "+str(rate)+"\n"+ko+"\n#Moist : "+str(moist),font=myFont, fill=(0, 0, 0))   
# if(k<float(l[0]) and k>=sig_lev_1):
#     I1.text((150, 150), str(per)+"%",font=myFont, fill=(255, 0, 0))  
img.show()
im.show(name)
# speak(f"Your skin type is {name}")
# # time.sleep(1)
# speak(f"with your skin Rating {rate}")
# # time.sleep(1)
# speak(f"and The moisture value is {moist}")
print(k,avg,sig_lev_1,sig_lev_2,lim)

# ret=bright.brightness()

# f = open("oily_bright.txt","a")
# val=ret
# a = f.write(f"{val}\n")
# f.close()

# f = open("oily_img_bright.txt","a")
# val = k
# a = f.write(f"{val}\n")
# f.close()



