# souce: https://github.com/realpython/python-speech-recognition/blob/master/guessing_game.py
import random
import time
import datetime
import speech_recognition as sr
from selenium import webdriver   # for webdriver
# for implicit and explict waits
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.common.by import By
import random
from pygame import mixer  # Load the popular external library


def recognize_speech_from_mic(recognizer, microphone):
    """Transcribe speech from recorded from `microphone`.
    Returns a dictionary with three keys:
    "success": a boolean indicating whether or not the API request was
               successful
    "error":   `None` if no error occured, otherwise a string containing
               an error message if the API could not be reached or
               speech was unrecognizable
    "transcription": `None` if speech could not be transcribed,
               otherwise a string containing the transcribed text
    """
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        # change to speak instead of text
        
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):

        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:

        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)

    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"

    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response


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
        'chromedriver_win32/chromedriver', options=option)
    driver.get(website)

    name = driver.find_element(By.CLASS_NAME, "card-text").text
    print("Activity: " + activity)
    print("Task: " + name)

    if boolean == True:

        webscript(False)


if __name__ == "__main__":

    #  set prompt limit
    PROMPT_LIMIT = 5
    PROMPT_NUM = 0
    alarmH = 0
    alarmM = 0
    isfour = False
    count = 0

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    mixer.init()
    mixer.music.load('stanley.mp3')

    while(True):

        # get the command from the user
        # if a transcription is returned, break out of the loop and
        #     continue
        # if no transcription returned and API request failed, break
        #     loop and continue
        # if API request succeeded but no transcription was returned,
        #     re-prompt the user to say their command again. Do this up
        #     to PROMPT_LIMIT times

        command = recognize_speech_from_mic(recognizer, microphone)
        print("listenting")
        text = command["transcription"]

        if command["success"] and command["transcription"]:
            print(command["transcription"])

            if 'alarm' in command["transcription"] or 'reset' in command["transcription"]:

                for j in range(PROMPT_LIMIT):

                    print('time')
                    time = recognize_speech_from_mic(recognizer, microphone)

                    if time['transcription']:
                        print(time['transcription'])

                        if time["transcription"].isnumeric() and len(time["transcription"]) >= 3:

                            if len(time['transcription']) == 4:
                                isfour = True
                                print('length is four')

                            break
                        else:

                            print("say number")

                    if not time["success"]:

                        break

                    mixer.music.play()
                    PROMPT_NUM += 1

            # make speak instead of text

                # check if prompt number is less than 5
                if PROMPT_NUM < 5:

                    print(time["transcription"])
                    alarm_time = time["transcription"]
                    PROMPT_NUM = 0

                    alarmM = alarm_time[-2]+alarm_time[-1]

                    if isfour == True:

                        alarmH = alarm_time[0]+alarm_time[1]

                    else:

                        alarmH = alarm_time[0]

                    # print(alarmH)

                    # print(alarmM)
                    for k in range(PROMPT_LIMIT):

                        print('am or pm')

                        # listen for user to say am or pm
                        isAmPm = recognize_speech_from_mic(
                            recognizer, microphone)

                        if isAmPm['transcription']:
                            # print(isAmPm['transcription'])

                            if ('a.m' in isAmPm['transcription'] or 'p.m' in isAmPm['transcription']
                                    or 'a.m.' in isAmPm['transcription'] or 'p.m.' in isAmPm['transcription']):

                                break

                        if not isAmPm["success"]:

                            break

                        mixer.music.play()
                        PROMPT_NUM += 1

                    # check if prompt number is less than 5
                    if PROMPT_NUM < 5:
                        print(isAmPm)

                        if ('p.m' in isAmPm['transcription'] or 'p.m.' in isAmPm['transcription']
                                or 'pm' in isAmPm['transcription']):
                            alarmH = str(int(alarmH) + 12)

        print("alarm time: ", alarmH, alarmM)
        # checking if alarm matches time
        #print('time now')
        print(datetime.datetime.now().hour)
        print(datetime.datetime.now().minute)

        if(int(alarmH) == (datetime.datetime.now().hour) and
                int(alarmM) == (datetime.datetime.now().minute)):

            mixer.music.load('toby_sad_boy.mp3')
            mixer.music.play()

            endTime = datetime.datetime.now() + datetime.timedelta(minutes=2)

            while True:

                if datetime.datetime.now() >= endTime:
                    break

                if count == 0:
                    count += 1
                    webscript(False)

                    # restart
