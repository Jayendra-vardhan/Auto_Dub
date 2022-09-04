#from google.cloud import speech_v1 as speech

#def speech_to_text(config, audio):
 #   client = speech.SpeechClient()
  #  response = client.recognize(config=config, audio=audio)
   # print_sentences(response)

#def print_sentences(response):
 #   for result in response.results:
  #      best_alternative = result.alternatives[0]
   #     transcript = best_alternative.transcript
    #    confidence = best_alternative.confidence
     #   print("-" * 80)
      #  print(f"Transcript: {transcript}")
       # print(f"Confidence: {confidence:.0%}")

#config = dict(language_code="en-US")
#audio = dict(uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac")
#speech_to_text(config, audio)
""" import sys
import os
import pydub
import glob

from pydub import AudioSegment

wav_files = glob.glob("X:\general\XXXXX\GSTT\Flac Dateien/*.wav")
print(flac_files) 


for wav_file in wav_files:
    flac_file = os.path.splitext(wav_file)[0] + ".flac" 

    sound = AudioSegment.from_file(wav_file, format = "wav") 
    sound.export(flac_file, format = "flac") """
    
#ffmpeg -i input-video.avi -vn -acodec copy output-audio.aac

# import subprocess
# import os
# import sys

# #import speech_recognition as sr
# #from pydub import AudioSegment

# def convert_video_to_audio_ffmpeg(video_file, output_ext="flac"):
#     #Converts video to audio directly using `ffmpeg` command
#     #with the help of subprocess module
#     filename, ext = os.path.splitext(video_file)
#     subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
#                     stdout=subprocess.DEVNULL,
#                     stderr=subprocess.STDOUT)

# if __name__ == "__main__":
#     vf = "D:\How to speak so that people want to listen _ Julian Treasure.mp4"
#     convert_video_to_audio_ffmpeg(vf)
    
    #  # convert mp3 file to wav                                                       
    # sound = AudioSegment.from_mp3("D:\How to speak so that people want to listen _ Julian Treasure.flac")
    # sound.export("D:\How to speak so that people want to listen _ Julian Treasure.wav", format="wav")


    # # transcribe audio file                                                         
    # AUDIO_FILE = "D:\How to speak so that people want to listen _ Julian Treasure.wav"

    # # use the audio file as the audio source                                        
    # r = sr.Recognizer()
    # with sr.AudioFile(AUDIO_FILE) as source:
    #         audio = r.record(source)  # read the entire audio file                  

    #         print("Transcription: " + r.recognize_google(audio))
            
import json
import requests
url = 'https://www.google.com/speech-api/v1/recognize?client=chromium&lang=en-US'
data = {'file': open('D:\How to speak so that people want to listen _ Julian Treasure.flac', 'rb')}
headers = {'Content-Type': 'audio/x-flac; rate=16000', 'User-Agent':'Mozilla/5.0'}
r = requests.post(url, data=data, headers=headers)
r = requests.post(url, files=data, headers=headers) ## does not work either
r = requests.post(url, data=open('file.flac', 'rb').read(), headers=headers) ## does not work either
print (r.text)

# import subprocess
# import os
# import sys
		
# def convert_video_to_audio_ffmpeg(video_file, output_ext="flac"):
#     #Converts video to audio directly using `ffmpeg` command
#     #with the help of subprocess module
#     filename, ext = os.path.splitext(video_file)
#     subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], 
#                     stdout=subprocess.DEVNULL,
#                     stderr=subprocess.STDOUT)

# if __name__ == "__main__":
#     vf = "D:\How to speak so that people want to listen _ Julian Treasure.mp4"
#     convert_video_to_audio_ffmpeg(vf)



# # Imports the Google Cloud client library
# from google.cloud import speech
# import os
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"d:\UPES\Project\translation project\Local_to_GCP\upheld-beach-360516-95be0c166639.json"

# # Instantiates a client
# client = speech.SpeechClient()

# # The name of the audio file to transcribe
# local_file_path = "D:\How to speak so that people want to listen _ Julian Treasure.flac"

# audio = speech.RecognitionAudio(uri=local_file_path)

# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
#     sample_rate_hertz=16000,
#     language_code="en-US",
# )

# # Detects speech in the audio file
# response = client.recognize(config=config, audio=audio)
# channel = grpc.insecure_channel('localhost:5005', options=(('grpc.enable_http_proxy', 0),))

# for result in response.results:
#     print("Transcript: {}".format(result.alternatives[0].transcript))


# Imports the Google Cloud client library
# import os
# from google.cloud import speech

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"d:\UPES\Project\translation project\Local_to_GCP\upheld-beach-360516-95be0c166639.json"

# # Instantiates a client
# client = speech.SpeechClient()

# # The name of the audio file to transcribe
# uri= "gs://flac_file111/how-to-speak-so-that-people-want-to-listen-julian-treasure_RRYwKciD.flac"

# audio = speech.RecognitionAudio(uri=uri)

# config = speech.RecognitionConfig(
#     encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
#     sample_rate_hertz=44100,
#     audio_channel_count=2,
#     language_code="en-US",
#     enable_word_confidence=True,
# )


# operation = client.long_running_recognize(config=config, audio=audio)

# print("Waiting for operation to complete...")
# response = operation.result(timeout=180)

# # Each result is for a consecutive portion of the audio. Iterate through
# # them to get the transcripts for the entire audio file.
# for result in response.results:
#     # The first alternative is the most likely one for this portion.
#     print(u"Transcript: {}".format(result.alternatives[0].transcript))
#     print("Confidence: {}".format(result.alternatives[0].confidence))
