import openai
import os 
from ApiKey import Apikey
os.environ['OPENAI_API_KEY']=Apikey
openai.organization = "org-9v4GCJ6MZ9Bxe35CE4zR6w6C"
openai.api_key = os.getenv("OPENAI_API_KEY")


def main():
    file_name="test/test_music_files/music_test4.wav"
    transcript= mp3_to_text_converter(file_name)
    print(transcript)
def mp3_to_text_converter(mp3):
    try :
        audio_file= open(mp3, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    except :
        return "speak again"
    else :
        return transcript
if __name__=="__main__":
    main()