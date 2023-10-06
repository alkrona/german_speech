import sounddevice as sd
from scipy.io.wavfile import write
import datetime
fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
file_name=str(datetime.datetime.now()) +  'output.wav'
write(file_name, fs, myrecording)  # Save as WAV file 