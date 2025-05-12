from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # lai imited keys press
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import time

# ceļš līdz edge draiveriem (lai vienkarši atvert edge) bez viņas nav iespējas
edge_driver_path = r"EdgeDriver\msedgedriver.exe"  

# vvod s klaviaturi opcij na vibor 
choice = input("Input 1 (Ortus), 2 (YouTube), 3 (Selenium Python Library info), 4 (DeepLTranslate), 0 EXIT: ")

# veidojam veb driveri tikai pec komandas lai nebija tukšas lapas 
service = Service(edge_driver_path)#Upravljaet zapuskom
driver = webdriver.Edge(service=service)#otkrivajet vebdriver po ego puti raspolozenija

while choice != '0':# esli ne vvedeno 0
    if choice == '1':
        driver.get("https://id2.rtu.lv/openam/UI/Login?module=LDAP&locale=lv") #zagruzaju veb stranicu po ssilke
        driver.minimize_window()
        time.sleep(2)
        try:
            driver.find_element(By.ID, "IDToken1").send_keys("")#sjuda login ot ORTUS(isju element na stranice ortusa s IDToken i posilaju v nego znacenija)
            driver.find_element(By.ID, "IDToken2").send_keys("")#sjuda parol ot ORTUS
            driver.find_element(By.NAME, "Login.Submit").click()#po imeni knopki na stranice otkrivaju
        except Exception as e:
            print("Some nasty error:( ", e)# vivozu prosto osibku sistemi esli slucitsa

    elif choice == '2':
        driver.get("https://www.youtube.com/")
        driver.minimize_window()
    elif choice == '3':
        driver.get("https://selenium-python.readthedocs.io")
        driver.minimize_window()
    elif choice == '4':
        driver.minimize_window() #svaracivaju okno
       # vvozu tekst dlja perevoda
        TextForTranslate = input("Write text to translate: ")

       
        driver.get("https://www.deepl.com/en/translator")
        time.sleep(2)  # daju progruzitsja stranice
        
        
        input_field = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true']")  #nahozu element(mesto dlja vvoda)
        input_field.clear()  #esli cto to est to ocisaju pole
        input_field.send_keys(TextForTranslate)  #posilaju tuda tekst
        
        # posilaju s pomosju emuljacii nazatija
        input_field.send_keys(Keys.RETURN)
        
        #daju progruzitsja
        time.sleep(5)
    else:
        print("Incorrect number.")

    #povtorno zaprasivaju vvod dlja togo ctobi nacat cikl zanova
    choice = input("Input 1 (Ortus), 2 (YouTube), 3 (Selenium Python Library info), 4 (DeepLTranslate), 0 EXIT: ")


driver.quit() #zakrivaju brauzer




