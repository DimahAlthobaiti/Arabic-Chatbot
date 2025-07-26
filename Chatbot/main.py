from record import record_audio
from stt import transcribe_audio
from response import generate_response
from tts import speak

import arabic_reshaper
from bidi.algorithm import get_display

def fix_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    return bidi_text

record_audio()

text = transcribe_audio()
print("📝 النص:", fix_arabic(text))

reply = generate_response(text)
print("🤖 الرد:", fix_arabic(reply))

speak(reply)