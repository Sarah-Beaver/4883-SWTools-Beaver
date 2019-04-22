from pydub import AudioSegment
from pydub.playback import play

sound = AudioSegment.from_file(".//words_us/aaa_us.mp3", format="mp3")
play(sound)
print('yes')