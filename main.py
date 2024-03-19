import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.latlong.net/")
previous_lat_lng = None

try:
    with open("coordinates.txt", "a") as file:
        while True:
            lat_lng_element = driver.find_element(By.ID, "latlngspan")
            lat_lng_text = lat_lng_element.text

            if lat_lng_text != previous_lat_lng:
                lat_lng_formatted = lat_lng_text.replace("(", "[").replace(")", "]")
                print("Latitude and Longitude:", lat_lng_formatted)
                file.write(lat_lng_formatted + ",")
                file.flush()
                previous_lat_lng = lat_lng_text

            time.sleep(0.5)

except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()
