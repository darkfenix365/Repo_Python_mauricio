# Librerias a ocupar
from sqlite3 import Cursor
import tempfile
from time import sleep
from selenium import webdriver
from datetime import timedelta, date, datetime
from webdriver_manager.chrome import ChromeDriverManager
from parametros import TIKR_MAIL, TIKR_PASSWORD

# Creacion de la carpeta temporal de directorio

temp = tempfile.TemporaryDirectory("w+t")
tempdir = temp.name

#Generacion de funcion de descarga en carpeta temporal

def create_driver():    
    # Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    download_argument = f'download.default_directory={tempdir}'
    print(download_argument)
    prefs = {'download.default_directory': f'{tempdir}'}
    options.add_experimental_option('prefs', prefs)
    # Conexccion a chrome driver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.get('https://app.tikr.com/login')
    return driver

driver = create_driver()