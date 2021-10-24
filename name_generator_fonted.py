from PIL import Image, ImageDraw, ImageFont
from os import listdir
from os.path import isfile, join
import random
from io import *
import string

names = ["Krzysztof", "Martyna"]


def load_words():
    newList = [];
    with open('E:\\BACKUPY\\python\\nft\\names\\names.txt', "r") as f:
        for line in f:
            newList.extend(line.split())
    return newList;
names = load_words();

count = 1
for word in names:
        Name = word;
        w = 800 # 100 pixels wide
        h = 400 # 100 pixels high
        img = Image.new('RGB', (w, h), color='#FFFFFF')
        canvas = ImageDraw.Draw(img)
        text_width, text_height = canvas.textsize(Name)
        x_pos = int(40)
        y_pos = int((h - (text_height)*4.8) / 2)
        #canvas.text( (x_pos, y_pos), Name, fill='#FFFFFF', font="Purisa")
        myFont = ImageFont.load_default()
        #myFont = ImageFont.truetype("Futurot.ttf", 32);
        myFont = ImageFont.truetype("C:/Users/Krevik/Downloads/future_rot/f.ttf", 64)
        canvas.text((x_pos, y_pos), fill='#000000', font=myFont, text=Name);
        
        save_path = "E:/BACKUPY/python/nft/names/result/"
        img.save(save_path + "Future Rot Name #" + str(count) + ".png", "PNG")
        count = count + 1


