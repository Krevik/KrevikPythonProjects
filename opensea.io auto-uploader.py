import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc

chromedriver_path = "D:/python/chromedriver"
chromium_path = "D:/python/chrome-win/chrome"

options = webdriver.ChromeOptions()
options.add_extension('E:/BACKUPY/python/MetaMask.crx')
options.add_argument("--start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("ignore-certificate-errors");
options.add_argument("--no-sandbox");
driver = uc.Chrome(options=options) 

isRunning = False;
MaxDelayTime = 60;
StartImageNumber = 2;
ActualImageNumber = StartImageNumber;
EndImageNumber = 10;
ImagesNameFilePrefix = "lovely_potato_#";
CatalogOfImages = "C:/Users/PC/Desktop/nft/python/images/resultForTest/";

ImagesNamePrefix = "Lovely Potato #";
DescPrefix = "Okay so it is one out of few ultra cute lovely potatoes. Take care of him! And remember not to peel him off!";

def Start():
    isRunning = True;
    print("Started Running Loop")
    close_last_tab();
    try:
        e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Rozpocznij"]')))
        e.click();
        e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Importuj portfel"]')))
        e.click();
        e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[text()="No Thanks"]')))
        e.click();
        e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div[4]/div[1]/div/input')))
        e.send_keys("wallet_keys");
        e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
        e.send_keys("passwd")
        e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="confirm-password"]')))
        e.send_keys("passwd")
        e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div[7]/div')))
        e.click();
        e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Importuj"]')))
        e.click();
        e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Wszystko gotowe"]')))
        e.click();
    except:
        print("whoops")
    time.sleep(2)
    driver.get('https://opensea.io');
    close_last_tab();
    login_into_opensea();
    

    
def close_last_tab():
    if (len(driver.window_handles) == 2):
        driver.switch_to.window(window_name=driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(window_name=driver.window_handles[0])

def login_into_opensea():
    print(str(len(driver.window_handles)));
    #click on wallet icon
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/nav/ul/div[2]/li/button')));
    driver.execute_script("arguments[0].click();", e)
    #click metamask button
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/aside[2]/div[2]/div/div[2]/ul/li[1]/button')));
    driver.execute_script("arguments[0].click();", e)
    #wait for metamask window opening
    while(len(driver.window_handles) < 2):
        time.sleep(1)
    driver.switch_to.window(window_name=driver.window_handles[-1])
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Dalej"]')));
    driver.execute_script("arguments[0].click();", e)
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Połącz"]')));
    driver.execute_script("arguments[0].click();", e)
    #switch window
    driver.switch_to.window(window_name=driver.window_handles[0])
    testingElement = 1;
    try:
        testingElement = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/aside/div[2]/div/div[1]/button')));
    except:
        print("fuck...")
        testingElement = 1
    if testingElement != 1:
        print("we're logged!")
        StartAddingItems();

def StartAddingItems():
    #e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[1]/nav/ul/div[1]/li[4]')));
    #driver.execute_script("arguments[0].click();", e)
    #e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/div[1]/nav/ul/li[4]/a')));
    #driver.execute_script("arguments[0].click();", e)
    #podpisano, create klikniete!
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/main/div/div/section/div/form/div[1]/div/div[2]/input')));
    print("found it!")
    e.sendKeys("E:\\BACKUPY\\python\\nft\\coins\\1.png");
    print("I did send file")

    #e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Drag & drop file"]')));
    #e = driver.findElement(By.linkText("Drag & drop file"));
    #e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="media"]')));
    e.sendKeys(CatalogOfImages + ImagesNameFilePrefix + str(ActualImageNumber) + ".png");
    #driver.execute_script("arguments[0].sendKeys(C:/Users/PC/Desktop/nft/python/images/resultForTest/);", e)
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="name"]')));
    e.click();
    e.sendKeys(ImagesNamePrefix+str(ActualImageNumber));
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="description"]')));
    e.sendKeys(DescPrefix);
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/section/div/form/section[5]/div/input')));
    e.click();
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tippy-74"]')));
    e.click();
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/section/div/form/section[8]/div/input')));
    e.click();
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tippy-76"]')));
    e.click();
    
    ActualImageNumber=ActualImageNumber+1;
    


        
Start();


    
