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

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    volume = int(volume_norm)
    print('|' * volume)
    if(volume > volume_threshold):
        ag.rightClick()
        am.get_stream().stop()

am.set_stream(print_sound)

while(True):
    am.get_stream().start()
    print("Sleep 2 seconds before previous fishing icon disappea111rs")
    time.sleep(2)
    am.get_stream().stop()

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
            am.sound_capture(print_sound)

    print("Cast to fish for next round...")
    ag.press('1')