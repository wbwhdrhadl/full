import openai

audio_file= open("audio.mp3", "rb")

transript = openai.Audio.transcribe("whisper-1", audio_file)

print(transript["text"])