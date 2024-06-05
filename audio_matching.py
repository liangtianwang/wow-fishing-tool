import sounddevice as sd
import numpy as np
import time



class audio_matching():
    def __init__(self, volume_threshold, monitor):
        self.volume_threshold = volume_threshold
        self.monitor = monitor
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

    def get_stream(self):
        return self.st
    
    def set_action_when_getting_fish(self, fish_action):
        self.fish_action = fish_action

    def sound_capture(self, max_wait_second):    
        time.sleep(2)
        
        self.st.start()
        print('Audio capture process started')
        #print(sd.default.device)
        
        i = 0
        while self.st.active:
            sd.sleep(1000)
            i = i + 1
            if i > max_wait_second:
                print('Reached maximum wait second, stopped audio capture and give up fishing')
                self.st.stop()
                break
        
        print('Audio capture process stopped')