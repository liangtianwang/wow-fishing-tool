import sounddevice as sd
import numpy as np
import time

class audio_matching():
    def __init__(self, volume_threshold, monitor, max_wait_second):
        self.volume_threshold = volume_threshold
        self.monitor = monitor
        self.max_wait_second = max_wait_second
        self.st = sd.Stream(callback=self.print_sound)

    def print_sound(self, indata, outdata, frames, time, status):
        volume_norm = np.linalg.norm(indata)*10
        volume = int(volume_norm)
        if self.monitor:
            print('|' * volume)
            #print(volume_norm)
        if(volume > self.volume_threshold):
            self.fish_action()
            self.st.stop()
            print('Audio capture process stopped..')

    def get_stream(self):
        return self.st
    
    def get_stream_without_callback(self):
        return sd.Stream()
    
    def set_action_when_getting_fish(self, fish_action):
        self.fish_action = fish_action

    def sound_capture(self):
        print('Initialise SD stream...')      
        self.st.start()
        print('Audio capture process started...')       
        
        i = 0
        while self.st.active:
            sd.sleep(1000)
            i = i + 1
            if i > self.max_wait_second:
                print('Reached maximum wait second, stopped audio capture and give up fishing')
                self.st.stop()
                print('Audio capture process stopped..')
                break