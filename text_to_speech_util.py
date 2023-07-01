
import gtts
language="de"
text = " Ich bin Rachel, ich bin zwei und zwanzig Jahre alt"
lang_string = gtts.lang.tts_langs()
#print(lang_string)
voice = gtts.tts.gTTS(text,lang=language)
voice.save("german.mp3")
print(voice)
def german_mp3_maker( text,voice):
    
    vice = gtts.tts.gTTS(text,lang="de")
    vice.write_to_fp(voice)
    return voice