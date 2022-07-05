import time
import cred_link
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Open browser
driver_path = Service("chromedriver.exe")
driver = webdriver.Chrome(service=driver_path)

# Browser setting
driver.set_window_size(1024, 600)
driver.maximize_window()
wait = WebDriverWait(driver, 10)


# Webpage dictionary
dict_link = dict({
    'Japan': cred_link.Japan,
    'US': cred_link.US,
    'Malaysia': cred_link.Malaysia,
    'Singapore': cred_link.Singapore,
    'Indonesia': cred_link.Indonesia
    })

country_list = ['Japan', 'US', 'Malaysia', 'Singapore', 'Indonesia']

# List for job data
job_data = []


def scroll(wait_val):
    # Scroll down
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait_val)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    return last_height


# Call value using key
def get_value(key_val):
    for key, value in dict_link.items():
        if key_val == key:
            return value

    return "key doesn't exist"


# Function to be used
def click_xpath(searched_element):
    ele = wait.until(EC.element_to_be_clickable(By.XPATH, searched_element))
    return ele.click()


def click_class(searched_element):
    ele = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, searched_element)))
    return ele.click()


def job_class(searched_element, num):
    ele = wait.until(EC.visibility_of_elements_located((By.CLASS_NAME, searched_element)[num]))
    return ele.click()


def extract_num(searched_element, num_val, redactor):
    try:
        count_att = (num_val - redactor)
        data_att = driver.find_elements(By.CLASS_NAME, searched_element)[count_att]
        text_att = BeautifulSoup(data_att.get_attribute('outerHTML'), 'html.parser').text
    except:
        text_att = "ERROR EMPLOYMENT"

    return text_att


def extract_att(element):
    try:
        attribute_data = driver.find_element(By.CLASS_NAME, element)
        text_att = BeautifulSoup(attribute_data.get_attribute('outerHTML'), 'html.parser').text
    except:
        text_att = "ERROR"
    return text_att


# Loop for every country
for country in country_list:
    driver.get(get_value(country))
    time.sleep(5)

    while len(driver.find_elements(By.CLASS_NAME, 'base-card.base-card--link')) < 500:
        driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        time.sleep(2)
        scroll(3.5)
        driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        scroll(3.5)
        time.sleep(2)
        click_class('infinite-scroller__show-more-button.infinite-scroller__show-more-button--visible')
        time.sleep(2)


    # Job list
    for job in range(0, 500):

        try:
            driver.find_elements(By.CLASS_NAME, 'base-card.base-card--link')[job].click()
        except:
            print("CLICK ERROR")
            break
        time.sleep(8)

        try:
            click_class('show-more-less-html__button.show-more-less-html__button--more')
        except:
            pass

        time.sleep(3)

        job_title = extract_att('top-card-layout__title.topcard__title')
        job_comp = extract_att('topcard__org-name-link.topcard__flavor--black-link')
        job_loc = extract_att('topcard__flavor.topcard__flavor--bullet')
        job_appli = extract_att('num-applicants__caption')
        job_desc = extract_att('show-more-less-html__markup')

        count = len(driver.find_elements(
            By.CLASS_NAME, 'description__job-criteria-text.description__job-criteria-text--criteria')) + 1

        if (count - 2) >= 0:
            job_emp = extract_num('description__job-criteria-text.description__job-criteria-text--criteria', count, 3)
        else:
            job_emp = "BLANK FIELD"

        if (count - 3) >= 0:
            job_sen = extract_num('description__job-criteria-text.description__job-criteria-text--criteria', count, 4)
        else:
            job_sen = "BLANK FIELD"

        to_list = {
            'country': country,
            'title': job_title,
            'company': job_comp,
            'location': job_loc,
            'employment_type': job_emp,
            'seniority': job_sen,
            'applicants': job_appli,
            'description': job_desc
        }
        job_data.append(to_list)

        # to delay
        time.sleep(5)

        print(job_title, job_comp, country, (job + 1))

# Dataframe and export to csv
df = pd.DataFrame(job_data)
df.to_csv('Output\Early_Scraped-Data-Raw.csv', index=False, encoding='utf-8')
