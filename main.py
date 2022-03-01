#README:
#-----------
#This is a script for scraping live wait times from ATM website
#Before running the script, make sure the following dependencies are installed:
#Selenium library (Command line: pip install selenium)
#webdriver for desired browser: https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
#After downloading the driver, unzip and (i) move the .exe file to the virtual environment/
#folder of the current project OR (ii) change path using os.path() function and run the file
#--------------------------------------------------------------------------------------------------------------------

#Enjoy scraping!

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

def wait_time(fermata):

    #For Chrome/Chromium use webdriver.Chrome()
    driver = webdriver.Edge()

    driver.get("https://giromilano.atm.it/#/home/")
    driver.refresh()

    print("Displaying wait time for first solution only",end="")
    sleep(1)
    print(".",end="")
    sleep(1)
    print(".",end="")
    sleep(1)
    print(".")


    #The following objects primarily wait until the site is loaded or for 10s, whichever comes first.
    #Then, specific css objects are assigned each object before performing an operation
    #For example, cercafermata first locates the find stop dropdown menu, and then clicks to open it
    cerca_fermata = WebDriverWait(driver,10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[translate='lblCercaFermata']")))

    cerca_fermata.click()

    #locating input
    fermata_input = WebDriverWait(driver,10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[id='txtFermata']")))

    #sending our function's parameters as input to the text box
    fermata_input.send_keys(fermata)
    fermata_input.send_keys(Keys.ENTER)

    #clicking only on the first solution (can be changed later)
    first_solution = WebDriverWait(driver,10)\
        .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='rowLinea']")))
    first_solution.click()

    #Printing the stop name and route number
    stop_name = WebDriverWait(driver,10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div[class='divPopupLine ng-binding']")))
    print(stop_name.text)

    #Printing wait time every 30s
    while(1):

        try:
            refresh = WebDriverWait(driver,10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[id ='btnRefreshWaitMessage']"))).click()
            waiting_time = WebDriverWait(driver,10)\
                .until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[class ='fontBold pull-right ng-binding']"))).text

            print("Waiting time: " + waiting_time)
        except: RuntimeError("No data received")
        sleep(30)

if __name__ == '__main__':
    fermata =input("Enter stop/via/piazza: ")
    wait_time(fermata)