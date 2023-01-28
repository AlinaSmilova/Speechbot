import pyttsx3
import speech_recognition as sr 
import subprocess

#1 Переводит текст в речь (английский язык только)
engine = pyttsx3.init()
engine.setProperty('voice', "com.apple.speech.synthesis.voice.daniel")


def text_to_file(text):
    audio_file = "data/income_file.mp3"
    ogg_file = "data/outcome_file.ogg"

    engine.save_to_file(text, audio_file)
    engine.runAndWait()
    subprocess.run(["ffmpeg", '-i', audio_file, '-acodec', 'libopus', ogg_file, '-y'])

    return ogg_file 

#2 Переводит речь в текст (английский язык только)
async def voice_handler(update, context):
   
    file = await context.bot.getFile(update.message.voice.file_id)
    print(update)
    await file.download('voice.ogg')
    filename = "voice.wav"
    subprocess.call(['ffmpeg', '-i', 'voice.ogg',
                         'voice.wav', '-y'])
    text = audio_to_text(filename)
    await update.message.reply_text(text)

def audio_to_text(name):
   
    r = sr.Recognizer() 
    
    message = sr.AudioFile(name)
    with message as source:
        audio = r.record(source)
    result = r.recognize_sphinx(audio) 
    return result

