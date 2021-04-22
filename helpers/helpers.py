import os
import subprocess
import sys


try:
    from google.cloud import texttospeech
except ModuleNotFoundError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'google-cloud-texttospeech'])
finally:
    from google.cloud import texttospeech

from const import const as c

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="PATH TO YOUR JSON FILE"
def set_settings(text_to_convert):
    client = texttospeech.TextToSpeechClient()
    synthesis_input = texttospeech.SynthesisInput(text=text_to_convert)
    voice = texttospeech.VoiceSelectionParams(language_code=c.LANGUAGE_CODE,
                                              ssml_gender=texttospeech.SsmlVoiceGender.MALE,
                                              name=c.VOICE_NAME)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response_return = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
    return response_return


def generate_mp3_file(response_to_write):
    with open(c.FILE_NAME, "wb") as out:
        out.write(response_to_write.audio_content)
        print('Audio content written to file "output.mp3"')


if __name__ == "__main__":
    response = set_settings(c.TEXT_TO_CONVERT)
    generate_mp3_file(response)
