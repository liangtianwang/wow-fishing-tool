import pyautogui
import os
import re

def locate_image(path, wildcard, conf, retry=20):
    icons = getFileListFromWildcard(path, wildcard)
    retry_count = 0
    while(True):
        retry_count = retry_count + 1
        
        for icon in icons:
            try:
                    fish_icon = f'{path}/{icon}'
                    #print(fish_icon)
                    location = pyautogui.locateOnScreen(fish_icon,confidence=conf)
                    print(f'Found fishing icon from {fish_icon}')
                    return pyautogui.center(location)  
            except Exception as e:
                    #print(f"Cannot find image from {icon}..")
                    continue
                
        #print(f"Cannot find image - retry: {retry_count}")
        if retry_count > retry:
            print(f"Cannot find image - exceeded retry count..")
            return -1
            

def getFileListFromWildcard(path, wildcard):
    fileList = []
    for filename in os.listdir(path):
        if re.match(wildcard, filename):
           fileList.append(filename)
    #print(f"fishing icons are: {fileList}")
    return fileList