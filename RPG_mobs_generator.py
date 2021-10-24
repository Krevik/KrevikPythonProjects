from PIL import Image, ImageDraw, ImageFont
from os import listdir
from os.path import isfile, join
import random


przymiotnik = ["Almighty", "Rookie", "Grossy", "Angry",
               "Compulsive", "Dominant", "Bloodthirsty", "Merciless", "Hostile", "Destructive",
               "Great", "Curious", "Furious", "Demonic", "Drunken", "Brutal", "Reckless",
               "Blind", "Eternal", "Cruel", "Awful", "Diseased", "Violent", "Mad", "Greasy",
               "Loud", "Faceless", "Mutated", "Wild", "Huge", "Little", "Small", "Tiny",
               "Giant", "Unstable", "Old", "Silver", "Golden", "Fallen", "Undead", "Scary",
               "Regular", "Necromantial", "Resurrected", "Reborn", "Hairy"]

moby = ["Demon", "Skeleton", "Human", "Wanderer", "Elf", "Dragon", "Knight", "Ghost", "King",
        "Guardian", "Murderer", "Minion", "Cultist", "Archer", "Mage", "Paladin", "Healer",
        "Berserker", "Gnom", "Troll", "Succub", "Destroyer", "Nightmare", "Lord", "Lurker",
        "Maiden", "Seraph", "Angel", "Devil", "Minotaur"]

def getColorForStat(i):
    if(i > 0 and i < 25):
        return "#ff0000"
    if(i >= 25 and i < 50):
        return "#FFFFFF"
    if(i >= 50 and i < 75):
        return "#81D7DC"
    if(i >= 75 and i < 98):
        return "#00ff00"
    if(i >= 98):
        return "#5E74EB"

def getColorForGoldLoot(i):
    if(i > 0 and i < 250):
        return "#ff0000"
    if(i >= 250 and i < 500):
        return "#FFFFFF"
    if(i >= 500 and i < 750):
        return "#81D7DC"
    if(i >= 750 and i < 980):
        return "#00ff00"
    if(i >= 980):
        return "#5E74EB"

def getColorForRarity(i):
    if( i == "Common" ):
        return "#ff0000"
    if( i == "Uncommon"):
        return "#FFFFFF"
    if( i == "Rare"):
        return "#81D7DC"
    if( i == "Epic"):
        return "#00ff00"
    if( i == "Legendary"):
        return "#5E74EB"
    
def getRarity(*args):
    i = 0
    for number in args:
        i = i + number
    if(i > 0 and i < 300):
        return "Common"
    if(i >= 300 and i < 500):
        return "Uncommon"
    if(i >= 500 and i < 700):
        return "Rare"
    if(i >= 700 and i < 780):
        return "Epic"
    if(i >= 780):
        return "Legendary"
    
count = 1
for str1 in przymiotnik:
    for str2 in moby:
        MobName = str(str1) + " " + str(str2);
        w = 200 # 100 pixels wide
        h = 150 # 100 pixels high
        img = Image.new('RGB', (w, h), color='#000000')
        canvas = ImageDraw.Draw(img)
        text_width, text_height = canvas.textsize(MobName)
        x_pos = int((w - text_width) / 2)
        canvas.text((x_pos, 10), MobName, fill='#FFFFFF')

        generated_value1 = random.randint(60, 100);
        health_points = str(generated_value1);
        string = "Health Points: ";
        text_width, text_height = canvas.textsize(string)
        x_pos1 = int((w - text_width) / 2)
        canvas.text((x_pos1, 40), string, fill="#FFFFFF")
        text_width, text_height = canvas.textsize(health_points)
        x_pos = int((w - text_width + canvas.textsize(string)[0]) / 2)
        canvas.text((x_pos, 40), health_points, fill=getColorForStat(generated_value1))
        
        generated_value2 = random.randint(60, 100);
        attack = str(generated_value2);
        string = "Attack Damage: ";
        text_width, text_height = canvas.textsize(string)
        x_pos1 = int((w - text_width) / 2)
        canvas.text((x_pos1, 50), string, fill="#FFFFFF")
        text_width, text_height = canvas.textsize(attack)
        x_pos = int((w - text_width + canvas.textsize(string)[0]) / 2)
        canvas.text((x_pos, 50), attack, fill=getColorForStat(generated_value2))

        generated_value3 = random.randint(60, 100);
        attack_speed = str(generated_value3);
        string = "Attack Speed: ";
        text_width, text_height = canvas.textsize(string)
        x_pos1 = int((w - text_width) / 2)
        canvas.text((x_pos1, 60), string, fill="#FFFFFF")
        text_width, text_height = canvas.textsize(attack_speed)
        x_pos = int((w - text_width + canvas.textsize(string)[0]) / 2)
        canvas.text((x_pos, 60), attack_speed, fill=getColorForStat(generated_value3))

        generated_value4 = random.randint(60, 100);
        defence = str(generated_value4);
        string = "Defence: ";
        text_width, text_height = canvas.textsize(string)
        x_pos1 = int((w - text_width) / 2)
        canvas.text((x_pos1, 70), string, fill="#FFFFFF")
        text_width, text_height = canvas.textsize(defence)
        x_pos = int((w - text_width + canvas.textsize(string)[0]) / 2)
        canvas.text((x_pos, 70), defence, fill=getColorForStat(generated_value4))

        generated_value5 = random.randint(60, 100);
        magic_defence = str(generated_value5);
        string = "Magic Defence: ";
        text_width, text_height = canvas.textsize(string)
        x_pos1 = int((w - text_width) / 2)
        canvas.text((x_pos1, 80), string, fill="#FFFFFF")
        text_width, text_height = canvas.textsize(magic_defence)
        x_pos = int((w - text_width + canvas.textsize(string)[0]) / 2)
        canvas.text((x_pos, 80), magic_defence, fill=getColorForStat(generated_value5))

        generated_value6 = random.randint(60, 100);
        aim_rate = str(generated_value6);
        string = "Aim Rate: ";
        text_width, text_height = canvas.textsize(string)
        x_pos1 = int((w - text_width) / 2)
        canvas.text((x_pos1, 90), string, fill="#FFFFFF")
        text_width, text_height = canvas.textsize(aim_rate)
        x_pos = int((w - text_width + canvas.textsize(string)[0]) / 2)
        canvas.text((x_pos, 90), aim_rate, fill=getColorForStat(generated_value6))

        generated_value7 = random.randint(60, 100);
        evade_rate = str(generated_value7);
        string = "Evade Rate: ";
        text_width, text_height = canvas.textsize(string)
        x_pos1 = int((w - text_width) / 2)
        canvas.text((x_pos1, 100), string, fill="#FFFFFF")
        text_width, text_height = canvas.textsize(evade_rate)
        x_pos = int((w - text_width + canvas.textsize(string)[0]) / 2)
        canvas.text((x_pos, 100), evade_rate, fill=getColorForStat(generated_value7))

        generated_value8 = random.randint(60, 100);
        movement_speed = str(generated_value8);
        string = "Movement Speed: ";
        text_width, text_height = canvas.textsize(string)
        x_pos1 = int((w - text_width) / 2)
        canvas.text((x_pos1, 110), string, fill="#FFFFFF")
        text_width, text_height = canvas.textsize(movement_speed)
        x_pos = int((w - text_width + canvas.textsize(string)[0]) / 2)
        canvas.text((x_pos, 110), movement_speed, fill=getColorForStat(generated_value8))

        generated_value9 = random.randint(60, 100);
        gold_loot = str(generated_value9);
        string = "Gold Loot: ";
        text_width, text_height = canvas.textsize(string)
        x_pos1 = int((w - text_width) / 2)
        canvas.text((x_pos1, 120), string, fill="#FFFFFF")
        text_width, text_height = canvas.textsize(gold_loot)
        x_pos = int((w - text_width + canvas.textsize(string)[0]) / 2)
        canvas.text((x_pos, 120), gold_loot, fill=getColorForStat(generated_value9))

        string = "Rarity: ";
        text_width, text_height = canvas.textsize(string)
        rarity = getRarity(generated_value1, generated_value2, generated_value3, generated_value4,
                           generated_value5, generated_value6, generated_value7, generated_value8,
                            );
        text_width1, text_height1 = canvas.textsize(rarity)
        x_pos = int((w - (text_width + canvas.textsize(string)[0])) / 2) + text_width;
        x_pos1 = int((w - (text_width + canvas.textsize(string)[0])) / 2)
        canvas.text((x_pos1, 130), string, fill="#FFFFFF")
        canvas.text((x_pos, 130), rarity, fill=getColorForRarity(rarity))
        
        save_path = "D:/Krzysiek Backupy/BACKUP v2/nft/python/generator/set2/"
        img.save(save_path + "RPG Mob #"+ str(count) + ".png", "PNG")
        count = count + 1


