from PIL import Image, ImageDraw, ImageFont
from os import listdir
from os.path import isfile, join
import os
import random

natures = ["Hardy", "Lonely", "Brave", "Adamant", "Naughty", "Bold", "Docile", "Relaxed", "Impish", "Lax", "Timid", "Hasty",
           "Serious", "Jolly", "Naive", "Modest", "Mild", "Quiet", "Bashful", "Rash", "Calm", "Gentle", "Sassy", "Careful",
           "Quirky"]

increased_stats = ["-", "Attack", "Attack", "Attack", "Attack", "Defense", "-", "Defense", "Defense", "Defense", "Speed", "Speed",
                   "-", "Speed", "Speed", "Sp. Atk", "Sp. Atk", "Sp. Atk", "-", "Sp. Atk", "Sp. Def", "Sp. Def", "Sp. Def", "Sp. Def", "-"]

decreased_stats = [ "-", "Defense", "Speed", "Sp. Atk", "Sp. Def", "Attack", "-", "Speed", "Sp. Atk", "Sp. Def", "Attack", "Defense", "-", "Sp. Atk",
                   "Sp. Def", "Attack", "Defense", "Speed", "-", "Sp. Def", "Attack", "Defense", "Speed", "Sp. Atk", "-"];

hiddenPowers = ["Fighting", "Flying", "Poison", "Ground", "Rock", "Bug", "Ghost", "Steel", "Fire", "Water", "Grass", "Electric", "Psychic",
                "Ice", "Dragon", "Dark", "Fairy"];

sexes = ["Male", "Female"];
shinyChanceWeight = 1024;
IVs = ["HP", "Attack", "Defense", "Speed", "Sp. Atk", "Sp. Def"];
pokemonsToGenerate = ["Bulbasaur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartotle", "Blastoise"];
typesOfPokemonsToGenerate = ["Grass, Poison", "Grass, Poison", "Grass, Poison", "Fire", "Fire", "Fire, Flying", "Water", "Water", "Water"];

def getShiny():
    if(random.randint(0, shinyChanceWeight) == 1):
        return True;
    else:
        return False;

def getPokemonName(shiny, pokemonName, index):
    result = pokemonName;
    if(shiny == True):
        result = result + " (Shiny)";
    result = result + " #" + str(index);
    return result;

def getSaveDir(pokemonName, partialPokemonName):
    result = "C:\\BACKUPY\\BACKUP v2\\nft\\python\\generator\\pokemon\\pokemons\\" + str(partialPokemonName);
    return result;

def getFullSavePath(pokemonName, partialPokemonName):
    result = "C:\\BACKUPY\\BACKUP v2\\nft\\python\\generator\\pokemon\\pokemons\\" + str(partialPokemonName) + "\\" + str(pokemonName) + ".png";
    return result;

def getStatColor(IV, natureID):
    result = "#ffffff";
    if(str(IV) == str(increased_stats[natureID])):
        result = "#00cc00";
    if(str(IV) == str(decreased_stats[natureID])):
        result = "#ff0000";
    return result;

def getPokemonTypes(generatingPokemonNameIndex):
    result = [];
    for str1 in hiddenPowers:
        if(str(str1) in typesOfPokemonsToGenerate[generatingPokemonNameIndex - 1]):
            result.append(str(str1));
    return result;

def getBackgroundColors(types):
    resultColors = []
    if("Fighting" in types):
        resultColors.append("#800000");
    if("Flying" in types):
        resultColors.append("#66d9ff");
    if("Poison" in types):
        resultColors.append("#993399");
    if("Ground" in types):
        resultColors.append("#e67300");
    if("Rock" in types):
        resultColors.append("#ffad33");
    if("Bug" in types):
        resultColors.append("#008040");
    if("Ghost" in types):
        resultColors.append("#666699");
    if("Steel" in types):
        resultColors.append("#c2c2d6");
    if("Fire" in types):
        resultColors.append("#ff5c33");
    if("Water" in types):
        resultColors.append("#66b3ff");
    if("Grass" in types):
        resultColors.append("#66ff66");
    if("Psychic" in types):
        resultColors.append("#ff1a75");
    if("Ice" in types):
        resultColors.append("#e6ffff");
    if("Dragon" in types):
        resultColors.append("#33ccff");
    if("Dark" in types):
        resultColors.append("#29293d");
    if("Fairy" in types):
        resultColors.append("#ff99dd");
    return resultColors;
    
generatingPokemonLocalIndex = 0
for generatingPokemonName in pokemonsToGenerate:
    generatingPokemonLocalIndex = generatingPokemonLocalIndex + 1
    actualPokemonIndex = 1
    x = 1;
    while(x < 999):
        #getting pokemon types
        pokemonTypes = [];
        pokemonTypes = getPokemonTypes(generatingPokemonLocalIndex);
        
        nameColor = "#000000";
        natureID = random.randint(0, len(natures) - 1);
        nature = natures[natureID];
        hiddenPower = hiddenPowers[random.randint(0, len(hiddenPowers) - 1)];
        shiny = getShiny();
        if(shiny == True):
            nameColor = "#e32dcb";
        pokemonName = getPokemonName(shiny, generatingPokemonName, actualPokemonIndex);
        w = 200 # 100 pixels wide
        h = 150 # 100 pixels high
        backgroundColor = "#66b3ff";

        img = Image.new('RGB', (w, h), color=backgroundColor)
        canvas = ImageDraw.Draw(img)
        text_width, text_height = canvas.textsize(pokemonName);
        center_x_pos = int((w - text_width) / 2)
        canvas.text((center_x_pos, 10), pokemonName, fill=nameColor)
        
        sex = sexes[random.randint(0, len(sexes) - 1)];

        #gender
        yShift = 30;
        textField = "Gender: " + str(sex);
        text_width, text_height = canvas.textsize(textField);
        center_x_pos = int((w - text_width) / 2);
        canvas.text((center_x_pos, yShift), textField, fill='#ffffff');
        
        #nature
        yShift = 40;
        textField = "Nature: " + str(nature);
        text_width, text_height = canvas.textsize(textField);
        center_x_pos = int((w - text_width) / 2);
        canvas.text((center_x_pos, yShift), textField, fill='#ffffff');

        #Hidden Power
        yShift = 50;
        textFieldPart1 = "Hidden Power: ";
        textFieldPart2 = str(hiddenPower);
        text_width, text_height = canvas.textsize(textFieldPart1 + textFieldPart2);
        text_width1, text_height1 = canvas.textsize(textFieldPart1);
        text_width2, text_height2 = canvas.textsize(textFieldPart2);
        center_x_pos = int((w - text_width) / 2);
        canvas.text((center_x_pos, yShift), textFieldPart1 + textFieldPart2, fill='#ffffff');
        
        #IVs
        yShift = 80;
        for IV in IVs:
            IVValue = random.randint(1,31);
            pokemonStatTextFieldPart1 = IV + ": ";
            pokemonStatTextFieldPart2 = str(IVValue);
            text_width, text_height = canvas.textsize(pokemonStatTextFieldPart1 + pokemonStatTextFieldPart2);
            text_width1, text_height1 = canvas.textsize(pokemonStatTextFieldPart1);
            text_width2, text_height2 = canvas.textsize(pokemonStatTextFieldPart2);
            center_x_pos = int((w - text_width) / 2);
            statColor = getStatColor(IV, natureID);
            canvas.text((center_x_pos, yShift), pokemonStatTextFieldPart1, fill='#ffffff');
            canvas.text((center_x_pos + text_width1, yShift), pokemonStatTextFieldPart2, fill=statColor);
            yShift = yShift + 10;

        save_path = getFullSavePath(pokemonName, generatingPokemonName);
        save_dir = getSaveDir(pokemonName, generatingPokemonName);
        if not os.path.exists(save_dir):
            os.mkdir(save_dir);
        #while(os.path.exists(save_path)):
            #actualPokemonIndex = actualPokemonIndex + 1;
            #pokemonName = getPokemonName(shiny, generatingPokemonName, actualPokemonIndex);
            #save_path = getFullSavePath(pokemonName, generatingPokemonName);
        
        img.save(save_path, "PNG");
        main_image = Image.open(save_path);
        sex_image = Image.open("C:\\BACKUPY\\BACKUP v2\\nft\\python\\generator\\pokemon\\sex\\" + sex + ".png");
        typesImages = [];
        for pokemonType in pokemonTypes:
            typesImages.append(Image.open("C:\\BACKUPY\\BACKUP v2\\nft\\python\\generator\\pokemon\\types\\32x32\\" + str(pokemonType) + ".png"));

        main_image.paste(sex_image, (5,80), mask = sex_image);
        shiftX=150;
        shiftY=80;
        for typesImage in typesImages:
            main_image.paste(typesImage, (shiftX,shiftY), mask = typesImage);
            shiftY = shiftY + 35;


        main_image.save(save_path, "PNG");
        actualPokemonIndex = actualPokemonIndex + 1;
        x = x + 1


        
