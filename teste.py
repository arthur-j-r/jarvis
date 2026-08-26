import sounddevice as sd
fs = 44100  # Sample rate

duration = 10.5  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
sd.play(myrecording, fs)