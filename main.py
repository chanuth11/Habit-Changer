import random
import time
import datetime
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.common.by import By
import random
from pygame import mixer  # Load the popular external library

def webscript(boolean):
    website = 'https://randomthingstodo.com/'
    activities = ['talk', 'draw', 'paint', 'home', 'outside',
                  'public', 'challenges', 'write', 'money', 'best', 'funniest']
    activity = ""
    rand_num = random.randint(1, 11)

    # make restart a key input instead
    restart = False

    if rand_num == 1:

        website = website + activities[0]
        activity = 'Things to Talk About'

    elif rand_num == 2:

        website = website + activities[1]
        activity = 'Drawing Ideas'

    elif rand_num == 3:

        website = website + activities[2]
        activity = 'Painting Ideas'

    elif rand_num == 4:

        website = website + activities[3]
        activity = 'Things to Do at Home'

    elif rand_num == 5:

        website = website + activities[4]
        activity = 'Things to Do Outside'

    elif rand_num == 6:

        website = website + activities[5]
        activity = 'Things to Do in Public'

    elif rand_num == 7:

        website = website + activities[6]
        activity = 'Challenges'

    elif rand_num == 8:

        website = website + activities[7]
        activity = 'Writing Prompts'

    elif rand_num == 9:
        website = website + activities[8]
        activity = 'Ways to Make Money'

    elif rand_num == 10:

        website = website + activities[9]
        activity = 'Best Things to Do'

    elif rand_num == 11:

        website = website + activities[10]
        activity = 'Funniest Things to Do'

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(
        'chromedriver', options=option)
    driver.get(website)

    name = driver.find_element(By.CLASS_NAME, "card-text").text
    print("Activity: " + activity)
    print("Task: " + name)

    if boolean == True:

        webscript(False)
print(datetime.datetime.now().minute)
if __name__ == "__main__":
    #make input nice display
    alarmH = 11
    alarmM = 5

    mixer.init()
    mixer.music.load('stanley.mp3')
    while(True):
        count = 0
        
        #make nice input

        restart = False

        if(alarmH == (datetime.datetime.now().hour) and
                alarmM == (datetime.datetime.now().minute)):

            mixer.music.load('toby_sad_boy.mp3')
            mixer.music.play()

            endTime = datetime.datetime.now() + datetime.timedelta(minutes=2)
            
            webscript(False)

            while True:

                if datetime.datetime.now() >= endTime:
                    break

                if restart == True:
                    webscript(False)