from gtts import gTTS
import os

text = "LOL this is really funny"
output = gTTS(text=text, lang='en',slow=False)
output.save('output.mp3')

os.system("mpg321 output.mp3")
