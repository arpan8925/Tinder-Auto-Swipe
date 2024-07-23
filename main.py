import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Configure Chrome options
options = uc.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
driver = uc.Chrome(options=options)

driver.get("https://tinder.com/app/recs")

wait = WebDriverWait(driver, 20)  # Increased timeout

login = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='q1503199108']/div/div[1]/div/main/div[1]/div/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]/div")))
login.click()

I_accept = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='q-225181968']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div")))
I_accept.click()

gmail_login = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "nsm7Bb-HzV7m-LgbsSe-BPrWId")))
gmail_login.click()

# Wait for the new window to open and switch to it
WebDriverWait(driver, 20).until(lambda d: len(d.window_handles) > 1)
window_handles = driver.window_handles
gmail_login_window = driver.window_handles[1]
driver.switch_to.window(gmail_login_window)

email_box = wait.until(EC.presence_of_element_located((By.NAME, "identifier")))
email_box.send_keys("sbxp1966@gmail.com")
next_button = driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span")
next_button.click()

passw = wait.until(EC.presence_of_element_located((By.NAME, "Passwd")))
passw.send_keys("arpan8925$#$#")
passw.send_keys(Keys.ENTER)

WebDriverWait(driver, 40).until(lambda d: len(d.window_handles) == 1)
# Switch back to Tinder window
driver.switch_to.window(driver.window_handles[0])

# Wait for the location permission button and click it
allow_location = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='q-225181968']/div/div/div/div/div[3]/button[1]/div[2]/div[2]/div")))
allow_location.click()

like = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='q1503199108']/div/div[1]/div/main/div[1]/div/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button/span/span")))
like.click()

# Keep the script running to keep the browser open
try:
    while True:
        pass
except KeyboardInterrupt:
    driver.quit()
