import openai

audio_file = open("aws2024.m4a", "rb")

transcript = openai.Audio.translate("whisper-1",audio_file)

print(transcript["text"])