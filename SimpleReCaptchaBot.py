from anticaptchaofficial.recaptchav2proxyless import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests
from requests.adapters import HTTPAdapter

i = 765
inputFile = open('IPList.txt', 'r').readlines()
requests.adapters.DEFAULT_RETRIES = 10

while True:

    driver = webdriver.Chrome(ChromeDriverManager().install())
    url = "https://faucet.avax-test.network"
    #url = "https://gemfinder.cc/gem/7734"
    page = driver.get(url)

    os.system('mullvad relay set hostname ' + inputFile[i])
    os.system('mullvad connect')
    time.sleep(3)
    os.system('mullvad status')
    print(inputFile[i])
    driver.find_element(By.CSS_SELECTOR, ".pk_in").send_keys("your address here")

    #sitekey = "6Lc2dNUUAAAAAIlOu63qA-ojum-vPIwGl64TqPaP"
    #sitekey = "6LcZFbAbAAAAAJSD_n7j-qIPFUolmWd8vJ81UkSk"
    sitekey = "your sitekey here"
    print(sitekey)
    print(i)

    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key('anticaptcha license key here')
    solver.set_website_url(url)
    solver.set_website_key(sitekey)

    g_response = solver.solve_and_return_solution()
    if g_response!= 0:
        print("g_response"+g_response)
    else:
        print("task finished with error"+solver.error_code)

    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')

    driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""", g_response)
    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
    print("here")
    print("here1")
    driver.find_element(By.CSS_SELECTOR, ".v-btn").click()

    time.sleep(5)
    driver.quit()
    os.system('mullvad disconnect')
    if i == 0:
        i = 765
    else:
        i -= 1

print("RIP")
