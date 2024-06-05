import sounddevice as sd
import numpy as np
import time

st = sd.Stream()

def set_stream(callback):
 return sd.Stream(callback=callback)

def get_stream():
   return st


def sound_capture(max_wait_second):
    time.sleep(2)
    
    st.start()
    print('Audio capture process started')
    
    i = 0
    while st.active:
        sd.sleep(1000)
        i = i + 1
        if i > max_wait_second:
            print('Reached maximum wait second, stopped audio capture and give up fishing')
            st.stop()
            break
    
    print('Audio capture process stopped')