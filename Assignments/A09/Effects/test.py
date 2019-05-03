import os
from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file("./"+"/words_us/cavern_us.mp3", format="mp3")
sound2 = AudioSegment.from_file("./"+"/words_us/aardvark_us.mp3", format="mp3")
bgm = AudioSegment.from_file("bgm.mp4", format="mp4")
#source:
#https://stackoverflow.com/questions/51434897/how-to-change-audio-playback-speed-using-pydub
def speed_change(sound, speed=1.0):
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)

#backround 
play(bgm[:10000]-5)
#concatinate
sound3 = sound+sound2
play(sound3)
#overlay sound3 with bgm
play(sound3.overlay(bgm[:10000]-7))
#pan to left channel
play(sound3.pan(-.99))
#set up speed up and down
slow_sound = speed_change(sound2, 0.75)
fast_sound = speed_change(sound, 2.0)
sound4 = fast_sound+slow_sound
play(sound4)
#reverse
reverse_sound = sound3.reverse()
play(reverse_sound)
print("Test Done")
