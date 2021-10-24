from PIL import Image
from os import listdir
from os.path import isfile, join

#import image
layer1 = listdir("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\tlo");
layer2 = listdir("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\cialo");
layer3 = listdir("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\twarz");
layer4 = listdir("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\nogi");
layer5 = listdir("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\czapeczka");

count = 1
for image1 in layer1:
    for image2 in layer2:
        for image3 in layer3:
            for image4 in layer4:
                for image5 in layer5:
                    image1_opened = Image.open("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\tlo\\"+image1)
                    image1_opened.load()
                    image2_opened = Image.open("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\cialo\\"+image2)
                    image2_opened.load()
                    image3_opened = Image.open("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\twarz\\"+image3)
                    image3_opened.load()
                    image4_opened = Image.open("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\nogi\\"+image4)
                    image4_opened.load()
                    image5_opened = Image.open("E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\czapeczka\\"+image5)
                    image5_opened.load()
                    result_image1 = Image.alpha_composite(image1_opened, image2_opened)
                    result_image2 = Image.alpha_composite(result_image1, image3_opened)
                    result_image3 = Image.alpha_composite(result_image2, image4_opened)
                    result_image4 = Image.alpha_composite(result_image3, image5_opened)
                    save_path = "E:\\BACKUPY\\BACKUP v2\\nft\\python\\images\\rotten potatoes\\result\\crypto_potato"
                    result_image4.save(save_path + "_" + "#" + str(count) + ".png", "PNG")
                    count = count + 1
