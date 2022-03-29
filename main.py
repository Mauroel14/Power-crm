from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time


lineas = []
line2 = []


path = "chromedriver.exe"
options = Options()
#options.add_argument("start-maximized")
browser = webdriver.Chrome()
browser.get('https://powercrm.movistar.com.ar/')
#wait = WebDriverWait(browser, 15)

time.sleep(6)

user = browser.find_element(By.CLASS_NAME,"form-control").send_keys("fbasan")
passw = browser.find_element(By.NAME,"password").send_keys("Global/2021")
select = Select(browser.find_element(By.NAME,"domain"))
select. select_by_visible_text("@telefonica")
button = browser.find_element(By.XPATH,"//*[@id='root']/div/form/div/button").click()
time.sleep(6)
file_1 = pd.read_excel("lineas.xlsx", header=None)
file_1 = pd.DataFrame(file_1)

for line in list(file_1[0]):
    time.sleep(6)
    try:
        line1 = lineas.append(line)
        line2 = lineas.pop(0)
        print(line2)
        buttonClick1 = browser.find_element(By.XPATH, "//*[@id='formBasicPassword']").click()
        buttonClick = browser.find_element(By.XPATH, "//*[@id='formBasicPassword']").send_keys(line2)
        time.sleep(4)
        buttonClick2 = browser.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[2]/div[2]/div[1]/div/div/form/div/div[3]/button").click()
        time.sleep(2)
        usuario = browser.find_element(By.CLASS_NAME,"tbody-tr").click()
        time.sleep(4)
        #alert = WebDriverWait.until(EC.visibility_of_element_located((By.CLASS_NAME,"svg-container")))
        alert1 = browser.find_element(By.CLASS_NAME, "svg-container").click()
        time.sleep(4)
        buttonFac = browser.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[1]/nav/a[4]/button").click()
        time.sleep(4)
        try: 
            Precio = browser.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[1]/nav/a[4]/button").click()
            precio_1 = browser.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div/div/div[4]/div[2]/div[1]/div[2]/label").get_attribute('value')
            print(precio_1)
            time.sleep(6)
            vol = browser.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[1]/nav/a[1]/button").click()

            file = open("datosFacturaImpaga.csv","a")
            file1 = file.write("{},{}\n".format(line2,precio_1))
            file.close()
            time.sleep(4)

        except:
            
            pass
            
            err = print("Sin factura")
            vol = browser.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[1]/nav/a[1]/button").click()
            file = open("datosFacturaImpaga.csv","a")
            file1 = file.write("{},{}\n".format(line2,err))
            file.close()
            time.sleep(4)    

        

    except NoSuchElementException:



        time.sleep(4)
        err = browser.find_element(By.CLASS_NAME,"tr-msj-errores").text
        print(err)
        file = open("datosFacturaImpaga.csv", "a")
        file1 = file.write("{},{}\n".format(line2, err))
        file.close()
        browser.refresh()














