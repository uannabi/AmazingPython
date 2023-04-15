
from gtts import gTTS

language = "en"

voice= "hello from the other side"

speech = gTTS(text=voice, lang=language, slow=False, tld="com.au")

speech.save("textToSpeech.mp3")


