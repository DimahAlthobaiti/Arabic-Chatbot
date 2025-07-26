import whisper
import os
import imageio_ffmpeg

os.environ["PATH"] += os.pathsep + os.path.dirname(imageio_ffmpeg.get_ffmpeg_exe())

def transcribe_audio(filename="input.wav"):
    model = whisper.load_model("medium")
    result = model.transcribe(filename, language="arabic")
    return result["text"]