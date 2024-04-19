
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from threading import Thread

with webdriver.Firefox() as driver:
    driver.get("https://humanbenchmark.com/tests/verbal-memory")
    wait = WebDriverWait(driver, 100)
    # click start
    start_xpath = "//button[text()='Start']"
    # Wait for the button to be located on the page
    start_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, start_xpath)))
    # click start
    start_button.click()

    div_css_selector = ".word"

    # word stack
    words = []
    points = int(input('How many points do you want?\t'))
    ## click consent
    
    score = 0 
    while score < points:
        score += 1
        # Wait for the div element to be located on the page
        div_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, div_css_selector)))
        # Get the text content of the div element
        word = div_element.text
        # if in stack, click seen. if not in stack, click other button and add to stack
        print(word)
        #score_class = "item score"
        #div_score = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, score_class)))
        #score = div_score.text
        #print(score)
        if word in words:
            # click seen
            seen_xpath = "//button[text()='SEEN']"
            # Wait for the button to be located on the page
            seen_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, seen_xpath)))
            # click start
            seen_button.click()
        else:
            words.append(word)
            # click new
            new_xpath = "//button[text()='NEW']"
            # Wait for the button to be located on the page
            new_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, new_xpath)))
            # click start
            new_button.click()
    input()
    

