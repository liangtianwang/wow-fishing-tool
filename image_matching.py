import pyautogui

def locate_image(path,icons, conf, retry=20):
    fish_icon_path = f'{path}/{icons[0]}'
    retry_count = 0
    while(True):
        try:
            retry_count = retry_count + 1
            location = pyautogui.locateOnScreen(fish_icon_path,confidence=conf)
            #print(location)
            print('Found fishing icon')
            return pyautogui.center(location)       
        except Exception as e:
            if retry_count > retry:
                print(f"Cannot find image: {e}")
                return -1