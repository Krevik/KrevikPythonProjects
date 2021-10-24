import time

from selenium import webdriver
import selenium.webdriver.chrome.service as service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2}) 
chromeOptions.add_argument("--no-sandbox") 
chromeOptions.add_argument("--disable-setuid-sandbox") 

chromeOptions.add_argument("--remote-debugging-port=9222")  # this

chromeOptions.add_argument("--disable-dev-shm-using") 
chromeOptions.add_argument("--disable-extensions") 
chromeOptions.add_argument("--disable-gpu") 
chromeOptions.add_argument("start-maximized") 
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument(r"user-data-dir=.\cookies\\test") 
chromeOptions.add_argument("--headless") 

driver = webdriver.Chrome(ChromeDriverManager().install(),options=chromeOptions) 
driver.get('https://creator.nightcafe.studio/login?view=password-login')
login = "kczyku.kw@gmail.com"
password = "passwd"
MaxDelayTime = 5

def Start():
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[2]/div/form/div[2]/div[1]/div/div[2]/input')));
    e.send_keys(login);
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[2]/div/form/div[2]/div[2]/div/div[2]/input')));
    e.send_keys(password);
    e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[3]/div[2]/div/form/div[2]/div[3]/button')));
    driver.execute_script("arguments[0].click();", e)
    while True:
        try:
            e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div/div[1]/div[4]/button')));
            driver.execute_script("arguments[0].click();", e)
        except:
            c = 1
        try:
            e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '//*[text()="Claim 3 credits"]')));
            driver.execute_script("arguments[0].click();", e)
        except:
            c = 1
        try:
            e = WebDriverWait(driver, MaxDelayTime).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div[1]/button')));
            driver.execute_script("arguments[0].click();", e)
        except:
            c = 1
        time.sleep(25)

Start();


    
