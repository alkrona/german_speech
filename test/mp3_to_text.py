"""The test would be 3 mp3 files with and the 
transcription should give accurate transcriptions"""

#import mo-to_textdule and function here 
import mp3_to_text_converter

mp3_files = ["a","b","c"]
mp3_transcription=["x","y","z"]
def test_mp3_to_text_converter():
    for index,mp3_file in enumerate(mp3_file):
        assert mp3_to_text_converter(mp3_file)==mp3_transcription[index]