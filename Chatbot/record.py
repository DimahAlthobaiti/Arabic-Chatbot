import sounddevice as sd
from scipy.io.wavfile import write

def record_audio(filename="input.wav", duration=7, fs=16000):  
    print("🎤 ابدأ التحدث الآن...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, recording)
    print("✅ تم تسجيل الصوت وحفظه.")