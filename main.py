import random
import datetime
from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.common.by import By
import random
from pygame import mixer  # Load the popular external library
from time import strftime
import tkinter as tk
import pygame
from threading import *
from queue import Queue

#setting the alarm
alarmH = 15
alarmM = 27
CHAR_LEN = 46
        
#thread which controls the clock
def clock(in_q):
    
    #setting the clock 
    def set_clock():
        clock.config(text = strftime("%H:%M:%S %p"))
        clock.after(1000,set_clock)

    #writing the task
    def set_task(activity):

        #splits the activity string into the name and task 
        name, task = activity.split(":", 1)
        isMaxChar = False

        #if the task string is too long, make a newline
        for index in range(len(task)):
            if index % CHAR_LEN == 0 and index != 0:
                isMaxChar = True
                space = index-1
                while (task[space] != " "):
                    space-=1
                first_line = task[:space]
                second_line = task[space+1:]
                break
         
        if(isMaxChar==False):
            text = tk.Label(root, text = name + ":\n" + task, bg = "black", fg = "white", font = ("arial",  25,  'bold'))
            text.place(relx=0.5, rely=0.2, anchor=tk.CENTER, width = w-20, height = 115)
        else:
            text = tk.Label(root, text = name + ":\n" + first_line + '\n' + second_line, bg = "black", fg = "white", font = ("arial",  25,  'bold'))
            text.place(relx=0.5, rely=0.2, anchor=tk.CENTER, width = w-20, height = 115)

    print(datetime.datetime.now().hour , ":", datetime.datetime.now().minute)
    root = tk.Tk()

    #FRONT
    root.title("Alarmania")
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry(f"{w}x{h}+0+0")
    root.resizable(0,0)
    root.config(bg = "black")
    root.attributes('-fullscreen', True)

    #LABEL
    clock = tk.Label(root, font = ('calibri', 60, 'bold'),
                background = 'black',
                foreground = 'white')
    
    # Placing clock at the centre of the tkinter window
    clock.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width = w, height = 80)
    set_clock()

    alarm = tk.Label(root, bg = "black", fg = "green", font = "arial 50 bold")
    alarm.pack()

    #get the data form the other thread
    def loop():
        if (q.empty() == False):        
            activity = in_q.get()
            set_task(activity)   
        root.after(10, loop)

    root.after(6, loop)
    root.mainloop()
 


#second thread which gets the information from the websites
def web_script(out_q):

    #first website
    def webscript_one():

        #gets information form below website
        website = 'https://randomthingstodo.com/'
        activities = ['talk', 'draw', 'paint', 'home', 'outside',
                    'public', 'challenges', 'write', 'money', 'best', 'funniest']
        
        #randomly choose a category from the website
        activity = ""
        rand_num = random.randint(1, 11)

        if rand_num == 1:

            website = website + activities[0]
            activity = 'Things to Talk About'

        elif rand_num == 1:

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

        #setup the chrome driver
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        
        #change path according to directory of chromedriver
        driver = webdriver.Chrome(
            'chromedriver', options=option)
        driver.get(website)

        name = driver.find_element(By.CLASS_NAME, "card-text").text
        
        text = activity + ": " + " " + name
        
        return text
        
    #second website
    def webscript_two():

        #gets information form below website
        website = 'https://randomwordgenerator.com/act-of-kindness.php'
        option = webdriver.ChromeOptions()
        option.add_argument('headless')

        #change path according to directory of chromedriver
        driver = webdriver.Chrome(
            'chromedriver', options=option)
        driver.get(website)
        driver.find_element(By.XPATH, '//*[@id="btn_submit_generator"]').click()
        act = driver.find_element(By.XPATH, '//*[@id="result"]/li/div/span').text
  
        return "Random Act of Kindness: " + act

    pygame.mixer.init()
    mixer.init()
    mixer.music.load('stanley.mp3')

    #keep waiting until the time matches the alarm time
    while(True):

        #play the music and put the website data onto the queue which is for the first thread
        if(alarmH == (datetime.datetime.now().hour) and
                alarmM == (datetime.datetime.now().minute)):

            mixer.music.load('toby_sad_boy.mp3')
            mixer.music.play()

            endTime = datetime.datetime.now() + datetime.timedelta(minutes=20)
            
            rand_num = random.randint(1, 2)

            if (rand_num == 1):
                out_q.put(webscript_one())
            
            else: 
                out_q.put(webscript_two())

            while True:

                if datetime.datetime.now() >= endTime:
                    break

#initialize the threads and queue to share the website information
q = Queue()
t1=Thread(target=web_script, args = (q, ))
t2=Thread(target=clock, args = (q,))
t1.start()
t2.start()
