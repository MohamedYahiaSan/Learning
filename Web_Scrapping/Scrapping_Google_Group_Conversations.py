# Scrapping all conversations from a Google group

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import requests


# Initialize Selenium WebDriver
driver = webdriver.Chrome()

# Navigate to the Google Group URL
url = 'https://groups.google.com/g/gprmax'
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Initialize BeautifulSoup with the loaded page content
soup = BeautifulSoup(driver.page_source, 'html.parser')


#collect urls of questions
questions=[]


# Looping through all the pages and scrapping the messages Urls
while True:
    # Scrapping the Urls
    curr_questions= soup.find_all('a',class_='ZLl54')
    questions+=curr_questions[::3]
    

    try:
        # Click the "Next" button to load more content
        next_button = driver.find_element(By.CSS_SELECTOR, '#yDmH0d > c-wiz.zQTmif.SSPGKf.eejsDc > c-wiz > div > c-wiz > div > div.GeR1W.xaq4Kc > html-blob > span > div > div:nth-child(3) > span > span > span')
        next_button.click()

        # Wait for the next page to load
        time.sleep(5)
        
        # Parse the newly loaded content with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

    except:
        break

# Adjusting all messages links in a list
links=[url+x.get('href')[10:] for x in questions]

# Closing the driver
driver.quit()

#Now we want to scrap the text in the messages


file= open('data.txt','w', encoding='utf-8', errors='ignore')

# URL of the Google Group Message
for m_url in links:

    # Send a GET request to the URL
    response = requests.get(m_url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Finding all messages in the post
    messages=soup.find_all('div',class_='ptW7te')

    # Writing the messages to a file
    for comment in messages:
        for txt in comment:

            file.write(txt.text,)
            file.write('\n')
        file.write('\nNext Comment\n\n')
    
file.close()