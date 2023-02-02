from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd



def Site():
    website = "https://www.adamchoi.co.uk/btts/detailed"
    path  = r"C:\Users\bilme\Desktop\programming\pythoncrawl\seleniumm\geckodriver.exe"
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
    driver.get(website)
    return driver

def LigSec():
    input("""
      ================================[-][o][x]
      | | - - - - - - - - - - - - - - - - - | |
      | |Github:https://github.com/Beratblm | |
      | |                                   | |
      | |           @CodderBerat            | |
      | |-----------------------------------| |
      |        Programımıza Hoşgeldiniz       |
      |                                       |
      |        Herhangi bir tuşa basın        |
      |                                       |
      |                                       |
      |                                       |
      |=======================================|


    """)
    while True:
       keys = input("""Lütfen bir lig seçiniz: 
1. Türkiye
2. İngiltere
3. İspanya
4. Almanya
5. Fransa
6. İtalya
7. Hollanda
8. Portekiz
9. Rusya
10. Danimarka
11. İsveç
12. İsviçre
13. Belçika
14. Avusturya
15. Polonya
Çıkmak İçin q'ya basınız. : Seçiminiz : """)
       Value = ""

       if keys == "1":
         Value = "Turkey"
         return Value
       
       elif keys == "2":
         Value = "England"
         return Value  
 
       elif keys == "3":
        Value  = "Spain" 
        return Value

       elif keys == "4":
        Value = "Germany"
        return Value

       elif keys == "5":
        Value = "France"
        return Value

       elif keys == "6":
        Value = "Italy"
        return Value

       elif keys == "7":
        Value = "Netherlands"
        return Value

       elif keys == "8":
        Value = "Portugal"
        return Value
        
       elif keys == "9":
         Value = "Russia"
         return Value

       elif keys == "10":
          Value = "Denmark"
          return Value   

       elif keys == "11":
            Value = "Sweden"
            return Value

       elif keys == "12":
         Value = "Switzerland"
         return Value

       elif keys == "13":
         Value = "Belgium"
         return Value

       elif keys == "14":
         Value = "Austria"
         return Value      

       elif keys == "15": 
          Value = "Poland"
          return Value 
       
       elif keys == "q":
         quit()

       else:
         print("Lütfen geçerli bir değer giriniz.")
         continue

def export_csv(Value):
    driver = Site()
    Tum_maclar = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//label[@analytics-event='All matches']"))
    )

    ligler = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "country"))
    ))
    ligler.select_by_visible_text(Value) 

    time.sleep(3)
    Tum_maclar.click()

    Maclari_al = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "tr"))
    )

    dates = []
    home_teams = []
    scores = []
    away_teams = []

    for i, Maclar in enumerate(Maclari_al):
        date = WebDriverWait(Maclar, 10).until(
            EC.presence_of_element_located((By.XPATH, f"./td[1]"))
        )
        dates.append(date.text)

        home_team = WebDriverWait(Maclar, 10).until(
            EC.presence_of_element_located((By.XPATH, f"./td[2]"))
        )
        home_teams.append(home_team.text)

        score = WebDriverWait(Maclar, 10).until(
            EC.presence_of_element_located((By.XPATH, f"./td[3]"))
        )
        scores.append(score.text)

        away_team =  WebDriverWait(Maclar, 10).until(
            EC.presence_of_element_located((By.XPATH, f"./td[4]"))
        )
        away_teams.append(away_team.text)
        #print(f"{i+1}. {date.text} {home_team.text} {score.text} {away_team.text}")

    datalar = pd.DataFrame({'date': dates, 'home_team': home_teams, 'score': scores, 'away_team': away_teams}).to_csv("Maçlar/"+Value+'.csv', index=False)
    driver.quit()
    return "Basarili"
   


Secilen_lig = LigSec()
if export_csv(Secilen_lig) == "Basarili":
    print("-----------------------Başarıyla kaydedildi.------------------------")
else:
    print("Bir hata oluştu. Tekrar deneyiniz. Olmazsa @CodderBerat'a ulaşınız. -_-")    

