import clean_folder as cf
import image_matching as im
import pyautogui as ag
import audio_matching as am
import time
import numpy as np

record_path = './recrod'
image_path = './imgID/default'
fishing_icons= ['fishingFloatImgStd.bmp']
sound_path = './soundID'

coordinate = 0.69  #数值越高越难定位但是越准确
retry = 25
volume_threshold = 30
max_wait_second = 15
enable_volume_monitor = False

ami = am.audio_matching(volume_threshold, enable_volume_monitor, max_wait_second)
ami.set_action_when_getting_fish(
    lambda: (
        ag.rightClick(),
        print('###########CAUGHT FISH!!!!#############')))


while(True):
    st = ami.get_stream()
    print("Sleep 2 seconds before previous fishing icon disappears")
    time.sleep(2)

    print("Start to capture fishing icon position")
    fish_position = im.locate_image(image_path, fishing_icons, coordinate,retry)
    
    if fish_position != -1:
        ag.moveTo(fish_position.x, fish_position.y)
        #validate = locate_image('./imgID/default/fishingCursorStd.bmp',0.65,20)
        validate = 1
        if validate == -1:
            print('incorrect mouse move')
        else:			
            print("Moved to fishing icon position")
            ami.sound_capture()

    print("Cast to fish for next round...")
    print("------------------------------")
    print("##########New Round##########")
    print("------------------------------")
    ag.press('1')